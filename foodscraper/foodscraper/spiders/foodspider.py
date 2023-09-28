import scrapy


class FoodspiderSpider(scrapy.Spider):
    name = "foodspider"
    allowed_domains = ["food.oregonstate.edu"]
    start_urls = ["https://food.oregonstate.edu/todays-hours"]

    def parse(self, response):
        #here you extract the specific things you want
        pass
