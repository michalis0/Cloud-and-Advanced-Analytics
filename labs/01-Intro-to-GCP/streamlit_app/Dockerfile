FROM python:3.7

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

# Expose the port that Streamlit runs on
EXPOSE 8080

# Set the environment variable PORT
ENV PORT 8080

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8080"]


