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

def menu_page(request):
    return render(request, 'pages/menu.html')
    
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

def updateReservation(request, pk):
    customer = Reservation.objects.get(id=pk)
    form = reservation(instance=customer)

    if request.method == 'POST':
        form = reservation(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    context = {'form':form}
    return render(request, 'pages/reservation.html', context)



def deleteReservation(request, pk):
     customer = Reservation.objects.get(id=pk)
     if request.method == 'POST':
        customer.delete()
        return redirect('homepage')
     context = {'customer':customer}
     return render(request, 'pages/delete_reservation.html', context)
