from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from .models import *


def test_view(request):
    return HttpResponse(
        """
        <h1 style="color: teal;">Bosh sahifa</h1>
        <hr>
        <p>Bugun djangoda MVT prinsiplarini qo'llash orqali website yaratamiz!</p>
        """
    )


def index_view(request):
    context = {
        'now': datetime.datetime.now(),
    }
    return render(request, 'index.html', context)


def talabalar_view(request):
    talabalar = Talaba.objects.all()

    search = request.GET.get('search')
    if search:
        talabalar = talabalar.filter(ism__contains=search)

    order = request.GET.get('order')
    if order:
        talabalar = talabalar.order_by(order)

    kurs = request.GET.get('kurs')
    if kurs and int(kurs) != 0:
        talabalar = talabalar.filter(kurs=kurs)

    context = {
        'talabalar': talabalar,
        'search': search,
        'order': order,
        'kurs': int(kurs),
    }
    return render(request, 'talabalar.html', context)


def talaba_retrieve_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba-retrieve.html', context)


def talaba_delete_confirm_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba-delete-confirm.html', context)


def talaba_delete_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('/talabalar/')


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)


