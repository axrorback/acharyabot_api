from rest_framework import serializers
from .models import FAQ


class FAQListSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = (
            "id",
            "question",
        )

    def get_question(self, obj):
        lang = self.context["request"].query_params.get(
            "lang",
            "uz"
        )

        return getattr(
            obj,
            f"question_{lang}"
        )
class FAQDetailSerializer(serializers.ModelSerializer):
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
        lang = self.context["request"].query_params.get(
            "lang",
            "uz"
        )

        return getattr(
            obj,
            f"question_{lang}"
        )

    def get_answer(self, obj):
        lang = self.context["request"].query_params.get(
            "lang",
            "uz"
        )

        return getattr(
            obj,
            f"answer_{lang}"
        )
