from mongoengine import connect, Document, StringField, DictField

connect('urls')


class UrlContentStore(Document):
    content = StringField()
    tag_count_summary = DictField()
    tag_position_summary = DictField()