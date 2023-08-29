from django.shortcuts import render
from rest_framework import request, status, viewsets
from .models import Rating,Phone
from .serializers import PhoneSerializer,RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class viewsets_phone(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    
    @action(detail=True,methods=['POST'])
    def rate_phone(self,request,pk=None):
        if 'stars' in request.data:
            phone = Phone.objects.get(pk=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id,phone=phone.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(Rating,many=False)
                json = {
                    'message':'rate updated with success',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            
            except:
                rating = Rating.objects.create(user=user,phone=phone,stars=stars)
                serializer = RatingSerializer(rating,many=False)
                json = {
                    'message':'rate updated with success',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_201_CREATED)
        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)
                
        
        
    
class viewsets_ratings(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer    