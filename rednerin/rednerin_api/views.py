from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from . models import *
from . serializers import *
from rest_framework.decorators import api_view

from rest_framework import status, viewsets


@api_view(['GET', 'POST'])
def user(request, format=None): 
    # format=None is used to obtain json from our url
    if request.method == 'GET':
        # Get the list of all Users
        users = Rednerin.objects.all()

        serializer = RednerinSerializer(users, many=True)

        return Response(serializer.data)

@api_view(['GET', 'POST'])
def info(request, format=None): 
    # format=None is used to obtain json from our url
    if request.method == 'GET':
        # Get the list of all Users
        info = RednerinInfo.objects.all()

        serializer = RednerinInfoSerializer(info, many=True)

        user = Rednerin.objects.get(pk=2)

        #s = RednerinSerializer(user, many=True)

        #serializer.data['rednerin_Id'] = s

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def test(request, pk, format=None): 
    # format=None is used to obtain json from our url
    if request.method == 'GET':

        # Get data from table Rednerininfo
        info = RednerinInfo.objects.get(id=pk)
        InfoSerializer = RednerinInfoSerializer(info)

        # Get Data from table Rednerin
        user = Rednerin.objects.get(id=InfoSerializer.data['rednerin_Id'])
        UserSerializer = RednerinSerializer(user)
    
        # Get Data from table Subject
        #subject = Subject.objects.get(rednerinInfo=InfoSerializer.data['id'])
        theme = RednerinInfo.objects.get(id=pk)#.subject_set.all()
        users = []
        result = set() 
        for user in theme.subject_set:
            result.add(user.subjectname)
            users.append(result)

        # Get Data from table Url
        #url = Url.objects.get(rednerinInfo=InfoSerializer.data['id'])
        #urlSerializer = UrlSerializer(url)

        # Get Data from table Social network
        #socialNetwork = SocialNetwork.objects.get(rednerinInfo=InfoSerializer.data['id'])
        #socialNetworkSerializer = SocialNetworkSerializer(socialNetwork)

        # Get data from table Video
        #video = Video.objects.get(rednerinInfo=InfoSerializer.data['id'])
        #videoSerializer = VideoSerializer(videoSerializer)

        context = {
            'Rednerin': UserSerializer.data,
            'Rednerin_Info': InfoSerializer.data,
            #'subject': subjectSerializer.data
            #'subject':result,
            'Theme':result
            #'url': urlSerializer.data,
            #'social_network': socialNetworkSerializer.data,
            #'video': videoSerializer.data

        }
        userFound = {
            'user_'+ f"{UserSerializer.data['id']}": context,
        }

        return Response(userFound)


class RednerinViewSet(viewsets.ModelViewSet):
    serializer_class = RednerinSerializer

    #@api_view(['GET'])
    def get_queryset(self):
        rednerin = Rednerin.objects.all()

        return rednerin

class RednerinInfoViewSet(viewsets.ModelViewSet):
    serializer_class = RednerinInfoSerializer

    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        rednerin_info = RednerinInfo.objects.all()

        return rednerin_info

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer

    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        subject = Subject.objects.all()

        return subject

class UrlViewSet(viewsets.ModelViewSet):
    serializer_class = UrlSerializer

    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        url = Url.objects.all()

        return url

class SocialNetworkViewSet(viewsets.ModelViewSet):
    serializer_class = SocialNetworkSerializer

    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        social_network = SocialNetwork.objects.all()

        return social_network

class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer

    #@api_view(['GET', 'POST'])
    def get_queryset(self):
        video = Video.objects.all()

        return video

