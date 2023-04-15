# Building a webapp with Flask or Streamlit

We will learn how to make a web application. It's a useful skill to have. You could think of building a simple website for your project, or if you have a startup idea in the future maybe!

## Plan
1. Creation of Hello World webapp with Flask
2. Walkthrough of example of ML webapp with Flask and Huggingface
3. Deploying a Flask web application on Google cloud
4. Building a webapp with Streamlit

## Part 1 - Flask
We will learn how to make a web application with flask. We will start by building a simple `HelloWorld` web application which will run locally on your computer. Then we will see how we can use HTML to shape the different pages of our web app. Furthermore, we will see how we can pass parameters to our web application. Finally, we will see how we can deploy our web application into Google cloud app engine so that it is accessible from anywhere in the Web.

![alt text](ml_demo.png)

To get a more in-depth knowledge of Flask, we would recommend you to watch this nice <a href="https://youtu.be/mqhxxeeTbu0">tutorial series</a> on flask.

Moreover, you can also follow <a href="https://www.youtube.com/watch?v=RbejfDTHhhg">this tutorial</a> in order to get to know more about deploying a Flask ML application on Google cloud.


## Part 2 - Streamlit

_Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. Basically, with respect to Flask+HTML, it makes your life easier, but slightly "limits" your possibilities._

**<a href="https://docs.streamlit.io/knowledge-base/tutorials/databases/gcs ">This</a>  is how you can connect streamlit to you Google Cloud Storage**

The goal of this lab is to get familiar with its functionnality.
You will have to complete a python code for a Streamlit app that allows the user to explore New York City's Uber pick-up data. The app includes a map of New York City where the user can see how the Uber pick-ups vary over time.
This code is available under the streamlit folder as `uber_step_01.py`. You will have to read it to understand what it does. Then you will have to fill the missing parts in order to get the expected result.

### STEP 1:
> The app first sets loads the data from a CSV file using the load_data() function that caches the data to improve performance. The data includes the date and time of the pick-up, latitude and longitude coordinates.
>
> This first file includes two mains functions:
> - **load_data()** that loads the data from a CSV file and caches the data to improve performance.
> - **filterdata()** that filters the data based on the hour selected by the user

You may run the code to test your app with the following command:
```bash
streamlit run uber_step_01.py
```

You should get the following result:
![alt text](streamlit/expected_result_intro_streamlit.png)

### STEP 2:
Next, there are several helper functions you will have to define that filter and manipulate the data. These include **filterdata()** that filters the data based on the hour selected by the user, **mpoint()** that calculates the midpoint for a given set of data, and **histdata()** that filters the data by hour and calculates the number of pick-ups for each minute of that hour.

Then, the second file `uber_step_02.py` includes the following functions:
- **mpoint()** that calculates the midpoint for a given set of data
- **histdata()** that filters the data by hour and calculates the number of pick-ups for each minute of that hour
- **map()** that renders the map of New York City and the three airports

The skeleton of the code is already provided. You will have to fill the missing parts.


You may run the code to test your app with the following command:
```bash
streamlit run uber_step_02.py
```

Overall, this script is an example of how to build an interactive data visualization app using Streamlit and several popular Python libraries, including Altair, NumPy, Pandas, and PyDeck.

The following image shows what you are supposed to get by the end of the tutorial.
![alt text](streamlit/expected_result_lab_streamlit.png)