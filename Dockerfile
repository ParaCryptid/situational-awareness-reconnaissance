
    FROM python:3.9-slim

    # Set working directory
    WORKDIR /app

    # Copy source code and requirements
    COPY ./src /app/src
    COPY ./requirements_final.txt /app/

    # Install dependencies
    RUN pip install --upgrade pip &&         pip install -r /app/requirements_final.txt

    # Expose application port
    EXPOSE 8080

    # Run the application
    CMD ["python", "/app/src/main.py"]
    