import re

import scrapy

from chinaz_py.items import ChinazItem


class ChinazSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['chinaz.com']
    start_urls = [
        'https://top.chinaz.com/hangye/index_yule.html',
        'https://top.chinaz.com/hangye/index_shopping.html',
        'https://top.chinaz.com/hangye/index_gov.html',
        'https://top.chinaz.com/hangye/index_zonghe.html',
        'https://top.chinaz.com/hangye/index_jiaoyu.html',
        'https://top.chinaz.com/hangye/index_qiye.html',
        'https://top.chinaz.com/hangye/index_shenghuo.html',
        'https://top.chinaz.com/hangye/index_wangluo.html',
        'https://top.chinaz.com/hangye/index_tiyu.html',
        'https://top.chinaz.com/hangye/index_yiliao.html',
        'https://top.chinaz.com/hangye/index_jiaotonglvyou.html',
        'https://top.chinaz.com/hangye/index_news.html'
    ]

    # def parse(self, response):
    #     industry = response.url.split('/')[-1].split('.')[0].split('_')[1] # 修改此处以正确获取行业信息
    #     sites = response.xpath('//div[@class="CentTxt"]')
    #     sites = response.xpath('/html/body/div[4]/div[3]/div[2]/ul')
    #     for site in sites:
    #         item = ChinazItem()
    #         item['url'] = site.xpath('.//div[2]/h3/a').get()
    #         item['title'] = site.xpath('.//内容对应的XPath路径').get()
    #         item['description'] = site.xpath('.//内容对应的XPath路径').get()
    #         item['industry'] = industry
    #         yield item
    def get_page_number_from_url(self, url):
        # 从URL中提取页码
        match = re.search(r'index_[^_]+_(\d+).html', url)
        if match:
            return int(match.group(1))
        return 1  # 如果没有匹配到页码，默认为第一页

    def parse(self, response):
        # 解析列表页面并生成详细页面的请求
        links = response.xpath('//a[@class="pr10 fz14"]/@href').extract()
        for link in links:
            yield response.follow(link, self.parse_detail)

        # 获取下一页的URL
        nexturl = response.xpath('/html/body/div[4]/div[3]/div[2]/div[2]/a[11]/@href').extract_first()

        # 转换为绝对路径
        next_page_url = response.urljoin(nexturl)

        # 解析页码
        current_page_num = self.get_page_number_from_url(response.url)
        next_page_num = self.get_page_number_from_url(next_page_url)

        # 打印当前正在爬取的页面

        # 如果下一页存在且不等于当前页，则继续爬取
        if nexturl and next_page_num and next_page_num <= 5:
        # if nexturl and next_page_num:
            print(f"Current page: {current_page_num}  Next page: {next_page_url}")
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        # 解析详细页面
        item = ChinazItem()
        # 提取详细页面的信息
        item['title'] = response.xpath('//h2[@class="h2Title fl"]/text()').get()
        item['description'] = response.xpath('//p[@class="webIntro"]/text()').get()
        item['url'] = response.xpath('/html/body/div[4]/div/div[2]/div[1]/div/p[1]/a/text()').get()
        item['industry'] = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/p[1]/a[1]/text()').get()
        item['keywords'] = response.xpath('/html/body/div[4]/div/div[2]/div[2]/div/div/p[1]/a[2]/text()').get()
        keywords = response.xpath('//ul[@class="TMainmobWrap"]/li/span[@class="Lnone"]/text()').extract()
        item['keywords'] = ' | '.join(keywords)  # 将关键词列表转换为字符串
        yield item
