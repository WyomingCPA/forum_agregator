from .models import TopicHide
import datetime


def CountTodayHidden(request):
    try:
        count_today_hidden = TopicHide.objects.filter(user=request.user, time_check__gte=datetime.date.today()).count()
    except:
        count_today_hidden = 0

    return { "count_today_hidden": count_today_hidden }