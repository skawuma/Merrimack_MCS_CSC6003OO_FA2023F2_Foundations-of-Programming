# Explanation

## I wanted to incorporated all concepts that have been so far been covered.most importantly if and else statement, while loop aand String Operations.The program therefore flows as follows

## 1. Create an empty dictionary called "music_collection" and initialize it to hold the songs

## 2. Make a function named "add_song" that asks for the song's title and artist from the user

Request the song's title from the user.
request that the user enter the artist.
To the "music_collection" dictionary, add the song title as the key and the artist as the value.

## 3. Make a "retrieve_song_details" function that asks for the song title and returns the artist matching to it

Request the song's title from the user.
Get the artist associated with the song title entered from the "music_collection" dictionary.
Present the artist.

## 4. Make a function named "update_song_details" that accepts the song title from the user and modifies the artist information

Prompt the song's title from the user.
Verify the "music_collection" dictionary to see if the entered song title is present.
Ask the user to enter the new artist information if it already exists.
Update the "music_collection" dictionary's artist information.
Show a message letting users know the update was successful.
Display an error message saying that the song title could not be discovered if it does not exist.

## 5. Create the "delete_song" function, which takes a song title from the user and deletes the relevant song from the "music_collection" dictionary

Request the song's title from the user.
Verify the "music_collection" dictionary to see if the entered song title is present.
Remove the song from the lexicon if it exists.
Show a message letting the user know the deletion was accomplished.

Display an error message saying that the song title could not be discovered if it does not exist.

## 6. Make a "display_all_songs" function that lists every song in the "music_collection" dictionary

The objects in the "music_collection" dictionary should be iterated over.
Show each song's title and associated artist.

## 7. Use a loop to keep asking the user for their input until they decide to stop

Show the user a menu of options from which to choose.
Ask the user to enter their selection.
Call the relevant function in accordance with the user's selection.
Stop the cycle if the user decides to leave.

## 8. End the program
