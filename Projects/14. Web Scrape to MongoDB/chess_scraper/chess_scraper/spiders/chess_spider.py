import scrapy


class ChessSpider(scrapy.Spider):
    """A spider which grabs the data of the top chess.com in descending order of rank."""
    name = 'chess_spider'
    start_urls = ['https://www.chess.com/ratings?page=1']

    n = 50
    current_depth = 1

    def parse(self, response):
        """
        Gets the grandparent tag for all table rows with class 'master-player-rating-rank' to
        reverse-engineer the player "cell". From there standard queries are made to scrape the
        relevant data.
        """
        # pylint: disable=line-too-long
        for player_tr in response.xpath("//div[@class='master-players-rating-rank']/../.."):
            yield {
                'rank': player_tr.xpath("td/div[@class='master-players-rating-rank']/text()").extract()[0].strip()[1:],
                'name': player_tr.xpath("td/div[@class='master-players-rating-user-wrapper']/a[@class='username']/text()").extract()[0].strip(),
                'classical_rating': player_tr.xpath("td/div[@class='master-players-rating-player-rank master-players-rating-rank-active']/text()").extract()[0].strip(),
                'rapid_rating': player_tr.xpath("td/div[@class='master-players-rating-player-rank ']/text()").getall()[0].strip(),
                'blitz_rating': player_tr.xpath("td/div[@class='master-players-rating-player-rank ']/text()").getall()[1].strip(),
            }

        # Get the next page of players
        next_page = response.xpath(
            "//a[@aria-label='Next Page']/@href").extract()[0]
        if next_page is not None and self.current_depth < self.n:
            self.current_depth += 1
            yield response.follow(next_page, callback=self.parse)
