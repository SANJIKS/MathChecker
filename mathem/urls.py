from django.urls import path
from .views import CheckFormula

urlpatterns = [
    path('check/', CheckFormula.as_view())
]