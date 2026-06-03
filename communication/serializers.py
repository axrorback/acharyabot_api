from rest_framework import serializers

from .models import FAQ


class LanguageMixin:
    def get_language(self):
        request = self.context.get("request")

        if not request:
            return "uz"

        lang = request.query_params.get("lang", "uz")

        if lang not in ["uz", "en", "ru"]:
            lang = "uz"

        return lang


class FAQListSerializer(LanguageMixin, serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = (
            "id",
            "question",
        )

    def get_question(self, obj):
        lang = self.get_language()
        return getattr(obj, f"question_{lang}")


class FAQDetailSerializer(LanguageMixin, serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = (
            "id",
            "question",
            "answer",
        )

    def get_question(self, obj):
        lang = self.get_language()
        return getattr(obj, f"question_{lang}")

    def get_answer(self, obj):
        lang = self.get_language()
        return getattr(obj, f"answer_{lang}")