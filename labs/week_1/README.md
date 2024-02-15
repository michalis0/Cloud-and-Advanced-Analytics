<h1 align="center"> LAB 1 - INTRO TO GCP</h1>
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
By the end of this lab, you should gain familiarity with the Google Cloud console and have made your first small-scale usage experiments.

## Introduction
Welcome to the first lab of Cloud and Advanced Analytics! In this week, we'll introduce you to cloud-based services, focusing primarily on **Google Cloud**, a leading platform in cloud services.

## Lab Walkthrough
In this lab, TAs will demonstrate the following on the Google Console:
* Google Cloud account setup
* Exploring Google Cloud Console features, specifically Billing, Storage, Big Query, AI, Cloud Functions
* Introduction to serverless backend with Cloud Functions
* Deploying your first streamlit app in Google Cloud

### Pre-Lab Setup 
Please follow these steps to prepare for this week's lab:

1. **Communication**:
    - Join our workspace on [Slack]([https://join.slack.com/t/cloud-and-analytics23/shared_invite/zt-1oh2n2asy-l70~dhXVmgy34cqgvRLheg](https://join.slack.com/t/cloudadvanced-kyj1491/shared_invite/zt-2carw20n5-u6bD1CC1mHRq4vI~RRR6_Q)). This will serve as our primary mode of communication.
2. **Google Cloud Setup**:
    - Create a Google account with your academic email address (if you do not already have one) on [Google Cloud](https://cloud.google.com). This needs to be a Google account.
    - Please do NOT activate your free $300 trial on Google Cloud yet. We will utilize this for a project later in the course. Instead, we'll start with a voucher.
3. **Voucher Redemption**:
    - Redeem the student voucher code we provided, using your .unil or .epfl account. See instructions in Moodle.
    - Verify that the $50 voucher code has been applied to your account by checking the billing tab on your Google Cloud Profile.
    - Important note: For the Google Cloud account, the student code will give you a free $50 credit. Once you've exhausted this, you'll need to enter your credit card information (you won't be charged). This simply verifies that you are not a bot. At this point, you'll receive a free $300 credit valid for 3 months. More details are available [here](https://edu.google.com/programs/students/?modal_active=none).

Make sure to create your account by the end of this week. Thereafter, familiarize yourself with various Google Cloud features. 

If you need help, consult the [Google Cloud Documentation](https://cloud.google.com/docs). This resource offers a comprehensive guide on using their services, alongside numerous code examples.

## Requirements

- [ ] GitHub account
- [ ] Google Cloud Account (with credits / credit card activated)
- [ ] Python Installed
- [ ] Code editor (Visual Studio Code)

--------------

## Table of contents for exercises: 
* [Exercise 1 TMDB API Key](#exercise-1-tmdb-api-key)
* [Exercise 2 Google Cloud Function with API Key](#exercise-2-google-cloud-function-with-api-key)
* [Exercise 3 Streamlit App and Deploying on Google Cloud Run](#exercise-3-streamlit-app-and-deploying-on-google-cloud-run)

-----------------------------------
### Exercise 1: TMDB API Key
-----------------------------------

We will be using the TMDB (The Movie DataBase) website to fetch information about movies, TV shows and actors, including details such as cast, ratings and user reviews. To do so, we will need to set up an API key to fetch this information. In this step we will focus on the creation of the account to get access to the API key. This can be done following this [link](https://www.themoviedb.org/signup)

**Main Steps:** 
1. Go to the profile and get the API Key using this [link](https://www.themoviedb.org/settings/api/request)
2. Select Developper - Accept the terms and conditions
3. You should now be able to see your API key (copy your API key for later use)
4. Now we can go back to the [API page](https://developer.themoviedb.org/reference/account-rated-movies) and you can play around to test the different requests i.e: GET / PUT / POST requests. An example could be the following: https://developer.themoviedb.org/reference/genre-movie-list - clicking on **Try it** you should receive the response from the request. 

**Hints (in case you get stuck):**

<img width="300" alt="TMDB Profile" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/9eba5cb3-d082-4a19-9efe-c1a375339f27">
<img width="300" alt="TMDB API Key" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/e6e46ffa-c4a1-4dc6-b1ea-49242d7f2ff0">
<img width="300" alt="Example Request" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/fcafddb1-d7b8-41be-a553-df8563b2370a">


-----------------------------------
### **Exercise 2: Google Cloud Function with API Key**
-----------------------------------

This exercise aims to familiarize yourself with Google Cloud Functions. You'll create a cloud function to retrieve different movies and specific movie posters using the API.

**Then General Steps are as follows:**

0. Check to see that the API key works correctly
1. Write a function on GCP in Python
2. Deploy the function on Google Cloud Platform
3. Call the function from a Notebook (using Google Colab). 
4. Please repeat those steps for the second function on the Notebook

**Step by Step Guide: In case you get stuck:**
* From the side menu, go to _View all products_ > _Serverless_ > _Cloud Functions_, or search for _Cloud Functions_ in the Search bar at the top.
* <img width="680" alt="Google Cloud Function" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/df6e4750-3129-48e3-967e-4584db23dd4a">
* Create a simple Python function that can be triggered over HTTP. Make sure to pick the "Allow unauthenticated invocations" option.
* <img width="400" alt="Unothenticated" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/535ec37a-459c-425a-962e-f4d6e00f17e9">
* You can now copy paste the code from the Notebook (by uncommenting the 3 lines and adding the packages in the requirements.txt)
* Please do not forget to put the same entry point as the function name:
* <img width="400" alt="Entry point" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/7c7da4d2-a24f-4787-8ac6-4992afb173b3">
* After having deployed your function, call it using its URL, trying different values for the Movie IDs (CF notebook)

-----------------------------------
### **Exercise 3 Streamlit App and Deploying on Google Cloud Run**
-----------------------------------

**The steps are as follows:**
1. Create a Streamlit Project and call the two Google Cloud Functions
2. Dockerize the project
3. Deploy the App on Cloud Run !

---


**Step 1:** Download the Skeleton code and try out your functions! 
- Recall: Streamlit is an open-source Python library that enables rapid creation of interactive web applications for data science and machine learning with minimal code.
- You can find attached a folder called **streamlit_app**, this folder contains three files: app.py, requirements.txt and Dockerfile
- Please download streamlit: pip(3) install streamlit
- Add the two URLs from Google Cloud and Run your App and run the following command: Streamlit run app.py
- You should be able to see something like this.
- <img width="520" alt="Streamlit" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/1cfe2cb0-eb0b-4a55-b678-747810ed96fa">

---


**Step 2:** Two possibilities: Dockerize the Web-Application and deploy it on Google Cloud Run: 
- Recall: Docker is a platform and toolset for developing, deploying, and running applications in lightweight, portable containers, facilitating consistent and reproducible software environments across different systems.



**Step 2.1:** 
- Go to Cloud Storage and create a new bucket, called: "my-streamlit-website" and select a region in Europe
- Once your Bucket is created, you can import the project folder with your JSON key and all the configurations done before ! 
- Then please select "Activate Cloud Shell" on the top right corner
- Once the shell is open, please copy paste this line: This allows to access the project you just imported on Cloud Storage ! 
-   ```bash
    gsutil cp -r gs://BUCKET_NAME/FOLDER_NAME ~/
-   ```bash
    cd ~/FOLDER_NAME
- Type ls to make sure all the files are present in your directory 
- Build the docker image using:
-   ```bash
    docker build -t gcp-api-website .
- Push Docker image to Google Container Registry (GCR).
-  ```bash
    gcloud builds submit --tag gcr.io/PROJECTID/gcp-api-website
- Deploy the app:
-  ```bash
   gcloud run deploy --image gcr.io/PROJECTID/gcp-api-website --region europe-west1 --allow-unauthenticated
- You should now see an URL which allows you to access your deployed website ! 


**Step by Step Guide: In case you get stuck:**

<img width="400" alt="bucket_2" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/9b3d6701-14e0-44a7-a733-86a2d7d5ad4d">
<img width="400" alt="bucket_3" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/ded3b8f8-04a0-4407-b2b3-a37bcb1f2b90">

<img width="400" alt="bucket_4" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/fb84b2b6-e190-473b-b47a-4c2dc6c20614">
<img width="400" alt="cloud shell" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/39595a10-d2a2-4ce7-bb70-62caac904827">


---



**Step 2.2: (more challenging!)** 
- Please connect to the Google Cloud from your code editor: **gcloud auth login**
- Once logged in, now get the project name: **gcloud config get-value project**, copy your project name
- ```bash
     docker build -t gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest .
- ```bash
  docker push gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest
- ```bash
  gcloud run deploy streamlit-website-deployed --image gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest --platform managed
  
**Note** you can select a deployment server in Europe, i.e: number 13: [13] europe-central2

Wait 2-3 minutes and Done ! You should have access to an URL allowing you to access your website from the Cloud ! 

<img width="744" alt="final" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/0f0736d9-dfb3-48c0-9da0-701342bb6680">








  


