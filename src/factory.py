from celery import Celery
from flask import Flask

import settings


def make_app():
    app = Flask(settings.APPNAME)
    app.config.from_object('settings')
    return app


def make_celery(app=None):
    app = app or make_app()
    celery = Celery(
        app.import_name,
        backend=settings.CELERY_RESULT_BACKEND,
        broker=settings.CELERY_BROKER_URL
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
