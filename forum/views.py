from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView


from .models import Topic, TopicHide, TopicOverdue

from datetime import datetime, timedelta



@login_required()
def index(request):
    return render(request, 'forum/index_dashboard.html', )

@login_required()
def read_topic(request):
    recent_times = request.session.get('recent_times')
    hours = 0
    minute = 0
    
    if (recent_times != None and recent_times != ''):
        split_recent_times = recent_times.split(':')
        hours = int(split_recent_times[0])    
        minute = int(split_recent_times[1])
   
    hide_ads = TopicHide.objects.filter(user=request.user).values('topic_item')
    oeverdue_ads = TopicOverdue.objects.filter(user=request.user).values('topic_item')
    list_topic =  Topic.objects.exclude(id__in=hide_ads)

    delta = datetime.now() - timedelta(hours=hours, minutes = minute)
    if (recent_times == ''):
        list_topic = list_topic.filter().exclude(id__in=oeverdue_ads)
    else:
        list_topic = list_topic.filter(time_parsing__gte=delta).exclude(id__in=oeverdue_ads)
    
     
    paginator = Paginator(list_topic, 50)
    page = request.GET.get('page')
    try:
        list_topic = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list_topic = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list_topic = paginator.page(paginator.num_pages)

    return render(request, 'forum/advert_table.html', {'list_topic': list_topic, 'recent_times' : recent_times })

@login_required()
def action_topic(request):
    if request.method == 'POST':
        pointer_user = request.POST.getlist('pointer_user[]')
        for item in pointer_user:
            ads = Topic.objects.get(id=int(item)) 
            hide = TopicHide(user = request.user, topic_item = ads, )
            hide.save()
 
    return redirect('/topic/')


@login_required()
def SetFilter(request):
     recent_times = request.POST.get('recent_times', '')

     request.session['recent_times'] = recent_times

     return redirect('/topic/')












