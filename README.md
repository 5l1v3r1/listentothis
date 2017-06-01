# listentothis
A simple script to update one of my Spotify playlists with the top 10 songs from /r/listentothis 

## Executing the script
The program can be invoked by the following command:

python listentothis.py keys.txt

Note: the input file "keys.txt" is user-specific since it contains all keys -- public and private -- needed for the script to run properly.

See the next section for information on how "keys.txt" should be formatted in order for the program to work as desired.

## Format of "keys.txt"
The file format must be of the form\:

\<reddit client_id\>

\<reddit client_secret\>

\<reddit user_agent\>

\<spotify client_id\>

\<spotify oauth code\>

\<spotify user id\>

\<spotify playlist key\>

