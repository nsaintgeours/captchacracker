# Install Python and required libraries
FROM python:3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy project sources
COPY src ./src

# Set port on which the web app' is served:
# either 8501, or a custom port passed as an environment variable named WEBAPP_PORT in the build command
ARG WEBAPP_PORT=8501
EXPOSE ${WEBAPP_PORT}
ENV STREAMLIT_SERVER_PORT ${WEBAPP_PORT}

# Run Streamlit web app'
ENTRYPOINT ["streamlit", "run"]
CMD ["src/app.py"]