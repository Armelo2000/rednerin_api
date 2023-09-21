
from rest_framework import serializers

from .models import *
#from drf_writable_nested import WritableNestedModelSerializer

# This class transform a Python Object to a JSON format
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'street',
            'houseNr',
            'zipCode',
            'city',
            'country',
            'phone',
        ]  

class SpeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeacherInfo
        fields = [
            'id',
            'language',
            'profession',
            'reference',
            'publication',
            'contactdetail',
            'contactform',
            'exampleLecture',
            'shortBiography',
            'longBiography',
        ]
       # depth = 1

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = [
            'id',
            'socialNetworkName',
            'icon',
        ]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'subjectname'
        ] 

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
            'id',
            'urlLink',
        ]    

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id',
            'caption',
            'photo',
        ]  

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'caption',
            'video',
        ]  


class SpeacherSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=True)
    info = SpeacherInfoSerializer(required=True)

    class Meta:
        model = Speacher
        fields = [
            'id', 
            'firstname', 
            'lastname', 
            'phonePublish',
            'accountType',
            'policy',
            'info',
            'contact',
            'subject',
            'url',
            'socialnetwork',
            'video',
            'photo'

        ]
        depth=1

