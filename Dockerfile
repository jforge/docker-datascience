FROM ubuntu:20.04
MAINTAINER "Klaus Pittig"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install numpy pandas matplotlib seaborn jupyter paho-mqtt

RUN ["mkdir", "notebooks"]
COPY conf/.jupyter /root/.jupyter
COPY run_jupyter.sh /

# Jupyter port
EXPOSE 8888

# Store notebooks in this mounted directory
VOLUME /notebooks

CMD ["/run_jupyter.sh"]
