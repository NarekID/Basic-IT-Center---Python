from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MyApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        with open("myfile.txt", "r") as content:
            return Response(content.read())

    def post(self, request):
        data = request.data
        with open("myfile.txt", "a") as content:
            for val in data:
                content.write("\n" + data[val])
            return Response(content)

