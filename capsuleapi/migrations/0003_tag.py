# Generated by Django 4.1.3 on 2023-10-01 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capsuleapi', '0002_capsuleuser_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capsuleUser', to='capsuleapi.capsuleuser')),
            ],
        ),
    ]