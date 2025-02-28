from rest_framework.viewsets import ModelViewSet

from lm.models import Learning
from lm.paginations import CustomPagination
from lm.serializers import LearningSerializer
from users.permissions import IsOwner


class LearningVieSet(ModelViewSet):
    """CRUD для Learning."""

    queryset = Learning.objects.all()
    serializer_class = LearningSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """Метод для управления созданием объекта и автом привязки созд. объекта к авторизованному пользователю."""
        lm = serializer.save()
        lm.owner = self.request.user
        lm.save()

    def get_permissions(self):
        """Метод определения действий в зависимости от того, является ли пользователь владельцем."""
        if self.action in ["update", "retrieve", "destroy"]:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()
