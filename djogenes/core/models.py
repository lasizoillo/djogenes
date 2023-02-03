from django.db import models
from django_softdelete.models import SoftDeleteModel


class Container(models.Model):
    """
    Represents where `Item` is stored.
    """
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=15, blank=True)

    def __str__(self):
        parents = [self.name]
        parent = self.parent
        while parent is not None:
            parents.append(parent.name)
            parent = parent.parent
        return " > ".join(parents[::-1])

    class Meta:
        unique_together = [
            ["name", "parent"],
        ]


class Kind(models.Model):
    """
    Taxonomy to categorize what kind of thing is a `Item`
    """
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        parents = [self.name]
        parent = self.parent
        while parent is not None:
            parents.append(parent.name)
            parent = parent.parent
        return " > ".join(parents[::-1])


class Item(SoftDeleteModel):
    """
    Represent physical objects that belong to me.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    container = models.ForeignKey(
        "Container", null=True, related_name="items", on_delete=models.SET_NULL
    )
    kind = models.ForeignKey("Kind", null=True, related_name="items", on_delete=models.SET_NULL)


class ItemPhoto(models.Model):
    """
    Store images of `Item` elements.
    """
    item = models.ForeignKey("Item", related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="item_photo/")
    caption = models.TextField(blank=True)

    class Meta:
        order_with_respect_to = "item"



