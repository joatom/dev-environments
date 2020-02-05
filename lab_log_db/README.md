# dev-environment/lab_log_db
Development environment containing:
- Database: postgres 12.1
- Webapp: pgadmin

## Please note!
The Dockerfile is setup for private purpose to quickly get started and runs as root (ignoring security issues)! Don't use it on critical environments.

## Requirements
- Linux
- Docker

## Install
Create a directory for the database files:

    mkdir ~/lab_log_db/datadir -p
    
If the database needs to be recreated delete content of *datadir*:
    
    # !! All former DB stored in the directory will be lost
    # rm -r ~/lab_log_db/datadir

Build container:

    docker build -t joatom/lab_log_db .
    
Run container:
    
    docker run --name lab_log_db -p 5432:5432 -v ~/lab_log_db/datadir:/var/lib/postgresql/data -e POSTGRES_PASSWORD=abc -d joatom/lab_log_db

For administration pgAdmin can be installed as a seperat container like this:

    docker pull dpage/pgadmin4
    
    docker run --name pgadmin4 -p 20080:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=a@b.cd' \
    -e 'PGADMIN_DEFAULT_PASSWORD=abc' \
    -d dpage/pgadmin4
    
    
## Resources
- https://hub.docker.com/_/postgres
- https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html
