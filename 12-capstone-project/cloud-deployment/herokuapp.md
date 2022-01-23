# Deployment process of containeraized app to Heroku cloud

Below, we describe briefly how to operate **Heroku CLI** from the command shell. \
To previosly download and install the software, follow the instructions from [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli) 

`1) Login to Heroku`

    heroku login

`2) Login to Heroku Containers`

    heroku container:login

`3) Creating app` \
("capstone-p12" is here an arbitrary name for this exercise)

    heroku create capstone-p12

`4) Pushing docker image pointing to the app` \
(execute only from current directory)

    heroku container:push web -a capstone-p12

`5) Releasing container`

    heroku container:release web -a capstone-p12
\
**Important comment:**
> In step #3 Heroku makes use of the Dockerfile in the current directory, creating the image locally before pushing it to the cloud

## Lessons learned

Heroku uses a different port each time it runs a container, so we need to capture the port as an environment variable and pass it to the app. \
This is implemented as follows in predict.py code:

    import os
    current_port = int(os.environ.get('PORT'))

**About the Dockerfile:** \
No binding should be specified for the entrypoint command. \
And most importantly, the ENTRYPOINT must be replaced by  a CMD statement. The former cannot be overridden later by the server and is rejected by Heroku (especially when passing parameters to the gunicorn/uvicorn execution)
