# Generated by Django 4.1.4 on 2023-02-28 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='downvote',
            field=models.ManyToManyField(related_name='commentdown', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='upvote',
            field=models.ManyToManyField(related_name='commentup', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='dislike',
            field=models.ManyToManyField(related_name='postdislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(related_name='postlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='place',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
