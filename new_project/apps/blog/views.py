# -*- coding: utf-8 -*-
'''
List of application specific views.

Replace "new_app" to your application name.
'''
from libs.project.decorators import render_to
from apps.blog.models import BlogPostModel


@render_to('blog/index.html')
def index(request):
    '''Main page of website'''
    posts = BlogPostModel.objects.all()
    return {'posts': posts}
