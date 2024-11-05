from django.shortcuts import render
from .models import Story


from django.shortcuts import render, redirect
from .models import Story
from django.contrib.auth.decorators import login_required

@login_required
def addstory(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            Story.objects.create(user=request.user, image=image)
            return redirect('home')  # Redirect to a success page or another view
    return render(request, 'story/addstory.html')

from django.utils import timezone
from django.shortcuts import redirect
from .models import Story
from django.shortcuts import get_object_or_404

@login_required
def latest_story(request):
    now = timezone.now()
    latest_story = Story.objects.filter(
        user=request.user,
        date__gte=now - timezone.timedelta(hours=24)
    ).order_by('-date').first()

    if latest_story:
        # Redirect with the story ID as a query parameter
        return redirect(f'/home/?story_id={latest_story.story_id}')
    else:
        return redirect('home')

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Story

@login_required
def delete_story(request, story_id):
    # Ensure the story belongs to the request.user
    story = get_object_or_404(Story, story_id=story_id, user=request.user)
    if request.method == 'POST':
        story.delete()
        return redirect('home')  
    return HttpResponse(status=405)  
