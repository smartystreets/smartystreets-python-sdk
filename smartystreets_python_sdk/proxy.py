class Proxy:
    def __init__(self, host, username=None, password=None):
        """
        Contains information about a proxy through which lookups should be sent
        :param host: The proxy host including port, but not scheme. (example: localhost:8080)
        :param username: Username to authenticate with the proxy server
        :param password: Password to authenticate with the proxy server
        """
        self.host = host
        self.username = username
        self.password = password
