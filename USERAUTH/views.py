from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm



@login_required



def profile(request):
    u_form =UserUpdateForm()
    p_form =ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'Users/profile.html', context)


def edit_profile(request):
    if request.method =='POST':
        name = request.POST.get('name')

        profile = Profile()
        profile.name = name
        profile.user = request.user
        profile.save()

        return render(request, 'Users/profile.html',{'Users/profile':profile, 'message': 'Profile saved successfully'})
    
