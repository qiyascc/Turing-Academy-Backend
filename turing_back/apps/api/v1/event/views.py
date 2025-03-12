from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@api_view(['GET'])
def last_events(request):
    count = request.GET.get('count', 5)
    try:
        count = int(count)
    except ValueError:
        return Response({"error": "unsupported format"}, status=400)

    events = Event.objects.order_by('-event_date')[:count]
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT', 'POST'])
def restricted_view(request, *args, **kwargs):
    return Response({"error": "only admin!"}, status=403)
