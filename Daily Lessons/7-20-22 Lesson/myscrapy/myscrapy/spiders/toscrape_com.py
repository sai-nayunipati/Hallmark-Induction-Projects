import scrapy
from myscrapy.items import QuoteItem


class ToscrapeComSpider(scrapy.Spider):
    name = 'toscrape.com'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quote = response.css('div.quote')
        text = quote.css('span.text::text').get()
        author = quote.css('small.author::text').get()
        tags = quote.css('a.tag::text').getall()

        item = QuoteItem()
        item['text'] = text
        item['author'] = author
        item['tags'] = tags

        yield item
