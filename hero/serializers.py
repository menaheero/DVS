from main.models import VideoPost, UserData, Comment
from rest_framework import serializers as serializers
class VideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'
        read_only_fields = ('user', 'pub_date', 'count', 'video_views')


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
        read_only_fields = ('user',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
        depth = 1
        # depth = 1 means that the serializer will include the user field in the serialized data.
        # This is useful when you want to display the user's name instead of their ID.
        # The user field is a one-to-one field, so it will be included in the serialized data.
        # The user field is not a foreign key, so it will not be included in the serialized data.
        # The user field is not a many-to-many field, so it will not be included in the serialized data.
        # The user field is not a one-to-many field, so it will not be included in the serialized data.
        # The user field is not a many-to-one field, so it will not be included in the serialized data.
        # The user field is not a many-to-many field, so it will not be included in the serialized data.
        # The user field is not a one-to-one field, so it will not be included in the serialized data.
        # The user field is not a one-to-many field, so it will not be included in the serialized data.
        # The user field is not a many-to-one field, so it will not be included in the serialized data.
        # The user field is not a many-to-many field, so it will not be included in the serialized data.
        # The user field is not a one-to-one field, so it will not be included in the serialized data.
        # The user field is not a one-to-many field, so it will not be included in the serialized data.
        # The user field is not a many-to-one field, so it will not be included in the serialized data.
        # The user field is not a many-to-many field, so it will not be included in the serialized data.
        # The user field is not a one-to-one field, so it will not be included in the serialized data.

        