from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import FileResponse
import os

class Index(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'tinku':'kalluri'} , status=status.HTTP_201_CREATED)

class APIKey(APIView):
    def get(self, request, *args, **kwargs):
        pass

class asset_images(APIView):
    def get(self, request, *args, **kwargs ):
        projectname=request.GET.get('projectname')
        filename=request.GET.get('filename')
        path_to_file=os.path.join(f'images/asset/images/{projectname}' ,filename)
        print("path to file" , path_to_file)
        print(projectname, filename)
        # "C:/Users/sintin/Desktop/Projects_3/assets-server/assets_server/images/asset/images/project1/1.jpeg"
        img = open(path_to_file, 'rb')
        print("image name",img.name)
        response = FileResponse(img)
        return response
        # return Response({'yoto':'guys'} , status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs ):
        projectname=request.data.get('projectname')
        filename=request.data.get('filename')
        path_to_file=os.path.join(f'images/asset/images/{projectname}' ,filename)
        print("path to file" , path_to_file)
        print(projectname, filename)
        # "C:/Users/sintin/Desktop/Projects_3/assets-server/assets_server/images/asset/images/project1/1.jpeg"
        img = open(path_to_file, 'rb')
        print("image name",img.name)
        response = FileResponse(img)
        return response
        # return Response({'yoto':'guys'} , status=status.HTTP_200_OK)
