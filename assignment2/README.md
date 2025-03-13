# Cloud & Advanced Analytics 2025 - Assignment Part 2

## Due Date: April 06

## Goal
You will create a **movie recommendation application** that allows users to input their movie preferences and receive personalized recommendations. The application should be deployed on **Google Cloud**.

---

## Details
In this assignment, you will:
- Train a **recommendation system** on the provided dataset.
- Implement a **web application** where users can select their preferred movies and receive recommendations.
- Develop a **search bar with autocomplete** for movie titles.
- Display the **top-n recommended movie titles** along with their posters.

Users will select multiple preferred movies, and after submission, the system will recommend movies based on the preferences. The application will determine similar users in the dataset and generate recommendations accordingly.

---

## Tasks

1. **Data Upload to BigQuery**
   - Upload **user ratings, links, and movies datasets** to BigQuery.
   - The datasets are from the **movielens-small dataset** (used in Week 5 recommender systems lab).
   - Retrieve datasets from the course's **GitHub repository**.

2. **Train a Recommender System**
   - Train a **matrix factorization** recommendation model using **BigQuery ML** (cf. Lab 5).
   - Generate recommendations for various user IDs using **BigQueryML SQL** statements.

3. **Handle Cold Start Problem**
   - The user who interacts with the web app is a **cold start user** (not in training data, no user ID).
   - Find **similar users** in the dataset based on shared movie preferences:
     - Identify users who have rated the same movies highly.
     - Rank users based on the number of common preferred movies.
     - Use the **top-k similar users'** recommendations to suggest movies.

   **Example:**
   
   | User | Rated Highly |
   |------|-------------|
   | u_1  | [2, 4, 6, 8, 9] |
   | u_2  | [1, 3, 7, 9] |
   | u_3  | [3, 5, 8, 9] |
   | u_4  | [7, 8, 9] |
   
   If the web app user selects **movies 1, 3, 5, 7**, user **u_2** is the most similar, followed by **u_3, u_4, and u_1**.

4. **Web Application Development**
   - **Backend (Flask Application)**
     - Train and store the **recommender model** in **BigQuery ML**.
     - Implement **autocomplete** using **Elasticsearch**.
     - Identify **similar users** (SQL queries on BigQuery).
     - Generate **movie recommendations** based on similar users.
     - Retrieve **movie posters** from **The Movie Database API**.

   - **Frontend (Streamlit Application)**
     - **Movie title search bar** with **autocomplete**.
     - Users can **select multiple movies** before requesting recommendations.
     - Display **recommended movies** along with their **posters**.

5. **Deployment**
   - **Dockerize the Flask backend** and deploy it on **Cloud Run**.
   - **Dockerize the Streamlit frontend** and deploy it on **Cloud Run**.
   - Ensure that the frontend interacts with the backend through API calls.

---

## Expected Components
- **Elasticsearch** (for autocomplete and search functionality).
- **BigQuery** (for storing and querying movie datasets).
- **BigQuery ML** (for training the recommendation system).
- **Docker** (for containerizing applications).
- **Google Cloud** (for hosting the application).
- **The Movie Database API** (for fetching movie posters).

---

## Deliverables
- A **ZIP file** containing your **GitHub repository**.
- A **README.md** file including:
  - The **Internet URL** where we can test your application.
  - A brief explanation of the **similarity computation method** used for identifying similar users.

---

## Evaluation Criteria
- **Quality of Application (50%)**
  - Functional movie recommendation system.
  - Proper deployment of backend and frontend.
  - Correct implementation of **autocomplete** using **Elasticsearch**.

- **Code Quality (50%)**
  - Well-structured and documented code.
  - Effective use of **BigQuery ML, SQL, and Python**.
  - Proper API calls and integration between frontend and backend.

- **Working URL Requirement**
  - If the application URL does **not work**, **zero points** will be awarded for the code.
  - To receive **full points**, the following must be implemented:
    - **Movie recommendation functionality**.
    - **2-tier structure** (backend and UI as separate Docker containers).
    - **Elasticsearch for autocomplete**.
  

Good luck with your assignment! 

