# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5001

# Command to run the application
CMD ["python", "app.py"]
