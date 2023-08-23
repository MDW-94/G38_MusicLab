from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id, track_list) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.genre. album.artisit.id, album.track_list]
    results = run_sql(sql, values)
    id = results[0]['album_id']
    album.album_id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['track_list'], row['album_id'])
        albums.append(album)
    return albums

def select(album_id):
    album = None
    sql = "SELECT * FROM albums WHERE album_id = %s"
    values = [album_id]
    results = run_sql(sql, values)
    if results:
        result = result[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['track_list'], result['album_id'])
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(album_id):
    sql = "DELETE FROM albums WHERE album_id = %s"
    values = [album_id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (title, genre, artist, track_list) = (%s, %s, %s, %s) WHERE album_id = %s"
    values = [album.title, album.genre, album.artisit.id, album.track_list, album.album_id]
    run_sql(sql, values)

def albums_of_artist(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.artisit_id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist, row['track_list'], row['album_id'])
        albums.append(album)
    return albums

