from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
firebaseConfig = {
     "type": "service_account",
    "project_id": "donatengo-c090d",
    "private_key_id": "644d8b6fff192494d9d5c8c37339efb5b409bba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCqk2VBjqcO35gA\nmxNTM3dXtio15/SC4zjC/wh5YxnjlF6kV+Q1AwaOQzNc93pZs1KN+XyVzQSFTCQy\nQoc8OIV2SnSsNlJrOe1H+ea5FSKyepESv5s0mgUHd5+HSKczAKeGpYTCu+m8iw8s\nJ6snRj+7d8oNLcTiwS1/FeRSg6chOT4zCni6QnJnWIQHXAeCrYpoOzQwI2irz/cJ\n14yZqq+OmhyWTjALMdoAzAnw6hhgEfq9Lmx9Esj+DAcmNVlbjYBBrO9r1FxIAavU\n848w8vKZtdwyd5l0SsbA6RDYvhNL/O+lEsCVKHVHtdzIpXw+8/KOi0acyHGM2DcG\njPRubjsdAgMBAAECggEABpYTYlEiRTI/+cIDIILLuGDJx3QR3l3sqqbTSnCXptBr\nSRg1sRBRV/vjR1Ms77q7VM0N0PDuHEGA4knsU9hw2szsLVwZmZdOgKl3Da1xvgd6\ng4lPclwCFrQ5Pi2Bezgqv8mzUxuTXlrWNqO/eZA+VLw+2nxqbkD8QzxyqPb5ZJBz\nj0LgdHxRoFPwWM0MO8aUnQ8jmIz+A0/+GShrGeHljwJAhVA/3aQeoEEY6u0n3LNj\nMnpi4OchpaW6mer9xDruPyknVq7QwMyu4UoNtBeTJSkOciDvrQvew7dgUzcnqj4H\nq+PSloOohtmDJrvZtkfZ3G8WJA9dW1Lkf7QP1MlOdwKBgQDlqFMgp5blF0QkCEkb\n+jwyloBxnvuYyqbwM7FaZvTcHH/ShrkJdyOl8gSdhjFIuPZJCl8glgt3JugK3oUJ\nD1Itb4TnS1ifV4XfPEJCzwg9gsdMWMPvw4E6fXNl2TYzffeaSG/cU+cxYp4R1T/I\n7pO4ehUi+Y/SApK9vikDsDt2TwKBgQC+JDDsZVhu2NlgribllQGQ6cgMMk2+JQq8\nkMxioEXkWZbSRiJcKBzyUA8VAdstpnnW1wTG8P4O1ycyl1jwN+2Ud+BBM2+0rshq\nA2DsQqDiCLKcRmqXIN/S0WGIIySkiDJcZqb9tu+4sKJwvJCzjbn/RhauhfvUu/gZ\nkft7taLI0wKBgAOjLN3hiaRLQAsKDo5g4j8y3wntqLJ80zQOvYpfAxXRZbzh4WBj\nAK+KK8SK8ZDjTRNPFL6hYcEbXqV9bMH9+iE6GPLI4Lh1XGtyuuHwAYNn5Nwys7fC\ncvOINSGx1QfvwNIyv4LP2WOQ2kwSApaeILzVQixxo3OCEuzqbB/g1LBFAoGAHn4T\nUnXWPsCL69NB7aN9ws2bBUmz6gBqvl7CSDbHvp0XcNVKgVj1e26XXJkVmzaNZ4TI\nAVd4hsy+PoDDBJMTiLHIxuwGyAUXotiz3G+6+UTH0AQC6AWfn2FwsLJiF/i3itXz\nhdCmlQnOoyG6WvEpmOSWkppuDmmumfstR2OTnX0CgYEAlqof19U15D2lYbZWWGAv\nPF7G3Kwn9GvSqxRxbEQoqGaqgbsp+ytCqdkE7iEnO6mLUg6MAR4acOPNlP7oUSnT\nM1Fy0uLmVX1Tg/xQkdlpJaOvl0GvdEA0fVZpDg2ycaqEl+cG866bWS+/KruJIDoZ\nGLHrqawwOb3liV1xLxD4mTA=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-769ww@donatengo-c090d.iam.gserviceaccount.com",
    "client_id": "109026389330420061788",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-769ww%40donatengo-c090d.iam.gserviceaccount.com",
  }

cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
db=firestore.client()
db.collection("demo").add({"shyam":40})


def home(request):
    return render(request, "home.html")


# Create your views here.
