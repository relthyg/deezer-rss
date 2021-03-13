import deezer
from flask import render_template

from app import app


@app.route('/<artist_id>')
def index(artist_id):
    client = deezer.Client()
    artist = client.get_artist(artist_id)
    albums = artist.get_albums()
    for album in albums:
        album.tracks = album.get_tracks()
    artist.albums = albums

    return render_template('feed.html', artist=artist)
