# dev-environment/apiserver
This Dockerfile contains the fastapi server. The installation follows [this](https://fastapi.tiangolo.com/deployment/docker/) description. 

**Experimental:** It is also possible to enable HTTPS for local development by uncommenting the specified parts in the Dockerfile using [mkcert](https://github.com/FiloSottile/mkcert). Don't do it on critical environments.

Docker contains:

- Language: python
- Libraries: fastapi
- others: mkcert, brew

## Please note!
The Dockerfile is setup for private purpose to quickly get started and runs as root (ignoring security issues)! Don't use it on critical environments.

## Requirements
- Linux (I haven't tried Windows or Mac.)
- Docker

Setting up the container.
```bash
docker build -t joatom/apiserver .

docker run -d --name mylocalapiserver -p [OPEN_PORT]:80 -v [PATH_TO_APP]/app:/app joatom/apiserver
```

For debugging remove `-d` option, e.g.
```bash
docker run --name mylocalapiserver -p 8123:80 -v  ~/git_repos/dev-environments/apiserver/app:/app joatom/apiserver
```


## Resources
- Fastapi docker installation guide: https://fastapi.tiangolo.com/deployment/docker/ and https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
- Uvicorn HTTPS options: https://www.uvicorn.org/deployment/#running-with-https
- Mkcert installation guide: https://github.com/FiloSottile/mkcert
- Brew installation guide: https://docs.brew.sh/Installation