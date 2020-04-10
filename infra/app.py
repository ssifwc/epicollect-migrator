import os
from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_codebuild as build,
    aws_codepipeline as pipeline,
    aws_codepipeline_actions as actions,
    aws_cloudformation as cfn,
)


class EpicollectMigratorLambdaPipelineStack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        artifact_bucket = s3.Bucket(
            self, 'BuildArtifactsBucket',
            removal_policy=core.RemovalPolicy.RETAIN,
            encryption=s3.BucketEncryption.KMS_MANAGED,
            versioned=True,
        )

        serverless_pipeline = pipeline.Pipeline(
            self, 'ServerlessPipeline',
            artifact_bucket=artifact_bucket,
            pipeline_name='serverless-pipeline',
        )

        source_output = pipeline.Artifact()
        build_output = pipeline.Artifact()

        secret_id = self.node.try_get_context('github.token.secretmanager.secret.id')

        github_token = core.SecretValue.secrets_manager(
            secret_id=secret_id)

        build_project = build.PipelineProject(
            self, 'BuildProject',
            project_name='serveless-pipeline',
            description='Build project for the serverless-pipeline',
            environment=build.LinuxBuildImage.STANDARD_2_0,
            environment_variables={
                'BUILD_ARTIFACT_BUCKET': build.BuildEnvironmentVariable(value=artifact_bucket.bucket_name),
            },
            build_spec=build.BuildSpec.from_source_filename('buildspec.yml'),
        )

        serverless_pipeline.add_stage(stage_name='Source', actions=[
            actions.GitHubSourceAction(
                action_name='SourceCodeRepo',
                owner=self.node.try_get_context('github.owner'),
                oauth_token=github_token,
                repo=self.node.try_get_context('github.repo'),
                branch=self.node.try_get_context('github.branch'),
                output=source_output,
            )
        ])

        serverless_pipeline.add_stage(stage_name='BuildAndDeploy', actions=[
            actions.CodeBuildAction(
                action_name='CodeBuildProject',
                input=source_output,
                outputs=[build_output],
                project=build_project,
                type=actions.CodeBuildActionType.BUILD,

            )
        ])

        core.CfnOutput(
            self, 'BuildArtifactsBucketOutput',
            value=artifact_bucket.bucket_name,
            description='Amazon S3 Bucket for Pipeline and Build artifacts',
        )
        core.CfnOutput(
            self, 'CodePipelineOutput',
            value=serverless_pipeline.pipeline_arn,
            description='AWS CodePipeline pipeline name',
        )


app = core.App()
EpicollectMigratorLambdaPipelineStack(app, "epicollect-migrator-lambda-pipeline")
app.synth()
