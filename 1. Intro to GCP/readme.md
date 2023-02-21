## Intro
Welcome to the first lab of Cloud and Advanced Analytics.

In this week, we will give you a brief overview of cloud-based services. More specifically, we will look into **Google Cloud**, one of the most popular cloud services platforms. 

* Register on [Slack](https://join.slack.com/t/cloud-and-analytics23/shared_invite/zt-1oh2n2asy-l70~dhXVmgy34cqgvRLheg). This will be our main communication channel.
* [Redeem the code](https://gcp.secure.force.com/GCPEDU?cid=JVXdXMsqt29K9hweAVG5vLI9hhB68%2BT5LZzAhjbq9TUwDxaLhjeQGUu88SEhBvyZ/) for students that we provide you. For this, you need to use your .unil or .epfl account.
* Create an account on [Google Cloud](https://cloud.google.com) with your academic email address. This needs to be a google account.

* **Note**: For the Google Cloud account, with the code for students you will get free $50 credit. When you will finish them, you will need to enter your credit card information, but you won't be charged. It is just to verify that you are not a bot. At that point, you will receive a free $300 credit valid for 3 months. See also [here](https://edu.google.com/programs/students/?modal_active=none) for classes on Google Cloud for students.
* Do some simple exercises using the cloud.

You are going to use this services all throughout the semester, so make sure that you have created your account by the end of the week. Afterwards try to explore the various features you see in Google Cloud.

**Highly recommended**: If at any point you feel lost while using this service, we encourage you to look at the documentation provided by [Google](https://cloud.google.com/docs). They teach you how to use their services, and provide numerous code examples.


## Learning Goals
The learning goal of this lab is to gain familiarity with the Google Cloud console and make some first small experiments of usage.

## Walkthrough
TAs will show (directly on the Google Console):
* Setup of Google Cloud accounts
* Useful aspects of the Google Cloud Console, especially Billing, Storage, Big Query, AI, Cloud Functions
* Serverless backend: Cloud Functions 


## Exercises

### Exercise 1 - Storage
* From the side menu, go to _Storage_ > _Storage_ and create a new bucket (or go directly to the Bucket section by googling). Besides a unique name, you can keep the default configuration (but read through it anyway to see what kind of options are available to you).
* Upload a CSV from your laptop (either an existing one or one that you create for that purpose).
* Change the permissions so that the file is readable by everyone (i.e., "Public").
* Access the CSV file from your browser (private session) using the public URL.
* Remove the previously set permission.
* For further reference the [documentation is available here](https://cloud.google.com/storage/docs/access-control/making-data-public?hl=en-GB).


### Exercise 2 - Cloud functions
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



