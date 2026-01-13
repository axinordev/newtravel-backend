from rest_framework import serializers
from .models import HeroModel, HeroImageModel, AnniversaryModel, AboutModel, OptionModel, UpcomingToursModel, UpcomingToursImagesModel, PopularDestinationModel, ServiceModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel, GalleryVideoModel, EnquiryModel, GetInTouchModel, UpcomingDestinationHighlightsModel
from django.conf import settings

class FullURLImageField(serializers.ImageField):
    def to_representation(self, value):
        if not value:
            return None
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(value.url)
        return f"{settings.MEDIA_URL}{value.name}"

class HeroImageSerializers(serializers.ModelSerializer):
    image = FullURLImageField()
    class Meta:
        model = HeroImageModel
        fields = '__all__'

class HeroSerializers(serializers.ModelSerializer):
    images = HeroImageSerializers(many=True, read_only=True)
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
    thumbnail = FullURLImageField()
    class Meta:
        model = UpcomingToursModel
        fields = '__all__'

class UpcomingToursImagesSerializers(serializers.ModelSerializer):
    image = FullURLImageField()
    class Meta:
        model = UpcomingToursImagesModel
        fields = '__all__'

class UpcomingDestinationHighlightsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UpcomingDestinationHighlightsModel
        fields = '__all__'

class PopularDestinationSerializers(serializers.ModelSerializer):
    thumbnail = FullURLImageField()
    class Meta:
        model = PopularDestinationModel
        fields = '__all__'

class ServiceSerializers(serializers.ModelSerializer):
    image = FullURLImageField()
    class Meta:
        model = ServiceModel
        fields = '__all__'

class ReviewsSerializers(serializers.ModelSerializer):
    image = FullURLImageField()
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
    image = FullURLImageField()
    class Meta:
        model = GalleryImageModel
        fields = '__all__'

class GalleryVideoSerializers(serializers.ModelSerializer):
    video = serializers.FileField(use_url=True)
    thumbnail = serializers.ImageField(use_url=True)

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