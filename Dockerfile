FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy only the requirements first to take advantage of Docker's cache
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Set the default command to run the application (ensure this points to the correct file)
CMD ["python3", "main.py"]
