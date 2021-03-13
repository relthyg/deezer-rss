# deezer-rss

This flask application provides an artist's discography on Deezer as
rss feed. Each album is represented by a feed item, so you can use
it to get notified about new releases.

## Quickstart
You may want to set up and enter a virtual environment

    python3 -m venv venv
    . venv/bin/activate

install the dependencies

    pip install -r requirements.txt

generate an `.env` file

    cp env-example .env

and run the application (on your localhost on port 5000)

    flask run

## Usage
There is only one route, `/artist_id_or_name`, so you can visit
either https://localhost:5000/2814 or https://localhost:5000/opeth
to get the same result. Note: Using the artist's name may be fuzzy
and end up in false results.

## Features

### Cache
A simple server side caching mechanism is done using
[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/index.html)
and can be tuned in `.env` via `config.py`. As default, nothing is
cached. 
