# encoding=utf-8
__author__ = 'kevinflynn'
from scrapy import Spider
from scrapy import Selector
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy import Request
from JDCrawler.items import JDGood


class JDSpider(Spider):
    name = "jdspider"
    download_delay = 3
    start_urls = ["http://list.jd.com/list.html?cat=670,671,672"]

    def start_requests(self):
        self.logger.info("start_requests...")
        # cookie = self.cookieprocess()
        for url in self.start_urls:
            yield Request(url = url, callback = self.list_parse)

    def list_parse(self, response):
        self.logger.info("list_parse...")
        self.logger.info(response.url)
        base_url = get_base_url(response)
        sel = Selector(response)
        hrefs = sel.xpath("//*[@id='plist']//div[@class='p-img']/a/@href").extract()
        for href in hrefs:
            detailurl = "http:" + href
            print detailurl
        #     yield Request(url=detailurl, callback=self.detail_parse)
        # nexturl = sel.xpath("//a[@class='pn-next']/@href").extract_first()
        # if nexturl:
        #     nexturl = urljoin_rfc(base_url, nexturl)
        #     self.logger.info(nexturl)
        #     yield Request(url=nexturl, callback=self.list_parse)

    def detail_parse(self, response):
        self.logger.info("detail_parse...")
        jdGood = JDGood()
        self.logger.info(response.url)
        sel = Selector(response)
        gName = sel.xpath("//*[@id='name']/h1/text()").extract_first()
        self.logger.info(gName)
        jdGood['gName'] = gName
        intros = []
        gIntros = sel.xpath("//*[@id='parameter2']/li/text()").extract()
        # self.logger.info(type(gIntros))
        for intro in gIntros:
            intros.append(intro)
        jdGood['gIntro'] = intros
        yield jdGood





        # def cookieprocess(self):
        #     cookiestr="unpl=V2_ZzNtbRYDERMiXRFWchkMVWILEw1LUEFHJg9PUXofXQRuUEdfclRCFXIUR1xnGVQUZAEZWUVcRhRFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHgeWQ1gBRpfQGdzEkU4dlZzEV0BbzMTbUNnAUEpCkVWfBhVSGcAFVhKUEUddwp2VUsa; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_eec7fdf381aa490a863cb68407008bd3; user-key=4bf1b9d7-1938-4298-a507-042de2b85766; cn=0; ipLoc-djd=1-72-4137-0; ipLocation=%u5317%u4EAC; areaId=1; listck=4b5286c8ae10360c3d045f9128a7ee84; __jda=122270672.1264967933.1473214358.1473835958.1474300600.4; __jdb=122270672.13.1264967933|4.1474300600; __jdc=122270672; __jdu=1264967933"
        #     cookies = cookiestr.split(";")
        #     cookiedic = {}
        #     for cookie in cookies:
        #         cstrs = cookie.split("=")
        #         cookiedic[cstrs[0]] = cstrs[1]
        #     return cookiedic
