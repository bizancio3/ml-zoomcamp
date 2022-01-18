# Deployment process of containeraized app to Heroku cloud

Below, we describe briefly how to operate `Heroku CLI` from the command shell. \
To previosly download and install the software, follow the instructions from [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli) 

**1) Login to Heroku**

    heroku login

**2) Login to Heroku Containers**

    heroku container:login

**3) Creating app** \
("capstone-p12" is here an arbitrary name for this exercise)

    heroku create capstone-p12

**4) Pushing docker image pointing to the app**

    heroku container:push -a capstone-p12

**5) Releasing container**

    heroku container:release web -a capstone-p12


> ### Footnote: 
> Command # 3 will use the Dockerfile from the current directory to build the Docker image
> *(which implies that one must first access this folder from the terminal)*