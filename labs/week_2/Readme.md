<h1 align="center"> Lab 2: Data-Buckets & BigQuery</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>


Welcome to this week's lab where we will delve into Google Storage and BigQuery. We will learn to leverage this powerful tool within our notebooks and enhance our SQL knowledge.

## Learning Goals
By the end of this lab, you will be able to:
- Understand the functionalities and navigation of Google BigQuery and Cloud Storage
- Upload and explore data in BigQuery
- Query public datasets in BigQuery to reinforce your SQL skills

## Introduction
Google BigQuery is a highly scalable and serverless data warehouse provided by Google that allows for rapid SQL queries and data analysis. It supports the analysis of large datasets in real-time, using the robust infrastructure of Google.

BigQuery is designed to make data analysis simple and cost-effective by eliminating the need for database administration and infrastructure management. It provides a convenient interface for loading, querying, and visualizing data.

The service uses standard SQL. Its seamless integration with other Google Cloud services and data visualization tools facilitates a wide range of data science and research applications. Google BigQuery serves as a potent resource for exploring complex datasets and enabling data-driven research


## Lab Walkthrough
In this lab, TAs will demonstrate the following on the Google Console:
* Cloud Storage and buckets 
* Exploring Google Cloud Console features, specifically Billing, Storage, Big Query, AI, Cloud Functions
* Introduction to serverless backend with Cloud Functions 


## Table of contents 
* [Exercise 1 Cloud Storage and Buckets](#step-1-TMDB-API-Key)
* [Exercise 2 Big Query](#step-3-data-cleaning)

-----------------------------------
### **Exercise 1: Cloud Storage and Buckets**
-----------------------------------

In this exercise we will look on how to create a bucket in Cloud Storage in Google Cloud and later we will see how we can call this file to compute SQL queries.

**Step 1: Creation of the Bucket:**

* In the Navigation panel, please click on "Cloud Storage" and on "Buckets"
* Click on the "Create" button
* Enter a name for the bucket, i.e: "cloud_analytics_bucket" and select all default parameters and click "CREATE"
* You can now go to the folder of this project and download the "movie.csv" dataset, we will use this for our cloud storage ! 
* Please select "UPLOAD FILES" and upload the given CSV file

**Step 2: Fetching the bucket keys:**

* On powerful aspect of Google Cloud is that we can access this file from any website, and this is what we will try to do ! To do so, please following the steps:
- Step 1: Navigate to IAM & Admin
- Step 2: "Create Service Account" and enter a name i.e: Movie-Dataset-CSV-Database-Access and add ad service access "Storage Admin"
- Step 3: Once created, click on the created service account and generate Keys, and download them

**Step 3: Python code and connection:**

- Step 1: Download the python code in the folder - **streamlit-google-cloud-storage**
- Download the code and install the packages : !pip install google-cloud-storage,  !pip install pandas, !pip install streamlit, pip install --upgrade google-cloud-speech
- Run the command line: streamlit run streamlit-google-cloud-storage.py, you should be able to see a simple title ! 
- Now you can upload the JSON keys inside the project and change the following paths:
    - Copy the path (RELATIVE Path) and paste it into the "Key path", please also put the bucket name and the file_name
- Run the command line: streamlit run streamlit-google-cloud-storage.py, you should be able to see this ! Done. 










- Step 3: Add "bucket storage" to grand this service account access 

Click the "Create Service Account" button.
Enter a name for the service account, set a role (e.g., Storage > Storage Object Admin if you need access to Cloud Storage), and click "Continue."
Click "Done" to skip granting additional permissions (you can do this later if needed).



* **Hints (in case you get stuck)**