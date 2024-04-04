from pathlib import Path
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner
import extruct
import re
import time


def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

class SUTDCrawler(CrawlSpider):
    name = 'SUTD'
    allowed_domains = ['sutd.edu.sg']

    start_urls = ['https://www.sutd.edu.sg'] # https://www.sutd.edu.sg/Education/Pillars-Programmes-Clusters

    rules = (
        Rule(
            LinkExtractor(
                deny=["https://mylibrary.sutd.edu.sg/availability/", "https://mylibrary.sutd.edu.sg/calendar/"]
            ),
            process_links=process_links,
            callback='parse_item',
            follow=True
        ),
    )

    timestr = time.strftime("%Y%m%d-%H%M%S")
    fname = "sutd"
    file_path = f'{fname}_{timestr}.jsonl'
    print(file_path)
    custom_settings = {
		'FEEDS': { file_path : { 'format': 'jsonlines', "overwrite": True}}
		}

    def parse_item(self, response):
        print(response.url)

        file_path = f"test.txt"
        with open(file_path, "a") as f:
            f.write(response.url + "\n")

        return {
            'url': response.url,
            'metadata': extruct.extract(
                response.text,
                response.url,
                syntaxes=['opengraph', 'json-ld']
            ),
        }