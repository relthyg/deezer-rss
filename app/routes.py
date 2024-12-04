from flask import render_template, redirect, request, Response

from app import app, cache
from app.deezer_client_facade import get_artist


@app.route('/<artist_id>')
@cache.cached()
def index(artist_id):
    artist = get_artist(artist_id)
    response = Response(render_template('feed.xml', artist=artist, request_url=request.base_url))
    response.headers['Content-Type'] = 'text/xml'

    return response
