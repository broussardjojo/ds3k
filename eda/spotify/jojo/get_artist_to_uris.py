# Imports
import pandas as pd
import pathlib
import requests

import tekore as tk

import api_setup

CWD = pathlib.Path.cwd()
REPO_ROOT = CWD.parent.parent.parent
DATA_DIR = REPO_ROOT / "data"
APP = 'spotify'
NAME = 'jojo'
SUBDIRS = 'my_spotify_data/MyData/'
USER_DATA_DIR = DATA_DIR / APP / NAME / SUBDIRS

env_vars = api_setup.parse_api_kvs(REPO_ROOT / "api-keys")

# Doing the same for all of us and turning that into a json file
if __name__ == "__main__":
    # Getting data
    print("Preparing streaming history data...")
    list_all_members_streaming_history = []
    for group_member in ['jojo', 'nick', 'richard']:
        data_path = USER_DATA_DIR = DATA_DIR / APP / group_member / SUBDIRS
        data_files = data_path.glob("StreamingHistory*.json")
        for file in data_files:
            with open(file, encoding='utf-8') as thisfile:
                data = pd.read_json(thisfile)
                list_all_members_streaming_history.append(data)
    all_members_streaming_history = pd.concat(list_all_members_streaming_history, ignore_index=True)
    all_artists = all_members_streaming_history.artistName.unique()
    print(f"Obtained {len(all_members_streaming_history)} records, with {len(all_artists)} unique artists.")

    # Set up API
    app_token = tk.request_client_token(env_vars['client_id'], env_vars['client_secret'])
    spotify = tk.Spotify(app_token)

    with spotify.max_limits():
        for artist_name in all_artists:
            query = f"artist:{artist_name}"
            artist_info = spotify.search(query=query, limit=0)
            print(artist_info)