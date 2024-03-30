#!/bin/bash

# Define the URLs
cache_url="https://storage.googleapis.com/mlops3/cache.zip"
faiss_index_url="https://storage.googleapis.com/mlops3/faiss_index.zip"
data_url="https://storage.googleapis.com/mlops3/data.zip"

# Download the zip files
if [ ! -f /cache.zip ]; then
    wget $cache_url
fi
if [ ! -f /faiss_index.zip ]; then
    wget $faiss_index_url
fi
if [ ! -f /data.zip ]; then
    wget $data_url
fi


# Unzip the zip files into their respective name folders
unzip -n cache.zip
unzip -n faiss_index.zip
unzip -n data.zip

# Delete the zip files
rm cache.zip
rm faiss_index.zip
rm data.zip