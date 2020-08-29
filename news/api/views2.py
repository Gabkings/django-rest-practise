from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from news.models import NewsModel
from news.api.serializers import NewsSerializer
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView


class NewsClass(APIView):

    def get(self, request):
        news = NewsModel.objects.filter(active=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailsModify(APIView):
    def get_object(self, pk):
        news = get_object_or_404(NewsModel, pk=pk)
        return news

    def get(self, request, pk):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        serializer = NewsSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(
                serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
