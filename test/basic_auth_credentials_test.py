import unittest
import smartystreets_python_sdk as smarty
from smartystreets_python_sdk.basic_auth_credentials import CredentialsRequired


class TestBasicAuthCredentials(unittest.TestCase):

    def test_new_basic_auth_credential_with_valid_credentials(self):
        cred = smarty.BasicAuthCredentials("testID", "testToken")

        self.assertIsNotNone(cred)
        self.assertEqual("testID", cred.auth_id)
        self.assertEqual("testToken", cred.auth_token)

    def test_new_basic_auth_credential_with_empty_auth_id(self):
        with self.assertRaises(CredentialsRequired):
            smarty.BasicAuthCredentials("", "testToken")

    def test_new_basic_auth_credential_with_empty_auth_token(self):
        with self.assertRaises(CredentialsRequired):
            smarty.BasicAuthCredentials("testID", "")

    def test_new_basic_auth_credential_with_both_empty(self):
        with self.assertRaises(CredentialsRequired):
            smarty.BasicAuthCredentials("", "")

    def test_new_basic_auth_credential_with_none_auth_id(self):
        with self.assertRaises(CredentialsRequired):
            smarty.BasicAuthCredentials(None, "testToken")

    def test_new_basic_auth_credential_with_none_auth_token(self):
        with self.assertRaises(CredentialsRequired):
            smarty.BasicAuthCredentials("testID", None)

    def test_new_basic_auth_credential_with_special_characters(self):
        cred = smarty.BasicAuthCredentials("test@id#123", "token!@#$%^&*()")

        self.assertIsNotNone(cred)
        self.assertEqual("test@id#123", cred.auth_id)
        self.assertEqual("token!@#$%^&*()", cred.auth_token)

    def test_sign_with_valid_credentials(self):
        cred = smarty.BasicAuthCredentials("myID", "myToken")
        request = smarty.Request()

        cred.sign(request)

        self.assertEqual(("myID", "myToken"), request.auth)

    def test_sign_with_password_containing_colon(self):
        cred = smarty.BasicAuthCredentials("validUserID", "password:with:colons")
        request = smarty.Request()

        cred.sign(request)

        self.assertEqual(("validUserID", "password:with:colons"), request.auth)

    def test_sign_with_special_characters(self):
        cred = smarty.BasicAuthCredentials("user@domain.com", "p@ssw0rd!")
        request = smarty.Request()

        cred.sign(request)

        self.assertEqual(("user@domain.com", "p@ssw0rd!"), request.auth)

    def test_sign_with_unicode_characters(self):
        cred = smarty.BasicAuthCredentials("用户", "密码")
        request = smarty.Request()

        cred.sign(request)

        self.assertEqual(("用户", "密码"), request.auth)

    def test_sign_overwrites_existing_auth(self):
        cred = smarty.BasicAuthCredentials("newID", "newToken")
        request = smarty.Request()
        request.auth = ("oldID", "oldToken")

        cred.sign(request)

        self.assertEqual(("newID", "newToken"), request.auth)


if __name__ == '__main__':
    unittest.main()
