from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="image",null=True)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="postlike")
    dislike=models.ManyToManyField(User,related_name="postdislike")
    def __srt__(self):
        return self.title
    @property
    def post_to_comment(self):
        return Comments.objects.filter(post_name=self).annotate(pcount=Count('upvote')).order_by('-pcount')
class Comments(models.Model):
    comment=models.CharField(max_length=300)
    post_name=models.ForeignKey(Posts,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    upvote=models.ManyToManyField(User,related_name="commentup")
    downvote=models.ManyToManyField(User,related_name="commentdown")
    @property
    def upvote_count(self):
        return self.upvote.all().count()
    
    
    def __str(self):
        return self.comment

class UserProfile(models.Model):
    is_active=models.BooleanField(default=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="images",null=True)
    bio=models.CharField(max_length=200)
    time_line_pic=models.ImageField(upload_to="images",null=True)
    place=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)


