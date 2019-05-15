from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:pk>/dimensions', views.dimension_edit, name='dimension-edit'),
    path('<int:pk>/events', views.get_events, name="get-events"),
    path('<int:pk>/attributes', views.get_attrs, name="get-attrs"),
]