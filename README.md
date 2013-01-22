espn_player_scraper
===================

Scrapes the espn player ID numbers and player links from various sports and outputs them into json

Run this at the top level of the project to get the different sports outputs:
scrapy crawl espn_players -a sport='nba' -o nba.json -t json

You can substitude the sport from 'nba' to 'nfl, 'nhl', and 'mlb'.  
You can also subtitute the filename (nba.json) to anything you want.  

The format output it only limited to what scrapy allows - I've tried XML output, but it haven't seen it work well straight from here; probably needs some configuration.

PIP requirements file is included in the repo