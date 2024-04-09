from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer
from .models import User

import robin_stocks.robinhood as robinhood

class Login(APIView):
    serializer_class = UserSerializer
    def post(self, request, fromat=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer.data.get('username'))
        print(serializer.data.get('password'))

        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            print(username)
            print(password)
            login = robinhood.login(username, password)
            if login:
                user = User(username, password)
                user.save()
                print("LOGGED IN!")
                return Response(UserSerializer(User).data, 
                                status=status.HTTP_200_OK)
            else:
                return Response({'Bad Request': 
                         'Invalid login credentials.'}, 
                         status=status.HTTP_400_BAD_REQUEST) 
        
        return Response({'Bad Request': 'Invalid data...'}, 
                        status=status.HTTP_400_BAD_REQUEST)
        