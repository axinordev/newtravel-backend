from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class HeroModel(models.Model):
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description
    
class AnniversaryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
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
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.tour.location}"
        
    
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
    Budget_Choices = [
        ('Estimate', 'Estimate'),
        ('Flexible', 'Flexible'),
        ('Maximum', 'Maximum'),
    ]
    Lodging_Choices = [
        ('5 Star', '5 Star'),
        ('4 Star', '4 Star'),
        ('3 Star', '3 Star'),
        ('2 Star', '2 Star'),
        ('Camping', 'Camping'),
    ]
    Departure_Month_Choices = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    Trip_Duration_Choices = [
        ('1 Day', '1 Day'),
        ('2 Days', '2 Days'),
        ('3 Days', '3 Days'),
        ('4 Days', '4 Days'),
        ('5 Days', '5 Days'),
        ('6 Days', '6 Days'),
        ('7 Days', '7 Days'),
        ('8 Days', '8 Days'),
        ('9 Days', '9 Days'),
        ('10 Days', '10 Days'),
        ('11 Days', '11 Days'),
        ('12 Days', '12 Days'),
        ('13 Days', '13 Days'),
        ('14+ Days', '14+ Days'),
    ]
    Number_of_People_Choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10+', '10+'),
    ]

    Age_Group_Choices = [
        ('5 and below', '5 and below'), 
        ('6-11', '6-11'), 
        ('12-17', '12-17'), 
        ('18-35', '18-35'), 
        ('36-49', '36-49'), 
        ('50-64', '50-64'), 
        ('65+', '65+'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=200) 
    budget_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    how_strict_budget = models.CharField(max_length=10, choices=Budget_Choices)
    Departure_Month = models.CharField(max_length=10, choices=Departure_Month_Choices)
    Trip_Duration = models.CharField(max_length=10, choices=Trip_Duration_Choices)
    lodging_preference = models.CharField(max_length=10, choices=Lodging_Choices)
    Destination = models.CharField(max_length=200)
    Destination2 = models.CharField(max_length=200, blank=True, null=True)
    Number_of_People = models.CharField(max_length=10, choices=Number_of_People_Choices)
    Age_Groups = models.CharField(max_length=15, choices=Age_Group_Choices)

    def __str__(self):
        return self.full_name

    



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
    video = models.FileField(upload_to='videos/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Gallery Video {self.id}"

    

