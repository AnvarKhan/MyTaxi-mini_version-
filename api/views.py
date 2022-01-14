from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from driver.models import User, Client, Driver, Order
from .serializers import UserSerializers, UserREGSerializer, DriverSerializers, OrdersSerializers, ClientSerializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework import permissions, status
from django.contrib.auth import authenticate
from rest_framework.response import Response


class AuthUserRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = UserREGSerializer(data=request.data)

        for user in User.objects.all():
            if not user:
                break
            else:
                try:
                    Token.objects.get(user_id=user.id)
                except Token.DoesNotExist:
                    Token.objects.create(user=user)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            return Response(
                {
                    "user": {
                        "id": serializer.data["id"],
                        "firstname": serializer.data["firstname"],
                        "lastname": serializer.data["lastname"],
                        "username": serializer.data["username"],
                    },
                    "status": {
                        "message": "User created",
                        "code": f"{status.HTTP_200_OK} OK",
                    },
                    "token": token.key,
                }
            )
        return Response(
            {
                "error": serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION}\
                    NON AUTHORITATIVE INFORMATION",
            }
        )


# userslar uchun
class UserView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializers


# clientlar uchun
class ClientView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class ClientDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


# haydovchilar uchun
class DriverView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers


class DriverDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializers


# Bron uchun
class OrderDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrdersSerializers


class OrderView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrdersSerializers


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is None:
            return Response({"error": "xatolik"}, status=status.HTTP_404_NOT_FOUND)

        token, is_create = Token.objects.get_or_create(user=user)

        return Response({
            "ok": status.HTTP_200_OK,
            'message': 'success',

            "username": token.user.username,
        }
        )
