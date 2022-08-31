import json
from mianshi.items import MianshiItem
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class MsSpider(scrapy.Spider):
    name = 'ms'
    allowed_domains = ['so.quandashi.com']
    start_urls = ['https://so.quandashi.com/search/search/search-list']
    #相当于 respond = requests.get()
    def parse(self, response):
        pass
    def start_requests(self):
        self.url = 'https://so.quandashi.com/search/search/search-list'
        self.post_data = {
            'page': '0',
            'key': '阿里',
            'pageSize': '20',
            'styles': 'all,jingzhun,high_low_similar,bufen,jiazi,jianzi,bianzi,huanxu,pinyin,teshuzi,xingjinzi',
        }
        temp = '%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; QDS_COOKIE=80D6C09F-59FB-0ED2-E4ED-167285F9599C; QDS_LOGIN_INFO=%7B%22userName%22%3A%22qds3798396%22%2C%22avtar%22%3A%22%22%7D; QDS_LOGIN_INFO_OFFICE=%7B%22operatorId%22%3A%22784626%22%2C%22operatorName%22%3Anull%2C%22userId%22%3A%226c32702f44715069556e44646e2b5747517477616d773d3d%22%2C%22userName%22%3Anull%2C%22userImg%22%3Anull%2C%22agentOrWriter%22%3A2%7D; QDS_AGENT_ORGAN_INFO=%7B%22agentIde%22%3A%226c32702f44715069556e44646e2b5747517477616d773d3d%22%2C%22account%22%3A%2218565111216%22%2C%22agentName%22%3Anull%2C%22agentOrganId%22%3Anull%2C%22agentOrganName%22%3Anull%2C%22agentOrganConName%22%3A%22%5Cu533f%5Cu540d%22%7D; INGRESSCOOKIE=1661581131.743.15403.552611; PHPSESSID=cdef6ee00a4e076b7af2a29765d8245c; nTalk_CACHE_DATA={uid:kf_9479_ISME9754_guest8167D74D-2944-54,tid:1661581130239379}; Hm_lvt_df2da21ec003ed3f44bbde6cbef22d1c=1661415871,1661493311,1661574017,1661581131; _csrf=34127f26f17bd23f770c7dee1ecde7589d3457920d6a126d235ed34daaac2421a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pT8cz8nk5uD6jcIg-_Zn84vX04zYU49j%22%3B%7D; Hm_lpvt_df2da21ec003ed3f44bbde6cbef22d1c=1661589702'
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split(';')}
        yield scrapy.FormRequest( url = self.url , callback = self.parse_second , formdata = self.post_data , cookies = cookies )


    def parse_second(self,response):
        content = response.text.encode('utf-8').decode('unicode_escape')
        content = json.loads(content, strict=False)
        # print(content)
        for i in range(20):
            try:
                item = MianshiItem()
                all_data = content['data']['items'][i]
                item['当前状态'] = all_data.get('statusZh')
                item['申请号'] = all_data.get('regNo')
                item['申请日期'] = all_data.get('appDate')
                item['初审日期'] = all_data.get('announcementDate')
                item['注册日期'] = all_data.get('privateStartDate')
                item['申请人'] = all_data.get('applicantCn')
                item['代理机构'] = all_data.get('agency')
                yield item
            except:
                break

        self.post_data['page'] = str(int(self.post_data['page'])+1)
        yield scrapy.FormRequest(self.url , callback = self.parse_second , formdata = self.post_data)











