# Generated by Django 3.0.5 on 2020-05-23 00:02

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
            name='BugTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticket_status', models.CharField(choices=[('N', 'New'), ('IP', 'In Progress'), ('D', 'Done'), ('IV', 'Invalid')], default='N', max_length=2)),
                ('assigned_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
                ('finished_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finished_user', to=settings.AUTH_USER_MODEL)),
                ('ticket_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
