FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Run the FastAPI app from app/api.py
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
>>>>>>> ce08ca89de51c934b46171db710dff73c3d54039
