"""
This module corresponds to task 12 of the induction program. 
It converts the list of top chess players from chess.com into
a MongoDB database.

Preconditions: top_chess_players.json does not exist in the current directory.
"""

import scrapy
from scrapy.crawler import CrawlerProcess
import pymongo
import json


class ChessSpider(scrapy.Spider):
    """A spider which grabs the data of the top chess.com in descending order of rank."""
    name = 'chess_spider'

    def start_requests(self):
        yield scrapy.Request('https://www.chess.com/ratings?page=1')

    # pylint: disable=arguments-differ
    def parse(self, response):
        """
        Gets the grandparent tag for all table rows with class 'master-player-rating-rank' to
        reverse-engineer the player "cell". From there standard queries are made to scrape the
        relevant data.
        """
        # pylint: disable=line-too-long
        for player_tr in response.xpath("//div[@class='master-players-rating-rank']/../.."):
            yield {
                'rank': int(player_tr.xpath("td/div[@class='master-players-rating-rank']/text()").extract()[0].strip()[1:]),
                'name': player_tr.xpath("td/div[@class='master-players-rating-user-wrapper']/a[@class='username']/text()").extract()[0].strip(),
                'classical_rating': int(player_tr.xpath("td/div[@class='master-players-rating-player-rank master-players-rating-rank-active']/text()").extract()[0].strip()),
                'rapid_rating': int(player_tr.xpath("td/div[@class='master-players-rating-player-rank ']/text()").getall()[0].strip()),
                'blitz_rating': int(player_tr.xpath("td/div[@class='master-players-rating-player-rank ']/text()").getall()[1].strip()),
            }

        for i in range(2, 51):
            yield scrapy.Request(f'https://www.chess.com/ratings?page={i}', callback=self.parse)


process = CrawlerProcess(settings={
    'FEED_URI': 'top_chess_players.json',
    'FEED_FORMAT': 'json',
})

# Get the relevant JSON data from the website
process.crawl(ChessSpider)
process.start()

client = pymongo.MongoClient('localhost', 27017)
db = client['chess_players']
my_collection = db['top_chess_players']

# my_collection.delete_many({})  # Clear the collection if necessary


with open('top_chess_players.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

my_collection.insert_many(data)
