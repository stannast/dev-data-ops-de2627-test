FROM python:3.12-slim

# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
# this will create /app directory in Docker image
WORKDIR /app

# add group and user to run a container
RUN groupadd -r webservice && useradd --no-log-init -r -m -g webservice webservice

# this will install some packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# this will copy application code to working directory
COPY ./web/web.py .

USER webservice:webservice

# indicates the ports on which a container listens for connections
EXPOSE 8050

# this command is started when container is ran
# below is recommended form of CMD
CMD ["streamlit", "run", "web.py", "--server.port=8050"]
