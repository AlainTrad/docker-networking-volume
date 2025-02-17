# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY consumer.py .

# Create a directory for logs
VOLUME /data

# Run the script
CMD ["python", "consumer.py"]
