from django.shortcuts import render
from rest_framework.response import Response
from test1.serializers import ClientSerializer
from .models import Client
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
import re
# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mohanad'})


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

    def create(self, request):
    #   request.data['linkedin_link']
        print( request.data['linkedin_link'])
        if(request.data['linkedin_link'].find('www.linkedin.com') < 0):
            return Response({'error': 'Just Linked in urls are supported.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = ClientSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
    
    
        


    def get_serializer_context(self):
        return {'request': self.request}




 # urls = re.search(
        #     r'(https?)?:?(\/\/)?(([w]{3}||\w\w)\.)?linkedin.com(\w+:{0,1}\w*@)?(\S+)(:([0-9])+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/+',
        #     request.data['linkedin_link'])
        
        # print(urls)
        # # if len(urls)> 0: 
        # return Response({'error': 'Bravo.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        # else:
        #     return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        #  if check_linked == 1:
        #     return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)