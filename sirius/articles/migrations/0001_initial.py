# Generated by Django 2.1.7 on 2019-03-02 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('article_type', models.CharField(choices=[('AD', 'Analyzed Data'), ('PO', 'Poster'), ('RD', 'Raw Data'), ('RE', 'Report'), ('OT', 'Other')], max_length=2)),
                ('description', models.TextField(blank=True, max_length=512)),
                ('subject', models.CharField(choices=[('BI', 'Biology'), ('CH', 'Chemistry'), ('CE', 'Civil Engineering'), ('EN', 'Environmental Studies'), ('GE', 'Geology')], max_length=2)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_media', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='articles.Article')),
            ],
        ),
    ]
