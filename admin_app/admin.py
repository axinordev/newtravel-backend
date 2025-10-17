from django.contrib import admin
from .models import HeroModel, AboutModel, AnniversaryModel, UpcomingToursModel, PopularDestinationModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel, GalleryVideoModel, OptionModel, UpcomingToursImagesModel, ServiceModel, EnquiryModel, GetInTouchModel, UpcomingDestinationHighlightsModel

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutModel.objects.exists():
            return False
        return True

@admin.register(AnniversaryModel)
class AnniversaryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding a new AnniversaryModel if one already exists
        if AnniversaryModel.objects.exists():
            return False
        return True

@admin.register(HeroModel)
class HeroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding a new HeroModel if one already exists
        if HeroModel.objects.exists():
            return False
        return True
    
admin.site.register(OptionModel)
admin.site.register(UpcomingToursImagesModel)
admin.site.register(PopularDestinationModel)
admin.site.register(UpcomingToursModel)
admin.site.register(ReviewsModel)

@admin.register(AdminContactModel)
class AdminContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding a new AdminContactModel if one already exists
        if AdminContactModel.objects.exists():
            return False
        return True
    

@admin.register(LocationModel)
class LocationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent adding a new LocationModel if one already exists
        if LocationModel.objects.exists():
            return False
        return True
    
admin.site.register(GalleryImageModel)
admin.site.register(GalleryVideoModel)
admin.site.register(GetInTouchModel)

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    def has_add_permission(self, request):
        # Allow add only until there are 9 items
        if ServiceModel.objects.count() >= 9:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Disable delete
        return False

    
@admin.register(EnquiryModel)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'Destination',
        'Departure_Month',
        'Trip_Duration',
        'budget_per_person',
    )
    search_fields = ('full_name', 'email', 'Destination', 'Departure_Month')
    list_filter = ('Departure_Month', 'Trip_Duration', 'lodging_preference')

admin.site.register(UpcomingDestinationHighlightsModel)



