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
You'll be working on two exercises for this lab: 

### Exercise 1: Google Cloud Storage

This exercise will walk you through creating a storage project, managing access permissions, and working with CSV files in Google Cloud Storage.

The steps are as follows:
* From the side menu, go to _Storage_ > _Storage_ and create a new project with a name of yyour choice, then create a bucket (or go directly to the Bucket section by googling). Besides a unique name, you can keep the default configuration (but read through it anyway to see what kind of options are available to you) except for the "Access Control" parameter (under "Permission") which should be set to __Fine Grained__ and not "Uniform". This will allow you to get a Public URL for one of your file (next steps).
* Upload a CSV from your laptop (either an existing one or one that you create for that purpose).
* Change the permissions so that the file is readable by everyone (i.e., "Public"). To make it publicly accessible, click on the three vertical dots of you csv file, then on _Edit Access_. You can now add an Entry where:
  * _Entity_ = _Public_,
  * _Name_N_ = _allUsers_,
  * _Access_N_ = _Reader_
* Access the CSV file from your browser (private session) using the public URL.
* Remove the previously set permission.
* For further reference the [documentation is available here](https://cloud.google.com/storage/docs/access-control/making-data-public?hl=en-GB).

### Exercise 2: Google Cloud Functions
This exercise aims to familiarize you with Google Cloud Functions. You'll create a cloud function to retrieve the latest value of a company's stock using an API.

The steps are as follows:
1. Write a function on GCP in Python
2. Call the function from a Notebook (either in Colab or in Jupyter).
The function will need to be based on the default “Hello world” function (in the provided notebook). You will need to add a call to the api, and extract the relevant info from the api response (the lines of code to do this are also available in the provided notebook). Finally, the code to call the function from a Python notebook is provided as well.


* From the side menu, go to _View all products_ > _Serverless_ > _Cloud Functions_, or search for _Cloud Functions_ in the Search bar at the top.
* Create a simple Python function that can be triggered over HTTP. Make sure to pick the "Allow unauthenticated invocations" option.
   * The function should accept one parameter called `company_stock_name` and call the following external API, using that parameter as the value for the `symbol` parameter: https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=demo. "demo" should be replaced with your own API key, which you can get for free [here](https://www.alphavantage.co/support/#api-key) and AAPL should be replaced with the value inserted by the user. Here the documentation for the API: https://www.alphavantage.co/documentation/#intraday
   * The function should return the last recorded value of the company's stock.
* After having deployed your function, call it using its URL, trying different values for the company name (MSFT, IBM, ZM, etc.) to make sure it works properly.


**Hints**:
* Build on top of the default code provided by Google; no need to start from scratch!
* Make sure the "Entry point" matches the name of the Python function in `main.py`.
* Try the API link above to see what the returned object looks like. It will make it easier for you to understand how to access the desired data from your code. You may also want to look into Python's default [`json`](https://docs.python.org/3/library/json.html) library.
* There are several ways to make HTTP requests from Python. You can use the [`requests`](https://requests.readthedocs.io/en/master/) library, for example.
* To go back to your code after having deployed the function, you must go to your list of cloud functions, click the function, then click the "Edit" button at the top. The console will ask you to review the configuration first; you can simply click "Next".
