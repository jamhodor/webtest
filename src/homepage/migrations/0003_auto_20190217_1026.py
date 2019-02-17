# Generated by Django 2.1.3 on 2019-02-17 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_testmodel_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='blogpics')),
            ],
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='pictures',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.TestModel'),
        ),
    ]
