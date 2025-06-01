from django.db import models

class MasterTable(models.Model):
    stock_name = models.CharField(max_length=255, blank=False)
    constant_name = models.CharField(max_length=255, unique=True, blank=False)
    stock_table = models.CharField(max_length=255, unique=True, blank=True)
    option_table = models.CharField(max_length=255, unique=True, blank=True)
    token_id = models.IntegerField(unique=False, blank=False)
    time_frame = models.CharField(max_length=255, default="1d")
    is_stock_active = models.BooleanField(default=False, blank=False)
    is_option_active = models.BooleanField(default=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.stock_name:
            self.stock_name = f"STOCK_{self.token_id}"
        self.last_modified = models.DateTimeField(auto_now=True)
        self.option_table = f"OPTION_{self.stock_name}".upper() + "_"+str(self.token_id)
        self.stock_table = f"STOCK_{self.stock_name}".upper() + "_"+str(self.token_id)
        if not self.constant_name:
            self.constant_name = f"CONSTANT_{self.stock_name}".upper()
        super(MasterTable, self).save(*args, **kwargs)

     
    def __str__(self):
        return self.table_name

class AuditTable(models.Model):
    master_table = models.ForeignKey(MasterTable, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
