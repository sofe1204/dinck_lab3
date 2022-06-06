# Generated by Django 4.0.5 on 2022-06-05 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogPost', '0002_user_interests_user_name_user_profession_user_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blocked_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogPost.user'),
        ),
        migrations.AddField(
            model_name='commentar',
            name='author_com',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='blog_files/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocked_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_user', to='BlogPost.user')),
                ('other_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_user', to='BlogPost.user')),
            ],
        ),
    ]
