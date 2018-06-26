from django.shortcuts import render
from restaurant.models import Restaurant,Food
# Create your views here.
# encoding: utf-8


def menu(request):
    food1 = {'name':'番茄炒蛋','price':'80','comment':'好吃','flavor':'辣'}
    food2 = {'name': '蒜泥白肉', 'price':'100', 'comment':'人氣推薦', 'flavor':'沒什麼味道'}
    foods = [food1,food2]
    #dic={'1':'a','2':'b'}
    #items = dic.items()
    return render(request,'menu.html',locals())


def home(request):
    # get all the posts
    return render(request,
                  'index.html')