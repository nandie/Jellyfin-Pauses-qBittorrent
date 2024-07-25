import requests
import time
from qbittorrentapi import Client

# Settings
# DO NOT DELETE THE APOSTROPHES ' '
jellyfin_url = 'http://localhost:8096' # This is the default for Jellyfin, change it if you use a different address
jellyfin_api_key = 'paste your API here' # You need to create an API key in the Jellyfin configuration panel
qbittorrent_host = 'localhost' # This is the default for qBittorrent, change it if you use a different address
qbittorrent_port = 8080 # This is the default for qBittorrent, change it if you use a different port
qbittorrent_username = 'change to your username' # Change this to your qBittorrent username
qbittorrent_password = 'change to your password' # Change this to your qBittorrent password

# qBittorrent Client
qb = Client(
    host=qbittorrent_host,
    port=qbittorrent_port,
    username=qbittorrent_username,
    password=qbittorrent_password
)

# Function to check if something is playing on Jellyfin
def is_jellyfin_playing():
    headers = {
        'X-Emby-Token': jellyfin_api_key
    }
    try:
        response = requests.get(f'{jellyfin_url}/Sessions', headers=headers)
        response.raise_for_status()  # Raise an error for HTTP status codes that are errors
        sessions = response.json()

        for session in sessions:
            if session.get('NowPlayingItem'):
                return True
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Jellyfin server. Check if it is running and accessible.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")

    return False

# Function to pause all torrents
def pause_torrents():
    try:
        qb.torrents.pause.all()
    except Exception as err:
        print(f"Error pausing torrents: {err}")

# Function to resume all torrents
def resume_torrents():
    try:
        qb.torrents.resume.all()
    except Exception as err:
        print(f"Error resuming torrents: {err}")

# Variable to store the previous state
was_playing = False

# Main loop
while True:
    is_playing = is_jellyfin_playing()

    if is_playing and not was_playing:
        pause_torrents()
        was_playing = True
    elif not is_playing and was_playing:
        resume_torrents()
        was_playing = False
    
    # Check every minute
    time.sleep(10)
