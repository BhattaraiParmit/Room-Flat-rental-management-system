from django.shortcuts import render



def Home_Page(request):
    return render(request, 'app/home.html')


def room_page(request):
    return render(request, 'app/rooms.html')


def room_detail(request):
    return render(request, 'app/room_detail.html')  