# Import Libraries
import streamlit as st
from google.cloud import storage
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data from Google Cloud Storage

# ----------------------------------------#
# Set the path to your service account key file
key_path = './' #'./big-scale-analytics-......json'
def load_data():
    try:
        bucket_name = 'YOUR_BUCKET_NAME' #'big_scale_analytics_bucket'
        file_name = 'YOUR_FILE_NAME' #'movies.csv'

        # Create a client with service account credentials
        client = storage.Client.from_service_account_json(key_path)

        bucket = client.get_bucket(bucket_name) # Get the bucket
        blob = bucket.blob(file_name) # Get file objects

        movie_csv = blob.download_as_text() # Download csv from Google Cloud and stores inside movie_csv variable
        df = pd.read_csv(StringIO(movie_csv))
        return df

    except Exception as e:
        st.error(f"Error during data loading: {e}")
        return None
# ----------------------------------------#
    
# Load Data

data = load_data()

st.title("Google Cloud Storage: Bucket and Movie CSV") # §Title

if data is not None: # If data is not empty
    st.table(data.head(10))  # Display the first 10 rows of the data
    plt.figure(figsize=(10, 6))
    sns.countplot(y='genres', data=data, order=data['genres'].value_counts().index[:10]) # Countplot
    plt.title('Number of Movies by Genre')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    st.pyplot(plt)