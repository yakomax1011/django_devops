from django.shortcuts import render
from datetime import datetime

# Create your views here.

def main(request):
    date = datetime.now()
    month = date.month

    winter = {12, 1, 2}
    spring = {3, 4, 5}
    summer = {6, 7, 8}
    fall = {9, 10, 11}

    if month in winter:
        current_month = 'этой зимы'
    if month in spring:
        current_month = 'этой весны'
    if month in summer:
        current_month = 'этого лета'
    if month in fall:
        current_month = 'этой осени'

    context = {
        "date_month": current_month,
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')

#def index_copy(request):
#    return render(request, 'mainapp/index_copy.html')