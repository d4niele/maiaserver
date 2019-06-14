"""maiadata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import json
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
        fields = ('espid', 'topic', 'timestamp', 'peso','temperatura','umidita')

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer   
    def create(self, request): # Here is the new update comes <<<<
        post_data = request.data
        v = json.loads(list(post_data.dict().keys())[0])
        #post_data.save()
        # do something with post data
        data = Data()
        for x in v:
            setattr(data,x,v[x])
            print()
        data.save()
         #data.save()
        return Response(data="return data")

router = routers.DefaultRouter()
router.register(r'records', DataViewSet)
#from rest_framework.views import APIView
#from rest_framework.response import Response#

#class DataView(APIView):
#    def get(self, request):
#        data = Data.objects.all()
#        serializer =DataSerializer(data) 
#       return Response({"records": data})
#        return Response({'records':serializer.data})
#    queryset = Data.objects.all()
#    serializer_class = DataSerializer
    # def post(self, request, format=None):
    #     print(request.data)
    #     serializer = DataSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('records/', DataView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#curl -X POST H "Authorization: JWT token" http://localhost:8000/records/ '{"key":"val"}'
