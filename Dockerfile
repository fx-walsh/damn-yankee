# Use official Python 3.12 slim image
FROM python:3.12-slim AS image-pull

# Install system dependencies: curl for uv, tesseract and its deps
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    pkg-config \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Astral's Python package manager)
RUN curl -Ls https://astral.sh/uv/install.sh | bash

# Set working directory
WORKDIR /app

RUN mkdir damn-yankee/ && mkdir damn-yankee-data/

# # Copy project files
# COPY ./temp-data/ /app/data/

# Optional: Install Python dependencies
# RUN uv pip install -r requirements.txt
# or if using pyproject.toml
# RUN uv pip install -e .

# Default command
CMD ["/bin/bash"]
