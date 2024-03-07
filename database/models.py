from .db import db

class Tenant(db.Document):
    name = db.StringField()

class ProjectMetadata(db.Document):
    tenant= db.ReferenceField(Tenant)
    csv_location = db.StringField()
    s3_location = db.StringField()
    results = db.DictField()
