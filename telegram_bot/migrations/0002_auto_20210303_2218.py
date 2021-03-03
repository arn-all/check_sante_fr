# Generated by Django 3.1.7 on 2021-03-03 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('telegram_bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='subscriptions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber',
                                    to='telegram_bot.centre'),
            preserve_default=False,
        ),
    ]