#!/bin/bash

# Define the URLs
cache_url="https://storage.googleapis.com/mlops3/cache.zip"
faiss_index_url="https://storage.googleapis.com/mlops3/faiss_index.zip"
data_url="https://storage.googleapis.com/mlops3/data.zip"

# Download the zip files
wget $cache_url
wget $faiss_index_url
wget $data_url

# Unzip the zip files into their respective name folders
unzip cache.zip -d cache
unzip faiss_index.zip -d faiss_index
unzip data.zip -d data

# Delete the zip files
rm cache.zip
rm faiss_index.zip
rm data.zip