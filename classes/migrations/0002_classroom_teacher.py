# Generated by Django 2.1.5 on 2019-07-26 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
