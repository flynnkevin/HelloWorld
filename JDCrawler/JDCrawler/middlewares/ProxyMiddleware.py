#encoding=utf-8
import base64
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

class ProxyMiddleWare(HttpProxyMiddleware):

    def process_request(self,request,spider):
        request.meta['proxy']="http://123.249.45.34:8080"
        proxy_user_pass = "minivision:xskj2016"
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        print request.meta['proxy']