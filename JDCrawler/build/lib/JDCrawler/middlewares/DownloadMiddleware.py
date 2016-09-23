#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib

# from scrapy.contrib.downloadermiddleware import DownloaderMiddleware
from scrapy.http import HtmlResponse

class JDDownloadMiddleware(object):

    def process_request(self,request,spider):
        result=requests.get(request.url)
        html = result.content
        return HtmlResponse(request.url, body=html)