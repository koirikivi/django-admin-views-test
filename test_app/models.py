from django.db import models


class UnchangeableModelDependency(models.Model):
    pass


class UnchangeableModel(models.Model):
    dependency = models.ForeignKey(UnchangeableModelDependency)
