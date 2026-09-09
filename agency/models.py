from django.db import models


class HeroContent(models.Model):
    tagline = models.CharField(max_length=100, default="Digital Product Studio")
    main_headline = models.CharField(max_length=200, default="We design and build products that")
    highlighted_word = models.CharField(
        max_length=100,
        default="matter.",
        help_text="The italicized word at the end"
    )
    description = models.TextField(
        default="We partner with forward-thinking teams to craft exceptional web and mobile experiences."
    )
    primary_button = models.CharField(max_length=50, default="Start a project")
    secondary_button = models.CharField(max_length=50, default="View our work")

    def __str__(self):
        return "Home Page Hero Settings"


class ValueProposition(models.Model):
    icon = models.CharField(max_length=10, help_text="Emoji or icon")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):
    CATEGORY_CHOICES = [
        ("Web", "Web"),
        ("App", "App"),
        ("E-commerce", "E-commerce"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    is_featured = models.BooleanField(
        default=False,
        help_text="Check this to show on the home page"
    )

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.CharField(max_length=10, help_text="Emoji or icon class")
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_price = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    initials = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    order = models.IntegerField(
        default=0,
        help_text="Order in which they appear"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


# Update this specific model in agency/models.py
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, default="") # <-- ADD THIS LINE
    project_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


class Stat(models.Model):
    value = models.CharField(
        max_length=20,
        help_text="e.g., '8 yrs', '120+', '96%'"
    )
    label = models.CharField(
        max_length=100,
        help_text="e.g., 'In business', 'Projects shipped'"
    )
    order = models.IntegerField(
        default=0,
        help_text="Order in which they appear"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} - {self.label}"


class ContactPageSettings(models.Model):
    heading = models.CharField(
        max_length=200,
        default="Tell us about your project"
    )
    subheading = models.TextField(
        default="Fill out the form and we'll reply within one business day, or reach us directly below."
    )
    email_address = models.EmailField(
        default="hello@curiositymatters.studio"
    )
    phone_number = models.CharField(
        max_length=20,
        default="+91 98765 43210"
    )
    location = models.CharField(
        max_length=100,
        default="Mumbai, India"
    )

    class Meta:
        verbose_name = "Contact Page Setting"
        verbose_name_plural = "Contact Page Settings"

    def __str__(self):
        return "Contact Page Content Settings"