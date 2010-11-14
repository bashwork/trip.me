from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from guides.models import City,Spot

# -------------------------------------------------------- #
# logged in views
# -------------------------------------------------------- #
@login_required
def example_view(request):
    pass
