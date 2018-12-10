# TMDb Search App using Django

A movie-search engine based on Django, powered by TMDb.

## Contents
- [TMDb Search App using Django](#tmdb-search-app-using-django)
    - [Contents](#contents)
    - [Platform](#platform)
    - [Dependencies](#dependencies)
    - [Usage](#usage)
        - [Install Dependencies](#install-dependencies)
    - [Run](#run)
    - [Live Demo](#live-demo)

## Platform

```
    python: 3.7.1
    vs code: 1.25.1
    ubuntu: 18.04
```

## Dependencies

- **`Django`**: A high-level Python web framework.
- **`tmdbsimple`**: A Python wrapper on the TMDb V3 API.
- **`gunicorn`**: A Python WSGI HTTP Server for UNIX, used to host the webiste on Heroku.
- **`whitenoise`**: A simple static file serving package for Python web apps.

## Usage

Dependencies must be set up in an enviroment before using the project. Follow the following instructions for setting up the environment:

### Install Dependencies

- **For pip:**
  ```
    python3 -m virtualenv <environment name>
    source <environment name>/bin/activate
    pip install -r requirements.txt
  ```
- **For Anaconda:**
  ```
    conda env create -f environment.yml
    source activate django-tmdb
    pip install -r requirements.txt
  ```

## Run
    ```
        python manage.py runserver
        OR
        gunicorn pytmdb.wsgi:application --log-file -
    ```

## [Live Demo](https://django-tmdb.herokuapp.com)

This web app has been deployed live on Heroku.

<img src="https://i.imgur.com/InHkGUW.jpg" alt="">
<img src="https://i.imgur.com/9U7UM7P.png" alt="">