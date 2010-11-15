from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from guides.models import *

# -------------------------------------------------------- #
# logged in views
# -------------------------------------------------------- #
def guide_detail(request, id):
    '''
    The view for retrieving detail about a given guide

    :param request: a handle to the main request
    :param id: the unique key for this guide
    '''
    guide = get_object_or_404(Guide, id=id)
    view  = 'guides/guide_detail.html'
    if request.user == guide.user:
        view  = 'guides/edit_guide.html'
    return render_to_response(view, { 'guide' : guide },
        context_instance=RequestContext(request))

def guide_detail_spots(request, id):
    '''
    The view for retrieving detail about a given guide

    :param request: a handle to the main request
    :param id: the unique key for this guide
    '''
    guide = get_object_or_404(Guide, id=id)
    view  = 'guides/guide_detail_spot.html'
    if request.user == guide.user:
        view  = 'guides/edit_guide_spot.html'
    return render_to_response(view, { 'guide' : guide },
        context_instance=RequestContext(request))
