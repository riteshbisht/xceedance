from django.conf.urls import url

from django.urls import reverse_lazy
from users.views import CustomFeatureView
urlpatterns = [
    url(r'^$', CustomFeatureView.as_view())
]