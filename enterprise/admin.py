from django.contrib import admin

from enterprise.models import Enterprise, Commodity, ProductCategory, District, Product, EnterpriseNetwork


class CommodityInline(admin.TabularInline):
    model = Commodity
    extra = 0


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_display = [
        'title',
        'description',
    ]
    inlines = [
        CommodityInline
    ]
    filter_horizontal = [
        'district',
    ]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(EnterpriseNetwork)
class EnterpriseNetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
    ]
