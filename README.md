[![CircleCI](https://circleci.com/gh/jforge/docker-datascience.svg?style=svg)](https://circleci.com/gh/jforge/docker-datascience)

## Docker image for mostly Python-based data science tools

This repository is created to work with data science tools in context of respective courses on the web.

Focuses on providing the essentials, but adds paho-mqtt a MQTT client library.
This is for interaction with environments for IIoT use cases.


This Docker images comes with:
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter
- paho-mqtt

Candidates for next integration steps:
- Sklearn
- pyyaml
- h5py
- Tensorflow
- Keras
- OpenCV 3

The images are built on top of [Ubuntu 20.04 Docker container](https://hub.docker.com/_/ubuntu/) ([Dockerfile](https://github.com/jforge/docker-datascience/blob/master/Dockerfile)) 

### Usage

Run a Docker container from this image using the following command:
```sh
docker run -it -p 8888:8888 -d \
  -v $(pwd)/notebooks:/notebooks \
  jforge/datascience
```

Exposing port 8888 and mapping the `notebooks` folder supports the work with the Jupyter UI.


### Contained tools & libraries

The following tools and libraries are integration to work in the field of data science
and scientific computing.

#### Numpy

[NumPy](https://numpy.org/) is a library for the Python programming language,
adding support for large, multi-dimensional arrays and matrices, along with a large collection
of high-level mathematical functions to operate on these arrays.

#### Pandas

[Pandas](https://pandas.pydata.org/) is a fast, powerful, flexible and easy to use open source 
data analysis and manipulation tool, built on top of the Python programming language.

#### Matplotlib

[Matplotlib](https://matplotlib.org/) Matplotlib is a comprehensive library for creating static, 
animated, and interactive visualizations in Python.

#### Seaborn

[Seaborn](https://seaborn.pydata.org/) is a library for making statistical graphics in Python.
It is built on top of matplotlib and closely integrated with pandas data structures.

### Jupyter

Project [Jupyter](https://jupyter.org/) exists to develop open-source software, open-standards, 
and services for interactive computing across dozens of programming languages.

The Jupyter Notebook is an open-source web application to create and share documents that 
contain live code, equations, visualizations and narrative text. 
Among others, uses include: data cleaning and transformation, numerical simulation, 
statistical modeling, data visualization, machine learning.

### Paho-MQTT

[paho-mqtt](https://pypi.org/project/paho-mqtt/) is the Eclipse Paho MQTT Python client library, 
which implements versions 5.0, 3.1.1, and 3.1 of the MQTT protocol.
