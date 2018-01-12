from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from second_task.models import UserModel, RolesModel, Base


class BaseTest(TestCase):

    engine = create_engine('sqlite:///test.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.session.add(UserModel("TestLogin", "TestPassword", False))
        self.session.add_all([RolesModel("Employee"), RolesModel("Manager"), RolesModel("Director")])
        self.session.commit()

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

