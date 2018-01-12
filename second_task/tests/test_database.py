from base_test import BaseTest

from second_task.models import UserModel, UserRoles, RolesModel, BusinessPartnerstData, ClientData, SellstData



class ModelTest(BaseTest):
    def test_create_user(self):
        UserModel.create_user("Test1", "Test2", False)

        self.assertIsNotNone(UserModel.find_by_name("Test1"))
        self.assertEqual(UserModel.find_by_name("Test1").password, "Test2")

    def test_roles(self):
        role = RolesModel.find_by_name("Employee")


        self.assertEqual(role.id, 1)

    def test_relationship(self):
        UserModel.find_by_id(1).set_role("Employee")

        self.assertEqual(UserRoles.find_by_id(1).user_id, 1)
        self.assertEqual(UserRoles.find_by_id(1).role_id, 1)
        self.assertEqual(UserModel.find_by_id(1).roles[0].id, 1 )

    def test_create_business_partners_data(self):
        BusinessPartnerstData("test", "test content").save_to_db()

        self.assertIsNotNone(BusinessPartnerstData.find_by_name("test"))
        self.assertEqual(BusinessPartnerstData.find_by_name("test").content, "test content")

    def test_create_client_data(self):
        ClientData("test", "test content").save_to_db()

        self.assertIsNotNone(ClientData.find_by_name("test"))
        self.assertEqual(ClientData.find_by_name("test").content, "test content")

    def test_sells_data(self):
        SellstData("test", "test content").save_to_db()

        self.assertIsNotNone(SellstData.find_by_name("test"))
        self.assertEqual(SellstData.find_by_name("test").content, "test content")
    def test_check_client_data_content(self):
        ClientData("test", "test content").save_to_db()

        self.assertIsNone(ClientData.find_by_id(1).show_content())

        UserModel.find_by_id(1).set_role("Employee")

        self.assertEqual(ClientData.find_by_id(1).show_content(), "test content")

    def test_check_sells_data_content(self):
        SellstData("test", "test content").save_to_db()

        self.assertIsNone(SellstData.find_by_id(1).show_content())

        UserModel.find_by_id(1).set_role("Employee")

        self.assertIsNone(SellstData.find_by_id(1).show_content())

        UserModel.find_by_id(1).set_role("Employee", "Manager")


    def test_check_sells_data_content_when_franchise(self):
        SellstData("test", "test content").save_to_db()

        user = UserModel.find_by_id(1)
        user.is_franchise = True
        user.set_role("Employee", "Manager")


        self.assertIsNone(SellstData.find_by_id(1).show_content())

        UserModel.find_by_id(1).set_role("Employee", "Manager", "Director")

        self.assertEqual(SellstData.find_by_id(1).show_content(), "test content")

    def test_check_business_partnerss_data_content(self):
        BusinessPartnerstData("test", "test content").save_to_db()

        UserModel.find_by_id(1).set_role("Employee", "Manager")

        self.assertIsNone(BusinessPartnerstData.find_by_id(1).show_content())

        UserModel.find_by_id(1).set_role("Employee", "Manager", "Director")

        self.assertEqual(BusinessPartnerstData.find_by_id(1).show_content(), "test content")
