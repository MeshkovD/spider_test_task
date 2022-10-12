from django.core.validators import MinValueValidator
from django.db import models


class District(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'район'
        verbose_name_plural = 'районы'

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'категория продуктов'
        verbose_name_plural = 'категории продуктов'

    def __str__(self):
        return self.title


class EnterpriseNetwork(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'сеть предприятий'
        verbose_name_plural = 'сети предприятий'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='категория',
        related_name='products',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.title


class Enterprise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    district = models.ManyToManyField(District)
    enterprise_network = models.ForeignKey(
        EnterpriseNetwork,
        verbose_name='сеть предприятия',
        related_name='enterprise_network',
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'производство'
        verbose_name_plural = 'производства'

    def __str__(self):
        return self.title


class Commodity(models.Model):
    enterprise = models.ForeignKey(
        Enterprise,
        verbose_name='предприятие',
        related_name='commodities',
        null=True,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='products',
        null=True,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        unique_together = [
            ['enterprise', 'product']
        ]

    def __str__(self):
        return f"{self.product.title} - {self.price}"
