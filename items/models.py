from django.db import models
from django.core.validators import RegexValidator


class Item(models.Model):
    """
    Model representing free item
    """

    # Define choices for Category, Condition and Delivery fields
    CATEGORY_CHOICES = [
        ('Toys', 'Toys'),
        ('Books', 'Books'),
        ('Baby and Kids stuff', 'Baby and Kids stuff'),
        ('Furniture', 'Furniture'),
        ('Kitchen and Home Appliance', 'Kitchen and Home Appliance'),
        ('Audio, TV and Photography', 'Audio, TV and Photography'),
        ('Computers and Software', 'Computers and Software'),
        ('Mobile Phones', 'Mobile Phones'),
        ('Bicycles', 'Bicycles'),
        ('Garden and Patio', 'Garden and Patio'),
        ('Video Games and Consoles', 'Video Games and Consoles'),
        ('Car Accessories', 'Car Accessories')
    ]

    CONDITION_CHOICES = [('New', 'New'), ('As Good as New', 'As Good as New'), ('Used', 'Used'), ('Poor', ' Poor')]
    DELIVERY_CHOICES = [('Pick Up Only', 'Pick Up Only'),
                        ('By Post Only', 'By Post Only'),
                        ('Pick Up or by Post', 'Pick Up or by Post')]

    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)
    giver = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=30, choices=CONDITION_CHOICES)
    image = models.ImageField(upload_to='images/')
    delivery = models.CharField(max_length=30, choices=DELIVERY_CHOICES)
    city = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+310000000'. "
                                         "Up to 15 digits allowed.")
    phone = models.CharField(max_length=17, validators=[phone_regex], blank=True)
    email = models.EmailField(max_length=300)
    created_date = models.DateTimeField(auto_now=True)

    # Display items title in django admin instead of "Item Object 1"
    def __str__(self):
        return self.title
