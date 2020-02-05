# dev-environment/ml
Development environment containing:
- Language: python
- Libraries: fastai, nbdev, pytorch, torchvision, torchaudio, opencv, pyarrow, librosa
- IDE: Jupyter Notebook and Jupyter Lab

## Please note!
The Dockerfile is setup for private purpose to quickly get started and runs as root (ignoring security issues)! Don't use it on critical environments. Don't run notebooks in this container, that you don't trust. (For a proper Jupyter installation go to https://github.com/jupyter/docker-stacks/)

## Requirements
- Linux (I haven't tried Windows or Mac.)
- Docker
- NVidia for GPU-Support (tested on RTX 2070 Super)

## Install
Build container:

    docker build -t joatom/ml
    
Run container:
    
    docker run --name ml --rm -p 8889:8889 -p 8888:8888 -v ~/.gitconfig:/etc/gitconfig -v ~/git_repos:/home/git_repos --gpus all joatom/ml

Starts the container for one-time usage (`--rm`). Routes port `8888` for jupyter notebook und port `8889` for jupyter lab throug the host system. If jupyter notebook is not accessable through http://<hostname>:8888 the ports on the host may be closed (A way to open ports on host could be: `sudo ufw allow 8888/tcp` `sudo ufw allow 8889/tcp` `sudo ufw enable`). The command includes the *gitconfig* of the host as a volume, in case github will be accessed from within the container. The commande also creates a volume including git repos of the host. Changes to the git repos will remain on the host (here `~/git_repos`) after the container was removed. Note: since the container is accessed as root the git repos will be mounted to `/home/git_repos` in the container. `--gpus all` enables GPU for the container.

Run and keep container:

    docker run --name ml -it -p 8889:8889 -p 8888:8888 -v ~/.gitconfig:/etc/gitconfig -v ~/git_repos:/home/git_repos --gpus all joatom/ml

Using `-it` instead of `--rm` will keep the container and doesn't changes the token after restart (`docker start <containerid>`).


## Resources
- https://docs.fast.ai/install.html
- https://github.com/NVIDIA/nvidia-docker
- https://github.com/jupyter/docker-stacks/

Known alternative containers (haven't tried them, though):
- https://github.com/Paperspace/fastai-docker