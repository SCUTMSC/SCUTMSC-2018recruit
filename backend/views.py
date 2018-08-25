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
    if re.match(r'^\d{12}$',request.POST.get('schoolID')) == None:
        return "学号格式错误"
    if re.match(r'^[\u4e00-\u9fa5]{0,}$',request.POST.get('name')) == None:
        return "请使用中文姓名"
    if re.match(r'^male|female$',request.POST.get('sex')) == None:
        return "秀吉来的？"
    if re.match(r'^1[34578]\d{9}$',request.POST.get('telephone')) == None:
        return "手机号码格式错误"
    if re.match(r'^Yes|No$',request.POST.get('adjust')) == None:
        return "是否服从调剂？"
    if re.match(r'^master|bachelor$',request.POST.get('degree')) == None:
        return "研究生or本科生"
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',request.POST.get('email')) == None:
        return "邮箱格式错误"
    return 0

@csrf_exempt
@require_http_methods(["POST"])
def add_layman(request):
    response = {}
    if  Layman.objects.filter( schoolID = str( request.POST.get('schoolID') ) ).count() != 0:
        response['msg'] = "该学号已经提交申请，请关注面试安排"
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
        response['msg'] = '申请成功'
        response['error_code'] = 0
    except IntegrityError:
        response['msg'] = '提供的参数/信息不够啊'
    except:
        response['msg'] = "发生了不应该出现的错误，请联系管理员"
        response['error_code'] = 1
    layman.save()
    response['msg'] = '申请成功'
    response['error_code'] = 0

    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["POST"])
def query(request):
    response = {}
    
    if re.match(r'^1[34578]\d{9}$',str(request.POST.get('telephone'))) == None:
        response['msg'] = "电话号码格式错误"
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        layman = Layman.objects.filter( schoolID = str( request.POST.get('schoolID') ) )
    except:
        response['msg'] = "数据库错误，请联系管理员"
        response['error_code'] = 1

    if layman.count() == 0:
        response['msg'] = "尚未报名，快去提交申请表吧！"
        response['error_code'] = 4
        return JsonResponse(response)
    layman = Layman.objects.get( schoolID = str( request.POST.get('schoolID') ) )
    if request.POST.get('name') != layman.name or request.POST.get('telephone') != layman.telephone:
        response['msg'] = "提供的三项信息不匹配"
        response['error_code'] = 2
    else:
        #response['list']  = json.loads(serializers.serialize("json", layman))
        response['arrangement'] = layman.interview
        response['result'] = layman.passed
        response['department'] = layman.department
        response['msg'] = '查询成功'
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
    return HttpResponse("index")
