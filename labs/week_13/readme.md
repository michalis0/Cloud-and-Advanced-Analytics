<h1 align="center"> LAB 13 - Docker</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>


## Introduction
Docker is an increasingly popular tool designed to make it easier to create, deploy, and run applications using containers. But what is Docker? How does it compare to a virtual machine? What are Docker images and containers, and how do they differ? This week, we'll dive into these questions and get hands-on with Docker, learning how to use it effectively in our projects.

## Learning goals
- Comprehend the difference between a Docker container and an image.
- Learn how to run a Docker image.
- Practice with useful Docker commands.
- Understand the concepts involved in building a Docker image.
- Learn how to create a Dockerfile.
- Learn how to build a Docker image.
- Learn how to publish a container's port to the host.

## Lab Walkthrough

### Part 1: Introduction to Docker
Our journey begins with understanding the basic concepts of Docker, differentiating between containers and images, and getting our hands dirty by running a Docker image. You will get a chance to test your Docker installation by running a "hello-world" container.

Test your docker installation:
`docker run hello-world`

### Part 2: building a docker image
After understanding the basics, we'll move on to building our Docker images. This stage will see us dockerizing a simple Flask app, and optionally pushing it to the Docker Hub. Once you have your Docker container, it's straightforward to host the app on the cloud, e.g., GCP, Heroku.


## Exercises
### Exercise 1 - Download an existing docker image and run locally
Next, we will get practical by downloading an existing Docker image from an online repository and running it locally on our machine.
- Go to the repository https://github.com/samik-saha/rasa-chatbot. It contains an implementation of a simple chatbot.
- Open your terminal and clone the repository. `git clone https://github.com/samik-saha/rasa-chatbot.git`
- Go to the directory of the repository you just cloned and build the dockerfile:
  ```
  cd rasa-chatbot
  docker build -t rasa-chatbot .
  ```
- Wait for the build to finish. Then you will be able to start a container and test the chat bot.
  `docker run -it --rm -p 5005:5005 --env-file $(pwd)/.env-sample rasa-chatbot`
- Open a new terminal tab(window) and test the API as instructed in the readme of the repository, e.g:
  ```
  curl --request POST \
  --url http://localhost:5005/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "Hi"
  }'
  ```

### Exercise 2: docker image of ubuntu
In the final part, we will pull an Ubuntu image and interactively explore it. You will install Python and pip inside the container, build a simple Flask app, and run it. Finally, you will test the API of the app from your local machine.
1. Pull an ubuntu image : `docker pull ubuntu`

2. Run the image in interactive mode with the port 5780 opened: `docker run -it -p 5780:5780 <id-image>`
Hint: you can find the id of the image with `docker images`

3. Install python3 and pip3 inside the container
Hint: you can use `apt-get` to install packages

4. Install flask and requests with pip3 : `pip3 install flask requests`

5. Create a simple flask app called server.py that returns "Hello world" when you go to the url http://localhost:5780/
Hint: you can use nano to create the file with the command `nano server.py` and then copy paste the following code:

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Client!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5780)
```

6. Run the flask app with `python3 server.py`

7. Open a new terminal tab(window) and test the API as instructed in the readme of the repository, e.g:
  ```
  curl --request GET \
  --url http://localhost:5780/
  ``` 

EXTRA:
You can use add more functionalities to the app by creating additional functions and decorators. For example, you can create a function that returns the current time when you go to the url http://localhost:5780/time


# Ressources:
We've also compiled a list of related tutorials and exercises to practice your Docker skills further. By the end of this module, you should be well-versed in the basics of Docker and be ready to integrate it into your workflow. Related tutorials are available to help reinforce and expand your understanding of Docker, and solutions are provided for each exercise.
- Running a Docker image in interactive mode: https://www.youtube.com/watch?v=QBOcKdh-fwQ&t=681s
- Creating an building a dockerfile: https://www.youtube.com/watch?v=LQjaJINkQXY
- Dockerizing python applications: https://runnable.com/docker/python/dockerize-your-python-application
- Convert a Python flask app to Docker container: https://www.youtube.com/watch?v=prlixoDIfrc
- Convert a Python flask app to Docker container (blog post): https://blog.logrocket.com/build-deploy-flask-app-using-docker/
- Deploying a dockerized flask app to google cloud: https://towardsdatascience.com/deploy-a-dockerized-flask-app-to-google-cloud-platform-71d91b39b25e


Solution of the exercise 1:
https://github.com/lvthillo/python-flask-docker

Enjoy exploring the world of Docker!