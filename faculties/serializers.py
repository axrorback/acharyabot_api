from rest_framework import serializers

from .models import Faculty


class LanguageMixin:
    def get_language(self):
        request = self.context.get("request")

        if not request:
            return "uz"

        lang = request.query_params.get("lang", "uz")

        if lang not in ["uz", "en", "ru"]:
            lang = "uz"

        return lang


class FacultyListSerializer(LanguageMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = (
            "id",
            "slug",
            "title",
        )

    def get_title(self, obj):
        lang = self.get_language()
        return getattr(obj, f"title_{lang}")


class FacultyDetailSerializer(LanguageMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = (
            "id",
            "slug",
            "title",
            "description",
            "image",
            "created_at",
        )

    def get_title(self, obj):
        lang = self.get_language()
        return getattr(obj, f"title_{lang}")

    def get_description(self, obj):
        lang = self.get_language()
        return getattr(obj, f"description_{lang}")