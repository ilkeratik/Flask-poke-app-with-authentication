from mongoengine import Document, StringField, ListField, IntField

class SearchResult(Document):
    name = StringField(required=True)
    description = ListField(StringField())
    status = IntField()
    message = StringField()