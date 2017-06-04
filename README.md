# Pr0nBot v0.69-alpha
A NSFW Discord Bot written in Python

A little sparse at the moment, but that will change in due time. Feel free to break it and suggest improvements.

### Current Dependencies
* [discord.py](https://github.com/Rapptz/discord.py)
* [requests](https://github.com/requests/requests)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Setup
1. Install the latest version of Python 3, and then install all dependencies above using `pip`
2. Go [here](https://discordapp.com/developers/applications/me), login, and then create a new App. Give it a nice name (Like "Pr0nBot")
3. Get an [invite link that will never expire](https://support.discordapp.com/hc/en-us/articles/208866998-Instant-Invite-101) for the Discord channel you want Pr0nBot to join. Add it as a "Redirect URL" for your App. Fill out a custom description and icon if you would like.
4. Create an App Bot User on your App's Settings page. Copy the Client ID of your App to your clipboard.
5. Go to this link: https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_GOES_HERE&scope=bot&permissions=0 but replace "CLIENT_ID_GOES_HERE" with the Client ID you just copied. This link should add the bot to your server.
6. Pull down the Pr0nBot GitHub repo to your computer
7. Rename config.default.json to config.json. Open it up and insert the Client ID you copied in-between the quotes on the right side of "discord_token"
8. Run MainBot.py. If all was done correctly, Pr0nBot should join your server and be good to go!

### Currently Available Commands
* .pornhub
  * A set of commands for browsing PornHub
  * .pornhub home
    * Lists some of the "Hottest" and "Most Viewed" videos from the front page of PornHub
  * .pornhub search \<query\> [page] [minRating]
    * Allows you to search PornHub for videos. Simple as that!
  * .pornhub category <categoryName> [page] [minRating]
    * Allows you to browse PornHub by category
  * .pornhub category list
    * Sends you a comprehensive list of all available categories you can use with .pornhub category
  * .pornhub hottest [page] [minRating]
    * Allows you to browse the "Hottest" videos on PornHub
  * .pornhub mostviewed [page] [minRating]
    * Allows you to browse the "Most Viewed" videos on PornHub
  * .pornhub toprated [page] [minRating]
    * Allows you to browse the "Top Rated" videos on PornHub

<sub><3 You Henry</sub>
