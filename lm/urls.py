from rest_framework.routers import SimpleRouter
from lm.views import LearningVieSet
from lm.apps import LmConfig

app_name = LmConfig.name

router = SimpleRouter()
router.register("", LearningVieSet)

urlpatterns = []

urlpatterns += router.urls
