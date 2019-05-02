from django import template
from ..models import FavouriteParkingLot
register = template.Library()


@register.filter
def is_favourite(parking_lot, user):
    if FavouriteParkingLot.objects.filter(user=user, parkinglot=parking_lot).count() > 0:
        return True
    return False


@register.filter
def subtract(value1, value2):
    return value1 - value2
