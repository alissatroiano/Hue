from django.conf import settings
from django.http import HttpResponseRedirect,
HttpResponsePermanentRedirect, get_host

SSL = 'SSL'


class SSLRedirect:
    def process_view(self, request, view_func, view_args, view_kwargs):
        if SSL in view_kwargs:
            secure = view_kwargs[SSL]
            del view_kwargs[SSL]
        else:
            secure = False
        if not secure == self._is_secure(request):
            return self._redirect(request, secure)

    def _is_secure(self, request):
        if request.is_secure():
            return True
        if 'HTTP_X_FORWARDED_SSL' in request.META:
            return request.META['HTTP_X_FORWARDED_SSL'] == 'on'
        return False

    def _redirect(self, request, secure):
        protocol = secure and "https" or "http"
        newurl = "%s://%s%s" % (protocol, get_host(request),
                                request.get_full_path())
        if settings.DEBUG and request.method == 'POST':
        	raise RuntimeError, \
        """Django can't perform SSL redirect while maintaining POST data. 
        Redirects should be used for GET requests"""
        return HttpResponsePermanentRedirect(newurl)
  	