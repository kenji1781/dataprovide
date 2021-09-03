from django.db import models




class machine_data(models.Model):
	machine_name = models.CharField(max_length=20)
	unit_no = models.CharField(max_length=80)
	course_no = models.IntegerField(default=0,blank=True,null=True)
	#ship_date = models.DateField()
	drying_time = models.IntegerField(default=0,blank=True,null=True)
	run_count = models.IntegerField(default=0,blank=True,null=True)
	run_time_m = models.IntegerField(default=0,blank=True,null=True)
	run_time_s = models.IntegerField(default=0,blank=True,null=True)
	gas_usage = models.IntegerField(default=0,blank=True,null=True)
	date_y = models.IntegerField(default=0,blank=True,null=True)
	date_m = models.IntegerField(default=0,blank=True,null=True)
	date_d = models.IntegerField(default=0,blank=True,null=True)
	date_ymd = models.DateField(blank=True,null=True)

	def __str__(self):
		return '<machine_data:id=' + str(self.id) + ',' + \
		self.machine_name + '(' + str(self.unit_no) + ')>'
# Create your models here.
