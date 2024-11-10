# Use an official Python image as a base
FROM python:3.8-slim

# Set the working directory
WORKDIR /

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code to the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
