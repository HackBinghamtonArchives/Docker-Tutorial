![alt](http://1000logos.net/wp-content/uploads/2017/07/Docker-Logo-500x148.png)

![alt](http://flask.pocoo.org/static/logo/flask.png)

# Flask example using Docker
This repository is to demonstrate how to create, run, and publish a Docker App. Currently, there
is an example for putting a Flask Web App into a Docker Container, making it runnable from any
computer with Docker regardless of system, environment, libraries, etc.

## What is Docker?
Taken straight from their website:

> Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers. The use of Linux containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

## Installing Docker
Visit this page: [https://docs.docker.com/install/](https://docs.docker.com/install/)

### Avoiding Root Privelige Issues (Mac/Linux)
```
# Create a docker user group
sudo groupadd docker
# Add yourself to the user group
sudo usermod -aG docker $USER
# Logout (or Ctrl+D) and open new terminal for it to take effect
exit
```

If you don't want docker to have root privelige by default, just add `sudo` before
every `docker` command for the rest of this tutorial.

### Testing your Docker Install
```
docker run hello-world
```

### Run my docker app anywhere
Here is an example of running a Docker app I created from anywhere without any environment setup:
```
docker run -p 80:80 rmccorm4/flask_example:latest
```

## Creating your own Docker Container

### Creating Dockerfile
Create a file called `Dockerfile`.

Add the following to your `Dockerfile`:

```
# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable $NAME equal to "FlaskBU"
# This isn't necessary, just demonstrating that you can do this
ENV NAME FlaskBU

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### Creating Flask App

#### requirements.txt
Our Dockerfile will try to install Python libraries from a `requirements.txt` file, so
create a `requirements.txt` and just add the word `Flask` to the first line:

On Mac/Linux, just run:

```
echo Flask > requirements.txt
```

#### app.py
This is the Python code that utilizes the `Flask` library to ship a Web App super quickly and easily!
Normally you would you need the right Python version installed to run someone else's code correctly, 
and for a Flask App you would need to install `Flask` using a package manager like `pip`, but `pip` would
have to be the correct version to install the correct version of `Flask` and so on...

Docker gets rid of all that version handling and packages everything into a Container that will work the same
way for everyone's computers.

`app.py` should contain:

```
import os
import socket

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Container ID:</b> {hostname}<br/>" \
           "<img src={image} alt={image}>"

    return html.format(name="Docker", hostname=socket.gethostname(), image='/static/head.jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

Make sure you create a `static` directory containing the image of your choice to be displayed
on your flask app. I have chosen `head.jpg` for example, and placed it in the `static/` directory.

### Building Container
We need to "build" the docker container to put everything together
```
# Creates an image named hello
docker build -t FlaskBU .
```

### Running Container
We're going to run our container to make sure it worked correctly:
```
# Run your local image
docker run -p 80:80 FlaskBU
```

### Publishing Container
Now we're going to make this Docker Container public so anyone can run it.

#### Create a Docker Account
Go to this website to create a Docker account so you can publish your Docker container:

[https://hub.docker.com/login](https://hub.docker.com/login)

#### Login to Docker Account
```
docker login
```

#### Push to a Repository
```
docker push YOUR_USERNAME/FlaskBU:latest
```

### Running your Published Container
```
docker run -p 80:80 YOUR_USERNAME/FlaskBU:latest
```
