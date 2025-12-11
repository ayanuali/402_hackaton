FROM python:3.11

WORKDIR /app

# Install basic utilities that Railway might need
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY agent/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code and startup script
COPY agent/simple_agent.py .
COPY start.sh .
RUN chmod +x start.sh

# Use bash entrypoint
ENTRYPOINT ["/bin/bash", "/app/start.sh"]
