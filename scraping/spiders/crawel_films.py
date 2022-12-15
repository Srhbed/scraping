import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImdbItem_Films
import re
from ast import literal_eval


class CrawlFilmsSpider(CrawlSpider):
    name = 'crawl_films'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.imdb.com/chart/top/', headers={
    #         'User-Agent': self.user_agent,
    #         "Accept-Language": self.langue
    #     })


    le_films_details = LinkExtractor(restrict_xpaths="//td[@class='titleColumn']/a")
    rule_films_details = Rule(le_films_details,
                             callback='parse_item',
                              follow=False)
    rules = (
      rule_films_details  ,
    )

    def parse_item(self, response):
        items=ImdbItem_Films()
        
        duree=response.xpath('//li[@class="ipc-inline-list__item"]/text()')[0:].extract()
        if duree==[]:
          duree_en_minute='non_connu'
        elif len(duree)==5:
          duree_en_heure=int(duree[0])*60
          duree_en_minute=int(duree[3])
          duree_en_minute =duree_en_heure+duree_en_minute
        elif len(duree)==2:
               if duree[1]=="h":
                duree_en_minute = int(duree[0])*60
               else:
                duree_en_minute = int(duree[0])
        items['titre']= response.xpath('//h1/text()').extract()
        items['titre_original']=response.xpath('//div[@class="sc-dae4a1bc-0 gwBsXc"]/text()').extract()
        items['score']=response.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]/text()').extract_first()
        items['genre']=response.xpath('//span[@class="ipc-chip__text"]/text()').extract()
        items['date']=response.xpath('//span[@class="sc-8c396aa2-2 itZqyK"]/text()').extract()
        items['duree']=duree_en_minute
        items['Description']=response.xpath('//span[@class="sc-16ede01-0 fMPjMP"]/text()').extract()
        items['acteurs']=response.xpath('//a[@class="sc-bfec09a1-1 gfeYgX"]/text()').extract()
        items['public']=response.xpath('//span[@class="sc-8c396aa2-2 itZqyK"]/text()')[-1].extract()
        # pays=response.xpath("//section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").extract()
        items['pays']=response.xpath('/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section/div[2]/ul/li[2]/div/ul/li/a/text()')[0].extract()





        

        yield items
            # 'titre': titre,
            # 'titre_original': titre_original,
            # 'score':score,
            # 'genre':genre,
            # 'date':date,
            # 'duree':duree,
            # ' Description': Description,
            # 'acteurs':acteurs,
            # 'public':public,
            # 'Pays' : pays,
            # 'langue':langue,
            
  
            
            
            

            
        