# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Flask is running on
EXPOSE 5050

# Run the app
CMD ["python", "run.py"]
