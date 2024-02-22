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
    - Redeem the voucher and add it in your Google Cloud Account using this [link](https://console.cloud.google.com/edu?_ga=2.76628693.1729908852.1708547866-247021585.1677676382), more information [here](https://cloud.google.com/billing/docs/how-to/edu-grants)
    - Verify that the $50 voucher code has been applied to your account by checking the billing tab on your Google Cloud Profile. 
    - Important note: For the Google Cloud account, the student code will give you a free $50 credit. Once you've exhausted this, you'll need to enter your credit card information (you won't be charged). This simply verifies that you are not a bot. At this point, you'll receive a free $300 credit valid for 3 months. More details are available [here](https://edu.google.com/programs/students/?modal_active=none).

Make sure to create your account by the end of this week. Thereafter, familiarize yourself with various Google Cloud features. 

If you need help, consult the [Google Cloud Documentation](https://cloud.google.com/docs). This resource offers a comprehensive guide on using their services, alongside numerous code examples.

## Requirements

- [ ] GitHub account
- [ ] Google Cloud Account (with credits / credit card activated)
- [ ] Python Installed (python3 -V or python -V)
- [ ] Code editor (Visual Studio Code)

--------------


## The General Pipeline:

<img width="924" alt="pipeline" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/16ded3bf-7d53-4136-8f46-0dd3e343ebb9">

--------------

## Table of contents for exercises: 
* [Exercise 1 TMDB API Key](#exercise-1-tmdb-api-key)
* [Exercise 2 Google Cloud Function with API Key](#exercise-2-google-cloud-function-with-api-key)
* [Exercise 3 Streamlit App and Deploying on Google Cloud Run](#exercise-3-streamlit-app-and-deploying-on-google-cloud-run)
* [Additional links:]
-----------------------------------
### Exercise 1: TMDB API Key
-----------------------------------

We will be using the TMDB (The Movie DataBase) website to fetch information about movies, TV shows and actors, including details such as cast, ratings and user reviews. To do so, we will need to set up an API key to fetch this information. In this step we will focus on the creation of the account to get access to the API key. This can be done following this [link](https://www.themoviedb.org/signup) and create an account (click on Join TMDB). 

**Main Steps:** 
1. Go to the profile and get the API Key using this [link](https://www.themoviedb.org/settings/api/request)
2. Select Developper - Accept the terms and conditions - Complete the required information (for URL: educational-course). 
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

- **Step 1:** Check to see that the API key works correctly.
    - Download the notebook [here](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/1-Intro-to-GCP/Lab_1_Notebook.ipynb) and open it on [Google Colab](https://colab.research.google.com/) (Upload - browse - select the file and upload it).
 
- **Step 2.** Write and test a cloud Function in Python 
    - In the Notebook, there are two fonctions: the first one allows to fetch the list of movies and the second one to fetch the poster of a specific movie ID. We will deploy them on Google Cloud Functions
    - Verify that the function 1 executes correctly **with your api key** on the Notebook.

- **Step 3.** Deploy the two functions on Google Cloud Functions
    - 3.1. Go on [Google Cloud](https://cloud.google.com/)
    - 3.2. From the side menu, go to _Cloud Functions_, or search for _Cloud Functions_ in the Search bar at the top.
    - 3.3. Select **CREATE FUNCTION** 
    - 3.4. On the setup screen, give a name to the function: **function_1_get_movie_list** and select Region - Zurich and select Allow unauthenticated invocations and click on **NEXT**.
    - 3.5. You now have the access to the code editor on which you can write your function. Select **Python 3.12**. 

- **Step 4.**

    - 4.1. **Copy** the function 1 code from the notebook and **paste** it in Google Cloud Functions - **Don't forget to paster your API key inside**
    - 4.2. **Change the entry point**: From **hello_http** to **get_movie_titles**
    - 4.3. **Copy** the libraries and **paste** them in the **requirements.txt**
    - ```bash
      functions-framework==3.*
      requests==2.31.0
    - 4.4. Now select **DEPLOY**
    - 4.5. Wait about two minutes, then your function should be deployed: click on the URL, you should be able to see a list of movie titles !

- **Step 5.** Test the deployed function from the Notebook
    - 5.1. **Copy** the URL of your newly deploy Google Cloud Function
    - 5.2. Go back to the Notebook and **paste** the URL in **YOUR_URL** and run the cell. You should be able to see the list of movies.
 
- **Step 6.** Repeat the same process as before but for function 2 (we recall the steps below)
    - 6.1. **Copy** the function 2 code with your API key (code under Step 3-4. Deploy the two functions on Google Cloud Functions)
    - 6.2. Go back to **Cloud Functions** and click **CREATE FUNCTION**
    - 6.3. Call it **get_movie_details** - select Zurich - Select Allow unauthenticated invocations and click on **NEXT**
    - 6.4. Select Python 3.12, **Paste** the function 2 in the code editor on Google Cloud, and change the entry point to **get_movie_details**
    - 6.5. **Copy** the libraries and **paste** them in the **requirements.txt**
    - ```bash
      functions-framework==3.*
      requests==2.31.0
    - 6.6. Click **DEPLOY** and wait another 2 minutes and copy the URL. **NOTE** If you open the URL directly on the browser it will not work, because the functions expects a parameter / placeholder {movieID} for a specific movie ID. So if you open directly the link, you will get an **Internal server error**, which is expected. 
    - 6.7. Go back to the Notebook, paste your URL and execute the cell.

 - **Step 7.** Save the two URLs for later !

**Step by Step Guide: In case you get stuck:**

- 3.2. <img width="130" height="120" alt="Screenshot 2024-02-21 at 15 32 46" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/dd3b92d2-1d11-40c5-b0cc-1b1bb95b5caf">
- 3.3. <img width="300" alt="Google Cloud Function" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/df6e4750-3129-48e3-967e-4584db23dd4a">
- 3.4. <img width="300" alt="Screenshot 2024-02-21 at 15 38 51" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/bd53a08d-c798-42c6-b77b-6091599b52f5">
- 4.5.<img width="400" alt="Screenshot 2024-02-21 at 15 49 45" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/240694ab-dcdd-4798-bb23-6dcf5fc939c3">
 <img width="500" alt="Screenshot 2024-02-21 at 15 50 27" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/d169d8cd-eb07-4b55-900b-cd68eb1167bc">


-----------------------------------
### **Exercise 3 Streamlit App and Deploying on Google Cloud Run**
-----------------------------------

**The steps are as follows:**
1. Create a Streamlit Project and call the two Google Cloud Functions (created previously)
2. Dockerize the project
3. Deploy the App on Cloud Run !

**Recall:** Streamlit is an open-source Python library that enables rapid creation of interactive web applications for data science and machine learning with minimal code.

---

**Step 1:** Download the Skeleton code from [github](https://github.com/michalis0/Cloud-and-Advanced-Analytics/tree/main/labs/1-Intro-to-GCP/streamlit_app) and try out your functions! 
- 1.1. You can find attached a [folder](https://github.com/michalis0/Cloud-and-Advanced-Analytics/tree/main/labs/1-Intro-to-GCP/streamlit_app) called **streamlit_app**, this folder contains three files: app.py, requirements.txt and Dockerfile, please **Download** that folder and open it without your code editor (i.e. Visual Studio Code)
- 1.2. Download streamlit:
    - ```bash
      pip install streamlit
- 1.3. Add the two URLs from Google Cloud Functions and run your App and run the following command:
    - ```bash
      streamlit run app.py
- 1.4. You should be able to see something like this.
- <img width="300" height="500" alt="Streamlit" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/1cfe2cb0-eb0b-4a55-b678-747810ed96fa">

---

**Step 2:** Dockerize the Web Application and deploy it on Google Cloud Run: 


- 2.1. Create a [new Github repository](https://github.com/new) **google_cloud_deploy_streamlit**, keep the code private, add a readme.md file and create the repository. Then upload the streamlit_app folder and push your code
- 2.2. On your Github Account, go to Settings - Developer Settings - [Personal Access Token](https://github.com/settings/tokens) - Tokens (classic): **Generate new token** and select:
    - **write:packages**
    - **delete:packages**
    - **user**
    - **delete_repo**
- copy your token to keep it somewhere safe
- 2.3. Go to [Google Cloud](https://console.cloud.google.com/) and activate cloud shell
- 2.3. Clone the Github repository from github to have access to the code 
- ```bash
  git clone https://github.com/YOUR_USERNAME/google_cloud_deploy_streamlit
- 2.4. You will have to insert your **github username** and the **API KEY** as password
- ```bash
  cd google_cloud_deploy_streamlit/
  cd streamlit_app/
- 2.5. Now you can build your docker, to do to copy your **PROJECT_ID** (can be found [here](https://console.cloud.google.com/))
- ```bash
   docker build -t eu.gcr.io/PROJECT_ID/my_streamlit_app:latest .
- This should take about 1-2 minutes to execute
- ```bash
  gcloud auth configure-docker
- Do you want to continue, select: Y
- ```bash
   docker push eu.gcr.io/PROJECT_ID/my_streamlit_app:latest
-  2.7. Now you can go to **Container Registery** (search on your search bar: container registery)
-  Select your repository: **my_streamlit_app_new**
-  Select **DEPLOY** -> **Deploy to Cloud Run**
-  Select your container image URL if it is not already selected
-  Select: Zurich as the region, add **Allow unauthenticated invocations** and click **CREATE**
- Wait 1-2 minutes and Done ! You should have access to an URL allowing you to access your website from the Cloud ! Click on the URL to show your app deployed on the Web. 


**Step by Step Guide: In case you get stuck:**
- 2.2 <img width="600" alt="Screenshot 2024-02-22 at 10 06 43" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/3875387e-9d47-46af-ac6b-6c1ae2df707a">

- <img width="434" alt="Capture d'écran 2024-02-19 182001" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/37b207bc-1fff-46e7-a7bd-b4e9c4282a3e">
- <img width="262" alt="Capture d'écran 2024-02-19 184325" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/0e041f11-ee8a-4dbd-b48a-2667b4675234">
- <img width="505" alt="Capture d'écran 2024-02-19 184523" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/a54a757a-18ab-4f37-94cb-ffab8540d366">
- <img width="417" alt="Capture d'écran 2024-02-19 184638" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/b75f1e18-570a-45df-88e2-b9b7a5d17cec">
- <img width="744" alt="final" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/0f0736d9-dfb3-48c0-9da0-701342bb6680">

-----------------------------------
### **Additional Links**
-----------------------------------

##### Difference between Cloud Run and Cloud Functions:

- **Cloud Run:** Enables to deploy and run containerized applications. Cloud Run then manages scaling and the infrastructure.  
- **Cloud Functions:** Handles individual functions which is then taken care by Google Cloud in terms of deployment, scaling and execution.

More information on this [link](https://cloud.google.com/blog/products/serverless/cloud-run-vs-cloud-functions-for-serverless)








  


