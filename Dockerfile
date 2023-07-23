FROM python:3.9-slim
WORKDIR /app
COPY . /app/

# Copy the static files into the image under /app/static
COPY static /app/static

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]