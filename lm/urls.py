from rest_framework.routers import SimpleRouter

from lm.apps import LmConfig
from lm.views import LearningVieSet

app_name = LmConfig.name

router = SimpleRouter()
router.register("", LearningVieSet)

urlpatterns = []

urlpatterns += router.urls
