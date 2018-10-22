from flask import Flask, render_template, request
from init import logger, payload_logger
import json

from webhook import Event


application = Flask(__name__)


@application.route("/jenkins-trigger", methods=["POST"])
def jenkins_trigger():
    logger.info(f"({request.method}) {request.path}")
    payload_logger.info(json.dumps(request.form, indent=2))

    event_type = request.headers.get("X-GitHub-Event")

    if not event_type:
        logger.warn("There is no X-GitHub-Event header")
        return render_template("result.html", result="FAIL"), 400
    else:
        event = Event.factory(event_type, request.form)

    if event and event.is_triggering_event():
        pass

    return render_template("result.html", result="SUCCESS"), 200


if __name__ == "__main__":
    application.run()
