import scrapy
import logging
'''
Extract player info from www.pro-football-reference.com
These players are displayed in the home page 
'''
class PlayersSpider(scrapy.Spider):
    name = 'players'

    start_urls = ['https://www.pro-football-reference.com/']

    def parse(self, response):
        #select all players in front page
        players = response.css('div.images a')

        #extract all players. Auto follow player links:
        yield from response.follow_all(players, self.parse_player_details)


    def parse_player_details(self,response):
        player_detail = response.css('div.players')
        # extract player name - text inside h1
        name = player_detail.css('h1::text').get()

        # other details - return all paragrah elements
        otherinfo = player_detail.css('p')

        #init default values
        position = "NA"
        height_and_weight = "NA"
        team = "NA"

        #each paragrah inside otherinfo
        for para in otherinfo:
            strong_text = para.css('p strong::text').get()

            # extract player position
            if strong_text == "Position":
                # ['\n\t', ': CB\n\t\n'] - sample text output so select 1
                position = para.css('p::text').getall()[1].strip()
                #discard first 2 characters
                logging.info('position text %s', position[2:])
            #check first span with itemprop attribute
            attribute_value = para.css('p span::attr(itemprop)').get()
            # extract player height and weight
            if attribute_value == "height":
                height_and_weight = para.css('p::text').getall()[1].strip()
                height_and_weight = height_and_weight.replace('\u00a0', ' ')
            # extract player team info
            if attribute_value == "affiliation":
                team = para.css('p a::text').get()
                break

        # output scrapped data
        yield {
            'name': name,
            'position': position[2:],
            'height and weight': height_and_weight,
            'team': team
        }

