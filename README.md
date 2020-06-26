# scrapy_nfl_players
Simply demo using scrapy web scrapping platform

scrap NFL players info from https://www.pro-football-reference.com/
These players are displayed in the home page of https://www.pro-football-reference.com/
If extracts the name, position, height,weight and Team info if present.

The extracted data can be saved to a database,csv file, json file ...
This demo uses postgresql database

use psql command line utility to create database and table

//create scrapy database
CREATE DATABASE scrapy;

//create players_data table
CREATE TABLE players_data(
   name VARCHAR UNIQUE NOT NULL,
   position VARCHAR NOT NULL,
   height_and_weight VARCHAR NOT NULL,
   team VARCHAR
);

scrapy command to run the script
scrapy crawl players -o players_info.csv
or
scrapy crawl players -o players_info.json 
for output in json format

refer to players_info.json in the root directory for sample output 

Also check the database for inserted rows
"SELECT * FROM players_data";
