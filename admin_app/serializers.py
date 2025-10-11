from rest_framework import serializers
from .models import HeroModel, AnniversaryModel, AboutModel, OptionModel, UpcomingToursModel, UpcomingToursImagesModel, PopularDestinationModel, ServiceModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel, GalleryVideoModel, EnquiryModel, GetInTouchModel

class HeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = '__all__'

class AnniversarySerializers(serializers.ModelSerializer):
    class Meta:
        model = AnniversaryModel
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = '__all__'

class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = '__all__'

class UpcomingToursSerializers(serializers.ModelSerializer):
    class Meta:
        model = UpcomingToursModel
        fields = '__all__'

class UpcomingToursImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UpcomingToursImagesModel
        fields = '__all__'

class PopularDestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = PopularDestinationModel
        fields = '__all__'

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReviewsModel
        fields = '__all__'

class AdminContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminContactModel
        fields = '__all__'

class LocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'

class GalleryImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryImageModel
        fields = '__all__'

class GalleryVideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideoModel
        fields = '__all__'

class EnquirySerializers(serializers.ModelSerializer):
    class Meta:
        model = EnquiryModel
        fields = '__all__'

class GetInTouchSerializers(serializers.ModelSerializer):
    class Meta:
        model = GetInTouchModel
        fields = '__all__'