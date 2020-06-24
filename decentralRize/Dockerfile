# Pull image
FROM python:3

# Setup working directory
WORKDIR /code

# Move requirements file into working directory in conatiner
COPY decentralRize/ /code

# Install requirements in the working directory
RUN pip3 install -r requirements.txt

# docker build -t robotgyal/decentralrize .