from datetime import datetime

import deezer


def get_artist(artist_id_or_name):
    client = deezer.Client()
    try:
        artist = client.get_artist(int(artist_id_or_name))
    except:
        artist = client.search(artist_id_or_name, relation='artist')[0]
    artist.albums = get_albums(artist)
    return artist


def get_albums(artist):
    albums = artist.get_albums()
    for album in albums:
        album.tracks = get_tracks(album)
        album.duration = 0
        for track in album.tracks:
            album.duration += track.duration
        album.duration_in_minutes = get_duration_in_minutes(album.duration)
        album.pub_date = datetime.strptime(album.release_date, '%Y-%m-%d').strftime("%a, %d %b %Y %H:%M:%S +0100")
    return albums


def get_tracks(album):
    tracks = album.get_tracks()
    for track in tracks:
        track.duration_in_minutes = get_duration_in_minutes(track.duration)
    return tracks


def get_duration_in_minutes(duration_in_seconds):
    m, s = divmod(duration_in_seconds, 60)
    return str(m).zfill(2) + ':' + str(s).zfill(2)
