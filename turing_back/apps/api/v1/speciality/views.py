from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Speciality
from .serializers import SpecialitySerializer

class SpecialityListView(generics.ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class SpecialityDetailView(generics.RetrieveAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

@api_view(['GET'])
def last_specialities(request):
    count = request.GET.get('count', 5)
    try:
        count = int(count)
    except ValueError:
        return Response({"error": "Unsupported format!"}, status=400)

    specialities = Speciality.objects.order_by('-id')[:count]
    serializer = SpecialitySerializer(specialities, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT', 'POST'])
def restricted_view(request, *args, **kwargs):
    return Response({"error": "only admin!"}, status=403)