# Billboard Hot 100 To Spotify Playlist
> Python 3 app that takes Billboard top 100 songs from a particular date you enter, then creates new Spotify playlist, and adds those tracks there.

## How to use
1. Install all requered libraries
2. Setup constants: Spotify keys, redirect URL ([Get it here](https://developer.spotify.com/dashboard))
3. Run the main.py, enter the date you want (YYYY-MM-DD)
4. Authorize into your Spotify account in the appeared window
5. It'll redirect you to your redirect page, copy the whole URL and put into the CLI
6. Done! Wait till the finish of execution

> Steps 4-5 needed only for the first launch. It'll generare .cache file for the furthers work

### Libraries
- requests (no need to install)
- bs4 (needed to install)
- spotipy (needed to isntall)

### Notes
- The app might not add exactly 100 tracks to your playlist because of not availability on Spotify or weird name on the Billboard website
- Available data is only from August 4, 1958
