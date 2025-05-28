# Use official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything 
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your test script
CMD ["python", "test_model.py"]
