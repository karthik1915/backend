from django.contrib import admin
from .models import ProjectsModal


@admin.register(ProjectsModal)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "href",
        "links",
        "date_created",
    )

    def external_links(self, obj):
        return ", ".join(obj.links) if obj.links else "N/A"

    external_links.short_description = "External Links"
