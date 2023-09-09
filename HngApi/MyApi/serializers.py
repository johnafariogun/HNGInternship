from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    slack_name = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%SZ')
    track = serializers.CharField()
    github_file_url = serializers.URLField()
    github_repo_url = serializers.URLField()
    status_code = serializers.IntegerField()
