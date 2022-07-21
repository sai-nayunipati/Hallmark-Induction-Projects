"""This is in the spiders folder. It is assumed you have a scrapy project."""

import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky']

    def parse(self, response):

        for products in response.css('div.product-item-info'):
            l = ItemLoader(item=WhiskyscraperItem(), selector=products)

            l.add_css('name', 'a.product-item-link')
            l.add_css('price', 'span.price')
            l.add_css('link', 'a.product-item-link::attr(href)')

            yield l.load_item()

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
