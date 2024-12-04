# deezer-rss

This flask application provides an artist's discography on Deezer as
an rss feed. Each album is represented by a feed item, so you can use
it to get notified about new releases.

## Quickstart
You may want to set up and enter a virtual environment

    python3 -m venv venv
    . venv/bin/activate

install the dependencies

    pip install -r requirements.txt

generate a `.env` file

    cp env-example .env

and run the application (on your localhost on port 5000)

    flask run

## Usage
There is only one route, `/artist_id`, so just try visiting https://localhost:5000/2814.

## Features

### Cache
A simple server side caching mechanism is done using
[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/index.html)
and can be tuned in `.env` via `config.py`. As default, nothing is
cached. 
