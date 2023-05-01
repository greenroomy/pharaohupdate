import scrapy


class ShopscrapingSpider(scrapy.Spider):
    name = "shopscraping"
    allowed_domains = ["rakuten.co.jp"]
    start_urls = ["http://rakuten.co.jp/"]

    def parse(self, response):
        pass
