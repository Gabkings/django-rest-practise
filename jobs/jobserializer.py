from rest_framework import serializers
from .models import JobsModel
from datetime import datetime
from django.utils.timesince import timesince
from django.core.validators import validate_email


class JobsSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = JobsModel
        exclude = ("id",)

    def get_time_since_publication(self, object):
        publication_date = object.createdAt
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate_job_title(self, value):
        '''field validations'''
        if len(value) < 20:
            raise serializers.ValidationError(
                "itle must have more than 20 characters")
        return value

    def validate_company_email(self, value):
        '''email validations '''
        try:
            validate_email(value)
            valid_email = True
            return valid_email
        except validate_email.ValidationError:
            valid_email = False
        
