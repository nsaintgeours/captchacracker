# Install Python and required libraries
FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy project sources
COPY src ./src

# Set port on which the REST API is served:
# either 80 by default, or a custom port passed as an environment variable named MODEL_PORT in the build command
ARG MODEL_PORT=80
EXPOSE ${MODEL_PORT}
ENV MODEL_PORT ${MODEL_PORT}

# Launch REST API
CMD uvicorn src.api:api --host 0.0.0.0 --port ${MODEL_PORT}