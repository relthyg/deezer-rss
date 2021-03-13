from flask import render_template, request, Response

from app import app, cache
from app.deezer_factory import get_artist


@app.route('/<artist_id_or_name>')
@cache.cached()
def index(artist_id_or_name):
    artist = get_artist(artist_id_or_name)
    response = Response(render_template('feed.xml', artist=artist, request_url=request.base_url))
    response.headers['Content-Type'] = 'text/xml'

    return response
