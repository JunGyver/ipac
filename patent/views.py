import json, xmljson
import requests
import httplib2
import xmltodict

from django.db.models import Q
from datetime import datetime, timedelta
from collections import OrderedDict, Counter
from django.http import JsonResponse
from background_task import background
from django.views import View
from .models import Master, History
from .utils import query_debugger
from tag.models import Tag

class ChartView(View):
    @query_debugger
    def get(self, request):
        date_type = request.GET.get("date", None)
        f_date = request.GET.get("f_date", None)
        e_date = request.GET.get("e_date", None)
        if date_type == 'year':
            dates = [f_date, e_date]
            start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
            a = list(OrderedDict(((start + timedelta(_)).strftime(r"%Y"), None) for _ in range((end - start).days)).keys())
            chart1 = []
            chart2 = []
            for x in a:
                base = [x, Master.objects.filter(file_date__contains = x).count()]
                base2 =[x, Master.objects.filter(pub_date__contains = x).count()]
                chart1.append(base)
                chart2.append(base2)

            dm = Master.objects.filter(file_date__range=(start, end))
            mm = [j.major for j in dm]
            md = Counter(mm)
            sort_orders = sorted(md.items(), key=lambda x: x[1], reverse=True)
            pro = [h.main_inventor for h in dm]
            pros = Counter(pro)
            pro_orders = sorted(pros.items(), key=lambda x: x[1], reverse=True)
            coworks = []
            for t in dm:
                t1 = t.applicant.split(' | ')
                coworks = coworks + t1
                cowork = Counter(coworks)
                co_orders = sorted(cowork.items(), key=lambda x: x[1], reverse=True)

            return JsonResponse({
                "chart1":chart1,
                "chart2":chart2,
                "major" :sort_orders,
                "professor":pro_orders,
                "cowork": co_orders
            })
        
        elif date_type == 'month':
# 기간에 대해 정리
            dates = [f_date, e_date]
            start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
            a = list(OrderedDict(((start + timedelta(_)).strftime("%Y-%m"), None) for _ in range((end - start).days)).keys())
# 조건별로 호출
            chart1 = []
            chart2 = []
            for x in a:
                base = [x, Master.objects.filter(file_date__contains = x).count()]
                base2 =[x, Master.objects.filter(pub_date__contains = x).count()]
                chart1.append(base)
                chart2.append(base2)

            dm = Master.objects.filter(file_date__range=(start, end))
            mm = [j.major for j in dm]
            md = Counter(mm)
            sort_orders = sorted(md.items(), key=lambda x: x[1], reverse=True)
            pro = [h.main_inventor for h in dm]
            pros = Counter(pro)
            pro_orders = sorted(pros.items(), key=lambda x: x[1], reverse=True)
            coworks = []
            for t in dm:
                t1 = t.applicant.split(' | ')
                print(t1)
                coworks = coworks + t1
                cowork = Counter(coworks)
                co_orders = sorted(cowork.items(), key=lambda x: x[1], reverse=True)

            return JsonResponse({
                "chart1":chart1,
                "chart2":chart2,
                "major" :sort_orders,
                "professor":pro_orders,
                "cowork": co_orders
            })
        
        elif date_type == 'day':
# 기간에 대해 정리
            dates = [f_date, e_date]
            start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
            a = list(OrderedDict(((start + timedelta(_)).strftime("%Y-%m-%d"), None) for _ in range((end - start).days)).keys())
# 조건별로 호출
            chart1 = []
            chart2 = []
            for x in a:
                base = [x, Master.objects.filter(file_date__contains = x).count()]
                base2 =[x, Master.objects.filter(pub_date__contains = x).count()]
                chart1.append(base)
                chart2.append(base2)

            dm = Master.objects.filter(file_date__range=(start, end))
            mm = [j.major for j in dm]
            md = Counter(mm)
            sort_orders = sorted(md.items(), key=lambda x: x[1], reverse=True)
            pro = [h.main_inventor for h in dm]
            pros = Counter(pro)
            pro_orders = sorted(pros.items(), key=lambda x: x[1], reverse=True)
            coworks = []
            for t in dm:
                t1 = t.applicant.split(' | ')
                coworks = coworks + t1
                cowork = Counter(coworks)
                co_orders = sorted(cowork.items(), key=lambda x: x[1], reverse=True)

            return JsonResponse({
                "chart1":chart1,
                "chart2":chart2,
                "major" :sort_orders,
                "professor":pro_orders,
                "cowork": co_orders
            })

class HistoryView(View):
    #@background(schedule=20)
    def get(self, request):
        apply_num = Master.objects.all().last()
        b = apply_num.file_num.split('-')
        n = ''
        for i in b:
            n = n + i
        
        url = f'http://plus.kipris.or.kr/openapi/rest/RelatedDocsonfilePatService/relatedDocsonfileInfo?applicationNumber={n}&accessKey=QWSwer5evYdATtLpvybUIqIPUQZR6ATVfDNMLksLZMU='


        h = httplib2.Http()
        response, content = h.request(url, 'GET')
        result = content.decode('utf-8')
        jsonString = json.dumps(xmltodict.parse(result), indent=4)
        json2 = json.loads(jsonString)
        ff = len(json2['response']['body']['items']['relateddocsonfileInfo'])
        t = json2['response']['body']['items']['relateddocsonfileInfo']
        for i in t:
            if History.objects.filter(documentNumber=i['documentNumber']).exists():
                pass
            else:
                History.objects.create(
                    applicationNumber = i['applicationNumber'],
                    documentNumber    = i['documentNumber'],
                    documentDate      = i['documentDate'],
                    documentTitle     = i['documentTitle'],
                    documentTitleEng  = i['documentTitleEng'],
                    status            = i['status'],
                    statusEng         = i['statusEng'],
                    step              = i['step'],
                    trialNumber       = i['trialNumber'],
                    registrationNumber = i['registrationNumber'],
                    master_id         = apply_num.data_id)
            
        return JsonResponse({"message":"success"})

class MainView(View):
    @query_debugger
    def get(self, request):
        tags = Tag.objects.select_related('category').prefetch_related('tagmaster').all().order_by('category')
        
        tag_bucket = []
        for i in tags:
            a = (i.name, i.count)
            tag_bucket.append(a)

        return JsonResponse({"data":tag_bucket})


    def post(self, request):
        data = json.loads(request.body)
        print(data['tag1'])
        index1 = Master.objects.filter(tags__contains=data['tag1'])
        print(len(index1))

        return JsonResponse({"data":"soon"})


