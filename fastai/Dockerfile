#docker run -it --gpus all nvidia/cuda:10.0-base
#docker exec -it xxxx bash
#https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile

FROM nvidia/cuda:10.0-base

ENV CONDA_DIR=/opt/conda

RUN apt update && apt -y upgrade && apt -y install curl python3-pip python3-dev less vim

RUN cd /tmp

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

ENV PATH /opt/conda/bin:$PATH

RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
RUN conda --version
RUN conda clean -tipsy
RUN ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
#RUN echo "conda activate base" >> ~/.bashrc

# create conda env
RUN conda update -n base -c defaults conda
RUN conda create -y -n fastai -c pytorch -c fastai fastai
ENV PATH /opt/conda/envs/fastai/bin:$PATH
RUN echo "conda activate fastai" >> ~/.bashrc
RUN conda init bash
RUN conda activate fastai
RUN conda install jupyter notebook
RUN conda install -c conda-forge jupyter_contrib_nbextensions 
RUN conda install jupyterlab
RUN conda install --quiet --yes tini

EXPOSE 8888

ENTRYPOINT ["tini","-g","--"]
CMD ["jupyter-lab.sh"]


#docker build -t ds:fastai .
#docker run -it --runtime=nvidia ds:fastai



