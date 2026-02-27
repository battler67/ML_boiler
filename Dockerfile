# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

RUN apt-get update && apt-get install -y git
# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Start the app with production-ready server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:app"]