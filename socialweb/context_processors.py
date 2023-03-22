from api.models import Posts,Comments

def activity(request):
    if request.user.is_authenticated:
        pcnt=Posts.objects.filter(user=request.user).count
        ccnt=Comments.objects.filter(user=request.user).count
        tcnt=Comments.objects.filter(upvote=request.user).count
        return{"pcount":pcnt,"ccount":ccnt,"totalup":tcnt}
    else:
        return{"pcount":0,"ccount":0,"totalup":0}