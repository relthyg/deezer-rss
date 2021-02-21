from flask import render_template

from app import app


@app.route('/<artist>')
def index(artist):
    return render_template('feed.html', artist=artist)
