# Generated by Django 4.1 on 2022-11-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_alter_expense_options_alter_expense_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("Self_care", "Self_care"),
                    ("Health_and_fitnes", "Health_and_fitnes"),
                    ("Cafes_and_restaurants", "Cafes_and_restaurants"),
                    ("Car", "Car"),
                    ("Education", "Education"),
                    ("Recreation_and_entertainment", "Recreation_and_entertainment"),
                    ("Payments_commissions", "Payments_commissions"),
                    ("Shopping: clothes, appliances", "Shopping: clothes, appliances"),
                    ("Products", "Products"),
                    ("Directions", "Directions"),
                ],
                max_length=255,
            ),
        ),
    ]
