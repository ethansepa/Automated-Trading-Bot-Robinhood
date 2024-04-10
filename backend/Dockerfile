# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the Django project code to the working directory
COPY . .

# Run migrations
RUN python3 manage.py migrate

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
