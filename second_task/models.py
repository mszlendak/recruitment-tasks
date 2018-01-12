from sqlalchemy import Column, ForeignKey, Integer, String, Boolean , create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



engine = create_engine('sqlite:///test.db')
Base = declarative_base()

BDSession = sessionmaker(bind=engine)
session = BDSession()


class BaseModel():
    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()\


    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()


class UserModel(Base, BaseModel):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True)
    password = Column(String())
    roles = relationship('RolesModel', secondary='user_roles')
    is_franchise = Column(Boolean())


    def __init__(self, name, password, is_franchise):
        self.name = name
        self.password = password
        self.is_franchise = is_franchise

    @classmethod
    def create_user(cls, name, password, is_franchise):
        cls( name, password, is_franchise).save_to_db()

    def set_role(self, *args):
        self.roles = [RolesModel.find_by_name(x) for x in args]
        self.save_to_db()



class RolesModel(Base, BaseModel):
    __tablename__ = "roles"
    id = Column(Integer(), primary_key=True)
    name = Column(String(), unique=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def set_roles():
        if not session.query(RolesModel).filter_by(id = 1).first():
            session.add_all([RolesModel("Employee"), RolesModel("Manager"), RolesModel("Director")])
            session.commit()



class UserRoles(Base, BaseModel):
    __tablename__= "user_roles"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id', ondelete='CASCADE'))
    role_id = Column(Integer(), ForeignKey('roles.id', ondelete='CASCADE'))



class ClientData(Base, BaseModel):
    __tablename__= "client_data"
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    content = Column(String)
    permission = Column(Integer())


    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.permission = 1

    def show_content(self):
        if  RolesModel.find_by_id(self.permission) in UserModel.find_by_id(1).roles:
            return self.content

class SellstData(Base, BaseModel):
    __tablename__= "sells_data"
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    content = Column(String)
    permission = Column(Integer)


    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.permission = 2

    def show_content(self):
        if  RolesModel.find_by_id(self.permission) in UserModel.find_by_id(1).roles and\
                        UserModel.find_by_id(1).is_franchise == 0:
            return self.content

        elif RolesModel.find_by_id(self.permission + 1) in UserModel.find_by_id(1).roles:
            return self.content


class BusinessPartnerstData(Base, BaseModel):
    __tablename__= "buisness_partners_data"
    id = Column(Integer(), primary_key=True)
    name = Column(String)
    content = Column(String)
    permission = Column(Integer)

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.permission = 3

    def show_content(self):
        if RolesModel.find_by_id(self.permission) in UserModel.find_by_id(1).roles:
            return self.content

