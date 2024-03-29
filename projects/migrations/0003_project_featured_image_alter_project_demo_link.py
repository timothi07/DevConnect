# Generated by Django 5.0.1 on 2024-03-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, default='default.jpg', max_length=2000, null=True),
        ),
    ]
