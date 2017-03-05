from google.appengine.ext import db

class KvData(db.Model):
    key_id = db.StringProperty(required=True)
    value = db.StringProperty()
