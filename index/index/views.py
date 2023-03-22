from django.http import HttpResponse
from django.shortcuts import render
import pymysql


def index(request):
    return render(request, "index.html")


def shopCart(request):
    return render(request, "shopCart.html")
