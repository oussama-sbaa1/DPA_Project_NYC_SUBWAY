# choose a base image
# see https://quay.io/organization/jupyter for some options
FROM jupyter/pyspark-notebook:spark-3.5.0

# remove pre-existing work directory
RUN rmdir /home/jovyan/work


WORKDIR /home/jovyan/project