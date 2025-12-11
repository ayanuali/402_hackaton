FROM python:3.11

WORKDIR /app

# Copy requirements and install dependencies
COPY agent/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code directly to /app
COPY agent/simple_agent.py .

# Run the agent
CMD ["python", "simple_agent.py"]
