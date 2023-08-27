
from rest_framework import serializers

from .models import Rednerin, RednerinInfo, SocialNetwork, Url, Subject, Video


# This class transform a Python Object to a JSON format
class RednerinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rednerin
        fields = ['id', 
        'firstname', 
        'lastname', 
        'street',
        'houseNr',
        'zipCode',
        'city',
        'country',
        'phone',
        'phonePublish',
        'information',
        'option',
        'image',
        'policy'

        ]

class RednerinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RednerinInfo
        fields = [
            'id',
            'rednerin_Id',
            'language',
            'profession',
            'reference',
            'publication',
            'contactdetail',
            'contactform',
            'exampleLecture',
            'shortBiography',
            'longBiography',
            'subject',
            'url',
            'socialnetwork',
            'video',
        ]
        depth = 1

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

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'caption',
            'video',
            #'rednerinInfo'
        ]  


