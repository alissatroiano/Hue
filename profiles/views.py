from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def profile(request):
    """ 
    Display the user's profile 
    """
    profile = get_object_or_404(Profile, user=request.user)
    
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
