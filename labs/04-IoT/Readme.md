

<h1 align="center"> IoT: Sending Data to BigQuery</h1>
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
By the end of this lab you will learn:

* How to setup an M5stack core2 device and connect it to Internet.
* How to program an M5stack device using the [uiFlow platform](https://flow.m5stack.com/)
* How to insert new data into a bigQuery database.
* How to get current weather data for a specific location using the [openweather api](https://home.openweathermap.org/).
* Creating a web-app with different endpoints using Flask and deploying it using GCloud cloud run.


## Table of contents for exercises: 
1. **Introduction and IOT devices:**

2. **Setting up the weather sensor for measuring the indoor temperature and humidity**

3. **Creating a BigQuery database with the proper schema**
- 3.1 Defining the BigQuery database
- 3.2 Test the BigQuery database we just created 
- 3.3 Insert new rows in the BigQuery table


4. **Creating a new web service that receives data form the IoT device**
5. **Deploying the Flask app in Google Cloud** 
6. **Updating the m5stack.py with the URL of the deployed web service**
7. **Your turn**


## General View of the Lab:

<img width="799" alt="Screenshot 2024-03-12 at 10 51 45" src="imgs/lab-overview.png">


  
