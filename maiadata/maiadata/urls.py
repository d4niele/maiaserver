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


class DataViewSet2(viewsets.ModelViewSet):
    queryset = Data.objects.filter(espid='Ascea')[-1000:]
    serializer_class = DataSerializer


router = routers.DefaultRouter()
router.register(r'records', DataViewSet)
router.register(r'records_ascea', DataViewSet2)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

