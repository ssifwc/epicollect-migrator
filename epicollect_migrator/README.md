# SSIFWC - Epicollect Migrator

This a service that activates once every 24hrs to transfer newly gathered Epicollect points into the SSIFWC postgres database.

## Setup

Install Serverless:

    npm install -g serverless
    
Install Serverless Python Requirements

    sls plugin install -n serverless-python-requirements
    
 Create a `serverless.env.yml` file which is used as part of the deployment process. Here is an example:
 
 ```buildoutcfg
dev:
  EPICOLLECT_BASE_URL: xxxxx
  EPICOLLECT_PROJECT_NAME: xxxxx
  EPICOLLECT_CLIENT_ID: xxxxx
  EPICOLLECT_CLIENT_SECRET: xxxxx
  EPICOLLECT_PROJECT_NAME_2: xxxxx
  EPICOLLECT_CLIENT_ID_2: xxxxx
  EPICOLLECT_CLIENT_SECRET_2: xxxxx
  DATABASE_CONNECTION_URI: xxxxx
  BUCKET_NAME: xxxxx
```

## Deployment

Deployment requires only a simple serverless command, dependencies are installed automatically:

    sls deploy