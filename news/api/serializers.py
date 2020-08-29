from rest_framework import serializers
from news.models import NewsModel


class NewsSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    created_at = serializers.CharField(read_only=True)
    publication_date = serializers.CharField()
    active = serializers.CharField()
    updated_at = serializers.CharField(read_only=True)

    # def __str__(self):
    #     return f"{self.author}  {self.title}"

    def create(self, validated_data):
        print(validated_data)
        return NewsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date)
        instance.active = validated_data.get("active", instance.active)
        instance.updated_at = validated_data.get(
            "updated_at", instance.updated_at)
