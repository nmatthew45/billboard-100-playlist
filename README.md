# billboard-100-playlist

This python program allows you to input a date and create a private spotify playlist featuring the billboard.com top 100 songs from the inputted date.

Prerequisites:
1. You will need to go to https://developer.spotify.com/dashboard/applications and create an app.
2. Go to your app and click "Edit settings".
3. Add a redirect URI and hit "Save".
4. Keep note of your Client ID, Client Secret, and Redirect URI

How to run:
1. Clone this repository
2. Add your Client ID, Client Secret, and Redirect URI to the .env file. Example: CLIENT_ID=abc123
3. Open a terminal and navigate to the project folder. Example: cd billboard-100-playlist
4. Run: pip install requests spotipy python-dotenv beautifulsoup4
5. Run program using: py main.py
