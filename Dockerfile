FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip3 install --no-cache-dir 


# run the command
CMD ["python3", "./automating_build"]