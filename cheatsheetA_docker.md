# Docker

## Terminology

* Container: environment that uns an applications that is not dependent on the OS. Kind of like a lightweight VM. Containers are ***stateless***; if you need to update the components inside, create another container instead.
* Image: template to create a container. Its components are defined by a `Dockerfile`.
* Volume: storage area detached from the container for maintaining state.
* Foreground/interactive vs background/detached: a detached container runs in the background whereas an interactive container will usually have a terminal of some sort for interacting with.

## Commands

List your local images

* `docker images`

Clean up images (many ways)
* `docker images -q -f dangling=true`
* `docker image rm`
* `docker image prune`

List your running containers
* `docker ps`

Run a Docker image inside a container

* `docker run -it --rm image_name:tag`
    * `-it` is a combination of `-i` (interactive mode) and `-t` (allocate a terminal).
    * `--rm` means that the container will be removed when exited.
    * You may find Docker images at the [Docker Hub](https://hub.docker.com/).
    * This command will use the entrypoint defined by the image. It won't necesarily open a terminal inside the container.

Run a Docker image inside a container and override the entrypoint
* `docker run -it --rm --entrypoint=bash image_name:version`
    * This will override the entrypoint of your image and open a bash terminal inside the container instead.

Run a Docker image inside a container and map a port in the container to a port in the host machine
* `docker run -it --rm -p 9696:9696 image_name:tag`

Create a `Dockerfile` with instructions to create a basic custom Docker image.

        # set base image
        FROM python:3.9

        # set the working directory in the container
        WORKDIR /app

        # copy dependencies to the working directory
        COPY requirements.txt .

        # Install dependencies
        RUN pip install -r requirements

        # Copy code to the working directory
        COPY . /app

        # command to run on container start
        CMD ["python", "./main.py"]

* Docker will process each line as a layer. Some layers are cached, so in order to speed up build time, first copy and run immutable objects and then take care of your code/modules, as shown in this example.
* Base images are useful because they save a lot of work and build time. Choose a lean base image and avoid unnecessary packages.
* Each container should only have one concern. Decouple applications into multiple containers.

Create a slightly more complex `Dockerfile` with pipenv dependencies and specific entrypoints.

        # set base image
        FROM python:3.9

        # (pipenv) install pipenv
        RUN pip install pipenv

        # set the working directory in the container
        WORKDIR /app

        # (pipenv) copy dependencies to the working directory
        COPY ["Pipfile", "Pipfile.lock", "./"]

        # (pipenv) Install dependencies
        # (pipenv) We don't need a virtualenv in Docker, so we can install dependencies to the system
        RUN pipenv install --system --deploy

        # Copy the model
        COPY ["predict.py", "model.bin", "./"]

        # Expose a port on the container
        # Remember to map the port to a port in the host when running the container!
        EXPOSE 9696

        # Specify entrypoint
        ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

* The `COPY` instruction has 2 forms, shown here. The second form (like for pipenv in this example) must be used if any paths may contain whitespaces. The last param is always the destination directoy, which may be `.` or `./` for copying to the directory specified by `WORKDIR`.

Build an image based on a Dockerfile

* `docker build -f Dockerfile -t my_image .`
    * The default Dockerfile that the command will look for is `$PATH/Dockerfile`. If your `Dockerfile` is in the same directory that you will run the command and you have not named it something else, `-f Dockerfile` can be removed from the command.
    * `my_image` will be the name of your image. You may optionally tag it like so: `my_image:my_tag`.