FROM python:3.11

# Copy requirements and install dependencies
COPY agent/requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code and startup script
COPY agent/simple_agent.py /app/
COPY start.sh /app/
RUN chmod +x /app/start.sh

# Use startup script for debugging
CMD ["/bin/bash", "/app/start.sh"]
