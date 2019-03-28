"""This module responds to the REST invocations from client side app."""

from flask import Flask, jsonify
from server_handler import ServerHandle

app = Flask(__name__)

server_prop = ServerHandle()


@app.route('/', strict_slashes=False)
def root():
    """Root method which returns with Server hostname.

    return: Hostname as JSON
    """
    return jsonify(server_prop.get_server_name())


@app.route('/CPU', strict_slashes=False)
def fetch_cpu_usage():
    """Method returns with CPU utilisation on Server.

    return: CPU usage as JSON
    example: 3.8
    """
    return jsonify(server_prop.get_cpu_usage())


if __name__ == "__main__":
    app.run(port=5001, debug="on", host='0.0.0.0')
