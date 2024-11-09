# Read the contents of the songs dataset file and return the data in a dictionary format
def data_to_dict(filename, header):
    # Open file to access data
    data_file = open(filename, "r")

    # If file has a header line read it and save it
    header_line = ""
    if header:  
        header_line = data_file.readline().strip() # Read the header line of the file to extract attributes

    # Initialize an empty dictionary to store the data
    data_dict = {}
    
    # Iterate over each line in the data file
    for line in data_file:

        # Remove leading and trailing whitespaces, and split the line into a list using commas
        line = line.strip().split(",")
        
        # Get the artist name
        artist = line[1]
        # Remove the artist name from the details since it is used as the key
        line.pop(1)
        # If artist in dictionary add line value list
        if artist in data_dict:
            data_dict[artist].append(line)
        else: # New type found
            data_dict[artist] = [line]
      
     # Close the file
    data_file.close()

    # Return the data organinzed in a dictionary
    return data_dict

########################################################
# uncomment the following line to display the data dictionary
#print(data_to_dict("SpotifySongs-Dataset.csv", True))
########################################################
# Add your solution here
########################################################
# Task 1: How many artists exists in this dataset?
def count_artists(data_dict):
    return len(data_dict)

artists_count = count_artists(data_to_dict("SpotifySongs-Dataset.csv", True))
print("Number of artists:", artists_count)
# Task 2: How many songs exist?
def count_songs(data_dict):
    total_songs = 0
    for artist in data_dict:
        total_songs += (len(data_dict[artist]))
    return total_songs

data_dict = data_to_dict("SpotifySongs-Dataset.csv", True)

songs_count = count_songs(data_dict)
print("Number of songs:", songs_count)
#Task 3: Select a song randomly and display its information
import random
def random_song(data_dict):
    random_artist = random.choice(list(data_dict.keys()))
    random_song = random.choice(data_dict[random_artist])
    return random_song
random_song_info = random_song(data_dict)
print("Here's random info about a song: ", random_song_info)
#Task 4: For each artist display the average value for each song property across all of the songs that belong to that artist.
def calculate_average(data_dict):
    # Initialize a dictionary to store the averages
    averages = {}
    # Iterate over each artist and their songs
    for artist, songs in data_dict.items():
        # Initialize lists to store the sum of each property
        sums = [0] * 8
        # Iterate over each song to calculate the sum of each property
        for song in songs:
            for i in range(8):
                sums[i] += float(song[i+1])
        # Calculate the average for each property
        #For each property (danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness), the code iterates over all the songs belonging to a particular artist and calculates the sum of that property. This sum is stored in the sums list.
        avg_properties = [s / len(songs) for s in sums]
        #To calculate the average value for each property, the code divides each sum by the total number of songs (len(songs)). This gives the average value of each property across all the songs belonging to the artist.
        # Store the averages in the dictionary
        averages[artist] = avg_properties
    return averages

def display_results(data_dict, averages):
    # Display artist averages
    print("Artist averages")
    for artist, avg_properties in averages.items():
        #Within the loop, prints out the artist's name followed by an arrow (-->) and the list of average properties -used f-strings for formatting.
        print(f"{artist} --> {avg_properties}")
# Calculate averages
averages = calculate_average(data_dict)
# Display results
display_results(data_dict, averages)
#Task 5: The song with the highest popularity.
max_popularity = 0
max_popularity_song = None
for artist_songs in data_dict.values():
    for song in artist_songs:
        #Song is list, popularity is index 1. Extracts popularity value, converts it to floating point so that it can be compared numerically
        popularity = float(song[1])
        # Check if the current song has higher popularity than the current maximum
        if popularity > max_popularity:
            # Update the maximum popularity and the corresponding song
            max_popularity = popularity
            max_popularity_song = song[0]
print("Song with the highest popularity: ", max_popularity_song)
#Task 6: Song with the shortest duration
#Initializes variable to infinity so any value encountered will be shorter
shortest_duration = float('inf')
shortest_duration_song_name = ''
for artist_songs in data_dict.values():
    for song in artist_songs:
        # Extract the duration value from the song
        duration = int(song[9])
        # Check if the current song has shorter duration than the current shortest
        if duration < shortest_duration:
            # Update the shortest duration and the corresponding song name
            shortest_duration = duration
            shortest_duration_song_name = song[0]
