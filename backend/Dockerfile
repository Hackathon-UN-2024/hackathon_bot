FROM python:3.12.4-alpine

RUN apk add gcc python3-dev libc-dev geos-dev

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY ./app .

# Command to run the application
CMD ["fastapi", "run", "main.py", "--port", "3000"]