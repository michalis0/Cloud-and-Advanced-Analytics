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
* [Exercise 3 Hints for Assignment 1](#exercise-3-hints-for-assignment-1)

-----------------------------------
### **Exercise 1: Cloud Storage and Buckets**
-----------------------------------

In this exercise we will look on how to **create a bucket in Cloud Storage** and later we will see how we can call this file to **compute SQL queries**.

**Step 1: Creation of the Bucket on Google Cloud:**

* **1.1** Please go to your [Google Cloud Console](https://console.cloud.google.com)
* **1.2** In the Navigation panel, please click on **"Cloud Storage"** and on **"Buckets"** (you can also search for "Buckets" in the search bar)
* **1.3** Click on the **"Create"** button
* **1.4** Enter a name for the bucket, i.e: **"caa-bucket"**, change the Location type to **region** and select **europe-west6 (Zurich)** and keep other default parameters. Now you can click **"CREATE"**
* **1.5** You can now go to the folder of this project and download the [file](https://github.com/alexerne-git/big_scale_analytics_2024/blob/main/labs/2-BigQuery/movies.csv) **"movies.csv"** dataset, we will use this for our cloud storage ! (**Hint:** To make it easier for future labs, you can clone the project on a private repository and pull each week. In this specific case, you can also download directly the file on Github - Go on the file and click on Download raw file <img width="20" alt="Download" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/e152ee70-4b27-4ce7-843d-d3c51e00778d"/>)
* **1.6** Now you can go back to your **bucket** select **"UPLOAD FILES"** and upload the given CSV file (movies.csv) - you should be able to see it in your uploaded files)

----

**Done! Recap of what was done**
- You imported your first file on Google Cloud Storage
- This facilitates access and storage of data on the cloud - in particular large files
- It is much more effective to store csv dataset files in Cloud Storage compared to Github.
- Github has a maximum individual file size of 100MB while google cloud storage accepts files up to 5TB.
- Google Cloud Storage could also be used as backup for files. 

**A few words on movies.csv:** This dataset contains three columns: movieId, title and genres and has a total of 27'278 rows
* <img width="450" alt="movies.csv" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/7bfce60b-8e18-4a8e-b9f7-34befb8b38a3">

----

**Hints (in case you get stuck)**

* <img width="500" alt="Cloud Storage 1" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/68726c3d-4979-4939-a4be-0eff530bb6da">
* <img width="500" alt="Cloud Storage 1" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/fa8b2b13-6414-464f-98d2-b47bbd023dd4" >

-----------------------------------


**Step 2: Fetching the bucket keys:** One powerful aspect of Google Cloud is that we can access this file from any website, and this is what we will try to do ! 

**Recall:** Why do we need keys ? 
  - Secure files by controlling access to them.
  - Authenticate and authorize specific users to access and manipulate the files

To generate authentification keys, please following the steps:
- **2.1:** Navigate to IAM & Admin and click on **"Service accounts"** (you can also search in the search bar for **Service account**)
- **2.2:** **"Create Service Account"** and enter a name i.e: **movie_dataset_csv_bucket**. You now need to grant this service account access to the bucket files. To do so, click on **Select a role** and select **Storage Admin** and click **CREATE**
- **2.3** Once created, click on the **created service account** should look like something like *movie-dataset-csv-bucket@your_project_name.iam.gserviceaccount.com*, click on the three dots <img width="10"   alt="Admin" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/74805f93-ff4c-4b08-a946-a6e89efb4f7e"> select **manage keys**.
- **2.4** Click on **ADD KEY** - **Create new key** - **key type: JSON** and click on **CREATE**

**Hints (in case you get stuck)**

<img width="320" alt="key_1" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/427f88e6-92e9-4e95-9ab8-8d062402b40f">
<img width="320" alt="key_2" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/c2679a98-9cc9-483f-8096-4f0888f711de">
<img width="320" alt="key_3" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/44100bec-fb20-4e52-8403-67ee98a7b14f">

- **Please check everything is working correctly !** By running this [Notebook](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/2-BigQuery/Keys_verification_cloud_storage.ipynb) (you can import it directly on Google Colab - open from Github - select your repository and notebook Keys-verification-cloud-storage.ipynb - then open it, you can then edit it and push it (file - save a copy on Github). 


-----------------------------------


**Step 3: Python code and connection:**
- **1.** Download the python code in the folder - [**streamlit_google_cloud_storage**](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/2-BigQuery/streamlit_google_cloud_storage.py) and open it in your code editor
- **2.** Install the packages/libraries :
- ```bash
  pip install streamlit 
  pip install google-cloud-storage
  pip install pandas
  pip install seaborn
  pip install matplotlib
  **If you are having error with google-cloud-storage** pip install --upgrade google-cloud-speech
- Run the command line: you should be able to see a **simple title** and an error **because the keys are still not imported** !  (CF Image)
- ```bash
  streamlit run streamlit_google_cloud_storage.py
- Now you can **upload the JSON keys** inside the project and change the following paths:
    - Copy the path (RELATIVE Path) and paste it into the **"big-scale-analytics-YOUR_PATH.json"**, please also put the **bucket_name** and the **file_name**
- Run the command line:
- ```bash
  streamlit run streamlit_google_cloud_storage.py

**Hints (in case you get stuck)**

<img width="400" alt="initial" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/f7fbe869-a36a-4246-bcee-312c365ed55a">
<img width="400" alt="final_2" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/5b276ef3-714a-4bb0-b444-0af999596710">

**Done! Recap of what was done**
- You imported the movie.csv dataset on Google Cloud Storage
- You create keys to access that file stored on Google Cloud
- You called that file using a function and imported it using a pandas dataframe
- You then displayed that csv file using streamlit !
- If you feel motivated, you can deploy the app on Google Cloud Run (as we did on Lab 1)

<img width="400" alt="final_2" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/6b7d0315-523a-4338-a2ec-61c52aab3c14">

-----------------------------------
### **Exercise 2: Big Query**
-----------------------------------

**What is Big Query and why do we use it ?**
- BigQuery allows to handle large datasets (in different formats, i.e: CSV) and complex SQL queries from your datasets
- It manages the infrastructure for you
- Provides easy integrations to websites or other Google Cloud services

**Pre-requirements:** In order to connect to the Big Query Database, you will need to use your Project ID, this can be found by clicking on the Google Cloud Logo and you can simply copy your project ID as shown below:
<img width="651" alt="Screenshot 2024-02-15 at 11 51 24" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/f7b5fe40-ec10-4306-9259-1c39d3364555">

-----------------------------------

**Step 1: Creation of the database:**

In this section, we will essentially focus on Big Query ! To do so, you can first download this [dataset](https://github.com/michalis0/Cloud-and-Advanced-Analytics/tree/main/labs/2-BigQuery/data). 

<img width="651" alt="dataset" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/20c9e6f0-76ef-4920-9e34-d51e57cc1657">


Now you can follow these steps:
- **1.1** On the left pannel, select **Big Query** or type **Big Query** in the search bar
- **1.2** We are now going to create our first **table** Select the **Add** Button
- **1.3** Click on **Local File**
- **1.4** **BROWSE** file and select **Teams.csv**
- **1.5** Click on **Dataset** and **CREATE A NEW DATASET**. In the **Dataset ID** add **world_cup** and select **Region**, put Zurich (or europe-west6) and click **CREATE DATASET**
- **1.6** Under **Table** insert the table name, in our case **players** (lowercase!) and select for the **Schema** -> **Auto detect** and click **CREATE TABLE**
- **1.7** You just created your first table ! you can click on the table and then on the plus symbol (<img width="20" alt="Screenshot 2024-02-15 at 11 51 24" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/9566de9f-7d28-4a33-87d6-9cb58bf82db5"/>). This opens an editor window, on which you can do SQL queries. Copy and paste the following SQL query to get all the teams from the table players in the database world_cup
- ```
    SELECT team FROM `YOUR_PROJECT_ID.world_cup.players` 

- **1.8** On the left menu, you can select the three dots next to **world_cup** and select **Create table**
- **1.9** As before, select **Create table from** and select **Upload**, then import **Browse** - select file **Teams.csv**,call the table **teams** (lowercase), select **Schema** -> **Auto detect** and click **CREATE TABLE**
- **1.10** Finally, do the same for the last table. Select **Create table from** and select **Upload**, then import **Browse** - select file **PlayersExt.csv**,call the table **players_and_teams** (lowercase), select **Schema** -> **Auto detect** and click **CREATE TABLE**
- **1.10** Done ! You just created your first Big Query Database

* **Hints (in case you get stuck)**

<img width="400" alt="Big Query" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/83ef700a-b831-445d-97e4-1279b4cc1beb">
<img width="400" alt="Big Query" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/623b28d8-be41-4ba4-8c71-9165ddd9bb2c">

-----------------------------------

**Step 2: Query of the dataset:**

In this section, we will essentially query the dataset that you just created ! Please follow the guidelines on [this Notebook](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/2-BigQuery/data/week_02_exercises_big_query.ipynb)


-----------------------------------
### **Exercise 3: Hints for Assignment 1**
-----------------------------------

**Note:** While here we are using sanitized datasets, please keep in mind that when working with large CSV some preprocessing might be necessary to allow the use of SQL queries in your uploaded datasets. For example, let's try to import a larger dataset.

For your information, the datasets we imported now were of size:
- **Players.csv:** 23.2 KB
- **Teams.csv:** 963 Bytes
- **PlayersExt.csv:** 34.3 KB
But in practice, those files are much larger, and Google Cloud can handle those larger files.

The dataset used for the assignment 1 - ratings.csv is **520 MB**. Therefore when importing it on Google Big Query you will receive this message **Local uploads are limited to 100MB. please use Google Cloud Storage**

Therefore, we will follow this suggestion using the following steps:
- Create a new bucket, i.e: **big_rating_dataset**
- Select **Region** - **Zurich** and click on **CREATE**
- **Click** on upload files and upload the dataset and wait for the upload to complete
- **Go back to Big Query** and create a new table, but this time instead of selecting **Upload** select **Google Cloud Storage** and **BROWSE** and select the CSV file in your bucket

**Hints (in case you get stuck)**

<img width="400" alt="Big Query" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/325c2320-b9b5-41bd-a29b-255e960cce78">


