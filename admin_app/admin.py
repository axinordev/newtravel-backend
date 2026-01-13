from django.contrib import admin
from .models import HeroModel, HeroImageModel, AboutModel, AnniversaryModel, UpcomingToursModel, PopularDestinationModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel, GalleryVideoModel, OptionModel, UpcomingToursImagesModel, ServiceModel, EnquiryModel, GetInTouchModel, UpcomingDestinationHighlightsModel, TermsAndConditions, PrivacyPolicy, CancellationPolicy

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
admin.site.register(HeroImageModel)
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
    list_display_links = ['title']

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
        'email',
        'phone',
        'Destination',
        'Destination2',
        'travelPlans',
    )
    search_fields = (
        'email',
        'Destination',
        'Destination2',
        'travelPlans',
    )

admin.site.register(UpcomingDestinationHighlightsModel)

class SingletonAdminMixin:
    """Mixin to ensure only one instance exists"""
    
    def has_add_permission(self, request):
        return not self.model.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'last_updated']
    readonly_fields = ['last_updated']
@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'last_updated']
    readonly_fields = ['last_updated']
@admin.register(CancellationPolicy)
class CancellationPolicyAdmin(SingletonAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'last_updated']
    readonly_fields = ['last_updated']



