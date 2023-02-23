from django.contrib.auth import get_user_model
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import  AddUserSerializer

User = get_user_model()


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer


#
class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        instance = serializer.instance
        refresh = RefreshToken.for_user(instance)
        data = {
            'access_token': str(refresh.access_token),
            'email': instance.email
        }
        return Response(data, status=status.HTTP_201_CREATED)
#
#
#
# class UserLoginAPIView(TokenViewBase):
#     serializer_class = AuthTokenSerializer
#     permission_classes = ()
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         access = serializer.validated_data['access']
#         refresh = serializer.validated_data['refresh']
#         data = {'access': access, 'refresh': refresh, 'user': user}
#         return Response(data, status=status.HTTP_200_OK)
