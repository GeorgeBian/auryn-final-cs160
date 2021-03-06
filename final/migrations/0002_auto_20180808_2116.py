# Generated by Django 2.1 on 2018-08-08 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map_Q',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('q_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.Activity')),
            ],
        ),
        migrations.DeleteModel(
            name='Map',
        ),
        migrations.AlterField(
            model_name='answers',
            name='q_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.Activity'),
        ),
        migrations.AlterField(
            model_name='files',
            name='q_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='final.Activity'),
        ),
    ]
