from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

def homepage(request):

    results = ParkingLot.objects.all().select_related()
    query = request.GET.get("query")

    if query:
        results = results.filter(
            Q(town__name__icontains=query) |
            Q(address__icontains=query) |
            Q(name__icontains=query)
            # | Q(town_country__name__icontains=query)
        ).order_by('actualparkedcars')

    photos = results.get(id=1).photo_set.all()
    for photo in photos:
        print(photo.photo)
    print("---+++---")
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 9)

    try:
        parkings = paginator.page(page)
    except PageNotAnInteger:
        parkings = paginator.page(1)
    except EmptyPage:
        parkings = paginator.page(paginator.num_pages)

    return render(request, "home.html", {'query': parkings})


def aboutpage(request):
    return render(request, "about.html", {})


def contactpage(request):
    return render(request, "contact.html", {})


def favouritepage(request):
    return render(request, "favourite.html", {})


def registerpage(request):

    if request.method == 'POST':

        password = make_password(request.POST.get('password'))
        verifiedPassword = make_password(request.POST.get('passwordVerification'))

        user = {"login": request.POST.get('login'), "password": password, "passwordVerification": verifiedPassword}

        form = RegisterForm(user)

        if request.POST.get('password') != request.POST.get('passwordVerification'):
            return render(request, "register.html", {'form': form})

        if form.is_valid():

            task = form.save(commit=False)

            try:
                User.objects.get(login=request.POST.get('login'))
            except User.DoesNotExist:
                task.save()
                return HttpResponseRedirect('/thanks/')
    else:

        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def loginpage(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        try:
            user = User.objects.get(login=request.POST.get('login'))
        except User.DoesNotExist:
            return render(request, "login.html", {'form': form})

        if form.is_valid():
            if check_password(request.POST.get('password'), user.password):
                return HttpResponseRedirect('/home/')
            return render(request, "login.html", {'form': form})
    else:

        form = LoginForm()

    return render(request, "login.html", {'form': form})


def thankspage(request):
    return render(request, "thanks.html", {})

