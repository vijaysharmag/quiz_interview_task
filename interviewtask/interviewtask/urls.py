from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView

admin.site.site_title = "Interviewtask Administration"
admin.site.site_header = "Interviewtask Administration"

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/v1/employee/', include('crud.urls')),
    path('api/v1/user/', include('user.urls'), name='user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    prefix_default_language=False
)

handler404 = 'interviewtask.views.handler404'
handler500 = 'interviewtask.views.handler500'

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
        path('500/', TemplateView.as_view(template_name='500.html'), name='500'),
    ]

    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
