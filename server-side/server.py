"""This module responds to the REST invocations from client side app.
This module stay on the server side (raspberry OS) and REST invocations
are made from Kotlin client side app."""

from flask import Flask, jsonify
from server_handler import ServerHandle

app = Flask(__name__)

server_prop = ServerHandle()


@app.route('/', strict_slashes=False)
def root():
    """Root method which returns with Server hostname.
    Server is raspberry host.

    return: Hostname as JSON
    """
    return jsonify(server_prop.get_server_name())


@app.route('/CPU', strict_slashes=False)
def fetch_cpu_usage():
    """Method returns with CPU utilisation on Server.
    Server is raspberry host.

    return: CPU usage as JSON
    example: 3.8
    """
    return jsonify(server_prop.get_cpu_usage())


if __name__ == "__main__":
    app.run(port=5001, debug="on", host='0.0.0.0')
