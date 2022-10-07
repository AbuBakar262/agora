from django.urls import path
from advocate.views import AdvocateViewSet, CompanyViewSet

urlpatterns = [
    path('advocates/', AdvocateViewSet.as_view({"post": "create_advocate"}), name='advocates'),
    path('advocates/<str:pk>/', AdvocateViewSet.as_view({"get": "list_advocate"}), name='advocates'),
    path('companies/', CompanyViewSet.as_view({"post": "create_company"}), name='companies'),
    path('companies/<str:pk>/', CompanyViewSet.as_view({"get": "list_company"}), name='companies'),
]
