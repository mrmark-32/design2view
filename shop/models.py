from django.db import models
from django.utils.text import slugify

# ==========================================
# 1. CATEGORY MODEL
# ==========================================
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    image = models.ImageField(upload_to='categories/', default='categories/default.webp')
    
    description = models.TextField(blank=True, null=True, help_text="Detailed description of this specific treatment.")
    
    highlight_1 = models.CharField(max_length=255, default="Custom built sizing explicitly engineered around your window configurations.", help_text="First bullet point highlight")
    highlight_2 = models.CharField(max_length=255, default="Premium luxury durability optimized for smooth everyday deployment tracking.", help_text="Second bullet point highlight")
    highlight_3 = models.CharField(max_length=255, default="Advanced protection safeguards blocking harmful UV fading exposure.", help_text="Third bullet point highlight")

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text="Uncheck this to hide the category from the website.")

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ==========================================
# 2. NAV ITEM MODEL
# ==========================================
class NavItem(models.Model):
    title = models.CharField(max_length=50, help_text="e.g., About Us, Fabrics")
    url_name = models.CharField(max_length=100, default="#", help_text="Named URL pattern or target route hash")
    order = models.PositiveIntegerField(default=0, help_text="Controls sorting order position")
    is_premium_highlight = models.BooleanField(default=False)
    
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name='children',
        help_text="Leave blank if this is a main, top-level menu item"
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} → {self.title}"
        return self.title


# ==========================================
# 3. FABRIC TYPE MODEL (ONLY ONE COPY)
# ==========================================
class FabricType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='fabrics')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fabrics/', default='fabrics/default.webp') # Primary cover thumbnail
    description = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Controls sorting display order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.category.name} — {self.name}"


# ==========================================
# 4. FABRIC IMAGE GALLERY MODEL
# ==========================================
class FabricImage(models.Model):
    fabric = models.ForeignKey(FabricType, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='fabrics/gallery/', help_text="Upload additional style or swatch images.")
    alt_text = models.CharField(max_length=150, blank=True, help_text="Optional description for accessibility and SEO.")
    order = models.PositiveIntegerField(default=0, help_text="Controls order of appearance.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Gallery Image for {self.fabric.name} (#{self.id})"


# ==========================================
# 5. FABRIC OPTIONAL DETAILS MODELS
# ==========================================
class FabricFeature(models.Model):
    fabric = models.ForeignKey(FabricType, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100, help_text="e.g., Solar Protection, Glare Control")
    image = models.ImageField(upload_to='fabrics/features/', default='fabrics/features/default.webp')
    description = models.TextField(help_text="Short detail explaining this design perk.")

    def __str__(self):
        return f"{self.fabric.name} - {self.name}"

class WhyChooseUsReason(models.Model):
    fabric = models.ForeignKey(FabricType, on_delete=models.CASCADE, related_name='reasons')
    title = models.CharField(max_length=150, help_text="e.g., Expert Craftsmanship, Perfect Fit")
    details = models.TextField(help_text="Detailed value proposition explanation.")

    def __str__(self):
        return f"{self.fabric.name} Trust Factor - {self.title}"