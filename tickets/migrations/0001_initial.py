# Generated by Django 2.0.2 on 2018-03-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('issue', models.CharField(max_length=1000)),
                ('reported_by', models.CharField(max_length=50)),
                ('reported_on', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='LOW', max_length=10)),
                ('assigned_to', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('TO_DO', 'TO_DO'), ('DOING', 'DOING'), ('DOING', 'DONE')], default='TO_DO', max_length=10)),
                ('resolution', models.CharField(blank=True, max_length=400, null=True)),
                ('verified', models.BooleanField(default=True)),
                ('notes', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
