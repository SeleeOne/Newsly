from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.articles_home, name='articles_home'),
    path('<int:pk>', views.fullArticlePageGen.as_view(), name='fullView'),
    path('create', views.create, name='create'),
    path('<int:pk>/edit', views.fullArticlePageEdit.as_view(), name='EditPage'),
    path('<int:pk>/delete', views.fullArticlePageDelete.as_view(), name='DeletePage')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)