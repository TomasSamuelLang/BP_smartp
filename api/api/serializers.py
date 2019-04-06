from rest_framework.serializers import ModelSerializer
from .models import *


class ParkingLotSerializer(ModelSerializer):
    class Meta:
        model = SmartpParkinglot
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = SmartpPhoto
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = SmartpCountry
        fields = '__all__'


class TownSerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = SmartpTown
        fields = '__all__'


class ParkingLotDetails(ModelSerializer):
    parkinglot = PhotoSerializer(read_only=True, many=True)
    town = TownSerializer(read_only=True)

    class Meta:
        model = SmartpParkinglot
        fields = "__all__"


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = SmartpFavouriteparkinglot
        fields = "__all__"


class OldCapacitySerializer(ModelSerializer):
    class Meta:
        model = SmartpOldcapacitydata
        fields = "__all__"
