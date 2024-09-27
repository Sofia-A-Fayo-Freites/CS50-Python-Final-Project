# TFT Statistics using Riot Games API

## Description:
This project retrieves data from the Riot Games Developer API, which provides extensive information on all games developed by Riot Games. The program focuses specifically on the game "Teamfight Tactics," gathering data to generate a line chart and table that display a player's placement and total damage dealt in the most recent n games. It also allows users to search multiple games, facilitating comparisons.

The idea for this project arose from my desire to combine three elements: video games, statistics, and API data. I find these three areas both fascinating and full of potential.

Initially, I spent time searching for the right API to use, eventually settling on the Riot Games Developer API Portal (https://developer.riotgames.com/apis). The data provided there is ideal for the kind of statistics I wanted to create.

The Riot Games Developer API provides a key that is valid for 24 hours after approval. This key must be kept private unless you're developing an approved product, so it cannot be hardcoded into the program. To manage this, I used an environment variable. The API key is set in the terminal using the command: $env:RIOT_API_KEY = "api key of the day".

To fetch data from the API, I used the "requests" library. Additionally, I incorporated the Pandas library for data manipulation and Matplotlib for data visualization.

While the program relies more heavily on Matplotlib, I used Pandas to store the retrieved data in a dataframe before creating the line chart and table.

A design decision I made was to have both the table and the chart appear simultaneously when the code is run, making it easier to view large datasets (e.g., 100 matches).

Regarding testing, many of the functions depend on data previously retrieved from the API, so I used mock data to perform pytest. Some functions, like "search_summoner_by_name," "get_match_id," and "get_match_info," as well as "get_placement" and "get_damage," share similar logic, resulting in similar tests.

This is my first Python project, and while it has taken time to grasp every step, I find Python to be a powerful and very valuable tool. I look forward to contiuing learning!
