from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf
from .forms import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from .utils import calculatePeakHours, calculatePeakDays
import datetime
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

def homepage(request):

    results = ParkingLot.objects.all().select_related()
    query = request.GET.get("query")

    # if request.user.is_authenticated:
        # print(request.user.id)

    if query:
        results = results.filter(
            Q(town__name__icontains=query) |
            Q(address__icontains=query) |
            Q(name__icontains=query)
            # | Q(town_country__name__icontains=query)
        ).order_by('actualparkedcars')

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


def registerpage(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            return HttpResponseRedirect('/thanks/')

    else:

        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form})


def loginpage(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    else:

        form = LoginForm()

    context = {'form': form}
    context.update(csrf(request))
    return render_to_response("registration/login.html", context, RequestContext(request))


def thankspage(request):
    return render(request, "thanks.html", {})


def parkingDetails(request, id):

    try:
        details = ParkingLot.objects.all().select_related().get(id=id)
    except details.DoesNotExist:
        raise Http404

    statshour = calculatePeakHours(details)
    statsdays = calculatePeakDays(details)
    labelhour = [str(x) for x in range(0, 24)]
    labelday = [datetime.date(2019, 3, x+3).strftime('%A') for x in range(1, 8)]
    print(labelday)
    context = {
        'details': details,
        'peakhours': statshour,
        'labels': labelhour,
        "peakdays": statsdays,
        "labelDay": labelday
    }

    return render(request, "parkingDetail.html", context)


def showFavourite(request):

    if request.user.is_authenticated:

        favourite = FavouriteParkingLot.objects.filter(user_id=request.user.id)
        ids = []
        for x in favourite:
            ids.append(x.parkinglot_id)

        print(favourite)
        result = ParkingLot.objects.filter(id__in=ids).select_related()

        query = request.GET.get("query")

        # if request.user.is_authenticated:
        # print(request.user.id)

        if query:
            result = result.filter(
                Q(town__name__icontains=query) |
                Q(address__icontains=query) |
                Q(name__icontains=query)
                # | Q(town_country__name__icontains=query)
            ).order_by('actualparkedcars')

        page = request.GET.get('page', 1)
        paginator = Paginator(result, 9)

        try:
            parkings = paginator.page(page)
        except PageNotAnInteger:
            parkings = paginator.page(1)
        except EmptyPage:
            parkings = paginator.page(paginator.num_pages)

        print(parkings)

    return render(request, "favourite.html", {'favourite': parkings})


def add_favourite(request, id):

    # if request.method == 'POST':
    if request.user.is_authenticated:
        user_id = request.user.id
        parking_id = id
        print(FavouriteParkingLot.objects.filter(user_id=user_id, parkinglot_id=parking_id))
        if FavouriteParkingLot.objects.filter(user_id=user_id, parkinglot_id=parking_id).count() == 0:
            print("Object create -------")
            FavouriteParkingLot.objects.create(user_id=user_id, parkinglot_id=parking_id)

        return HttpResponse(status=200)

    return HttpResponse(status=404)
    # return HttpResponse(status=404)


def dislike(request, id):

    if request.user.is_authenticated:

        user_id = request.user.id
        parking_id = id
        print(FavouriteParkingLot.objects.all())
        if FavouriteParkingLot.objects.filter(user_id=user_id, parkinglot_id=parking_id).count() != 0:

            parking = FavouriteParkingLot.objects.filter(user_id=user_id, parkinglot_id=parking_id)
            parking.delete()
        return HttpResponse(status=200)

    return HttpResponse(status=404)
