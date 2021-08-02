from django.db import models

class Account(models.Model):
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    objects = models.Manager()

    def __str__(self):
        return f'Username: {self.email}, Password: {self.password}'

class Customer(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    province = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000, null=True)
    number =  models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}: {self.firstname} {self.lastname}, {self.address} {self.city}, {self.email}, {self.number}'

class Food(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return f'{self.id}: {self.name} | Php {self.price}'

class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'),
        ('CD', 'Card')
    ]
    paymentmode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderdatetime = models.DateTimeField(auto_now_add=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.customer.firstname} {self.customer.lastname}, {self.food.name}, {self.quantity}, {self.paymentmode}, {self.orderdatetime}'

    def total_price(self):
        return self.food.price * self.quantity