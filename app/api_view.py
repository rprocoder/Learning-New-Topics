from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.generics import CreateAPIView
from .models import *
import logging

logger = logging.getLogger(__name__)

###  MEthod : 1
# class UserRegistrationAPIView(APIView):
#     print('api',APIView)
#     def post(self, request):
#         print('request',request)
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             print('user',user,type(user))
#             return Response({"userserlizerdaa":serializer.data,'user':str(user)}, status=status.HTTP_201_CREATED)
#         else:
#             print("Serializer Errors:", serializer.errors)  # Print out the errors
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### Method : 2        
class UserRegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            user = serializer.instance
            logger.debug('User: %s', user)
            return Response({"userserlizerdaa": serializer.data, 'user': str(user)}, status=status.HTTP_201_CREATED)
        else:
            logger.error('Serializer Errors: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
