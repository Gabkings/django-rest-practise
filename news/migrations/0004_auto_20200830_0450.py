# Generated by Django 3.1 on 2020-08-30 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200830_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NewsModels', to='news.journalist'),
        ),
    ]