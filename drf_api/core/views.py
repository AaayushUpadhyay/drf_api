from .models import Post
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer

# imports from third party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):

    permission_classes=(IsAuthenticated,)



    def get(self,request,*args,**kwargs):
        qs=Post.objects.all()
        serializer=PostSerializer(qs,many=True)
        # agar objects ek se zyada hai toh many=True likhenge
        return Response(serializer.data)

        
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# Create your views here.
# def test_view(request):
#     data={
#         'name':'Ayush',
#         'age':23
#     }
#     return JsonResponse(data)

    # JsonResponse by-default accepts dictionary but we can also pass 
    # list or other data types by passing parameter safe=False
