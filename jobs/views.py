from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from jobs.models import JobsModel
from jobs.jobserializer import JobsSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.


class JobVC(APIView):

    def get(self, request):
        news = JobsModel.objects.all()
        serializer = JobsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailsModify(APIView):
    def get_object(self, pk):
        news = get_object_or_404(JobsModel, pk=pk)
        return news

    def get(self, request, pk):
        news = self.get_object(pk)
        serializer = JobsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        serializer = JobsSerializer(
            self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
