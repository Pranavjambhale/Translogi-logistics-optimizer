# Base image for Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Expose ports
EXPOSE 5000 8501

# Start Flask app
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=5000 & streamlit run dashboard.py --server.port=8501 --server.address=0.0.0.0"]
