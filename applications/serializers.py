from rest_framework import serializers
from .models import Application , ApplicationDocument


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = (
            "application_number",
            "status",
            "created_at",
        )

class ApplicationDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicationDocument
        fields = "__all__"