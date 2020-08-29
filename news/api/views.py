from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.api.serializers import NewsSerializer
from news.models import NewsModel


@api_view(["GET", "POST"])
def news_list_create(request):
    if request.method == "GET":
        news = NewsModel.objects.filter(active=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def list_update_delete(request, pk):
    try:
        news = NewsModel.objects.get(pk=pk)
    except NewsModel.DoesNotExist:
        return Response({
            "code": 404,
            "status": status.HTTP_404_NOT_FOUND,
            "message": "News Does not exists"
        })

    if request.method == "GET":
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(
                serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
