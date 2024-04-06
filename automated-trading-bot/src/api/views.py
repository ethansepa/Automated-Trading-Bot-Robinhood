from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import robin_stocks.robinhood as robinhood

class Login(APIView):
    def post(self, request, fromat=None):
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        print(password)
        login = robinhood.login(username, password)
        if login != None:
            return Response({'message': 'Loged In!'}, 
                                status=status.HTTP_200_OK)
        return Response({'Bad Request': 
                         'Invalid login credentials.'}, 
                         status=status.HTTP_400_BAD_REQUEST) 