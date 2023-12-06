class Music:
  
    """
       Base class for a Music.

  Global  Variables:
    - music_collection: Dictionary
    -str1:String
    -str2:String

    Methods:
    - add_song() -> None:
         Add the song title as the key and the artist name as the value to the music collection dictionary
    
    - get_song_details() -> str:
         Retrieve the corresponding artist from the music collection dictionary using the song title as the key.
         Display the artist information.
    - update_song_details() -> str:
         Update the artist information in the music collection dictionary using the song title as the key.
         Display a message indicating the update was successful.
   - def delete_song() -> None:
        Remove the song from the music collection dictionary using the song title as the key.
        Display a message indicating the song was successfully deleted
   - display_all_songs() -> str:
        terate over the keys and values in the music collection dictionary.
        Display each song title and its corresponding artist
 
    """ 
  
    str1="Enter the song title: "
    str2="Song title not found."
    music_collection={}
    
    
    def __init__(self) -> None:
      
       """
        Constructor to instantiate the Music  class.

        Parameters:-> None
        
       """ 
    
     

    def add_song(self):
        
     """Prompt the user to enter the song title.
      Prompt the user to enter the artist name.
      Add the song title as the key and the artist name as the value to the music collection dictionary
     Args:
        None

     Returns:
           The string .
           
     """
 
    
     song_title = input(self.str1)
     artist = input("Enter the artist: ")
     self.music_collection[song_title] = artist
   
     print("Song added successfully.")
     return self.music_collection
    
    def get_song_details(self):
     """Prompt the user to enter the song title.

     Args:
       None.

     Returns:
       If the song title exists in the music collection:
        Retrieve the corresponding artist from the music collection dictionary using the song title as the key.
        Display the artist information.
     If the song title does not exist in the music collection, display an appropriate message.

      """
    #  str1="Enter the song title: "
    #  str2="Song title not found."
    #  music_collection={}
     song_title = input(self.str1)
     if song_title in self.music_collection:
      artist = self.music_collection[song_title]
      print(f"The artist for '{song_title}' is '{artist}'.")
     else:
       print(self.str2)
       
    def update_song_details(self):
    
     """Prompt the user to enter the song title.

      Args:
        None.

      Returns:
      If the song title exists in the music collection:
         Prompt the user to enter the updated artist name.
         Update the artist information in the music collection dictionary using the song title as the key.
         Display a message indicating the update was successful.
      If the song title does not exist in the music collection, display an appropriate message.
      """
    #  str1="Enter the song title: "
    #  str2="Song title not found."
    #  music_collection={}
     song_title = input(self.str1)
     if song_title in self.music_collection:
       artist = input("Enter the new artist: ")
       self.music_collection[song_title] = artist
       print("Song details updated successfully.")
     else:
       print(self.str2)

    def delete_song(self):
      """Prompt the user to enter the song title.

       Args:
         None.

        Returns:
          If the song title exists in the music collection:

             Remove the song from the music collection dictionary using the song title as the key.
             Display a message indicating the song was successfully deleted
          If the song title does not exist in the music collection, display an appropriate message.
      """
    
      song_title = input(self.str1)
      if song_title in self.music_collection:
         del self.music_collection[song_title]
         print("Song deleted successfully.")
      else:
       print(self.tr2)
       
    def display_all_songs(self):
       """

       Args:
        None.

       Returns:
         If the music collection dictionary is not empty:
          Iterate over the keys and values in the music collection dictionary.
           Display each song title and its corresponding artist.
         If the music collection dictionary is empty, display a message indicating there are no songs in the collection.
       """
       if len(self.music_collection) > 0:
           print("All songs in the music collection:")
           for song_title, artist in self.music_collection.items():
             print(f"Song: {song_title}, Artist: {artist}")
       else:
         print("The music collection is empty.")