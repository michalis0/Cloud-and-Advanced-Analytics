import streamlit as st
from google.cloud import storage
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt

# Set the path to your service account key file
key_path = '' #'./project-......json'
def load_data():
    try:
        # Set the Bucket Name and the File name 
        bucket_name = 'BUCKET_NAME_HERE'#'cloud_analytics_bucket'
        file_name = 'FILE_NAME_HERE'#'movies.csv'

        # Create a client with service account credentials
        client = storage.Client.from_service_account_json(key_path)

        # Get the bucket and file objects
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(file_name)

        csv_content = blob.download_as_text()
        df = pd.read_csv(StringIO(csv_content))
        return df

    except Exception as e:
        st.error(f"Error during data loading: {e}")
        return None

data = load_data()

st.title("Google Cloud Storage: Bucket and Movie CSV")

if data is not None:
    
    st.table(data.head(10)) 
    plt.figure(figsize=(10, 6))
    sns.countplot(y='genres', data=data, order=data['genres'].value_counts().index[:10])
    plt.title('Number of Movies by Genre')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    st.pyplot(plt)