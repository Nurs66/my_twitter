from rest_framework import serializers

from ..models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)  # write only
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + "ago"
