# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Ticketcategories
from .models import Ridestable
from .models import Sunburst
from .models import RideCount
from .models import MasterUsage
from .models import MallMinutes
from .models import DistinctRides
from .models import PathProb
from .models import Tickets
from django.db.models import Sum
from django.http import JsonResponse
import json 
# Create your views here.

def graph(request):
    return render(request, 'nu_eda/graph.html')

def index(request):
    data = RideCount.objects.all() \
        .values('no_of_rides') \
        .annotate(count_items=Sum('cust_count'))
    return JsonResponse(list(data), safe=False)


def index2(request):
    data2 = Tickets.objects.all().values('ticket_type','category','subcategory','ticketname').annotate(size = Sum('size'))
    flare = {}
    ticktype = []
    for i in range(0,len(data2)):
        ticktype.append(data2[i]['ticket_type'])
    ticktype = list(set(ticktype))
    categ_type = []
    for i in range(0,len(data2)):
        categ_type.append(data2[i]['category'])
    categ_type = list(set(categ_type))
    flare['name'] = "Total Customer Count"
    flare['children'] = []
    for types in ticktype:
        categ = {}
        categ['name'] = types
        categ['children'] = []
        flare['children'].append(categ)
    
    for i in range(0,len(flare['children'])):
        categ_flag = []
        for category in range(0,len(data2)):
            if flare['children'][i]['name'] == data2[category]['ticket_type'] and data2[category]['category'] not in categ_flag:
                cat = {}
                cat['name'] = data2[category]['category']
                categ_flag.append(data2[category]['category'])
                cat['children'] = []
                flare["children"][i]["children"].append(cat)
    for i in range(0,len(flare['children'])):
        for j in range(0,len(flare['children'][i]['children'])):
            sub = []
            print flare['children'][i]['name'],flare['children'][i]['children'][0]['name']
            for sub_categ in range(0,len(data2)):
                if flare['children'][i]['children'][j]['name'] == data2[sub_categ]['category'] and data2[sub_categ]['subcategory'] not in sub:
                    sub_cat = {}
                    sub_cat['name'] = data2[sub_categ]['subcategory']
                    sub_cat['children'] = []
                    sub.append(data2[sub_categ]['subcategory'])
                    flare["children"][i]["children"][j]['children'].append(sub_cat)
    for i in range(0,len(flare['children'])):
        for j in range(0,len(flare['children'][i]['children'])):
            for k in range(0,len(flare['children'][i]['children'][j]['children'])):
                names_flag = []
                print flare['children'][0]['children'][2]['name'],len(flare['children'][0]['children'][2]['children'])
                for name_counter in range(0,len(data2)):
                    if flare['children'][i]['children'][j]['children'][k]['name'] == data2[name_counter]['subcategory'] and data2[name_counter]['ticketname'] not in names_flag:
                        names = {}
                        names['name'] = data2[name_counter]['ticketname']
                        names['size'] = data2[name_counter]['size']
                        names_flag.append(data2[name_counter]['ticketname'])
                        flare["children"][i]["children"][j]['children'][k]['children'].append(names)
    return JsonResponse(flare, safe=False)

def index3(request):
    data3 = PathProb.objects.all().values('ride1','ride2','cust_count')
    data3_list = []
    for i in range(0,len(data3)):
        list_temp = []
        list_temp.append(data3[i]['ride1']) 
        list_temp.append(data3[i]['ride2']) 
        list_temp.append(data3[i]['cust_count']) 
        data3_list.append(list_temp)
    return JsonResponse(data3_list, safe=False)    

def index4(request):
    data4 = Sunburst.objects.all().values('ride','hr').annotate(count_items=Sum('cust_count'))
    return JsonResponse(list(data4), safe=False)    
def index5(request):
    data5 = DistinctRides.objects.all().values('distinct_rides').annotate(count_items=Sum('cust_count'))
    return JsonResponse(list(data5), safe=False)
	
def index6(request):
    data6 = MallMinutes.objects.all().values('miniutes_in_mall').annotate(count_items=Sum('cust_count'))
    return JsonResponse(list(data6), safe=False)