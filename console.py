import pdb
from models.artist import Artist
import repository.artist_repository as artist_repository


artists = artist_repository.select_all()

for artist in artists:
    print(artist.__dict__)