# MSiA423-Project

## Setting up the environment

SSH into the MSiA 423 server and run the command below:
conda env create -f hpark.yml
conda activate hpark

## Running the python script

1) Run data_download.py python script to download the h1b.csv from AWS S3
2) Run data_upload.py python script to upload the h1b.csv from current directory to AWS S3
3) Run models.py python script to create a table in the RDS server
    (A sample row has already been created so you can uncomment the last few lines to see a sample output from a select all query)
