from rest_framework import serializers
from .models import AuthModel

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthModel
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthModel
        fields = ["username","email","password"]
        extra_kwargs = {"password":{"write_only":True}}

    
    def create(self, validated_data): # assuming that already sent details are validated
        usr = AuthModel.objects.create(
            email = validated_data["email"],
            username =validated_data["username"]
        )
        usr.savePassword(validated_data["password"]) # this will hash the sent data
        usr.save() # saving the user
        return usr


class LoginSerizalizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()