from django.urls import path

urlpatterns = [
    path(r'sudo/', 'sudo.views.sudo', name='sudo'),
]
