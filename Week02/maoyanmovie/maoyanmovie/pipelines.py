# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanmoviePipeline:
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='test',charset='utf8mb4')
        self.con1 = self.conn.cursor()

    def process_item(self, item, spider):
        mname = item['mname']
        mtype = item['mtype']
        mtime = item['mtime']

        count = self.con1.execute('insert into test values(%s,%s,%s);',(mname, mtype, mtime))
        count = self.con1.execute('commit;')

        return item

    def close_spider(self,spider):
        self.con1.close()
        self.conn.close()




