# Example project repository

<!-- toc -->

- [Project Charter](#project-charter)
- [Project Backlog](#project-backlog)
- [Repo structure](#repo-structure)
- [Documentation](#documentation)
- [Running the application](#running-the-application)
  * [1. Set up environment](#1-set-up-environment)
    + [With `virtualenv` and `pip`](#with-virtualenv-and-pip)
    + [With `conda`](#with-conda)
  * [2. Configure Flask app](#2-configure-flask-app)
  * [3. Initialize the database](#3-initialize-the-database)
  * [4. Run the application](#4-run-the-application)
- [Testing](#testing)

<!-- tocstop -->

## Project Charter

**Vision**: This project is aimed at predicting H1-B visa applicants probability of getting their visa approved based on the previous H1-B filings. The project has been inspired by international students at Northwestern who are thinking about working in the US after graduation. H1-B is very important for these students and anyone applying for this visa because H1-B allows immigrants to be able to live and work in the US legally while they apply for permanent residency. While it is absolutely necessary to have H1-B visa, it is very hard to file, and it is even harder to refile after a rejection. This project will help make cases stronger before filing for H1-B visa by allowing users to check what the chances are before filing or even experimenting with different options to make their case stronger.

**Mission**: A predictive model will be built using the previous H1-B visa applications data from Kaggle. The model will be used to predict how likely each filing is likely to succeed. The users will be able to use the model that will be called by a website. Users will be able to input their filing data and possible filing options in an interactive website to see what their chances are of getting an approval.

**Success criteria**: The success criteria will be determined by two different factors. First, by how easy it is for users to interact with the website and get the predictions that they want in meaningful time. The website and model should work seamlessly and should not break easily. Second factor is how accurate the model is for predicting the filing approval odds. The classification success rate should be above 70% where success is defined as getting the approval and rejection correctly. This project contains a lot of business value because compared to what is at stake, there is not much public information or interactive tools that users can use to check their chances of getting their visa approved. This service could be sold to customers individually, host ads, and connect users to specialists such as lawyers. <br/>

## Project Backlog

### Planning

**Theme**: Allow users to check different possible filings to see what the chances are of getting their visa approved

Epic 1: Understand the Problem <br/>
&nbsp;&nbsp;&nbsp;Story 1: Understand the H1-B filing process in more detail <br/>
&nbsp;&nbsp;&nbsp;Story 2: Do more research on how hard it is to file and refile for H1-B <br/>

Epic 2: Data Collection and Exploration <br/>
&nbsp;&nbsp;&nbsp;Story 1: Downloading and loading the data from Kaggle <br/>
&nbsp;&nbsp;&nbsp;Story 2: Checking for outliers and performing EDA <br/>

Epic 3: Feature Engineering <br/>
&nbsp;&nbsp;&nbsp;Story 1: Cluster by company size/industry or school prestige <br/>
&nbsp;&nbsp;&nbsp;Story 2: Hot-encoding by 1 for modeling <br/>

Epic 4: Modeling

Epic 5: Website Implementation <br/>
&nbsp;&nbsp;&nbsp;Story 1: Create a website using Flask <br/>
&nbsp;&nbsp;&nbsp;Story 2: Deploy it in the cloud <br/>

### Backlog

1. Research.H1-B Process (2 points)
2. Research.Refiling H1-B (1 point)
3. Data.Find and Download from Kaggle (1 point)
4. Data.EDA (4 points)
5. Feature.Clutering (3 points)
6. Feature.Hot-Encoding (2 points)
7. Modeling (8 points)
8. Website.Flask (3 points)
9. Website.Hosting (6 points)


### Icebox

Use a more complex model for higher accuracy <br/>
Provide users with recommendation on how to increase the chances of approval <br/>

## Repo structure

```
├── README.md                         <- You are here
│
├── app
│   ├── static/                       <- CSS, JS files that remain static
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── models.py                     <- Creates the data model for the database connected to the Flask app
│   ├── __init__.py                   <- Initializes the Flask app and database connection
│
├── config                            <- Directory for yaml configuration files for model training, scoring, etc
│   ├── logging/                      <- Configuration files for python loggers
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git.
│   ├── archive/                      <- Place to put archive data is no longer usabled. Not synced with git.
│   ├── external/                     <- External data sources, will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── docs                              <- A default Sphinx project; see sphinx-doc.org for details.
│
├── figures                           <- Generated graphics and figures to be used in reporting.
│
├── models                            <- Trained model objects (TMOs), model predictions, and/or model summaries
│   ├── archive                       <- No longer current models. This directory is included in the .gitignore and is not tracked by git
│
├── notebooks
│   ├── develop                       <- Current notebooks being used in development.
│   ├── deliver                       <- Notebooks shared with others.
│   ├── archive                       <- Develop notebooks no longer being used.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports and helper functions.
│
├── src                               <- Source data for the project
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files
│   ├── sql/                          <- SQL source code
│   ├── add_songs.py                  <- Script for creating a (temporary) MySQL database and adding songs to it
│   ├── ingest_data.py                <- Script for ingesting data from different sources
│   ├── generate_features.py          <- Script for cleaning and transforming data and generating features used for use in training and scoring.
│   ├── train_model.py                <- Script for training machine learning model(s)
│   ├── score_model.py                <- Script for scoring new predictions using a trained model.
│   ├── postprocess.py                <- Script for postprocessing predictions and model results
│   ├── evaluate_model.py             <- Script for evaluating model performance
│
├── test                              <- Files necessary for running model tests (see documentation below)

├── run.py                            <- Simplifies the execution of one or more of the src scripts
├── app.py                            <- Flask wrapper for running the model
├── config.py                         <- Configuration file for Flask app
├── requirements.txt                  <- Python package dependencies
```
This project structure was partially influenced by the [Cookiecutter Data Science project](https://drivendata.github.io/cookiecutter-data-science/).

## Documentation

* Open up `docs/build/html/index.html` to see Sphinx documentation docs.
* See `docs/README.md` for keeping docs up to date with additions to the repository.

## Running the application
### 1. Set up environment

The `requirements.txt` file contains the packages required to run the model code. An environment can be set up in two ways. See bottom of README for exploratory data analysis environment setup.

#### With `virtualenv`

```bash
pip install virtualenv

virtualenv pennylane

source pennylane/bin/activate

pip install -r requirements.txt

```
#### With `conda`

```bash
conda create -n pennylane python=3.7
conda activate pennylane
pip install -r requirements.txt

```

### 2. Configure Flask app

`config.py` holds the configurations for the Flask app. It includes the following configurations:

```python
DEBUG = True  # Keep True for debugging, change to False when moving to production
LOGGING_CONFIG = "config/logging/local.conf"  # Path to file that configures Python logger
PORT = 3002  # What port to expose app on
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tracks.db'  # URI for database that contains tracks

```

The configuration currently says to save the database to a temporary location as it is just for testing. However, if you are not on your local machine, you may have issues with this location and should change it to a location within your home directory, where you have full permissions. To change it to saving in the data directory within this repository, run the Python code from this directory and change the `config.py` to say:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///../data/tracksB.db'
```

The three `///` denote that it is a relative path to where the code is being run (which is from `src/add_songs.py`).

You can also define the absolute path with four `////`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/chloemawer/repos/MSIA423-example-project-repo-2019/data/tracks.db'
```

### 3. Initialize the database

To create the database in the location configured in `config.py` with one initial song, run:

`python run.py create --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`

To add additional songs:

`python run.py ingest --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`


### 4. Run the application

 ```bash
 python app.py
 ```

### 5. Interact with the application

Go to [http://127.0.0.1:3000/]( http://127.0.0.1:3000/) to interact with the current version of hte app.

## Testing

Run `pytest` from the command line in the main project repository.


Tests exist in `test/test_helpers.py`
