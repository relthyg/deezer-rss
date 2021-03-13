import deezer
from flask import render_template, request, Response

from app import app, cache


@app.route('/<artist_id>')
@cache.cached()
def index(artist_id):
    client = deezer.Client()
    artist = client.get_artist(artist_id)
    albums = artist.get_albums()
    for album in albums:
        tracks = album.get_tracks()
        for track in tracks:
            m, s = divmod(track.duration, 60)
            track.duration_in_minutes = str(m) + ':' + str(s)
        album.tracks = tracks
    artist.albums = albums

    response = Response(render_template('feed.xml', artist=artist, request_url=request.base_url))
    response.headers['Content-Type'] = 'text/xml'

    return response
