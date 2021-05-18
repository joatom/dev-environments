## following https://fastapi.tiangolo.com/deployment/docker/
FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

## some additional libraries, e.g. aiofiles for FileResponse
COPY requirements.txt /tmp
RUN pip install -q -r /tmp/requirements.txt

# COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

####################### DANGER ZONE ##################################
####### Don't do this on PROD env. ######
## for running with https on local environment
## install cert server (development only)

## following https://github.com/FiloSottile/mkcert
#RUN apt update && apt -y upgrade
#RUN apt -y install libnss3-tools

## install brew following https://docs.brew.sh/Installation
#RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#ENV PATH=/home/linuxbrew/.linuxbrew/bin:$PATH

#RUN brew install mkcert

## RUN mkcert -key-file key.pem -cert-file cert.pem my_server_name
#RUN mkcert localhost
#RUN mkcert -CAROOT

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--ssl-keyfile", "/localhost-key.pem", "--ssl-certfile", "/localhost.pem", "--reload"]

## "--ssl-keyfile", "/key.pem", "--ssl-certfile", "/cert.pem",