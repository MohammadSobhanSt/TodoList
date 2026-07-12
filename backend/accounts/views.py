from rest_framework.views import APIView, Response, status


class RegistrationView(APIView):
    def get(self, request):
        return Response("This is home", status=status.HTTP_200_OK)