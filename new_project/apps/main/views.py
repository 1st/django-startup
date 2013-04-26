# -*- coding: utf-8 -*-
'''
List of project specific views, that can't be placed in a separate application.
'''
from libs.project.decorators import render_to


@render_to('main/index.html')
def index(request):
    '''Main page of website'''
    return {'say': 'Hello!'}
