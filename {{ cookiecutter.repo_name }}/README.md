{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── data               <- directory is for consistent data placement. contents are gitignored by default.
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- intermediate results (mostly for debugging)
    │   ├── processed      <- The final transformed data used for reporting, modeling, etc
    │   └── raw            <- Raw data to use as inputs to rest of pipeline
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries (gitignored by default)
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │    
    ├── tests              <- Tests for the code
    │
    ├── requirements.txt   <- The requirements file for reproducing the environment
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    └── README.md          <- The top-level README for developers using this project.




To perform various task use can use `make`.

For example:
* `make create_environment` will create a new virtual environment 
* `make requirements` will install requirements from `requirements.txt`

To see a complete list of tasks run `make help`.
