from twit_app.models.tweet_model import Tweet
from twit_app.models.user_model import User

class TestTweetTable:
    __tablename__ = 'tweet'

    __table__ = Tweet

    __fields__ = [
        {
            "name": "id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "text",
            "type": "TEXT",
            "primary_key": False,
            "nullable": True
        },
        {
            "name": "embedding",
            "type": "BLOB",
            "primary_key": False,
            "nullable": True
        },
        {
            "name": "user_id",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_session):
        db = db_session
        metadata = db.metadata

        assert metadata.tables.get(self.__tablename__, None) is not None

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']

class TestUserTable:
    __tablename__ = 'user'

    __table__ = User

    __fields__ = [
        {
            "name": "id",
            "type": "INTEGER",
            "primary_key": True,
            "nullable": False
        },
        {
            "name": "username",
            "type": "VARCHAR(64)",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "full_name",
            "type": "VARCHAR(64)",
            "primary_key": False,
            "nullable": False
        },
        {
            "name": "followers",
            "type": "INTEGER",
            "primary_key": False,
            "nullable": True
        }
    ]

    def test_table_exists(self, db_session):
        db = db_session
        metadata = db.metadata

        assert metadata.tables.get(self.__tablename__, None) is not None

    def test_fields(self):
        for field in self.__fields__:
            field_attr = object.__getattribute__(self.__table__, field['name'])
            assert str(field_attr.type) == field['type']
            assert field_attr.primary_key == field['primary_key']
            assert field_attr.nullable == field['nullable']
