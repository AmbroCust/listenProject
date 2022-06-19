# Generated by Django 4.0.5 on 2022-06-17 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_author', models.CharField(default='user1', max_length=50)),
                ('song_title', models.CharField(max_length=50)),
                ('song_image', models.FileField(upload_to='spotify/images')),
                ('audio', models.FileField(upload_to='spotify/audio')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]