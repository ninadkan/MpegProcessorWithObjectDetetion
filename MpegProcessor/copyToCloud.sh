#! /bin/bash
# Copy the files to Azure storage

# $SASTokenForDest is stored as environmental variable
destinationLocation="https://mpegparserimages.file.core.windows.net/images/"
sourceLocation="/home/azureuser/MpegProcessorWithObjectDetetion/MpegProcessor/Data/"

sudo azcopy cp "${sourceLocation}" "${destinationLocation}${SASTokenForDest}" --recursive