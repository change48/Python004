# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        mname = item['mname']
        mtype = item['mtype']
        mtime = item['mtime']
        content = f"{mname},{mtype },{ mtime} \r\n"
        # with open("./movies.csv", mode="a+", encoding="utf-8") as file:
        #     file.write(content)
        # # movie_info = pd.DataFrame(data=result)
        # # movie_info.to_csv('./movie.csv', encoding='utf8', index=False, header=True)
        # return item
        with open('./maoyan.csv', 'a+', encoding='utf-8') as m_csv:
            m_csv.write(content)
            m_csv.close()
        return item




