from datetime import datetime

import deezer, time


def get_artist(artist_id_or_name):
    client = deezer.Client()
    try:
        artist = client.get_artist(int(artist_id_or_name))
    except:
        artist = client.search(artist_id_or_name, relation='artist')[0]
    artist.albums = get_albums(artist)
    return artist


def get_albums(artist):
    counter = 3 # The Deezer API allows 50 requests in 5 seconds. Up to 3 were already made here.
    albums = artist.get_albums(limit = 999)
    for album in albums:
        if counter > 49:
            time.sleep(5)
            counter = 0
        album.tracks = get_tracks(album)
        counter = counter + 1
        album.duration = 0
        for track in album.tracks:
            album.duration += track.duration
        album.duration_in_minutes = get_duration_in_minutes(album.duration)
        album.pub_date = datetime.strptime(album.release_date, '%Y-%m-%d').strftime("%a, %d %b %Y %H:%M:%S +0100")
        album.is_complete = str(is_complete(album))
    return albums


def get_tracks(album):
    tracks = album.get_tracks()
    for track in tracks:
        track.duration_in_minutes = get_duration_in_minutes(track.duration)
    return tracks


def get_duration_in_minutes(duration_in_seconds):
    m, s = divmod(duration_in_seconds, 60)
    return str(m).zfill(2) + ':' + str(s).zfill(2)


def is_complete(album):
    for track in album.tracks:
        if not track.readable:
            return False
    return True
