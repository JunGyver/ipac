'''
import json    
import PyPDF2

pdf_file = open('aa.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
print(read_pdf)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()

print(page_content)

def get_data(page_content):
    _dict = {}
    page_content_list = page_content.splitlines()
    for line in page_content_list:
        if ':' not in line:
            continue
        key, value = line.split(':')
        _dict[key.strip()] = value.strip()
    return _dict

page_data = get_data(page_content)
json_data = json.dumps(page_data, indent=4)
print(json_data)


import httplib2
import json, xmljson
import xmltodict
from .models import Master

apply_num = Master.objects.all().first()
print(apply_num)
#url = 'http://plus.kipris.or.kr/openapi/rest/RegistrationService/registrationInfo?registrationNumber=1018301090000&accessKey=QWSwer5evYdATtLpvybUIqIPUQZR6ATVfDNMLksLZMU='
#url2 = f'http://plus.kipris.or.kr/openapi/rest/RelatedDocsonfilePatService/relatedDocsonfileInfo?applicationNumber={1020160087644}&accessKey=QWSwer5evYdATtLpvybUIqIPUQZR6ATVfDNMLksLZMU='
#city = 'Seoul'
#mykey = '&APPID=5e19e0a4433cbb1b0a6e5f0e5b784af2'

#h = httplib2.Http()
#myrequest = url+city+mykey
#response, content = h.request(url, 'GET')
#result = json.loads(content.decode('utf-8'))
#result = content.decode('utf-8')
#print(result)
#jsonString = json.dumps(xmltodict.parse(result), indent=4)
#json2 = json.loads(jsonString)
#print(json2)

import json
from elasticsearch import Elasticsearch

from django.views import View
from django.http  import JsonResponse

#from my_settings import ELASTICSEARCH

class SearchView(View):
    def get(self, request):
        es = Elasticsearch('http://127.0.0.1:9200')

        search_word = request.GET.get('search')

        if not search_word:
            return JsonResponse({'message':'INVALID_REQUEST'}, status=400)

        data_list = es.search(
            index       = 'dictionary',
            filter_path = ['hits.hits._source'],
            body        = {
                "query" : {
                    "multi_match" : {
                        "query"  : search_word,
                        "fields" : [
                            "tags_name",
                            "st_master_abstract",
                            "st_master_title",
                            "st_master_claim"
                        ]
                    }
                }
            }
        )

        return JsonResponse({'data': data_list}, status=200)
'''
