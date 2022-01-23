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
(execute only from current directory)

    heroku container:push web -a capstone-p12

**5) Releasing container**

    heroku container:release web -a capstone-p12


> **Footer comment:** \
> Command #3 makes use of the Dockerfile in current directory to create the Docker image 