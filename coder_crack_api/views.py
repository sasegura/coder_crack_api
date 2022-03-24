# from django.shortcuts import render
from .models import UserMessage, EmailSubscription
from rest_framework import viewsets
from .serializers import UserMsgSerializer, EmailSubsSerializer


# Create your views here.
class UserMsgViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMsgSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        serializer.save()


class EmailSubsViewSet(viewsets.ModelViewSet):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubsSerializer
