# Generated by Django 4.2.7 on 2024-03-04 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message_body',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
    ]
