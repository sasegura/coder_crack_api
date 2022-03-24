from .models import EmailSubscription, UserMessage
from rest_framework import serializers


class EmailSubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = '__all__'


class UserMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'
