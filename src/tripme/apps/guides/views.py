from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from guides.models import *
from guides.forms import GuideForm

@login_required
def create_guide(request):
    '''
    The view for creating a new guide

    :param request: a handle to the main request
    '''
    if request.method == 'POST':
        guide = Guide(user=request.user)
        form = GuideForm(request.POST, instance=guide)
        
        if form.is_valid():
            guide = form.save()
            return HttpResponseRedirect('/guides/%s/' % guide.id)
    else:
        form = GuideForm()
    return render_to_response('guides/create_guide.html',
        { 'form': form, },
        context_instance=RequestContext(request))

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

def guide_detail_spots(request, id, city):
    '''
    The view for retrieving detail about a given guide

    :param request: a handle to the main request
    :param id: the unique key for this guide
    '''
    guide = get_object_or_404(Guide, id=id)
    location = guide.entries.get(id=city)
    view  = 'guides/guide_detail_entry.html'
    if request.user == guide.user:
        view  = 'guides/edit_guide_entry.html'
    return render_to_response(view,
        { 'guide' : guide, 'location' : location },
        context_instance=RequestContext(request))

