# scrapy_nfl_players
Simply demo using scrapy web scrapping platform

scrap NFL players info from https://www.pro-football-reference.com/
These players are displayed in the home page of https://www.pro-football-reference.com/
If extracts the name, position, height,weight and Team info if present.

The extracted data can be saved to a csv file, json file ...

scrapy command to run the script
scrapy crawl players -o players_info.csv
or
scrapy crawl players -o players_info.json 
for output in json format
