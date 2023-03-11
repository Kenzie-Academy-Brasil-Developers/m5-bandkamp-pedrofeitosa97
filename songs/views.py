from .models import Song
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from .serializers import SongSerializer

class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))
