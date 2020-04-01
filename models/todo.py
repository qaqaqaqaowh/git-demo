import peewee as pw
from database import db

class Todo(pw.Model):
	todo = pw.CharField(null=False)
	completed = pw.BooleanField(default=False)

	class Meta:
		database = db
		legacy_table_names = False