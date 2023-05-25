# Part 1: Introduction to Docker

We will learn about Docker and its advantages. We will answer to the following questions:
- What is Docker? How is it different from a virtual machine?
- What are images and containers and what is their difference?


## Goals

1. Understand the difference between a container and an image
2. How to run a Docker image
3. Practicing some useful Docker commands


# Part 2: building a docker image

We will now see how to dockerize and run a simple flask app.

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


### Related tutorials:

- Running a Docker image in interactive mode: https://www.youtube.com/watch?v=QBOcKdh-fwQ&t=681s
- Creating an building a dockerfile: https://www.youtube.com/watch?v=LQjaJINkQXY
- Dockerizing python applications: https://runnable.com/docker/python/dockerize-your-python-application
- Convert a Python flask app to Docker container: https://www.youtube.com/watch?v=prlixoDIfrc
- Deploying a dockerized flask app to google cloud: https://towardsdatascience.com/deploy-a-dockerized-flask-app-to-google-cloud-platform-71d91b39b25e

