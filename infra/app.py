from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_ssm as ssm,
    aws_codebuild as build,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as actions,
)


class EpicollectMigratorLambdaPipelineStack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        the_lambda = _lambda.Function(
            self, 'Singleton',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('../epicollect_migrator_lambda'),
            handler='epicollect_migrator_lambda.handler.handle',
            timeout=core.Duration.minutes(10)
        )

        events.Rule(
            self,"schedule",
            description="",
            enabled=True,
            schedule=events.Schedule.rate(core.Duration.hours(24)),
            targets=[targets.LambdaFunction(handler=the_lambda)])

        artifact_bucket = s3.Bucket(
            self, 'BuildArtifactsBucket',
            versioned=True,
        )

        project_pipeline = codepipeline.Pipeline(
            self, 'epicollect-migrator-pipeline',
            artifact_bucket=artifact_bucket,
            pipeline_name='epicollect-migrator-pipeline',
        )

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        secret_id = self.node.try_get_context('github.token.secretsmanager.secret.id')

        github_token = core.SecretValue.secrets_manager(secret_id=secret_id)

        db_conn = ssm.StringParameter(
            self, "DATABASE_CONNECTION_URI",
            string_value="host='ssifwc-dev.cfm8cse59vi9.us-east-1.rds.amazonaws.com' dbname='postgres' user='postgres' password='shorteststraw'"
        )

        build_project = build.PipelineProject(
            self, 'BuildProject',
            project_name='epicollect-migrator-build',
            description='Build project for epicollect-migrator',
            environment=build.LinuxBuildImage.AMAZON_LINUX_2_3,
            environment_variables={
                'EPICOLLECT_BASE_URL': build.BuildEnvironmentVariable(
                    value='https://five.epicollect.net'),
                'EPICOLLECT_PROJECT_NAME': build.BuildEnvironmentVariable(
                    value='ssi-watershed-stewardship-group'),
                'EPICOLLECT_PROJECT_NAME_2': build.BuildEnvironmentVariable(
                    value='ssi-watershed-groups-version-2'),
                'DATABASE_CONNECTION_URI': build.BuildEnvironmentVariable(
                    value="host='ssifwc-dev.cfm8cse59vi9.us-east-1.rds.amazonaws.com' dbname='postgres' user='postgres' password='shorteststraw'"),
            },
            build_spec=build.BuildSpec.from_source_filename('infra/buildspec.yml'),
        )

        project_pipeline.add_stage(stage_name='CheckoutRepoSource', actions=[
            actions.GitHubSourceAction(
                action_name='CheckoutRepoSource',
                owner=self.node.try_get_context('github.owner'),
                oauth_token=github_token,
                repo=self.node.try_get_context('github.repo'),
                branch=self.node.try_get_context('github.branch'),
                output=source_output,
            )
        ])

        build_project_action = actions.CodeBuildAction(
            action_name='BuildAndDeploy',
            input=source_output,
            outputs=[build_output],
            project=build_project,
            type=actions.CodeBuildActionType.BUILD,
        )
        project_pipeline.add_stage(stage_name='BuildAndDeploy', actions=[build_project_action])

        core.CfnOutput(
            self, 'BuildArtifactsBucketOutput',
            value=artifact_bucket.bucket_name,
            description='Amazon S3 Bucket for Pipeline and Build artifacts',
        )
        core.CfnOutput(
            self, 'CodePipelineOutput',
            value=project_pipeline.pipeline_arn,
            description='AWS CodePipeline pipeline name',
        )


app = core.App()
EpicollectMigratorLambdaPipelineStack(app, "epicollect-migrator-lambda-pipeline")
app.synth()
