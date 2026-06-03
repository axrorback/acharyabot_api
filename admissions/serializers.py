from rest_framework import serializers

from .models import (
    AdmissionProcess,
    TuitionFee,
    Scholarship,
    Grant,
    RequiredDocument,
)


class LanguageMixin:

    def get_language(self):
        request = self.context.get("request")

        if not request:
            return "uz"

        lang = request.query_params.get("lang", "uz")

        if lang not in ["uz", "en", "ru"]:
            lang = "uz"

        return lang

class AdmissionProcessListSerializer(LanguageMixin,serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = AdmissionProcess
        fields = (
            "id",
            "process_type",
            "title",
        )

    def get_title(self, obj):
        lang = self.get_language()
        return getattr(obj, f"title_{lang}")

class AdmissionProcessDetailSerializer(LanguageMixin,serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        model = AdmissionProcess
        fields = (
            "id",
            "process_type",
            "title",
            "content",
        )

    def get_title(self, obj):
        lang = self.get_language()
        return getattr(obj, f"title_{lang}")

    def get_content(self, obj):
        lang = self.get_language()
        return getattr(obj, f"content_{lang}")

class TuitionFeeSerializer(LanguageMixin,serializers.ModelSerializer):
    faculty_name = serializers.SerializerMethodField()

    class Meta:
        model = TuitionFee
        fields = (
            "id",
            "faculty",
            "faculty_name",
            "national_fee",
            "international_fee",
        )

    def get_faculty_name(self, obj):
        lang = self.get_language()
        return getattr(
            obj.faculty,
            f"title_{lang}"
        )