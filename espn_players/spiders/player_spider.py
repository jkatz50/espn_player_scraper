from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from espn_players.items import ESPN_team,ESPN_player
import re

class ESPNSpider(BaseSpider):
    name = 'espn_players'
    allowed_domains = ["espn.go.com"]
    start_urls = ["http://espn.go.com/nba/players"]
    
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        team_links = hxs.select("//div[@class='mod-content']/ul/li/div")

        teams = []
        for link in team_links:
            team = ESPN_team()
            team["name"] = link.select("a/text()").extract()
            team["link"] = link.select("a/@href").extract()
            teams.append(team)

        for team in teams:
            url = "http://espn.go.com" + team["link"][0]
            request = Request(url,callback = lambda r: self.parse_players(r))
            request.meta['team'] = team
            yield request

    def parse_players(self,response):
        team = response.request.meta['team']
        hs = HtmlXPathSelector(response)

        even_player_links = hs.select("//tr[contains(concat(' ',@class,' '),' evenrow ')]/td[2]")
        odd_player_links = hs.select("//tr[contains(concat(' ',@class,' '),' oddrow ')]/td[2]")

        players = []
        for link in even_player_links:
            player = ESPN_player()
            player["name"] = link.select("a/text()").extract()
            player["link"] = link.select("a/@href").extract()
            player["id_num"] = re.findall('\d+',str(player["link"]))
            if player["id_num"]:
                players.append(player)

        for link in odd_player_links:
            player = ESPN_player()
            player["name"] = link.select("a/text()").extract()
            player["link"] = link.select("a/@href").extract()
            player["id_num"] = re.findall('\d+',str(player["link"]))
            if player["id_num"]:
                players.append(player)

        team['players'] = players
        yield team
