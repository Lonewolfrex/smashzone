from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    user = request.user
    if user.user_type == 'admin':
        # admin-specific context
        context = {'admin_data': 'some admin data'}
    elif user.user_type == 'seller':
        # seller-specific context
        context = {'seller_data': 'some seller data'}
    elif user.user_type == 'player':
        # player-specific context
        context = {'player_data': 'some player data'}
    elif user.user_type == 'organizer':
        # organizer-specific context
        context = {'organizer_data': 'some organizer data'}
    else:
        context = {}

    context['user'] = user
    return render(request, 'dashboard/dashboard.html', context)
