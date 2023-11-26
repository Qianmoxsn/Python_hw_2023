import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run_spider(spider_name):
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_name)
    process.start()


# 设置CSV文件路径
csv_file_path = 'D:\\Code\\chinaz_py\\outputfile.csv'

if __name__ == "__main__":
    # 检查文件是否存在，如果存在，则删除
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
    run_spider('chinaz')  # 'chinaz' 是你的爬虫名称
