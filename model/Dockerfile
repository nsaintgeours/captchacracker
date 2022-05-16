# Install Python and required libraries
FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy project sources
COPY src ./src

# Expose API port
EXPOSE 80

# Launch app'
CMD ["uvicorn", "src.api:api", "--host", "0.0.0.0", "--port", "80"]