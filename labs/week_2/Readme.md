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
- Query datasets in BigQuery to reinforce your SQL skills

## Introduction
Google BigQuery is a highly scalable and serverless data warehouse provided by Google that allows for rapid SQL queries and data analysis. It supports the analysis of large datasets in real-time, using the robust infrastructure of Google.

BigQuery is designed to make data analysis simple and cost-effective by eliminating the need for database administration and infrastructure management. It provides a convenient interface for loading, querying, and visualizing data.

The service uses standard SQL. Its seamless integration with other Google Cloud services and data visualization tools facilitates a wide range of data science and research applications. Google BigQuery serves as a potent resource for exploring complex datasets and enabling data-driven research


## Lab Walkthrough
In this lab, TAs will demonstrate the following on the Google Console:
* Cloud Storage and buckets 
* Exploring Google Cloud Console features

## Table of contents 
* [Exercise 1 Cloud Storage and Buckets](#exercise-1-cloud-storage-and-buckets)
* [Exercise 2 Big Query](#exercise-2-big-query)

-----------------------------------
### **Exercise 1: Cloud Storage and Buckets**
-----------------------------------

In this exercise we will look on how to create a bucket in Cloud Storage and later we will see how we can call this file to compute SQL queries.

**Step 1: Creation of the Bucket:**

* In the Navigation panel, please click on "Cloud Storage" and on "Buckets"
* Click on the "Create" button
* Enter a name for the bucket, i.e: "cloud_analytics_bucket" and select all default parameters and click "CREATE"
* You can now go to the folder of this project and download the "movie.csv" dataset, we will use this for our cloud storage ! 
* Please select "UPLOAD FILES" and upload the given CSV file

**Hints (in case you get stuck)**

<img width="300" alt="Cloud Storage 1" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/a3f9f550-fd42-4fc6-ad50-047a720aa941">
<img width="400" alt="bucket" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/5f140d33-a6ae-4ae3-9883-17f34216236a">
<img width="300" alt="Screenshot 2024-02-13 at 07 49 05" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/e87f8c65-2849-40ce-8c5b-7a8afcfe621c">

-----------------------------------


**Step 2: Fetching the bucket keys:**

* One powerful aspect of Google Cloud is that we can access this file from any website, and this is what we will try to do ! To do so, please following the steps:
- **Step 1:** Navigate to IAM & Admin and click on "Service accounts"
- **Step 2:** "Create Service Account" and enter a name i.e: Movie-Dataset-CSV-Database-Access and add ad service access "Storage Admin"
- **Step 3:** Once created, click on the created service account and generate Keys, and download them

**Hints (in case you get stuck)**

<img width="320" alt="Screenshot 2024-02-13 at 07 56 30" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/5f7921e1-c66b-4ed8-b3e8-af4b673a7b18">
<img width="320"   alt="Admin" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/13c253dd-b710-4176-b575-5f6577a45c89">
<img width="320" alt="keys1" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/eb21692d-5547-40fa-9ab1-3dab8c75d0af">

-----------------------------------


**Step 3: Python code and connection:**
- **1.** Download the python code in the folder - **streamlit-google-cloud-storage** and open it in your code editor
- **2.** Install the packages :
- ```bash
  !pip install google-cloud-storage
  !pip install pandas
  !pip install streamlit
  !pip install --upgrade google-cloud-speech
- Run the command line: you should be able to see a simple title !  (CF Image)
- ```bash
  streamlit run streamlit-google-cloud-storage.py
- Now you can upload the JSON keys inside the project and change the following paths:
    - Copy the path (RELATIVE Path) and paste it into the "Key path", please also put the bucket name and the file_name
- Run the command line:
- ```bash
  streamlit run streamlit-google-cloud-storage.py

**Hints (in case you get stuck)**

<img width="400" alt="initial" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/f7fbe869-a36a-4246-bcee-312c365ed55a">
<img width="400" alt="final_2" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/5b276ef3-714a-4bb0-b444-0af999596710">

-----------------------------------
### **Exercise 2: Big Query**
-----------------------------------

**NOTE:** In order to connect to the Big Query Database created, you will need to use your Project ID, this can be found by clicking on the Google Cloud Logo and you can simply copy your project ID as shown below:
<img width="651" alt="Screenshot 2024-02-15 at 11 51 24" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/f7b5fe40-ec10-4306-9259-1c39d3364555">

**Step 1: Creation of the database:**

In this section, we will essentially focus on Big Query ! To do so, you can first download this [dataset](https://github.com/michalis0/Cloud-and-Advanced-Analytics/tree/main/labs/week_2/data). Now you can follow these steps:
- **Step 1:** On the left pannel, select **Big Query**
- **Step 2:** Select the **Add** Button
- **Step 3:** Click on **Local File**
- **Step 4:** Change the File format to CSV and import the "Teams.csv"
- **Step 5:** Click on Dataset and add a Dataset ID, i.e: "world_cup" and select Multi-region: EU
- **Step 5:** Put "teams" as the table name
- **Step 6:** Select "Auto Detect", then click on "CREATE TABLE"
- **Step 7:** Now please create another table by clicking the **three dots** next to the dataset and import Players.csv, following the exact same steps as before. Note, as before, please select the correct file format (CSV), Auto Detect and call the table name players (lowercase!).
- **Step 8:** Now please do the same process for the csv PlayersExt.csv and call it as players_and_teams. 


* **Hints (in case you get stuck)**

<img width="400" alt="Big Query" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/0fa7ed55-1e90-4eca-b8e1-9c678acb019d">
<img width="400" alt="add" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/3f053f6c-0625-42d9-a192-8f6293be4e26">

<img width="400" alt="Lcoa" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/7d1e3da5-55f6-4ab9-a726-957041cb91a0">
<img width="400" alt="world" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/726510f9-6680-4b84-b891-595eff210924">

<img width="400" alt="f" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/d1f99c1d-472b-452d-83cf-7fc5957768da">
<img width="400" alt="data" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/57a93cc5-94a7-4eed-9587-59a2b5355165">


**Step 2: Query of the dataset:**

In this section, we will essentially query the dataset that you just created ! Please follow the guidelines on [this Notebook]()

**Final Note:** While we are using sanitized datasets, please keep in mind that when working with large CSV some preprocessing might be necessary to allow the use of SQL queries in your uploaded datasets. 

-----------------------------------


