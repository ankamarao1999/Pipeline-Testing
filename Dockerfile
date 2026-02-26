FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy ALL project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir flask

# Expose application port
EXPOSE 5000

# Run your main Flask API file
CMD ["python", "sample_api.py"]