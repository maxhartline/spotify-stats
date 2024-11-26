import csv
import data_functions

# Initializes empty list to store data read from CSV file
songs_data = []

def main():
    global songs_data
    try:
        with open("spotify-2023.csv", "r") as file:    
            csv_reader = csv.DictReader(file) # Creates CSV reader object
            for row in csv_reader:                     
                songs_data.append(row) # Append each row as a dictionary to the list

    except FileNotFoundError:
        print(f"File not found.")
        return

    # Display welcome message and data searching options
    print("Welcome to the Most Streamed Spotify Songs of 2023.\n")
    print("There are 3 options for searching the data.")
    print("The first method searches by song name.")
    print("The second method searches by artist name.")
    print("The final method displays the most streamed songs, allowing you to specify the number of results.")

    while True: 
        # Display search options
        print("\nSearch Options:")
        print("1. Search by song name")
        print("2. Search by artist")
        print("3. Search top streamed songs\n")

        # User input search method choice
        search_method = input("Enter your choice (1-3): ")

        # Search songs by name
        if search_method == "1":
            while True:  # While loop continues indefinitely until search results are found
                track_name = input("\nEnter the song name: ")
                search_results = data_functions.search_by_track_name(track_name, songs_data)
                if search_results:        
                    break # Break out of loop to output results
        
        # Search songs by artist
        elif search_method == "2":
            while True:
                artist_name = input("\nEnter the artist name: ")
                search_results = data_functions.search_by_artist(artist_name, songs_data)
                if search_results:
                    break

        # Display top streamed songs
        elif search_method == "3":
            while True:
                try:
                    num_results = int(input("\nEnter the number of top streamed songs to display (1-952): "))
                    if 1 <= num_results <= 952:  
                        break # Valid integer inputted, break out of loop to output results
                    else:
                        print("Invalid input. Please enter a number between 1 and 952.") # Error handling - integer out of range
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 952.") # Error handling - non-integer 
                    continue
            search_results = data_functions.search_by_top_streamed(num_results, songs_data)
        
        else: 
            print("Invalid search option.")
            continue # Prompt for valid input until received 

        # Output search results
        print("\nResults:")

        # Iterate over each item in list, use enumerate() to keep track of each item's index
        for index, song in enumerate(search_results): 
            stream_count = int(song["streams"]) # Extract the value associated with the streams key, convert to integer
            print(f"{index + 1}. Song: {song['track_name']}, Artist: {song['artist(s)_name']}, Streams: {stream_count}")

        while True: 
            user_choice = input("\nWhat would you like to do next? Enter 'save' to save the search result data, 'continue' to search again, or 'quit' to end the program: ").lower()

            if user_choice == "save":
                filename = input("\nEnter file name to save search results (must end in .csv): ")   
                with open(filename, "w", newline='') as output_file:
                    csv_writer = csv.writer(output_file)  # Creates CSV writer object
                    csv_writer.writerow(["Song Name", "Artist", "Number of Streams"])  # Header row

                    # Iterate over each dictionary in the list and write row to CSV
                    for song in search_results:
                        csv_writer.writerow([song.get("track_name"), song.get("artist(s)_name"), song.get("streams")])  
                
                print("\nSearch results saved successfully.")
            
            elif user_choice == "continue":
                break
            elif user_choice == "quit":
                print("Ending program.")
                exit()

if __name__ == "__main__":
    main()
