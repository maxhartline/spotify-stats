# Function to search songs by song name
def search_by_track_name(track_name, songs_data):
    track_name_lower = track_name.lower()  # Convert to lowercase so search is not case-sensitive 
    results = [song for song in songs_data if song["track_name"].lower() == track_name_lower] # If match is found, include in list
    if not results:
        print("No matching results found for the entered song name.")
    return results

# Function to search songs by artist
def search_by_artist(artist_name, songs_data):
    artist_name_lower = artist_name.lower()
    results = [song for song in songs_data if song["artist(s)_name"].lower() == artist_name_lower]
    if not results:
        print("No matching results found for the entered artist name.")
    return results

# Function to extract stream count from song dictionary
def top_stream_count(song):
    return int(song["streams"]) # Convert streams key to integer

# Function to get top streamed songs
def search_by_top_streamed(num_results, songs_data):
    # Sort songs based on stream count in descending order
    sorted_songs = sorted(songs_data, key=top_stream_count, reverse=True) 
    # Return slice containing the top number of songs
    return sorted_songs[:num_results]