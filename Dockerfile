# Base Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY src/ /app/

# Install Python dependencies
RUN pip install --no-cache-dir \
    requests \
    feedparser \
    psycopg2-binary \
    python-dotenv \
    fastapi \
    uvicorn


# Default command
CMD ["bash"]
