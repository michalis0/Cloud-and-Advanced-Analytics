# Cloud & Advanced Analytics 2025
## Assignment 1 (due date: March 09)

### Goal
You will implement a simple interface that interacts with a BigQuery cloud database. The application should run on the Google Cloud.

### Details
In this assignment, you will implement a web application that will issue queries on a movie database. You can search titles of movies and also issue more advanced search functionalities. The advanced search functionality will allow users to specify filters to refine their search results. For instance, a user may want to find all the movies from Germany that are in the comedy genre and were released in 2019. 

### Tasks
Upload the movies and the user ratings datasets in BigQuery in the proper tables. You can find these datasets in the following zip file:
- [**assignment1-data.zip**](https://unils-my.sharepoint.com/:u:/g/personal/dimitri_roulin_unil_ch/EUB9EaTsDddIqKBs7xosJZcBsea800PmN2FFDjxF7Q923g?e=qN3O5D)

Here’s a preview of how the movies and the rating tables look like respectively:

### Functionalities to implement:

- **Autocomplete (in SQL)** to help you explore the titles based on what you type.
- **Filter by language (SQL).**
- **Filter by movie genre (SQL).**
- **Filter by average rating of a movie (SQL)** - e.g., getting the movies with an average rating higher than 4.0. This requires doing a group by / average aggregation and also a join in SQL.
- **Filter by release year (e.g., after 2019).**

Show the results of the user query. If a movie is selected, show more details. Use the **OpenMovieDatabase** or **The Movie Database** to show the cover of the movie selected, as well as more details (e.g., overview of the movie, cast of the movie, etc.). Your database should be **BigQuery**. Your UI will be implemented in **Streamlit**.

Typically, we would break our application into 3 parts: **database**, **middleware (the logic)**, and **the UI**. Just to simplify things for this assignment, we will implement it in **2 parts**: the **database** and the **logic+UI**, so the SQL queries will be incorporated into the UI.

The **Streamlit visual application will be dockerized and deployed** to run on the Google Cloud. We will test the endpoints and the code quality.

### Expected components:
- **BigQuery**
- **SQL**
- **Docker**
- **Google Cloud**
- **Streamlit** for the user interface

### Deliverables
A zip of your git repository with your code (**zip of GitHub**). The `README.md` should include the **Internet URL** where we can test your application.

### Evaluation
- **Quality of the application (50%)**
- **Code quality (50%)**
- If the URL does not work, you won’t receive any points for your code.
- You will receive **one grade** for both Part 1 and Part 2 of the assignment, but we will give you textual feedback for Part 1.

### Steps to complete the assignment
1. Download the dataset.
2. Upload the movie dataset in **Google Cloud BigQuery**.
3. Test the different queries directly on **BigQuery**.
4. Create a **Streamlit application** (as done in the previous lab – CF lab 1).
5. Create the functions and print the results of the **SQL queries** when you click buttons.
6. Deploy your app on **Cloud Run** to see if everything runs as expected.
7. Improve the UI (modify the buttons with tables, filters…) and deploy your final app!
