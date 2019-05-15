# MSiA423-Project

## Setting up the environment

<br>
SSH into the MSiA 423 server and clone the repository by running this command:<br>
git clone -b midproject https://github.com/henrypark133/MSiA423-Project.git
<br>
<br>

Run the command below in MSiA 423 server:<br>
conda env create -f hpark.yml<br><br>
Activate the conda environment that was created to run the python script:<br>
conda activate hpark<br>

## Running the python script

1) Run data_download.py python script to download the h1b.csv from AWS S3
2) Run data_upload.py python script to upload the h1b.csv from current directory to AWS S3
3) Run models.py python script to create a table in the RDS server
    (A sample row has already been created so you can uncomment the last few lines to see a sample output from a select all query)
