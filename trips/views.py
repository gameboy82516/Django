# -*- coding:utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, HttpResponse
from trips.models import Post
#from trips.models import Staff

'''
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=120.113.70.217,1434;DATABASE=Django;UID=sa;PWD=nfu123@@@')
cursor = conn.cursor()
'''

'''
def hello_world(request):
	return HttpResponse("Hello World!")

'''


def hello_world(request):
	return render(request,
				'hello_world.html',
				{'current_time': datetime.now()})

def post(request):
        # get all the posts
        post_list = Post.objects.all()
        return render(request,
        'post.html',
        {'post_list': post_list})

def post_detail(request, id):
        post = Post.objects.get(id=id)
        return render(request, 'post_list.html', {'post': post})

'''

def home(req):
    QuerySet = Staff.objects.all()
    Info = 'World'
    cursor.execute("select * from trips_staff")
    row = cursor.fetchall()
    for Item in QuerySet:
        print(Item.Name)
        Info = Item.Name
    return HttpResponse('Hello %s!' % row)


def insertdata(req):
    try:
        s = Staff(LoginID='aa', Name='tryman', Sex=True, Birthday='2016-03-30', JoinTime=datetime.now())
        s.save()
        Info = 'OK'
    except:
        Info = 'Fail'
    return HttpResponse(Info)
'''
