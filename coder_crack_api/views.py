# from django.shortcuts import render
from .models import UserMessage, EmailSubscription
from rest_framework import viewsets
from .serializers import UserMsgSerializer, EmailSubsSerializer
# from django.core.mail import send_mail, BadHeaderError
from mailjet_rest import Client
from decouple import config


def send_mail(user_data):
    api_key = config('MAILJET_API_KEY')
    api_secret = config('MAILJET_API_SECRET')
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": config('EMAIL_FROM'),
                    "Name": "vladimir"
                },
                "To": [{
                    "Email": 'codercrackschool@gmail.com',  # config('EMAIL_TO'),
                    "Name": "Antonio"
                }, ],
                "TemplateID": config('MAILJET_TEMPLATE_ID', cast=int),
                "TemplateLanguage": True,
                "Subject": config('EMAIL_SUBJECT'),
                "Variables": {
                    "name": user_data["name"],
                    "lastname": user_data["lastname"],
                    "email": user_data["email"],
                    "phone": user_data["phone"],
                    "message": user_data["message"],
                }
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())


# Create your views here.
class UserMsgViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMsgSerializer

    def perform_create(self, serializer):
        user_data = serializer.validated_data
        print(user_data)
        try:
            send_mail(user_data=user_data)
        except Exception as excep:
            print(excep)
        serializer.save()


class EmailSubsViewSet(viewsets.ModelViewSet):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubsSerializer
