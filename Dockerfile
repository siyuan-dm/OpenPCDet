FROM nvcr.io/nvidia/pytorch:20.10-py3 

ENV DEBIAN_FRONTEND noninteractive
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -q -y \
	vim git cmake build-essential libboost-all-dev

RUN git clone https://github.com/siyuan-dm/spconv.git --recursive

RUN cd spconv && python setup.py bdist_wheel && cd dist && pip install *.whl
