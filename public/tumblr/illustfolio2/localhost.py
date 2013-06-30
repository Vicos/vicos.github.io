from flask import Flask
from flask import redirect, send_from_directory

app = Flask(__name__)

# static files

@app.route('/<path:filename>')
def send_static_files(filename):
    return send_from_directory('./', filename)

# main process

if __name__ == "__main__":
    # TODO add cli option to change host, port and debug mode
    app.run(port=80)
