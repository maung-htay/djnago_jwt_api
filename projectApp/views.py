from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import safe
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from projectApp.models import Book
from projectApp.serializers import BookSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def project_detail(request):
    if request.method == 'GET':
        pj_list = Book.objects.all()
        pj_serializer = BookSerializer(pj_list, many=True)

        return JsonResponse({

            "data": pj_serializer.data
        }, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        pj_data = JSONParser().parse(request)
        pj_data_serializer = BookSerializer(data=pj_data)
        if pj_data_serializer.is_valid():
            pj_data_serializer.save()
            return JsonResponse(pj_data_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pj_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def hello(request):
    return JsonResponse({
        "msg": "Hellow"
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_books(request):
    book_list = Book.objects.all()
    search_book = request.GET.get('title',None)
    if search_book:
        book_list = Book.objects.filter(title__icontains = search_book)

    book_serializer = BookSerializer(book_list, many=True)

    return JsonResponse(
        book_serializer.data, safe=False
    )
