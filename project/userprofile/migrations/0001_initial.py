# Generated by Django 4.0.5 on 2022-07-30 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('fullName', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('profileimg', models.ImageField(default='profile.png', upload_to='profile_images')),
                ('backgroundimg', models.ImageField(default='images/profile.png', upload_to='backgroundimg_images')),
                ('email', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
