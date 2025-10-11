from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import HeroModel, AboutModel, AnniversaryModel, UpcomingToursModel, PopularDestinationModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel,GalleryVideoModel, OptionModel, UpcomingToursImagesModel, ServiceModel, EnquiryModel, GetInTouchModel
from .serializers import HeroSerializers, AboutSerializers, AnniversarySerializers, UpcomingToursSerializers, PopularDestinationSerializers, ReviewsSerializers, AdminContactSerializers, LocationSerializers, GalleryImageSerializers, GalleryVideoSerializers, OptionSerializers, UpcomingToursImagesSerializers, ServiceSerializers, EnquirySerializers, GetInTouchSerializers
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated


class HeroListCreateView(generics.GenericAPIView):
    serializer_class = HeroSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        hero = HeroModel.objects.first()
        if not hero:
            return Response({"detail": "No hero found"}, status=404)
        serializer = self.serializer_class(hero)
        return Response(serializer.data)

    def post(self, request):
        hero = HeroModel.objects.first()

        if hero:
            serializer = self.serializer_class(hero, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class AnniversaryListCreateView(generics.ListCreateAPIView):
    serializer_class = AnniversarySerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        anniversary = AnniversaryModel.objects.first()
        if not anniversary:
            return Response({"detail": "No anniversary found"}, status=404)
        serializer = self.serializer_class(anniversary)
        return Response(serializer.data)

    def post(self, request):
        anniversary = AnniversaryModel.objects.first()

        if anniversary:
            serializer = self.serializer_class(anniversary, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class AboutListCreateView(generics.ListCreateAPIView):
    serializer_class = AboutSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        about = AboutModel.objects.first()
        if not about:
            return Response({"detail": "No about found"}, status=404)
        serializer = self.serializer_class(about)
        return Response(serializer.data)
    
    def post(self, request):
        about = AboutModel.objects.first()

        if about:
            serializer = self.serializer_class(about, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class OptionListCreateView(generics.ListCreateAPIView):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializers
    permission_classes = [IsAuthenticated]    

class OptionManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class UpcomingToursListCreateView(generics.ListCreateAPIView):
    queryset = UpcomingToursModel.objects.all()
    serializer_class = UpcomingToursSerializers
    permission_classes = [IsAuthenticated]

class UpcomingToursManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingToursModel.objects.all()
    serializer_class = UpcomingToursSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class UpcomingToursImagesListCreateView(generics.ListCreateAPIView):
    queryset = UpcomingToursImagesModel.objects.all()
    serializer_class = UpcomingToursImagesSerializers
    permission_classes = [IsAuthenticated]

class UpcomingToursImagesManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingToursImagesModel.objects.all()
    serializer_class = UpcomingToursImagesSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class OptionListCreateView(generics.ListCreateAPIView):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializers
    permission_classes = [IsAuthenticated]

class PopularDestinationListCreateView(generics.ListCreateAPIView):
    queryset = PopularDestinationModel.objects.all()
    serializer_class = PopularDestinationSerializers
    permission_classes = [IsAuthenticated]

class PopularDestinationManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PopularDestinationModel.objects.all()
    serializer_class = PopularDestinationSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class ServiceListUpdateView(generics.GenericAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        services = ServiceModel.objects.all().order_by('id')
        serializer = self.serializer_class(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Block creation if 9 items already exist
        if ServiceModel.objects.count() >= 9:
            return Response({"detail": "Cannot add more than 9 services."}, status=400)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
class ServiceManageView(generics.RetrieveUpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # 👈 this line makes patch optional
        return super().update(request, *args, **kwargs)

class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [IsAuthenticated]

class ReviewsManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class AdminContactListCreateView(generics.ListCreateAPIView):
    serializer_class = AdminContactSerializers
    permission_classes = [IsAuthenticated]
    def get(self, request):
        admin_contact = AdminContactModel.objects.first()
        if not admin_contact:
            return Response({"detail": "No admin contact found"}, status=404)
        serializer = self.serializer_class(admin_contact)
        return Response(serializer.data)
    
    def post(self, request):
        admin_contact = AdminContactModel.objects.first()

        if admin_contact:
            serializer = self.serializer_class(admin_contact, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class GetInTouchListCreateView(generics.ListCreateAPIView):
    queryset = GetInTouchModel.objects.all()
    serializer_class = GetInTouchSerializers
    permission_classes = [IsAuthenticated]

class GetInTouchManageView(generics.RetrieveDestroyAPIView):
    queryset = GetInTouchModel.objects.all()
    serializer_class = GetInTouchSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class LocationListCreateView(generics.ListCreateAPIView):
    serializer_class = LocationSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request):
        location = LocationModel.objects.first()
        if not location:
            return Response({"detail": "No location found"}, status=404)
        serializer = self.serializer_class(location)
        return Response(serializer.data)
    
    def post(self, request):
        location = LocationModel.objects.first()

        if location:
            serializer = self.serializer_class(location, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class GalleryImageListCreateView(generics.ListCreateAPIView):
    queryset = GalleryImageModel.objects.all()
    serializer_class = GalleryImageSerializers
    permission_classes = [IsAuthenticated]

class GalleryImageManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryImageModel.objects.all()
    serializer_class = GalleryImageSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class GalleryVideoListCreateView(generics.ListCreateAPIView):
    queryset = GalleryVideoModel.objects.all()
    serializer_class = GalleryVideoSerializers
    permission_classes = [IsAuthenticated]

class GalleryVideoManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryVideoModel.objects.all()
    serializer_class = GalleryVideoSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class EnquiryView(APIView):
    permission_classes = [IsAuthenticated]
    # Handle POST request (user submits form)
    def post(self, request):
        serializer = EnquirySerializers(data=request.data)
        if serializer.is_valid():
            enquiry = serializer.save()

            # Construct email message for admin
            subject = f"New Enquiry from {enquiry.full_name}"
            message = f"""
                            New enquiry received:

                            Full Name: {enquiry.full_name}
                            Email: {enquiry.email}
                            Phone: {enquiry.phone}
                            Location: {enquiry.location}
                            Destination 1: {enquiry.Destination}
                            Destination 2: {enquiry.Destination2 or 'N/A'}
                            Number of People: {enquiry.Number_of_People}
                            Age Groups: {enquiry.Age_Groups}
                            Budget per Person: ₹{enquiry.budget_per_person}
                            Budget Flexibility: {enquiry.how_strict_budget}
                            Lodging Preference: {enquiry.lodging_preference}
                            Departure Month: {enquiry.Departure_Month}
                            Trip Duration: {enquiry.Trip_Duration}

                            Please check the admin panel for full details.
            """

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # Add multiple admins if needed
                fail_silently=False,
            )

            return Response(
                {"message": "Enquiry submitted successfully!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET request (admin views all enquiries)
    def get(self, request):
        enquiries = EnquiryModel.objects.all().order_by('-id')
        serializer = EnquirySerializers(enquiries, many=True)
        return Response(serializer.data)
