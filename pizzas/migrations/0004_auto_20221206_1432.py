# Generated by Django 3.0.5 on 2022-12-06 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_remove_comments_commentor_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
