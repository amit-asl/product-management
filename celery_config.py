from datetime import datetime
from celery import Celery
from celery.schedules import crontab
from models.product import Product
from db import session
import os
import logging
from logging.handlers import RotatingFileHandler
# from fastapi.logger import logger
log_folder = 'logs'
log_file = os.path.join(log_folder, f'{datetime.now():%Y-%m-%d}.log')
log_level = logging.INFO

if not os.path.exists(log_folder):
    os.mkdir(log_folder)

handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=-1)
handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
handler.setLevel(log_level)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

celery_app = Celery('product', broker="redis://redis:6379/0")

celery_app.conf.beat_schedule = {
    "change attribute every 12 hour": {
        "task": "celery_config.update_status",
        "schedule": crontab(minute="*/1")
    },
}

@celery_app.task
def update_status():
    session.query(Product).filter(Product.status == "pending").update({"status": "confirm"})
    session.commit()
    logger.info('Product Status Updated')