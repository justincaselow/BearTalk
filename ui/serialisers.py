from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()#format="%Y-%m-%d %H:%M:%S")
    message = serializers.CharField()
    bearId = serializers.CharField()
