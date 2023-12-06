
from Music import Music


def main():
   
  """Prints the menu and prompts the user for a choice.

  Args:
    None.

  Returns:
    The user's choice.
  """

  print(""" 
  ******** WELCOME TO MY MMUSIC COLLECTION MANAGER"***********
  -------------------------------------------------------------
  1.add - Prompt the user to enter the song title and artist, and add it to the music collection"
  2.getSongDetials - Prompt the user to enter a song title, and display the corresponding artist from the music collection "
  3.del - Prompt the user to enter a song title, and remove the corresponding song from the music collection"
  4.UpdateSongDetails - Prompt the user to enter a song title, and update the artist information in the music collection"
  5.diplayAllSongs - Display all songs in the music collection"
  6.EXIT/QUIT
  """)
 
 

  while True:
    choice = input("Enter your choice (1-6): ")
    #Creating an Onject of Class Music
    music =Music()
   
    if choice == '1':
      music.add_song()
    elif choice == '2':
      music.get_song_details()
    elif choice == '3':
       music.delete_song()
    elif choice == '4':
       music.update_song_details()
    elif choice == '5':
       music.display_all_songs()
    elif choice == '6':
       break
    else:
       print("Invalid choice. Please try again.")

  print("Program terminated.")
if __name__ == "__main__":
    main()