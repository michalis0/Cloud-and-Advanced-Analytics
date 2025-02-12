<h1 align="center"> LAB 3 - AutoML</h1>
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
In this lab, you'll learn how to build a classification and a regression model from data using Vertex AI.

## Introduction
Welcome to the third lab of Cloud and Advanced Analytics! In this week, we'll introduce you to Vertex AI tool to build Machine Learning models.

## Lab Walkthrough

Vertex AI offers two model training methods, AutoML and custom training. AutoML lets you train with minimal effort and machine learning experience, while custom training gives you complete control over training functionality. In this lab, we will only use AutoML to keep things simple.

Vertex AI examines the source data type and feature values and infers how it will use that feature in model training. It's recommended that you review each column's data type to verify that it's been interpreted correctly. If needed, you can specify a different supported transformation for any feature. Learn more about transformations.

## Table of contents for exercises: 
* [Exercise 1 Notebook Setup and Initialization](#exercise-1-notebook-setup-and-initialization)
* [Exercise 2 Deploy and Train a model and make a prediction](#exercise-2-deploy-and-train-a-model-and-make-a-prediction)
* [Exercise 3 Important disable the deployed model](#exercise-3-important-disable-the-deployed-model)
  
### Pre-Lab Setup 

* Enable vertex AI APIs



-----------------------------------
### **Exercise 1 Notebook Setup and Initialization**
-----------------------------------

In this exercise, we will look on how to **create a Notebook** that we will use for our Machine Learning algorithm later in. 

**Step 1: Creation of Notebook:**

* **1.1** Please go to your [Google Cloud Console](https://console.cloud.google.com)
* **1.2** In Search enter **Vertex AI**, then press return - you will arrive on the Dashboard of Vertex AI, where you will need to **Enable all recommended APIs**
* **1.3** In the left-navigation pane, under **Tools**, **Notebooks**, choose **Workbench**.
* **1.4** Click **User-managed notebooks**
* **1.5** You will need to create a new Notebook - click on **CREATE NEW** and as **environment** select **Python 3 (with Intel MKL)** and click **Create** (you can also change the region to europe-west (Switzerland) ).
* **1.6** Once the Notebook was created, click on the instance, and **wait for it to be provisioned** (about 1-2 minutes), then select **Open JupyerLab** - this will open an instance of **jupyterlab**.
* **1.7** Install the Vertex AI SDK for Python and its dependent SDKs by adding the following code at the top of your notebook and running it. To do so, please select **Python 3 (Local)** in **Notebook**, and paste the following code in a cell of the notebook and run it:
* ``` python
  !pip install --upgrade --quiet google-cloud-aiplatform
  !pip install --upgrade google-cloud-storage # if you get an error, specifically choose version "pip install --upgrade google-cloud-storage==2.14.0"
  !pip install protobuf

* **1.8** Once these two packages are installed successfully, restart the kernel. You can restart the kernel by adding and running this code to your notebook. Click **OK** once you get the message pop-up. 

    ```python
    import os

    if not os.getenv("IS_TESTING"):
        import IPython

        app = IPython.Application.instance()
        app.kernel.do_shutdown(True)
    ```
**Done!** You just initialized your Jupyter Notebook in Vertex AI!


**Hints in case you get stuck:**
* **1.2** <img width="200" alt="Workbench" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/a8f0168b-2e02-4c6b-84b6-d0d08cd3f6e2">
* **1.3** <img width="200" alt="Workbench" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/c340778f-e3eb-4b0a-a1a1-785f0e3d64e7">
* **1.5** <img width="200" alt="Workbench" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/3f13f202-4c60-44a0-9992-293edb3bb34b">
* **1.7** <img width="200" alt="Workbench" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/bcbfa3b3-6d8b-4c49-8f11-34d574eed0aa"> <img width="400" alt="Workbench" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/bc23fe7a-78ce-4581-9fb6-bbee33b19dc6">

-------

**Step 2: Adding a training dataset in AutoML:** Here, you are still working in the same Jupyter Notebook. 

* **2.1** As done in the previous lab, please create a bucket in the Google Cloud Storage and add a name, i.e.: vertex_ai_bucket_storage, and select **Region** Zurich, then click on **CREATE**. You can now go into **CONFIGURATION** and copy the **gsutil URI** - we will need it in the next step. You can now download the dataset found [here](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/03-AutoML/data/train_data.csv) and upload it in your bucket.


* **2.2** Now you can copy the code below and insert your: project ID, the gsutil URI and the REGION "europe-west6".

* ```python
  #set project id, bucket name and region
  PROJECT_ID = 'your_project_id' #from the above code you can get your project id
  BUCKET_NAME = 'gs://BUCKET_NAME' #you can set your own bucket name
  REGION = 'europe-west6' #change the region if different
  ```
* **2.3** You can now add this code, which will fetch the file (the training set) that you just imported. 
    ```python
    IMPORT_FILE = 'train_data.csv'
    gcs_path = f"{BUCKET_NAME}/{IMPORT_FILE}"
    ```

* **2.4** Initialize the AI platform and create the dataset in AutoML by adding these lines to the same notebook.

* ```python
  #import necessary libraries
  import os
  from google.cloud import aiplatform

  #initializing the AI platform
  aiplatform.init(project=PROJECT_ID, location=REGION)

  #creating dataset in AutoML
  ds = aiplatform.TabularDataset.create(
    display_name = 'data_tabular', #set your own name
    gcs_source = gcs_path)

**Hints in case you get stuck:**
* **1.2** <img width="500" alt="Screenshot 2024-03-05 at 16 56 42" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/2befb9bb-d482-4367-8f94-d830881aa762">

--------------------------------------------
### **Exercise 2 Deploy and Train a model and make a prediction**
--------------------------------------------

**Step 1: Deploying the model:**

* **1.1** Run these lines in the same notebook. This will create a job to perform the training.
* ```python
  #create a training job in AutoML to run the model
  job = aiplatform.AutoMLTabularTrainingJob(
    display_name = 'training_lab3',
    optimization_prediction_type = 'classification',
    column_transformations = [
         {'text': {'column_name': 'sentence'}}])
  
  #run the model
  #this will take time, depending on your dataset
  model = job.run(
    dataset = ds,
    target_column = 'difficulty',
    model_display_name = 'training_lab3',
    disable_early_stopping = False)
* **Note**: In this lab, we choose to perform the training on a small batch of the dataset to gain some time. **train_data.csv**. However, this is expected to take about 1 hour and 50 minutes.
* **Note**: You can check the status of the training in **Google cloud console** under the **Vertex AI tool**. Go to **Training** under 
**Model development**. You should see a new row that has as name: **training_lab3**

* **1.2** Once training is done we will deploy our model using endpoint. Endpoint is one of the components of Vertex AI where you can deploy your model. We will use this endpoint to perform predictions later on. 
* **1.2.1** Click on **model registery**, find your model (make sure to filter the correct region), then click on **training_lab3**
* **1.2.2** Click on **Deploy & test** at the top of the page
* **1.2.3** Then , click on **Deploy to endpoint**
* **1.2.4** Choose an endpoint name and keep the location and the access as it is by default and click on **Continue**
* **1.2.5** For **Model settings**, change the machine_type to **n1-standard-4**. Also set **Feature attribution** instead of **No explainability** under **Explainability options** and click on **Continue**
* **1.2.6** Disable model monitoring for this endpoint and click on **Deploy**. This might take a while (~30min).

**Hints in case you get stuck:**
* **1.2.2** <img width="372" alt="Screenshot 2024-03-05 at 16 56 42" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/9256c218-882d-42cb-b0fd-3613ad68f346">
* **1.2.6**  <img width="372" alt="Screenshot 2024-03-05 at 16 56 42" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/df801c31-d1bd-4ff2-8296-05d0230fd591">

**Step 2: Make a prediction:**

You're now ready to use the test data to make a prediction request. The prediction request invokes your model to predict a given sentence's difficulty.

* **2.1** Once you model is deployed, go to **Test your model** at the bottom of the page
* **Note**: Remember that the model predicts from a given French sentence the difficulty of that sentence (A1 or A2 or B1 or B2 or C1 or C2)

* **2.2** Under value, give a sentence (in French) to see the predicted outcome and click on **Predict**.

* There are some examples: 
* Pour que les actions de terrain contre la diffusion des campagnols terrestres aient une certaine efficacité, il est important qu'elles soient déployées dans des lieux où les possibilités de passage entre deux taches sont en nombre limité ; inversement, si on met en place une action dans un contexte paysager où de nombreuses alternatives de passage existent, il y a plus de chance que le dispositif soit ""contourné"".
* Un saison parfaite pour les sorcières
* Le tableau paraissait plus beau qu'avant.
* Tu as eu des nouvelles de Marie
* Sur les cinq heures, il entendit la canonnade : c'étaient les préliminaires de Waterloo.
* L'homme impoli est le lépreux du monde fashionable.


**Hints in case you get stuck:**
* **2.2** <img width="372" alt="Screenshot 2024-03-05 at 16 56 42" src="https://github.com/michalis0/Cloud-and-Advanced-Analytics/assets/43532600/6c33165c-924c-47c3-93cf-6b9421505f74">

--------------------------------------------
### **Exercise 3 Important disable the deployed model**
--------------------------------------------

**Step 1:** It is important that you remove your instance from running, or else you will be charged continuously even if you are not using it anymore. To do so, you can go to Model Registry, find your deployed model, and undeploy it! Please **do not forget this step**, or else you will be charged and you will not have enough credits for the end of the class! 
