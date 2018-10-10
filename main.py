import json
import logging.config
from flask import Flask, render_template, request


application = Flask(__name__)

with open('configs/logging.json', 'rt') as f:
    logging_config = json.load(f)
logging.config.dictConfig(logging_config)
Logger = logging.getLogger("payload")


@application.route("/jenkins-trigger", methods=["POST"])
def jenkins_trigger():
    Logger.info(request.form)
    return render_template("empty.html"), 200


if __name__ == "__main__":
    application.run()
