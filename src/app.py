import logging

from flask import jsonify

import settings
from factory import make_app, make_celery
from tasks.task import test_task

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(settings.APPNAME)

app = make_app()

# referenced by run_worker.sh
celery = make_celery(app)


@app.route('/test', methods=['POST'])
def test_trigger():
    logger.info('POST /test')
    test_task.delay()
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
