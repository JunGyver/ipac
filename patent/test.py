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
