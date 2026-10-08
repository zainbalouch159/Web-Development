from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField( blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Collection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField( blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField( blank=True)

    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    sales = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        null=True
    )
    image = models.ImageField(blank=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        blank=True,
        null=True
    )
    info = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=1,
        blank=True
    )

    collections = models.ManyToManyField(
        Collection,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Hero(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(blank=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        blank=True,
        null=True
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    bg_color = models.CharField(
        max_length=7,
        default="#FFB86A",
        blank=True
    )
    font_btn_color = models.CharField(
        max_length=7,
        default="#FF6900",
        blank=True
    )
    
class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.user.username}'s Cart"
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    total_amount = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"