#spider weibo.cn
import requests
import json
import os
import uuid
file_path='weiboimages'
if not os.path.exists(file_path):
    os.makedirs(file_path)
def get_info(url):
    imgs_list=[]
    response=requests.get(url).text
    jd = json.loads(response)
    for content in jd['data']['cards']:#type(content) dict
        for c in content['card_group']:#list
            try:
                img_list=c['mblog']['pics']
                if len(img_list) !=0:
                    imgs_list.extend(img_list)
            except:
                pass
    for element in imgs_list:
        img_url=element['large']['url']
        img_name=img_url.split('/')[-1]
        if os.path.exists(os.path.join(file_path,img_name)):
            continue
        with open(os.path.join(file_path,img_name),'wb')as fp:
            fp.write(requests.get(img_url).content)
if __name__=='__main__':
    keywords='长裙'
    start_url='https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D{}&page_type=searchall&page={}'
    for page in range(1,10):#suggest:page from 2 to end
        url=start_url.format(keywords,page)
        get_info(url)

