from django.db import models




class machine_data(models.Model):
	machine_name = models.CharField(max_length=16)
	unit_no = models.IntegerField(default=0)
	#ship_date = models.DateField()
	drying_time = models.IntegerField(default=0)
	run_count = models.IntegerField(default=0)
	run_time_m = models.IntegerField(default=0)
	run_time_s = models.IntegerField(default=0)
	gas_usage = models.IntegerField(default=0)
	date_m = models.IntegerField(default=0)
	date_d = models.IntegerField(default=0)

	def __str__(self):
		return '<machine_data:id=' + str(self.id) + ',' + \
		self.machine_name + '(' + str(self.unit_no) + ')>'
# Create your models here.
