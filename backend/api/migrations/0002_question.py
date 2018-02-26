# Generated by Django 2.0 on 2018-02-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Goal')),
            ],
        ),
    ]
