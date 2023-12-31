# Generated by Django 4.1.3 on 2023-08-22 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapsuleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('profile_image', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo_url', models.CharField(max_length=500)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='capsuleapi.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsuleapi.capsuleuser')),
            ],
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capsuleapi.capsuleuser')),
            ],
        ),
        migrations.CreateModel(
            name='OutfitItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemId', to='capsuleapi.item')),
                ('outfit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outfitId', to='capsuleapi.outfit')),
            ],
        ),
    ]
