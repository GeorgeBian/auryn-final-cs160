# Generated by Django 2.1 on 2018-08-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0003_remove_map_q_q_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youranswer', models.CharField(max_length=3000)),
            ],
        ),
    ]
