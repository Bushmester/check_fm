import os

from flask import Flask

from local_configs import Configuration


app = Flask(__name__)


def main():
    if not os.getenv('IS_PRODUCTION', None):
        app.config.from_object(Configuration)
    print(app.url_map)

    app.run()


if __name__ == '__main__':
    main()
