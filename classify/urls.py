from django.urls import path
from . import views


urlpatterns = [
    path("", views.classify_number_api, name="home"),
    path(
        "api/classify-number",
        views.classify_number_api,
        name="classify_number_api",
    ),
    # path(
    #     "api/classify-number/<int:number>",
    #     views.classify_number_api,
    #     name="classify_number_api",
    # ),
]
