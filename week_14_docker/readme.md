# Part 1: Introduction to Docker

We will learn about Docker and its advantages. We will answer to the following questions:
- What is Docker? How is it different from a virtual machine?
- What are images and containers and what is their difference?

Test your docker installation:
`docker run hello-world`

## Goals

1. Understand the difference between a container and an image
2. How to run a Docker image
3. Practicing some useful Docker commands


# Part 2: building a docker image

We will now see how to dockerize and run a simple flask app.

Optional: push the repo to docker hub

FYI: once you have your docker container, it is easy to host the app on cloud, e.g. GCP, heroku

## Goals
1. Understand concepts in building a docker image
2. How to create a dockerfile
3. How to build an image
4. How to publish a container's port to the host


## Exercise: build and run the sentiment analysis app from week 7


# Part 3: pulling a docker image


## Exercise - Download an existing docker image and run locally
- go to the repository https://github.com/samik-saha/rasa-chatbot. It contains an implementation of a simple chatbot.
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

# Part 4: walkthrough of a docker image of ubuntu

## Exercise - 
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


# Related tutorials:

- Running a Docker image in interactive mode: https://www.youtube.com/watch?v=QBOcKdh-fwQ&t=681s
- Creating an building a dockerfile: https://www.youtube.com/watch?v=LQjaJINkQXY
- Dockerizing python applications: https://runnable.com/docker/python/dockerize-your-python-application
- Convert a Python flask app to Docker container: https://www.youtube.com/watch?v=prlixoDIfrc
- Convert a Python flask app to Docker container (blog post): https://blog.logrocket.com/build-deploy-flask-app-using-docker/
- Deploying a dockerized flask app to google cloud: https://towardsdatascience.com/deploy-a-dockerized-flask-app-to-google-cloud-platform-71d91b39b25e


Solution of the exercise 1:
https://github.com/lvthillo/python-flask-docker
