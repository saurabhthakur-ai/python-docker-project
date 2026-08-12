"""Flask application factory and route definitions."""

import json
import platform
import time

from flask import Flask, Response

from app.config import get_config
from app.logger import get_logger

_START_TIME = time.time()


def create_app() -> Flask:
    """Create and configure the Flask application."""
    config = get_config()
    logger = get_logger(__name__, config.LOG_LEVEL)

    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["DEBUG"] = config.DEBUG

    @app.route("/health")
    def health() -> Response:
        payload = {
            "status": "ok",
            "environment": config.ENV,
            "uptime_seconds": round(time.time() - _START_TIME, 2),
            "python": platform.python_version(),
        }
        logger.debug("Health check called")
        return Response(
            json.dumps(payload),
            status=200,
            mimetype="application/json",
        )

    @app.route("/")
    def index() -> Response:
        payload = {"message": f"Welcome to {config.APP_NAME}"}
        return Response(
            json.dumps(payload),
            status=200,
            mimetype="application/json",
        )

    logger.info("App created | env=%s debug=%s", config.ENV, config.DEBUG)
    return app


if __name__ == "__main__":
    cfg = get_config()
    application = create_app()
    application.run(host=cfg.HOST, port=cfg.PORT, debug=cfg.DEBUG)
