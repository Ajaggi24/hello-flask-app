# 1. Base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy app code
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Expose port
EXPOSE 5000

# 6. Start Flask app
CMD ["python3", "app.py"]
