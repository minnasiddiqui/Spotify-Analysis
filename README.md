# Spotify-Analysis
*hint: for code, switch branch
Hello all! Here's a python project that was done using the input file, SpotifySongs-Dataset.csv and displays relevant information about songs and artists available on the popular platform Spotify. It completes the following tasks using the function data_to_dict that returns a dictionary with the data from input file:

How many artists exists in this dataset?

How many songs exists?

Select a song randomly and display its information.

For each artist display the average value for each song property across all of the songs that belong to that artist.

The song with the highest popularity.

The song with the shortest duration

The song with the longest duration

Find the most common Key used in songs.

Create a function called find_artist_by_property with two parameters: the first should be a song property (e.g., 'tempo', 'loudness'), and the second a boolean value. The function returns the name of an artist based on the specified song property. If the boolean value is True, the function should return the artist with the highest average value for that song property. If it is False, the function should return the artist with the lowest average value for that song property. Add statements that call this function and demonstrates the function works as intended. 

For example this statement should display the artist with the highest average for the tempo property:

print(find_artist_by_property("tempo", True))
