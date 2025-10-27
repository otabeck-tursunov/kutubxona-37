from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', index_view),
    path('talabalar/', talabalar_view),
    path('talabalar/<int:talaba_id>/', talaba_retrieve_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('talabalar/<int:talaba_id>/delete/confirm/', talaba_delete_confirm_view),
    path('mualliflar/', mualliflar_view),
]
