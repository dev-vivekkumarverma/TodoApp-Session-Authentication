from django.urls import path
from .views import taskViewSet,taskSearchView,taskUpdateView

urlpatterns = [
    path('',taskViewSet.as_view()),
    path('search/<str:onDate>',taskSearchView.as_view()),
    path('update/<int:id>',taskUpdateView.as_view()),
]
