import scrapy
from scrapy.loader import ItemLoader


class Product(scrapy.Item):
    pdtName = scrapy.Field()
    pdtPrice = scrapy.Field()
    lastUpdated = scrapy.Field(serializer=str)

class QuotesSpider(scrapy.Spider):
    name = "bbNaps"
    start_urls = [
        'https://www.babybunting.com.au/huggies-drynites-boys-4-7-yrs.html',
        'https://www.babybunting.com.au/huggies-nappy-pants-girl-toddler-31.html',
    ]

    def parse(self, response):
          pdtName = response.css('div.product-view form#product_addtocart_form > div.row > div.col-sm-10.col-xs-6 > div.product-name > h1::text').extract_first()
          pdtPrice = response.xpath('/html/body/div[2]/div[5]/div/div[4]/div/div[2]/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/meta[2]').extract()
          lastUpdated = today()
          print "[%s] [%s] [%s]" % (pdtName, pdtPrice, lastUpdated)
##        l = ItemLoader(Item = Product(), response=response)
##        l.add.css('pdtName', 'div.product-view form#product_addtocart_form > div.row > div.col-sm-10.col-xs-6 > div.product-name > h1::text')
##        l.add.xpath('pdtPrice', '/html/body/div[2]/div[5]/div/div[4]/div/div[2]/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/meta[2]')
##        l.add_value('last_updated', 'today')
##        return l.load_item()
##        for nappies in response.css('div.main'):
##            yield {
##                'pdtURL': self,
##                'pdtName': nappies.css('div.breadcrumbs > ul > li.product > h1::text').extract_first(),
               ## 'pdtOldPrice': nappies.css('div.container-fluid-nested > div.row price-row > div.col-sm-6 > div.price-box > p.old-price > span.price::text').extract_first(),
               ## 'pdtNewPrice': nappies.css('div.price-box > p.special-price > span.price::text').extract_first(),
##                'pdtRegPrice': nappies.xpath('/html/body/div[2]/div[5]/div/div[4]/div/div[2]/div[2]/form/div[3]/div[2]/div[3]/div[2]/div/div[1]/div/meta[2]').extract_first()
##            }
