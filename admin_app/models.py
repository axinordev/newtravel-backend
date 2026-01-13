from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


# Create your models here.

class HeroModel(models.Model):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or "Hero Section"

class HeroImageModel(models.Model):
    hero = models.ForeignKey(HeroModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    order = models.PositiveIntegerField(default=0, help_text="Order of the image in the carousel")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Hero Image {self.id}"
    
class AnniversaryModel(models.Model):
    logo = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
    
class AboutModel(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.description
    


class OptionModel(models.Model):
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option


class UpcomingToursModel(models.Model):
    type = models.ForeignKey(OptionModel, on_delete=models.CASCADE, related_name='tour_type')
    location = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.location
    
class UpcomingToursImagesModel(models.Model):
    tour = models.ForeignKey(UpcomingToursModel, on_delete=models.CASCADE, related_name='tour_images')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Image for {self.tour.location}"
    
class UpcomingDestinationHighlightsModel(models.Model):
    tour = models.ForeignKey(UpcomingToursModel, on_delete=models.CASCADE, related_name='highlights')
    highlight = models.CharField(max_length=500)

    def __str__(self):
        return f"Highlight for {self.tour.location}: {self.highlight}"
        
    
class PopularDestinationModel(models.Model):
    type = models.ForeignKey(OptionModel, on_delete=models.CASCADE, related_name='destination_type')
    location = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.location
    
class ServiceModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')

    def clean(self):
        # Prevent adding more than 9 items
        if not self.pk and ServiceModel.objects.count() >= 9:
            raise ValidationError("You can only have 9 service items.")

    def delete(self, *args, **kwargs):
        # Prevent deletion of any service item
        raise ValidationError("Deleting service items is not allowed.")

    def __str__(self):
        return self.title


class EnquiryModel(models.Model):
    Destination = models.CharField(max_length=200)
    Destination2 = models.CharField(max_length=200, blank=True, null=True)
    travelPlans = models.TextField(blank=True, null=True)  # new field for step 2
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.email

    



class ReviewsModel(models.Model):
    choices = [
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
        ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    rating = models.CharField(max_length=1, choices=choices)

    def __str__(self):
        return self.name
    
class AdminContactModel(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    whatsapp_contact = models.CharField(max_length=10)
    whatsapp_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    x_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.email
    
class GetInTouchModel(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    fullname = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.email

class LocationModel(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link
    
class GalleryImageModel(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Gallery Image {self.id}"
    
class GalleryVideoModel(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"Gallery Video {self.id}"

    

class TermsAndConditions(models.Model):
    title = models.CharField(max_length=255, default="Terms and Conditions")
    content = RichTextField(help_text="Enter the terms and conditions content")
    last_updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Terms and Conditions"
        verbose_name_plural = "Terms and Conditions"
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        # Singleton pattern - only one instance allowed
        if not self.pk and TermsAndConditions.objects.exists():
            existing = TermsAndConditions.objects.first()
            existing.title = self.title
            existing.content = self.content
            existing.save()
            return
        super().save(*args, **kwargs)
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255, default="Privacy Policy")
    content = RichTextField(help_text="Enter the privacy policy content")
    last_updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.pk and PrivacyPolicy.objects.exists():
            existing = PrivacyPolicy.objects.first()
            existing.title = self.title
            existing.content = self.content
            existing.save()
            return
        super().save(*args, **kwargs)
class CancellationPolicy(models.Model):
    title = models.CharField(max_length=255, default="Cancellation and Refund Policy")
    content = RichTextField(help_text="Enter the cancellation and refund policy content")
    last_updated = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Cancellation Policy"
        verbose_name_plural = "Cancellation Policy"
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.pk and CancellationPolicy.objects.exists():
            existing = CancellationPolicy.objects.first()
            existing.title = self.title
            existing.content = self.content
            existing.save()
            return
        super().save(*args, **kwargs)