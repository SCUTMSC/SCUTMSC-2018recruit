# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Layman, NorthCampus,CC
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
import re
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
import csv


def valid_check(request):
    if re.match(r'^\d{12}$',request.POST.get('schoolID')) == None:
        return "学号格式错误"
    if re.match(r'^[\u4e00-\u9fa5]{0,}$',request.POST.get('name')) == None:
        return "请使用中文姓名"
    if re.match(r'^male|female$',request.POST.get('sex')) == None:
        return "秀吉来的？"
    if re.match(r'^1[3456789]\d{9}$',request.POST.get('telephone')) == None:
        return "手机号码格式错误"
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',request.POST.get('email')) == None:
        return "邮箱格式错误"
    if len(request.POST.get('QQnumber')) <4 or len(request.POST.get('QQnumber')) > 14:
        return "QQ号错误"
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
            #grade = request.POST.get('grade'),
            QQnumber = request.POST.get('QQnumber'),
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
    
    if re.match(r'^1[3456789]\d{9}$',str(request.POST.get('telephone'))) == None:
        response['msg'] = "电话号码格式错误"
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        layman = Layman.objects.filter( schoolID = str( request.POST.get('schoolID') ) )
        if layman.count() == 0:
            layman = NorthCampus.objects.filter( schoolID = str( request.POST.get('schoolID') ) )
    except:
        response['msg'] = "数据库错误，请联系管理员"
        response['error_code'] = 1

    if layman.count() == 0:
        response['msg'] = "尚未报名，快去相应的校区提交申请表吧！"
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

@csrf_exempt
@require_http_methods(["POST"])
def add_layman_north(request):
    response = {}
    if  NorthCampus.objects.filter( schoolID = str( request.POST.get('schoolID') ) ).count() != 0:
        response['msg'] = "该学号已经提交申请，请关注面试安排"
        response['error_code'] = 3
        return JsonResponse(response)
    if valid_check(request) != 0:
        response['msg'] = str(valid_check(request))
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        layman = NorthCampus(
            schoolID = request.POST.get('schoolID'),
            name = request.POST.get('name'),
            sex = request.POST.get('sex'),
            college = request.POST.get('college'),
            #grade = request.POST.get('grade'),
            QQnumber = request.POST.get('QQnumber'),
            dorm = request.POST.get('dorm'),
            telephone = request.POST.get('telephone'),
            department1 = request.POST.get('department1'),
            department2 = request.POST.get('department2'),
            adjust = request.POST.get('adjust'),
            degree = request.POST.get('degree'),
            email = request.POST.get('email'),

            professor_name = request.POST.get('pro_name'),
            professor_major = request.POST.get('pro_major'),
            aimat = request.POST.get('aimat'),
            monologue = request.POST.get('monologue'),
            habbit = request.POST.get('habbit'),
            speciality = request.POST.get('speciality'),
            keypoint = request.POST.get('keypoint'),
            whyjoin = request.POST.get('whyjoin'),
            whychoose = request.POST.get('whychoose'),

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
def cc(request):

    msg=""
    if re.match(r'^\d{12}$',request.POST.get('schoolID')) == None:
        msg= "学号格式错误"
    if re.match(r'^[\u4e00-\u9fa5]{0,}$',request.POST.get('name')) == None:
        msg= "请使用中文姓名"
    if re.match(r'^male|female$',request.POST.get('sex')) == None:
        msg= "秀吉来的？"
    if re.match(r'^1[3456789]\d{9}$',request.POST.get('telephone')) == None:
        msg = "手机号码格式错误"
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',request.POST.get('email')) == None:
        msg= "邮箱格式错误"
    if len(request.POST.get('QQnumber')) <4 or len(request.POST.get('QQnumber')) > 14:
        msg= "QQ号错误"

    response = {}
    if  CC.objects.filter( schoolID = str( request.POST.get('schoolID') ) ).count() != 0:
        response['msg'] = "该学号已经提交申请，请关注面试安排"
        response['error_code'] = 3
        return JsonResponse(response)
    if msg != "":
        response['msg'] = msg
        response['error_code'] = 2
        return JsonResponse(response)
    try:
        ccc = CC(
            schoolID = request.POST.get('schoolID'),
            name = request.POST.get('name'),
            sex = request.POST.get('sex'),
            QQnumber = request.POST.get('QQnumber'),
            dorm = request.POST.get('dorm'),
            telephone = request.POST.get('telephone'),
            leader = request.POST.get('leader'),
            email = request.POST.get('email'),
            introduce = request.POST.get('introduce'),
            classes = request.POST.get('class'),
        )
        ccc.save()
        response['msg'] = '申请成功'
        response['error_code'] = 0
    except IntegrityError:
        response['msg'] = '提供的参数/信息不够啊'
    except:
        response['msg'] = "发生了不应该出现的错误，请联系管理员"
        response['error_code'] = 1
    ccc.save()
    response['msg'] = '申请成功'
    response['error_code'] = 0

    return JsonResponse(response)

def export_csv_msc(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment;filename = "msc_info_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['姓名','学号','性别','介绍','学院','邮箱','是否调剂','学历','qq号','手机号','寝室','注册时间','录取部门','备注',])
    for i in Layman.objects.all():
        writer.writerow([i.name,i.schoolID,i.sex,i.introduce, i.college,i.email,i.adjust,i.degree,i.QQnumber,i.telephone,i.dorm,i.applydate])

    return response

def export_csv_cc(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment;filename = "cc_info_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['姓名','学号','性别','介绍','邮箱','是否愿意成为组长','手机号','qq号','寝室','班级','是否录取','备注',])
    for i in CC.objects.all():
        writer.writerow([i.name,i.schoolID,i.sex,i.introduce,i.email,i.leader,i.telephone,i.QQnumber,i.dorm,i.classes,i.passed])
       
    return response


"""
0 for valid
1 for others error
2 for data error
3 for dual
4 for not apply
"""

def index(request):
    return HttpResponse("index")
