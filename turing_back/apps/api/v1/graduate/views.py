from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Graduate
from .serializers import GraduateSerializer

class GraduateListView(generics.ListAPIView):
    queryset = Graduate.objects.all()
    serializer_class = GraduateSerializer

class GraduateDetailView(generics.RetrieveAPIView):
    queryset = Graduate.objects.all()
    serializer_class = GraduateSerializer

@api_view(['GET'])
def last_graduates(request):
    count = request.GET.get('count', 5)
    try:
        count = int(count)
    except ValueError:
        return Response({"error": "unsupported format"}, status=400)

    graduates = Graduate.objects.order_by('-id')[:count]
    serializer = GraduateSerializer(graduates, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT', 'POST'])
def restricted_view(request, *args, **kwargs):
    return Response({"error": "only admin!"}, status=403)