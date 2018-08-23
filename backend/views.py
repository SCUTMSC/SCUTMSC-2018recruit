# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Layman
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
import re
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError


def valid_check(request):
    """try:
        if re.match(r'^\d{12}$',request.POST.get('schoolID')) == None:
            return request.POST.get('schoolID')
        if re.match(r'^[\u4e00-\u9fa5]{0,}$',request.POST.get('name')) == None:
            return 2
        if re.match(r'^male|female$',request.POST.get('sex')) == None:
            return 3
        if re.match(r'^1[34578]\d{9}$',request.POST.get('telephone')) == None:
            return 4
        if re.match(r'^Yes|No$',request.POST.get('adjust')) == None:
            return 5
        if re.match(r'^master|bachelor$',request.POST.get('degree')) == None:
            return 6
        if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',request.POST.get('email')) == None:
            return 7
    except TypeError:
        return "not completed"""
    if re.match(r'^\d{12}$',request.POST.get('schoolID')) == None:
        return request.POST.get('schoolID')
    if re.match(r'^[\u4e00-\u9fa5]{0,}$',request.POST.get('name')) == None:
        return 2
    if re.match(r'^male|female$',request.POST.get('sex')) == None:
        return 3
    if re.match(r'^1[34578]\d{9}$',request.POST.get('telephone')) == None:
        return 4
    if re.match(r'^Yes|No$',request.POST.get('adjust')) == None:
        return 5
    if re.match(r'^master|bachelor$',request.POST.get('degree')) == None:
        return 6
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',request.POST.get('email')) == None:
        return 7
    return 0

@csrf_exempt
@require_http_methods(["POST"])
def add_layman(request):
    response = {}
    if  Layman.objects.filter( schoolID = str( request.POST.get('schoolID') ) ).count() != 0:
        response['msg'] = "already applied"
        response['error_code'] = 3
        return JsonResponse(response)
    if valid_check(request) != 0:
        response['msg'] = str(valid_check(request))
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        layman = Layman(
            schoolID = request.POST.get('schoolID'),
            name = request.POST.get('name'),
            sex = request.POST.get('sex'),
            college = request.POST.get('college'),
            grade = request.POST.get('grade'),
            dorm = request.POST.get('dorm'),
            telephone = request.POST.get('telephone'),
            department1 = request.POST.get('department1'),
            department2 = request.POST.get('department2'),
            adjust = request.POST.get('adjust'),
            degree = request.POST.get('degree'),
            email = request.POST.get('email'),
            introduce = request.POST.get('introduce')
        )
        layman.save()
        response['msg'] = 'success'
        response['error_code'] = 0
    except IntegrityError:
        response['msg'] = str('some parameters missing')
    except:
        response['msg'] = str("unexpect error")
        response['error_code'] = 1
    layman.save()
    response['msg'] = 'success'
    response['error_code'] = 0

    return JsonResponse(response)

"""@csrf_exempt
@require_http_methods(["POST"])########## delete method after test
def show_laymans(request):
    response = {}
    try:
        laymans = Layman.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", laymans))
        response['msg'] = 'success'
        response['error_code'] = 0
    except:
        response['msg'] = str("unexpect error")
        response['error_code'] = 1

    return JsonResponse(response)"""

@csrf_exempt
@require_http_methods(["POST"])
def query(request):
    response = {}
    
    if re.match(r'^1[34578]\d{9}$',str(request.POST.get('telephone'))) == None:
        response['msg'] = "phone number error"
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        layman = Layman.objects.filter( schoolID = str( request.POST.get('schoolID') ) )
    except:
        response['msg'] = "database error"
        response['error_code'] = 1

    if layman.count() == 0:
        response['msg'] = "not applied yet"
        response['error_code'] = 4
        return JsonResponse(response)
    layman = Layman.objects.get( schoolID = str( request.POST.get('schoolID') ) )
    if request.POST.get('name') != layman.name or request.POST.get('telephone') != layman.telephone:
        response['msg'] = "information not match"
        response['error_code'] = 2
    else:
        #response['list']  = json.loads(serializers.serialize("json", layman))
        response['arrangement'] = layman.interview
        response['result'] = layman.passed
        response['department'] = layman.department
        response['msg'] = 'success'
        response['error_code'] = 0
    return JsonResponse(response)

"""
0 for valid
1 for others error
2 for data error
3 for dual
4 for not apply
"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""(
    schoolID='201730612345',
    name='%E9%95%BF%E8%80%85',
    sex='male',
    college='%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2',
    grade='2017',
    dorm='C10-233',
    telephone='13533222333',
    department1='%E6%8A%80%E6%9C%AF%E9%83%A8',
    department2='%E6%8A%80%E6%9C%AF%E9%83%A8',
    adjust='Yes',
    degree="bachelor",
    email="i@waynest.com",
    introduce="hdfsdavgdfgd",
}"""