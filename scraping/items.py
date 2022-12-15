# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem_Films(scrapy.Item):
    
    titre =scrapy.Field()
    titre_original= scrapy.Field()
    score=scrapy.Field()
    genre=scrapy.Field()
    date=scrapy.Field()
    duree=scrapy.Field()
    Description=scrapy.Field()
    acteurs=scrapy.Field()
    public=scrapy.Field()
    pays= scrapy.Field()
    langue=scrapy.Field()

class ImdbItem_Series(scrapy.Item):
    titre =scrapy.Field()
    titre_original= scrapy.Field()
    score=scrapy.Field()
    genre=scrapy.Field()
    date=scrapy.Field()
    duree=scrapy.Field()
    Description=scrapy.Field()
    acteurs=scrapy.Field()
    public=scrapy.Field()
    pays= scrapy.Field()
    langue=scrapy.Field()
