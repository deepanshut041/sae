# Generated by Django 2.0 on 2018-01-09 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_eventteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreWorkshopMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_detail', models.TextField()),
                ('material_link', models.CharField(default='https://', max_length=200)),
                ('material_name', models.CharField(max_length=100)),
                ('material_img', models.CharField(default='https://', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_link', models.CharField(default='https://', max_length=200)),
                ('material_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Project')),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(editable=False, max_length=30)),
                ('payment_id', models.CharField(editable=False, max_length=200)),
                ('enroll_date', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('leader_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='workshop',
            name='wall_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshopenrollment',
            name='workshop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Workshop'),
        ),
        migrations.AddField(
            model_name='projectmaterial',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Workshop'),
        ),
        migrations.AddField(
            model_name='preworkshopmaterial',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Workshop'),
        ),
    ]