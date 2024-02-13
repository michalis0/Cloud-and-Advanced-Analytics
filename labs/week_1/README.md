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

### Pre-Lab Setup 
Please follow these steps to prepare for this week's lab:

1. **Communication**:
    - Join our workspace on [Slack](https://join.slack.com/t/cloud-and-analytics23/shared_invite/zt-1oh2n2asy-l70~dhXVmgy34cqgvRLheg). This will serve as our primary mode of communication.
2. **Google Cloud Setup**:
    - Create a Google account with your academic email address (if you do not already have one) on [Google Cloud](https://cloud.google.com). This needs to be a Google account.
    - Please do NOT activate your free $300 trial on Google Cloud yet. We will utilize this for a project later in the course. Instead, we'll start with a voucher.
3. **Voucher Redemption**:
    - Redeem the student voucher code we provided, using your .unil or .epfl account. See instructions in Moodle.
    - Verify that the $50 voucher code has been applied to your account by checking the [billing tab](https://console.cloud.google.com/billing/01B32E-AE678C-E613F9?organizationId=0).
    - Important note: For the Google Cloud account, the student code will give you a free $50 credit. Once you've exhausted this, you'll need to enter your credit card information (you won't be charged). This simply verifies that you are not a bot. At this point, you'll receive a free $300 credit valid for 3 months. More details are available [here](https://edu.google.com/programs/students/?modal_active=none).

Make sure to create your account by the end of this week. Thereafter, familiarize yourself with various Google Cloud features. 

If you need help, consult the [Google Cloud Documentation](https://cloud.google.com/docs). This resource offers a comprehensive guide on using their services, alongside numerous code examples.

## Exercises
You'll be working on three exercises for this lab: 


## Table of contents 
* [Exercise 1 TMDB API Key](#step-1-TMDB-API-Key)
* [Exercise 2 Google Cloud Function with API Key](#step-3-data-cleaning)
* [Exercise 3 Streamlit App and Deploying on Google Cloud Run](#hour-2-data-visualization)

-----------------------------------
### **Exercise 1: TMDB API Key**
-----------------------------------

We will be using the TMDB (The Movie DataBase) website to fetch information about movies, TV shows and actors, including details such as cast, ratings and user reviews. To do so, we will need to set up an API key to fetch this information. In this step we will focus on the creation of the account to get access to the API key. This can be done following this [link](https://www.themoviedb.org/signup)

**Next:** 
1. Go to the profile and get the API Key using this [link](https://www.themoviedb.org/settings/api/request)
2. Select Developper - Accept the terms and conditions
3. You should now be able to see your API key (copy your API key for later use)
4. Now we can go back to the [API page](https://developer.themoviedb.org/reference/account-rated-movies) and you can play around to test the different requests i.e: GET / PUT / POST requests. An example could be the following: https://developer.themoviedb.org/reference/genre-movie-list - clicking on **Try it** you should receive the response from the request. 

**Hints (in case you get stuck):**

<img width="400" alt="TMDB Profile" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/9eba5cb3-d082-4a19-9efe-c1a375339f27">
<img width="400" alt="TMDB API Key" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/e6e46ffa-c4a1-4dc6-b1ea-49242d7f2ff0">
<img width="400" alt="Example Request" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/fcafddb1-d7b8-41be-a553-df8563b2370a">


-----------------------------------
### **Exercise 2: Google Cloud Functions**
-----------------------------------

This exercise aims to familiarize you with Google Cloud Functions. You'll create a cloud function to retrieve different movies and specific movie posters using the API.

**The steps are as follows:**
0. Check to see that the API key works correctly
1. Write a function on GCP in Python
2. Deploy the function on Google Cloud Platform
3. Call the function from a Notebook (either in Colab or in Jupyter).
4. Please repeat those steps for the second function on the Notebook

**Hints to 2. Deploy the function on Google Cloud Platform (in case you get stuck) :**
* From the side menu, go to _View all products_ > _Serverless_ > _Cloud Functions_, or search for _Cloud Functions_ in the Search bar at the top.
*<img width="680" alt="Google Cloud Function" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/df6e4750-3129-48e3-967e-4584db23dd4a">
* Create a simple Python function that can be triggered over HTTP. Make sure to pick the "Allow unauthenticated invocations" option.
*<img width="400" alt="Unothenticated" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/535ec37a-459c-425a-962e-f4d6e00f17e9">
* You can now copy paste the code from the Notebook (by uncommenting the 3 lines and adding the packages in the requirements.txt)
* Please do not forget to put the same entry point as the function name:
* <img width="400" alt="Entry point" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/7c7da4d2-a24f-4787-8ac6-4992afb173b3">
* After having deployed your function, call it using its URL, trying different values for the Movie IDs (CF notebook)



-----------------------------------
### **Exercise 3: Streamlit / Dockerizing and Deploy on Cloud Run**
-----------------------------------

**The steps are as follows:**
1. Create a Streamlit Project and call the two Google Cloud Functions
2. Dockerize the project
3. Deploy the App on Cloud Run !

**Step 1:** Download the Skeleton code and try out your functions! 
- Recall: Streamlit is an open-source Python library that enables rapid creation of interactive web applications for data science and machine learning with minimal code.
- You can find attached a folder called **streamlit_app**, this folder contains three files: app.py, requirements.txt and Dockerfile
- Please download streamlit: pip(3) install streamlit
- Add the two URLs from Google Cloud and Run your App and run the following command: Streamlit run app.py
- You should be able to see something like this.
- <img width="520" alt="Streamlit" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/1cfe2cb0-eb0b-4a55-b678-747810ed96fa">

**Step 2:** Dockerize the Web-Application and deploy it on Google Cloud Run: 
- Recall: Docker is a platform and toolset for developing, deploying, and running applications in lightweight, portable containers, facilitating consistent and reproducible software environments across different systems.
- Please connect to the Google Cloud from your code editor: **gcloud auth login**
- Once logged in, now get the project name: **gcloud config get-value project**, copy your project name
- docker build -t gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest .
- docker push gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest
- gcloud run deploy streamlit-website-deployed --image gcr.io/YOUR_PROJECT_NAME/streamlit-website:latest --platform managed
**Note** you can select a deployment server in Europe, i.e: number 13: [13] europe-central2
- Wait 2-3 minutes
Done ! You should have access to an URL allowing you to access your website from the Cloud ! 

<img width="744" alt="final" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/0f0736d9-dfb3-48c0-9da0-701342bb6680">






  


