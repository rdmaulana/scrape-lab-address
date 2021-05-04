import scrapy
import pandas as pd

df = pd.read_excel('lab.xlsx', sheet_name='TARGET_MONEV')
arr = df['lab_tujuan_nm'].to_numpy()

class LabSpider(scrapy.Spider):
    name = 'lab'
    allowed_domains = ['google.com']
    start_urls = ['https://google.com/search?&q='+loc.replace(' ', '+') for loc in arr]

    def parse(self, response):
        lab_name = response.xpath('//div[@class="SPZz6b"]/h2/span/text()').get()
        address = response.xpath('//span[@class="LrzXr"]/text()').get()
        prov = response.xpath('//span[@class="Eq0J8 LrzXr kno-fv"]/a/text()').get()

        yield {
            'nama_lab': lab_name,
            'address': address,
            'prov': prov
        }