""" Getter and Setter class for fetching hostname and IP."""

import socket
import psutil


class ServerHandle:
    """class with getter methods returning various system variables."""

    def __init__(self):
        """Constructor."""

        self.ip = ''
        self.hostname = ''
        self.cpu_percentage = ''

    def get_server_IP(self):
        """returns IP address of the server.

        :return: IP address as String
        """
        # https://stackoverflow.com/questions/166506/
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.connect(("8.8.8.8", 80))
        self.ip = soc.getsockname()[0]
        return self.ip

    def get_server_name(self):
        """returns the hostname of the server.

        :return: hostname as String
        """

        self.hostname = socket.gethostname()
        return self.hostname

    def get_cpu_usage(self):
        """returns the current cpu usage of the server.

        :return: cpu usage as Float
        """

        self.cpu_percentage = psutil.cpu_percent()
        return self.cpu_percentage
