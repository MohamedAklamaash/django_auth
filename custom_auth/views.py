from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerizalizer,AuthSerializer
from .models import AuthModel
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class SignupUser(APIView):
    def post(self, request):
        # usr = AuthModel.objects.create(request.data)
        serializedUser = RegisterSerializer(data = request.data)
        if serializedUser.is_valid():
            usr = serializedUser.save() # a user is created successfully
            refresh = RefreshToken.for_user(usr) # creating a refresh token
            access_token = str(refresh.access_token) # access a access token  using a refresh token
            return Response(
                {
                  "access_token":access_token  ,
                  "data":serializedUser.data,
                  "refresh":str(refresh)
                },
            )

class SigninView(APIView):
    def post(self, request):
        serialized = LoginSerizalizer(data=request.data)
        if serialized.is_valid():
            usr = AuthModel.objects.get(email = serialized.validated_data["email"])
            if not usr:
                return Response({"message":"No user found with the given mail id","errors":serialized.errors})

            if not usr.checkPassword(serialized.validated_data["password"]):
                return Response({"message":"Incorrect Password","errors":serialized.errors})
            
            refresh = RefreshToken.for_user(usr)
            access_token = str(refresh.access_token)
            return Response({
                "messages":"User signin successful",
                "access_token":access_token,
                "refresh":str(refresh)
            })