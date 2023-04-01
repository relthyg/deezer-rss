from flask import render_template, redirect, request, Response

from app import app, cache
from app.deezer_client_facade import get_artist


@app.route('/<artist_id_or_name>')
@cache.cached()
def index(artist_id_or_name):
    artist = get_artist(artist_id_or_name)
    if artist.name != artist_id_or_name:
        return redirect(f'/{artist.name}', 302)
    response = Response(render_template('feed.xml', artist=artist, request_url=request.base_url))
    response.headers['Content-Type'] = 'text/xml'

    return response
