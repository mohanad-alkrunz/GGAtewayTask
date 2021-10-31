
from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'father_name', 'middle_name', 'last_name','bio','full_address',
                  'date_of_birth', 'gender', 'nationality','phone_number','linkedin_link','client_profile_img']

    
