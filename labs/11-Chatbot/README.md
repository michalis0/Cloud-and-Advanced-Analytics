<h1 align="center"> LAB 12 - Chatbot</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>

## Learning Goals
In this lab, we will create a chatbot that receives our questions via Gradio and responds via the Gemini API, taking into account the entire conversation history instead of just answering single questions.
## Introduction
Welcome to the twelfth lab of Cloud and Advanced Analytics! In this week, we'll use Vertex AI tool to call GEMINI API

## Lab Walkthrough

Gemini is Google’s cutting-edge artificial intelligence that allows us to develop a wide variety of applications, including chatbots. With Gemini, we can send instructions in text format to create our own solutions.
The Gemini model, as of today, has the use of Gemini 1.5 Pro and Gemini 1.0 Pro text models available


### Pre-Lab Setup 

* Open Google cloud Plateform. Go to IAM Admi -> Service accounts.
* Retrieve the service account that you use for Big query for example.
* Add to your service account these roles:
- Admin AI Platform
- Admin Vertex AI

* Install these packages using *pip* command : **vertexai**, **gradio**


### Exercice

* Download the notebook from GitHub and upload it to Google Colab. This lab is quite short. The aim is to help you get familiar with Gradio. At the end of the notebook, there is an exercise for you to complete. The Pizza chatbot example provides a useful hint for this exercise. Good luck! 😊












