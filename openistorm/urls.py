from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
# from .views import ApiEndpoint
from django.contrib.auth import views as authViews
from oauth2_provider import views as oauthViews
# from django.urls import reverse_lazy
# from .views import ProfileViewSet

# app_name = 'oauth'

urlpatterns = [
    url(r'oauth/', include('openistorm.oauth.urls')),
    url(r'openistorm/favorites/', include('openistorm.favorites.urls'), name='favorites'),
    url(r'openistorm/layers/', include('openistorm.layers.urls'), name='imagelayers'),
    url(r'openistorm/notifications/', include('openistorm.notifications.urls'), name='notifications'),
    url(r'openistorm/stations/', include('openistorm.stations.urls'), name='stations'),
    url(r'openistorm/stormevents/', include('openistorm.stormeventsapi.urls'), name='stormeventsapi'),
    url(r'openistorm/settings/', include('openistorm.settings.urls'), name='settings'),
]

# router.register(r'users', UserViewSet)
# urlpatterns = router.urls
