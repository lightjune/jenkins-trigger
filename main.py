from flask import Flask, render_template, request
from init import logger, payload_logger
import json

application = Flask(__name__)


@application.route("/jenkins-trigger", methods=["POST"])
def jenkins_trigger():
    logger.info("(%s) %s", request.method, request.path)
    payload_logger.info(json.dumps(request.form, indent=2))
    return render_template("empty.html"), 200


if __name__ == "__main__":
    application.run()
