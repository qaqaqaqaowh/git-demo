import peewee as pw
from database import db

class User(pw.Model):
	username = pw.CharField(null=False)

	class Meta:
		database = db
		legacy_table_names = False