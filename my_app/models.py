from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Category"

    class Meta:
        verbose_name_plural = "Categories"

# Sample model for testing
class GeeksModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Position model
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'position'
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.position_name

# Staff model with gender, name, DOB, and position FK
class Staff(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, db_column='position_id')

    class Meta:
        db_table = 'staff'
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
