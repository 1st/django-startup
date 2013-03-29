# -*- coding: utf-8 -*-
'''
List of project specific views, that can't be placed in a separate application.
'''
from apps.decorators import render_to


@render_to('index.html')
def index(request):
    '''Main page of website'''
    return {'say': 'Hello!'}
