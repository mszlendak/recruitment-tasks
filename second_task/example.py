from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from second_task.models import UserModel, RolesModel, ClientData, Base



engine = create_engine('sqlite:///test.db')

BDSession = sessionmaker(bind=engine)
session = BDSession()

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

RolesModel.set_roles()

UserModel.create_user("TestUser", "TestPassword", False)


UserModel.find_by_name("TestUser").set_role("Employee", "Manager")


ClientData("TestData", "TestContent").save_to_db()

print(ClientData.find_by_id(1).show_content())
