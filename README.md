# Jellyfin-qBittorrent Pause/Resume Script

This script monitors playback activity on a Jellyfin media server and pauses or resumes all torrents on a qBittorrent client based on whether media is playing.

## Features

- Checks if any media is currently being played on Jellyfin.
- Pauses all torrents in qBittorrent when media playback starts.
- Resumes all torrents in qBittorrent when media playback stops.
- Runs continuously, checking playback status every 10 seconds.

## Requirements

- Python 3.x
- `requests` library
- `qbittorrent-api` library

## Installation

1. Download the script to your local machine.
   
2. Install the required Python libraries:
   ```sh
   pip install requests qbittorrent-api
   
3. Open the script file and update the following variables with your own settings:
```sh
jellyfin_url = 'http://localhost:8096'
jellyfin_api_key = 'your_jellyfin_api_key'
qbittorrent_host = 'localhost'
qbittorrent_port = 8080
qbittorrent_username = 'your_qbittorrent_username'
qbittorrent_password = 'your_qbittorrent_password'

