from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import HeroModel, HeroImageModel, AboutModel, AnniversaryModel, UpcomingToursModel, PopularDestinationModel, ReviewsModel, AdminContactModel, LocationModel, GalleryImageModel,GalleryVideoModel, OptionModel, UpcomingToursImagesModel, ServiceModel, EnquiryModel, GetInTouchModel, UpcomingDestinationHighlightsModel
from .serializers import HeroSerializers, HeroImageSerializers, AboutSerializers, AnniversarySerializers, UpcomingToursSerializers, PopularDestinationSerializers, ReviewsSerializers, AdminContactSerializers, LocationSerializers, GalleryImageSerializers, GalleryVideoSerializers, OptionSerializers, UpcomingToursImagesSerializers, ServiceSerializers, EnquirySerializers, GetInTouchSerializers, UpcomingDestinationHighlightsSerializers
from rest_framework.views import APIView
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from rest_framework.permissions import IsAuthenticated


class HeroListCreateView(generics.GenericAPIView):
    serializer_class = HeroSerializers

    def get_serializer_context(self):
        # Ensure 'request' is passed to serializer
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get(self, request):
        hero = HeroModel.objects.first()
        if not hero:
            return Response({"detail": "No hero found"}, status=404)
        serializer = self.get_serializer(hero)
        return Response(serializer.data)

    def post(self, request):
        hero = HeroModel.objects.first()

        if hero:
            serializer = self.get_serializer(hero, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class HeroImageListCreateView(generics.ListCreateAPIView):
    queryset = HeroImageModel.objects.all()
    serializer_class = HeroImageSerializers

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class HeroImageManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeroImageModel.objects.all()
    serializer_class = HeroImageSerializers
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context




class AnniversaryListCreateView(generics.ListCreateAPIView):
    serializer_class = AnniversarySerializers

    def get_serializer_context(self):
        # Pass the request to the serializer
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get(self, request):
        anniversary = AnniversaryModel.objects.first()
        if not anniversary:
            return Response({"detail": "No anniversary found"}, status=404)
        serializer = self.get_serializer(anniversary)
        return Response(serializer.data)

    def post(self, request):
        anniversary = AnniversaryModel.objects.first()

        if anniversary:
            serializer = self.get_serializer(anniversary, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class AboutListCreateView(generics.ListCreateAPIView):
    serializer_class = AboutSerializers

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

class OptionManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializers
    lookup_field = 'id'

class UpcomingToursListCreateView(generics.ListCreateAPIView):
    queryset = UpcomingToursModel.objects.all()
    serializer_class = UpcomingToursSerializers

class UpcomingToursManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingToursModel.objects.all()
    serializer_class = UpcomingToursSerializers
    lookup_field = 'id'

class UpcomingToursImagesListCreateView(generics.ListCreateAPIView):
    queryset = UpcomingToursImagesModel.objects.all()
    serializer_class = UpcomingToursImagesSerializers

class UpcomingToursImagesManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingToursImagesModel.objects.all()
    serializer_class = UpcomingToursImagesSerializers
    lookup_field = 'id'

class UpcomingDestinationHighlightsListCreateView(generics.ListCreateAPIView):
    queryset = UpcomingDestinationHighlightsModel.objects.all()
    serializer_class = UpcomingDestinationHighlightsSerializers

class UpcomingDestinationHighlightsManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingDestinationHighlightsModel.objects.all()
    serializer_class = UpcomingDestinationHighlightsSerializers
    lookup_field = 'id'

class OptionListCreateView(generics.ListCreateAPIView):
    queryset = OptionModel.objects.all()
    serializer_class = OptionSerializers

class PopularDestinationListCreateView(generics.ListCreateAPIView):
    queryset = PopularDestinationModel.objects.all()
    serializer_class = PopularDestinationSerializers

class PopularDestinationManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PopularDestinationModel.objects.all()
    serializer_class = PopularDestinationSerializers
    lookup_field = 'id'

class ServiceListUpdateView(generics.GenericAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializers

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
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # 👈 this line makes patch optional
        return super().update(request, *args, **kwargs)

class ReviewsListCreateView(generics.ListCreateAPIView):
    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializers

class ReviewsManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewsModel.objects.all()
    serializer_class = ReviewsSerializers
    lookup_field = 'id'

class AdminContactListCreateView(generics.ListCreateAPIView):
    serializer_class = AdminContactSerializers
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

class GetInTouchManageView(generics.RetrieveDestroyAPIView):
    queryset = GetInTouchModel.objects.all()
    serializer_class = GetInTouchSerializers
    lookup_field = 'id'

class LocationListCreateView(generics.ListCreateAPIView):
    serializer_class = LocationSerializers

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

class GalleryImageManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryImageModel.objects.all()
    serializer_class = GalleryImageSerializers
    lookup_field = 'id'

class GalleryVideoListCreateView(generics.ListCreateAPIView):
    queryset = GalleryVideoModel.objects.all()
    serializer_class = GalleryVideoSerializers

class GalleryVideoManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryVideoModel.objects.all()
    serializer_class = GalleryVideoSerializers
    lookup_field = 'id'


class EnquiryView(APIView):
    def post(self, request):
        try:
            serializer = EnquirySerializers(data=request.data)
            if serializer.is_valid():
                enquiry = serializer.save()

                # Update the email content for new fields
                subject = "New Enquiry Received"
                message = f"""
New enquiry received:

Email: {enquiry.email}
Phone: {enquiry.phone}
Destination 1: {enquiry.Destination}
Destination 2: {enquiry.Destination2 or 'N/A'}
Travel Plans: {enquiry.travelPlans or 'N/A'}

Please check the admin panel for full details.
                """

                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [settings.ADMIN_EMAIL],
                        fail_silently=False,
                    )
                except Exception as e:
                    print("Mail sending error:", e)
                    # For testing with console backend, this should not fail

                return Response(
                    {"message": "Enquiry submitted successfully!"},
                    status=status.HTTP_201_CREATED,
                )

            else:
                print("Serializer errors:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("View error:", e)
            return Response({"error": str(e)}, status=500)
