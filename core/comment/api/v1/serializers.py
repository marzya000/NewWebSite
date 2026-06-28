from rest_framework import serializers
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "post",
            "message",
            "snippet",
            "relative_url",
            "absolute_url",
            "created_date",
        ]
        read_only_fields = ["author","created_date"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(obj.pk)
        return None

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("message", None)

        return rep

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
