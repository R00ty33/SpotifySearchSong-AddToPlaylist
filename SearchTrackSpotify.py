# This python script opens a .txt file in format: 
# Artist - Song Title
# Then searches each song title and adds each song to your playlist using Spotify's WEB API

#Imports
import requests 
from requests.api import get
import time


file = "<insert_file_name_here>"
playlistURL = "<insert_playlist_code_here>"
token = "Bearer <insert_token_here>"

getSearchReq = "https://api.spotify.com/v1/search"
postPlaylistReq= "https://api.spotify.com/v1/playlists/" + playlistURL + "/tracks"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": token
}


def main():
    errorCount = 0
    failedSongArray = [] #holds songs which weren't added

    with open(file) as song_file: #open file
        for song in song_file: #read each line
            #time.sleep(0.25)
            q = song
            params = {
                "q": q,
                "type": "track",
                "market": "US",
                "limit": 1,
            }

            try: #Find song
                print("\n\nGetting song..................       ", q.strip('\n'))

                response = requests.get(getSearchReq, headers=headers, params=params)
                json = response.json()
                name = json.get('tracks').get('items')[0].get('name')
                uri = json.get('tracks').get('items')[0].get('uri')

                print("Found song....................       ", uri.strip('\n'))


                params = {
                    "uris": json.get('tracks').get('items')[0].get('uri')
                }

                try: #Add song to playlist
                    print("Adding song to playlist.......       ", name.strip('\n'))
                    response = requests.post(postPlaylistReq, headers=headers, params=params)
                except:
                    errorCount += 1
                    failedSongArray.append(q.strip('\n'))
                    print("\nERROR\nException caught while adding song to playlist\n")
            except:
                errorCount += 1
                failedSongArray.append(q.strip('\n'))
                print("\nERROR\nException caught getting song\n")

    print("\nFinished......................")
    print("Total Errors..................       ", errorArray)
    print("Failed to add song:........... ")

    for failedSong in failedSongArray:
        print(failedSong)

 
main()