
from dataclasses import fields
from rest_framework import serializers
from .models import Article, Comments


class FilterCommentSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent = None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
      def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentsSerializer(serializers.ModelSerializer):
    '''"user": 1,'''
    user = serializers.SlugRelatedField('username', read_only=True)
    Comments = RecursiveSerializer(many=True, read_only=True)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Comments.objects.create(**validated_data)


    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments
        fields = ('user', 'body', 'Comments', 'parent', )


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField('username', read_only=True)
    Comments = CommentsSerializer(read_only=False, many=True, required=False)
    #Comments = serializers.SerializerMethodField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Article.objects.create(**validated_data)

    '''def get_comments(self, obj):
        queryset = Comments.objects.filter(post_id=obj.id, parent_id=None)
        serializer = CommentsSerializer(queryset, many=True)
        return serializer.data'''

    class Meta:

        model = Article
        exclude = ("comments", )

