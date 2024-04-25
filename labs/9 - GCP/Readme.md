<h1 align="center"> Continuous integration</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>


# Continuous Integration using Google Cloud Build

## Introduction

This guide will walk you through setting up continuous integration (CI) for a Streamlit web application using Google Cloud Build. With CI, you can automate the testing and deployment process whenever changes are made to your codebase.

### Prerequisites

Before getting started, make sure you have the following:

- Enable the APIs [documentation](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build#existing-service) or you can just click on this [link](https://console.cloud.google.com/flows/enableapi?apiid=sourcerepo.googleapis.com,cloudbuild.googleapis.com)
- Enable the Identity and Access Management (IAM) API for your GCP project [here](https://console.cloud.google.com/apis/library/iam.googleapis.com).


## Getting Started

1. **Create a new GitHub Repository**:
   - Create a new repository named "continuous_deployment_lab" on GitHub.
   - Clone this repository to your local machine (or create it directly using github desktop)

2. **Add Files to Repository**:
   - Copy the following files from this repository:
     - Dockerfile
     - app.py
     - requirements.txt
   - Add these files to your newly created GitHub repository.

3. **Test the Code**:
   - Run the Streamlit app locally to ensure everything is working:
     ```
     streamlit run app.py
     ```
   - Once verified, commit the code changes to your GitHub repository.

## Deploy to Google Cloud

1. **Deploy to Google Cloud Run**:
   - Deploy your Streamlit app to Google Cloud Run as we have done in the past. But first start by pushing your code to Github !

2. **Push to Artifact Registry**:
   - Build the Docker image:
     ```
     docker build -t eu.gcr.io/PROJECT_ID/my_streamlit_app_v1:latest .
     ```
   - Push the Docker image to Google Cloud Artifact Registry:
     ```
     docker push eu.gcr.io/PROJECT_ID/my_streamlit_app_v1:latest
     ```

3. **Verify Deployment**:
   - Check the Artifact Registry to ensure the image has been pushed successfully.
   - Deploy the image to Cloud Run, allowing unauthenticated invocations.
   - <img src="./imgs/artifact_reg.png" width="300">
   - <img src="./imgs/cloud_deploy_without_cd.png" width="300">
  - Check that everything runs correctly !

## Setting Up Continuous Integration

1. **Connect GitHub with Cloud Build**:
   - Navigate back to the artifact Registery and as before select the image and **Deploy to Cloud Run**
   - Click on "Continuously deploy from a repository" and follow the prompts to connect your GitHub account (Select: SET UP WITH CLOUD BUILD)
   - <img src="./imgs/github_connect_for_ci.png" width="300">
   - Select the corresponding github repository and for the build configuration select **Dockerfile**
    - <img src="./imgs/git_conf.png" width="300">
    - <img src="./imgs/build_docker_file_conf.png" width="300">
   - Then click **Save**

2. **Building process**:
   - This will launch the building process, you can click on **logs** to see where it stands
   - <img src="./imgs/building.png" width="300">
   - Once built (approx. 3-4 minutes), you can view the details
   - <img src="./imgs/process.png" width="300">
   - Then you can search for cloud build in the search bar and select **Dashboard** which will show you all the builds status
   - <img src="./imgs/build_status.png" width="300">
   - Alternatively, you can go to your repository and look if the build has passed 
   - <img src="./imgs/passed_github.png" width="300">
   - Finally you can go to cloud run to see your URL where the app is deployed

3. **Further changes**:
   - Now that your project is set up for continuous deployment you can go ahead and change the title of your streamlit app, for example
   - ```bash
      st.write("This is the modified title")
      ```
   - Then you can commit and wait for the new version to build and be pushed on google Cloud run ! 
   - This will appear as **Checked** on your github 
   - <img src="./imgs/image.png" width="300">
