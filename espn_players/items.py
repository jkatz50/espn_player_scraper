# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ESPN_team(Item):
    name = Field()
    link = Field()
    players = Field()
    # define the fields for your item here like:
    # name = Field()

class ESPN_player(Item):
    name = Field()
    link = Field()
    id_num = Field()
