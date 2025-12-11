FROM python:3.11

# Copy requirements and install dependencies
COPY agent/requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY agent/simple_agent.py /app/

# Run directly with python - no shell, no cd, no bullshit
ENTRYPOINT ["python3"]
CMD ["/app/simple_agent.py"]
