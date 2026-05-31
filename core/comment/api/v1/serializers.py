from rest_framework import serializers
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model = Comment
        fields = ['id','author','post','message','snippet','relative_url','absolute_url','created_date']


    def get_abs_url(self,obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.pk)
        return None