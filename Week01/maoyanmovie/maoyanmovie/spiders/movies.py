# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3' # 已修改
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.url)
        items = [dict(mname ='电影名称', mtype = '电影类型', mtime = '上映时间' )]
        movies = Selector(response=response).xpath('///div[@class="movie-hover-info"]')
        for movie in movies[:10]: # 需要限制次数
            item = MaoyanmovieItem()
            mname = movie.xpath('./div[1]/span[1]/text()')
            mtype = movie.xpath('./div[2]/text()')
            mtime = movie.xpath('./div[4]/text()')
            item['mname'] = mname.extract_first().strip()
            item['mtype'] = mtype.extract()[1].strip()
            item['mtime'] = mtime.extract()[1].strip()
            items.append(item)

        return items