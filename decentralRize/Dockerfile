# Pull image
FROM library/python:3.6.3-alpine

# Make directory
RUN mkdir /code

# Setup working directory
WORKDIR /code

# Move requirements file into working directory in conatiner
COPY ./decentralRize/ /code

# Install requirements in the working directory
RUN pip3 install -r requirements.txt

# docker build -t robotgyal/decentralrize .
CMD python3 manage.py runserver 0.0.0.0:8000