print("Song with shortest duration: ", shortest_duration_song_name)
#Task 7: Song with the longest duration
longest_duration = 0
longest_duration_song_name = ''
for artist_songs in data_dict.values():
    for song in artist_songs:
        duration = int(song[9])
        if duration > longest_duration:
            longest_duration = duration
            longest_duration_song_name = song[0]
print("Song with longest duration: ", longest_duration_song_name)
#Task 8: Find the most common Key used in songs.
key_counts = {}
for artist_songs in data_dict.values():
    #iterates over each song entry within list of songs
    for song in artist_songs:
        key = int(song[4])
        # Increments  count of current key in key_counts dictionary.. if key doesn't exist in the dictionary yet, it'll initialize it with a count of 0 and then increment it by 1.
        key_counts[key] = key_counts.get(key, 0) + 1
#Uses the max function to find the key with the maximum count in the key_counts dictionary. uses key_counts.get to get the count associated with each key.
most_common_key = max(key_counts, key=key_counts.get)
# Retrieves the count associated with the most common key from the key_counts dictionary.
count = key_counts[most_common_key]
print("Most common key: ", most_common_key)
#Task 9: Create a function called find_artist_by_property with two parameters: the first should be a song property (e.g., 'tempo', 'loudness'), and the second a boolean value.
def find_artist_by_property(property_name, is_highest):
    # Define a dictionary to map property names to their corresponding indices
    properties_dict = {
        "popularity": 1,
        "danceability": 2,
        "energy": 3,
        "key": 4,
        "loudness": 5,
        "liveness": 6,
        "valence": 7,
        "tempo": 8,
        "duration_ms": 9
    }

    # Initialize variables to store the artist with the highest/lowest average property value
    target_artist = None
    target_value = None if is_highest else float('inf')
    
    # Iterate over each artist and calculate the average property value
    for artist, songs in data_dict.items():
        # Initialize variable to store the total property value for the artist
        total_value = 0
        # Count the number of songs by the artist
        num_songs = len(songs)
        # Calculate the total property value for all songs by the artist
        for song in songs:
            total_value += float(song[properties_dict[property_name]])
        # Calculate the average property value for the artist
        avg_value = total_value / num_songs
        # Update target artist based on whether we are looking for highest or lowest value
        if is_highest:
            if target_value is None or avg_value > target_value:
                target_artist = artist
                target_value = avg_value
        else:
            if target_value is None or avg_value < target_value:
                target_artist = artist
                target_value = avg_value
    
    return target_artist

# Test the function to make it look like output
print("Artist with highest popularity average: ", find_artist_by_property("popularity", True))
print("Artist with lowest popularity average: ", find_artist_by_property("popularity", False))
print("Artist with highest danceability average: ", find_artist_by_property("danceability", True))
print("Artist with lowest danceability average: ", find_artist_by_property("danceability", False))
print("Artist with highest energy average: ", find_artist_by_property("energy", True))
print("Artist with lowest energy average: ", find_artist_by_property("energy", False))
print("Artist with highest key average: ", find_artist_by_property("key", True))
print("Artist with lowest key average: ", find_artist_by_property("key", False))
print("Artist with highest loudness average: ", find_artist_by_property("loudness", True))
print("Artist with lowest loudness average: ", find_artist_by_property("loudness", False))
print("Artist with highest liveness average: ", find_artist_by_property("liveness", True))
print("Artist with lowest liveness average: ", find_artist_by_property("liveness", False))
print("Artist with highest valence average: ", find_artist_by_property("valence", True))
print("Artist with lowest valence average: ", find_artist_by_property("valence", False))
print("Artist with highest tempo average: ", find_artist_by_property("tempo", True))
print("Artist with lowest tempo average: ", find_artist_by_property("tempo", False))
print("Artist with highest duration_ms average: ", find_artist_by_property("duration_ms", True))
print("Artist with lowest duration_ms average: ", find_artist_by_property("duration_ms", False))