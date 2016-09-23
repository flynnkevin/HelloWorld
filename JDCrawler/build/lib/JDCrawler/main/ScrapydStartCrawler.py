#encoding=utf-8
import urllib
import urllib2
def executePostRequest():
    # # 定义一个要提交的数据数组(字典)
    # data = {}
    # # data['tasks'] = tasks
    # data['project'] = 'JDCrawler'
    # data['spider'] = 'jdspider'
    # # 定义post的地址
    # url = 'http://localhost:6800/schedule.json'
    # post_data = urllib.urlencode(data)
    # # 提交，发送数据
    # req = urllib2.urlopen(url)
    # # 获取提交后返回的信息
    # content = req.read()
    # print content
    # return content
    data={'project':'JDCrawler','spider':'jdspider'}
    data_urlencode=urllib.urlencode(data)
    requrl="http://localhost:6800/schedule.json"
    req=urllib2.Request(url=requrl,data=data_urlencode)
    response=urllib2.urlopen(req)
    result=response.read()
    print type(result)
    print result
    dict=eval(result)
    print dict['status']
    print dict['jobid']

if __name__ == '__main__':
    executePostRequest()
    # {"status": "ok", "jobid": "81ac25ae7fc311e6abe7a45e60e38487", "node_name": "kevinflynndeMacBook-Pro.local"}
    #
    # ok
    # 81
    # ac25ae7fc311e6abe7a45e60e38487