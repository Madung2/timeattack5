from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)


class Drink(models.Model):
    class Meta:
        db_table = "drink"
    def __str__(self):
        return self.drink_name
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    drink_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)





