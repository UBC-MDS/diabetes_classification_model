FROM quay.io/jupyter/minimal-notebook:2023-11-19

# base image comes with ipykernel, ipython, jupyterLab

RUN conda install -y pandas=2.1.3 \
    altair=5.1.2 \
    scikit-learn=1.3.2 \
    vegafusion=1.4.5 \
    vegafusion-python-embed \
    click=8.1.7 \
    jupyter-book=0.15.1 \
    make=4.3

RUN pip install vl-convert-python==1.1.0 \
    pytest==7.4.3 \
    ucimlrepo==0.0.3 \
    myst-nb==1.0.0
