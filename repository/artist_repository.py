from db.run_sql import run_sql  

from models.artist import Artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        # artist = artist_repository.select(row['artist_id'])
        artist = Artist(row['name'])
        artists.append(artist)
    return artists