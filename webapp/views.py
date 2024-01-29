from django.shortcuts import render, redirect
from .models import *
from .forms import reservation, feedback

def home_page(request):
    return render(request, 'pages/home.html')

def about_page(request):
    feedbacks = Feedback.objects.all()
    form = feedback()
    if request.method == 'POST':
        form = feedback(request.POST)
        if form.is_valid():
                form.save()
                return redirect('homepage')
    context = {
        'feedbacks':feedbacks,
        'form':form

    }
    return render(request, 'pages/about.html', context)

def reservation_page(request):
    reservations = Reservation.objects.all()
    total_reservation = reservations.count()
    form = reservation()
    if request.method == 'POST':
        form = reservation(request.POST)
        if form.is_valid():
                form.save()
                return redirect('homepage')
    context = {
        'reservations':reservations,
        'total_reservation':total_reservation,
        'form':form

    }
    return render(request, 'pages/reservation.html', context)

def menu_page(request):
    return render(request, 'pages/menu.html')