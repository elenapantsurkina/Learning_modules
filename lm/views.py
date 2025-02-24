from rest_framework.viewsets import ModelViewSet
from lm.models import Learning
from lm.serializers import LearningSerializer


class LearningVieSet(ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer

