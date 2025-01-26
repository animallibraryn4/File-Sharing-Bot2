FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy all the application files
COPY . /app

# Set the default command to run the application
CMD ["python3", "main.py"]
