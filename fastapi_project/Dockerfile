# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /fastapi

# Copy the current directory contents into the container at /app
COPY . /fastapi

# Install any needed dependencies specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install uvicorn
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME FastAPI-Docker

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

