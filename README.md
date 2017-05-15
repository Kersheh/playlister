Playlister
===
A Spotify to Youtube playlist converter. Playlister authorizes with your Spotify account, pulls a list of tracks for a playlist, and creates a text file consisting of links of the first Youtube search result for each song.

requirements
---
- [spotipy](https://github.com/plamere/spotipy)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

config
---
Rename `config_example.json` to `config.json` and fill out username, id, and secret from Spotify API.

run
---
- `playlister 'Playlist Name' -o=output.txt -s=true`

Parameters -o (file output) and -s (shuffle) are optional. Default exports to cwd as autoplaylist.txt without shuffle.
