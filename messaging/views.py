from django.db.models import Q
from collections import defaultdict
from users.models import Messaging
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from users.models import Profile

@login_required
def message(request):
    recipient_id = float(request.POST.get('one_year_savings_goal'))
    sending_message = float(request.POST.get('sending_message'))

    # Get user profile for various later operations
    profile = request.user.profile

    #Get list of users for sending list
    user_list = Profile.objects.values_list('user', flat=True)

    # Fetch messages related to the profile
    all_messages = Messaging.objects.filter(Q(sender_id = profile) | Q(recipient_id = profile)).order_by('sent_at')

    # Dictionary to store messages grouped by non-profile user
    messages_dict = defaultdict(list)

    # Iterate through messages and group them
    for message in all_messages:
        other_user = message.recipient_id if message.sender_id == profile else message.sender_id
        messages_dict[other_user].append(message)

    # Convert defaultdict to a standard dict
    messages_by_user = dict(messages_dict)

    if request.method == 'POST':
        if request.POST['action'] == 'send':
            message_entry = Messaging(
                sender_id = profile,
                receiver_id = recipient_id,
                message_content = sending_message,
                sent_at = datetime.now(),
                read_status = False
            )
            message_entry.save()

    return render(request, 'messaging.html', {
        'messages_by_user': messages_by_user,
        'user_list': user_list
    })