from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from cars.models import Car
from cars.serializers import CarSerializer

from rest_framework import status


#@api_view(['GET'])
def getCars(request):
    if request.method=='GET':
        cars = Car.objects.all()
        cars_serializer = carSerializer(cars,many=True)
        return JsonResponse(cars_serializer.data,safe=False)



    
    #query = request.query_params.get('keyword')
    #if query == None:
    #    query = ''

    #cars = Car.objects.filter(
    #    name__icontains=query).order_by('-createdAt')

    #page = request.query_params.get('page')
    #paginator = Paginator(cars, 5)

    #try:
    #    cars = paginator.page(page)
    #except PageNotAnInteger:
    #    cars = paginator.page(1)
    #except EmptyPage:
    #    cars = paginator.page(paginator.num_pages)

    #if page == None:
    #    page = 1

    #page = int(page)
    #print('Page:', page)
    #serializer = CarSerializer(cars, many=True)
    #return Response({'cars': serializer.data, 'page': page, 'pages': paginator.num_pages})




@api_view(['GET'])
def getCar(request, pk):
    product = Car.objects.get(_id=pk)
    serializer = CarSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createCar(request):
    user = request.user

    product = Car.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        link='',
        description=''
    )

    serializer = CarSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Car.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')