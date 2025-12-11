FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY agent/requirements.txt ./agent/

# Install dependencies
RUN pip install --no-cache-dir -r agent/requirements.txt

# Copy the rest of the application
COPY agent/ ./agent/

# Run the agent
CMD ["python", "agent/simple_agent.py"]
