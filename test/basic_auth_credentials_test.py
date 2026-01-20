import unittest
from smartystreets_python_sdk import basic_auth_credentials, Request
from smartystreets_python_sdk.exceptions import SmartyException


class TestBasicAuthCredentials(unittest.TestCase):
    def test_new_basic_auth_credential_with_valid_credentials(self):
        cred = basic_auth_credentials.BasicAuthCredentials("testID", "testToken")

        self.assertIsNotNone(cred)
        self.assertEqual(cred.auth_id, "testID")
        self.assertEqual(cred.auth_token, "testToken")

    def test_new_basic_auth_credential_with_empty_auth_id(self):
        with self.assertRaises(SmartyException) as context:
            basic_auth_credentials.BasicAuthCredentials("", "testToken")
        self.assertEqual(str(context.exception), 'credentials (auth id, auth token) required')

    def test_new_basic_auth_credential_with_empty_auth_token(self):
        with self.assertRaises(SmartyException) as context:
            basic_auth_credentials.BasicAuthCredentials("testID", "")
        self.assertEqual(str(context.exception), 'credentials (auth id, auth token) required')

    def test_new_basic_auth_credential_with_both_empty(self):
        with self.assertRaises(SmartyException) as context:
            basic_auth_credentials.BasicAuthCredentials("", "")
        self.assertEqual(str(context.exception), 'credentials (auth id, auth token) required')

    def test_new_basic_auth_credential_with_none_auth_id(self):
        with self.assertRaises(SmartyException) as context:
            basic_auth_credentials.BasicAuthCredentials(None, "testToken")
        self.assertEqual(str(context.exception), 'credentials (auth id, auth token) required')

    def test_new_basic_auth_credential_with_none_auth_token(self):
        with self.assertRaises(SmartyException) as context:
            basic_auth_credentials.BasicAuthCredentials("testID", None)
        self.assertEqual(str(context.exception), 'credentials (auth id, auth token) required')

    def test_new_basic_auth_credential_with_special_characters(self):
        cred = basic_auth_credentials.BasicAuthCredentials("test@id#123", "token!@#$%^&*()")

        self.assertIsNotNone(cred)
        self.assertEqual(cred.auth_id, "test@id#123")
        self.assertEqual(cred.auth_token, "token!@#$%^&*()")

    def test_sign_with_valid_credentials(self):
        cred = basic_auth_credentials.BasicAuthCredentials("myID", "myToken")
        request = Request()

        cred.sign(request)

        self.assertIsNotNone(request.basic_auth)
        self.assertEqual(request.basic_auth[0], "myID")
        self.assertEqual(request.basic_auth[1], "myToken")

    def test_sign_with_password_containing_colon(self):
        # Note: Per RFC 2617, userid must NOT contain colons, but password can
        cred = basic_auth_credentials.BasicAuthCredentials("validUserID", "password:with:colons")
        request = Request()

        cred.sign(request)

        self.assertIsNotNone(request.basic_auth)
        self.assertEqual(request.basic_auth[0], "validUserID")
        self.assertEqual(request.basic_auth[1], "password:with:colons")

    def test_sign_with_special_characters(self):
        cred = basic_auth_credentials.BasicAuthCredentials("user@domain.com", "p@ssw0rd!")
        request = Request()

        cred.sign(request)

        self.assertIsNotNone(request.basic_auth)
        self.assertEqual(request.basic_auth[0], "user@domain.com")
        self.assertEqual(request.basic_auth[1], "p@ssw0rd!")

    def test_sign_with_unicode_characters(self):
        cred = basic_auth_credentials.BasicAuthCredentials("用户", "密码")
        request = Request()

        cred.sign(request)

        self.assertIsNotNone(request.basic_auth)
        self.assertEqual(request.basic_auth[0], "用户")
        self.assertEqual(request.basic_auth[1], "密码")

    def test_sign_overwrites_existing_basic_auth(self):
        cred = basic_auth_credentials.BasicAuthCredentials("newID", "newToken")
        request = Request()
        request.basic_auth = ("oldID", "oldToken")

        cred.sign(request)

        self.assertIsNotNone(request.basic_auth)
        self.assertEqual(request.basic_auth[0], "newID")
        self.assertEqual(request.basic_auth[1], "newToken")


if __name__ == '__main__':
    unittest.main()
