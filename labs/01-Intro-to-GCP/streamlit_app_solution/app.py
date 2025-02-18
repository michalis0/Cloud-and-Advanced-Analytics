

import streamlit as st
import requests

def fetch_movie_details():
    # URL of your deployed Google Cloud Function
    cloud_function_url = 'https://europe-west6-monjoor.cloudfunctions.net/function_1_get_movie_list'
    
    try:
        # Make a request to the Google Cloud Function
        response = requests.get(cloud_function_url)
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        if 'movie_details' in data:
            return data['movie_details']
        else:
            return None
    except requests.RequestException as e:
        st.error(f"Error making API request: {e}")
        return None
def main():
    # Fetch movie details from the Google Cloud Function
    movie_details = fetch_movie_details()
    st.title("Movies from the TMDB Dataset")

    if movie_details:
        st.table(movie_details)
            
        st.text_input("Enter a Movie ID to search:", key='search_movie_id')
        if st.button("Search"):
            search_movie_id = st.session_state.search_movie_id
            search_url = f'https://europe-west6-monjoor.cloudfunctions.net/function_2_get_movie_details?movie_id={search_movie_id}'
            try:
                search_response = requests.get(search_url)

                search_response.raise_for_status()
                search_data = search_response.json()
             
                img = list(search_data.values())[-1]
              
                st.text("Search Results:")
                st.table(search_data)
                st.image(img)
            except requests.RequestException as e:
                st.error(f"Error making search API request: {e}")
    else:
        st.warning("No movie details available.")

if __name__ == '__main__':
    main()

