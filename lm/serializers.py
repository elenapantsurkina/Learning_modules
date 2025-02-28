from rest_framework.serializers import ModelSerializer

from lm.models import Learning


class LearningSerializer(ModelSerializer):
    class Meta:
        model = Learning
        fields = "__all__"
