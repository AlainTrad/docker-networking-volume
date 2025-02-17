# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY producer.py .

# Expose the port
EXPOSE 5000

# Run the script
CMD ["python", "producer.py"]
