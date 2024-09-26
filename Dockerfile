# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]

