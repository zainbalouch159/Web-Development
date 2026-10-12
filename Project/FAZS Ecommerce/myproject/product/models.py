from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.conf import settings
import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


def compress_image(image_field, max_size=1000, quality=80):
    img = Image.open(image_field)
    img.load()
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    img.thumbnail((max_size, max_size))
    buffer = BytesIO()
    img.save(buffer, format="WEBP", quality=quality)
    name = os.path.splitext(os.path.basename(image_field.name))[0] + ".webp"
    return name, ContentFile(buffer.getvalue())

def make_unique_slug(instance, source):
    base = slugify(source) or "item"
    model = instance.__class__
    slug = base
    n = 2
    while model.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
        slug = f"{base}-{n}"
        n += 1
    return slug


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Collection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

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
    image = models.ImageField(upload_to="products/", blank=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        blank=True,
        null=True
    )
    info = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    collections = models.ManyToManyField(
        Collection,
        blank=True
    )

    @property
    def final_price(self):
        percent = min(self.discount or 0, 100)
        if percent <= 0:
            return self.price
        return self.price * (100 - percent) // 100

    @property
    def has_discount(self):
        return bool(self.discount) and self.discount > 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Hero(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="hero/", blank=True)
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
    
    def save(self, *args, **kwargs):
        if self.image and not self.image._committed:
            name, content = compress_image(self.image, max_size=1400)
            self.image.save(name, content, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or f"Hero {self.pk}"


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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cart", "product"],
                name="unique_product_per_cart",
            )
        ]

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
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    product_name = models.CharField(max_length=100, blank=True)

    quantity = models.PositiveIntegerField()

    price = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = make_unique_slug(self, self.name)

        if self.image and not self.image._committed:
            name, content = compress_image(self.image)
            self.image.save(name, content, save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name or 'Deleted product'} × {self.quantity}"
    
    