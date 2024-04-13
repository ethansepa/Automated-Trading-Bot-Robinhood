from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .serializers import TraderSerializer
from .models import Trader
from ml_model.bots.rolling_avg_trend_bot import RollingAvgTrendBot
import robin_stocks.robinhood as robinhood


class Login(APIView):
    serializer_class = TraderSerializer
    def post(self, request, fromat=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            print(username)
            print(password)
            login = robinhood.login(username, password)
            #robinhood.authentication.logout()
            print(login["detail"])
            if login["detail"] != "":
                bot = RollingAvgTrendBot()
                print(bot.get_holding_value("SOFI"))
                robinhood.logout()
                trader = Trader(id=2, username=username, password=password)
                trader.save()
                print("LOGGED IN!")
                return Response(TraderSerializer(Trader).data, 
                                status=status.HTTP_200_OK)
            else:
                return Response({'Bad Request': 
                         'Invalid login credentials.'}, 
                         status=status.HTTP_400_BAD_REQUEST) 
        
        return Response({'Bad Request': 'Invalid data...'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
class Trader(generics.ListAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer