from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Owner, Property, Feedback
from .serializers import OwnerSerializer, PropertySerializer, FeedbackSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"detail": "City parameter is required."}, status=400)

        properties = Property.objects.filter(city__iexact=city)  # Case-insensitive filter
        if not properties.exists():
            return Response({"detail": "No properties found for this city."}, status=404)

        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_zip_code(self, request):
        zip_code = request.query_params.get('zip_code')
        if not zip_code:
            return Response({"detail": "Zip code parameter is required."}, status=400)

        properties = Property.objects.filter(zip_code=zip_code)
        if not properties.exists():
            return Response({"detail": "No properties found for this zip code."}, status=404)

        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer