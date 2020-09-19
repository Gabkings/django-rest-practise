from rest_framework import serializers
from news.models import NewsModel, Journalist
from datetime import datetime
from django.utils.timesince import timesince


class NewsSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = NewsModel
        exclude = ("id",)
    # id = serializers.CharField(read_only=True)
    # author = serializers.CharField()
    # title = serializers.CharField()
    # description = serializers.CharField()
    # body = serializers.CharField()
    # created_at = serializers.CharField(read_only=True)
    # publication_date = serializers.CharField()
    # active = serializers.CharField()
    # updated_at = serializers.CharField(read_only=True)

    # # def __str__(self):
    # #     return f"{self.author}  {self.title}"

    # def create(self, validated_data):
    #     print(validated_data)
    #     return NewsModel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.author = validated_data.get("author", instance.author)
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.description = validated_data.get("description",
    #                                               instance.description)
    #     instance.body = validated_data.get("body", instance.body)
    #     instance.publication_date = validated_data.get(
    #         "publication_date", instance.publication_date)
    #     instance.active = validated_data.get("active", instance.active)
    #     instance.updated_at = validated_data.get(
    #         "updated_at", instance.updated_at)

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        '''check that description and title are different'''
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                "Title and description must be different")
        return data

    def validate_title(self, value):
        '''field validations'''
        if len(value) < 30:
            raise serializers.ValidationError(
                "itle must have more than 30 characters")
        return value


class JournalistSerializer(serializers.ModelSerializer):

    news = NewsSerializer(read_only=True, many=True)

    class Meta:
        model = Journalist
        fields = "__all__"
