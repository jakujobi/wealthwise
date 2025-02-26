from django.urls import path
from .views import redirect_to_blog

urlpatterns = [
    path('blog/', redirect_to_blog, name='redirect_to_blog'),
]
