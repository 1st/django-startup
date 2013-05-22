# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import simplejson


def render_to(template):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter.

    Example:
    >>> @render_to('app_name/welcome.html')
    >>> def welcome(request):
    >>>    # ...
    >>>    return {'obj': obj}, 'app_name/please_register.html'
    >>>    # or use default template: return {'obj': obj}

    Parameters:
     - template: template name to use

    @url https://github.com/1st/django-startup/
    @author Anton Danilchenko <anton.danilchenko@me.com>
    """
    def _renderer(func):
        def _wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return _wrapper
    return _renderer


def ajax_request(func):
    """
    AJAX request decorator

    Example:
    >>> @ajax_request
    >>> def my_view(request):
    >>>     return {'key': 'value', 'key2': 'value2'}

    @url https://github.com/1st/django-startup/
    @author Anton Danilchenko <anton.danilchenko@me.com>
    """
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        context = func(request, *args, **kwargs)
        return HttpResponse(simplejson.dumps(context), mimetype='application/json')

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap


def login_required(function=None, message=None):
    """
    Decorator for views that checks that the user is logged in,
    or show error page with message.

    Example (we can use any of this forms of decorator):
    >>> # 1. without parameters
    >>> @login_required
    >>> def my_function(request):
    >>>     pass
    >>>
    >>> # 2. with parameters
    >>> @login_required(message='This page available only for logged in users')
    >>> def my_function(request):
    >>>     pass

    @url https://github.com/1st/django-startup/
    @author Anton Danilchenko <anton.danilchenko@me.com>
    """
    def real_decorator(func):
        def _wrapper(request, *args, **kwargs):
            if request.user.is_authenticated():
                return func(request, *args, **kwargs)
            raise Http404(message)
        return _wrapper

    if function:
        return real_decorator(function)
    return real_decorator
