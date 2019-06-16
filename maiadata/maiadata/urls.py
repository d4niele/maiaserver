from django.contrib import admin
import json,datetime
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Data

admin.site.site_header = 'MAIA SERVER ADMIN'
admin.site.site_title = admin.site.site_header


class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('timereg','espid', 'topic', 'timestamp', 'peso','temperatura','umidita')

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer   
    def create(self, request): 
        post_data = request.data
        v = post_data
        data = Data()
        for x in v:
            setattr(data,x,v[x])
        data.timereg = datetime.datetime.now()
        data.save()
        return Response('OK')

router = routers.DefaultRouter()
router.register(r'records', DataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

