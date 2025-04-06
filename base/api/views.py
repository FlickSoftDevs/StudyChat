# Tunapakia decorator ya API na class ya Response kutoka Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Tunapakia model ya Room kutoka kwenye app ya base
from base.models import Room

# Tunapakia serializer wa Room
from .serializers import RoomSerializer


# Endpoint ya kutoa routes (njia za API) zinazopatikana — ni kwa ajili ya maelezo tu
@api_view(['GET'])  # Inaruhusu HTTP GET requests pekee
def getRoutes(request):
    routes = [
        'GET /api',              # Njia ya kupata routes zote
        'GET /api/rooms',        # Njia ya kupata list ya rooms
        'GET /api/rooms/:id'     # Njia ya kupata room moja kwa kutumia ID
    ]
    return Response(routes)  # Tunarudisha array ya njia kama JSON response


# Endpoint ya kupata list ya rooms zote
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()  # Tunachukua rooms zote kutoka database
    serializer = RoomSerializer(rooms, many=True)  # Tunaziserialize zote kwa sababu ni nyingi
    return Response(serializer.data)  # Tunarudisha data kama JSON


# Endpoint ya kupata room moja tu kwa kutumia primary key (ID)
@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)  # Tunapata room kwa ID
    serializer = RoomSerializer(room, many=False)  # Serialize room moja tu
    return Response(serializer.data)  # Rudisha data kama JSON
