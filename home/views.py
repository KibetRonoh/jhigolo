from django.shortcuts import render
from accounts.models import User


def index(request):
    regulars = User.objects.filter(regular=True)
    vips = User.objects.filter(vip=True)

    context = {
        'regulars': regulars,
        'vips': vips,
    }

    return render(request, 'home/index.html', context)


def male(request):
    regulars = User.objects.filter(gender='Male')
    vips = User.objects.filter(vip=True)

    context = {
        'regulars': regulars,
        'vips': vips,
    }
    return render(request, 'home/male.html', context)


def female(request):
    regulars = User.objects.filter(gender='Female')
    vips = User.objects.filter(vip=True)

    context = {
        'regulars': regulars,
        'vips': vips,
    }

    return render(request, 'home/female.html', context)


def gay(request):
    regulars = User.objects.filter(gender='Gay')
    vips = User.objects.filter(vip=True)

    context = {
        'regulars': regulars,
        'vips': vips,
    }
    return render(request, 'home/gay.html', context)


def online(request):
    return render(request, 'home/online.html')

