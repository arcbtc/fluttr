import asyncio

from fastapi import APIRouter
from lnbits.tasks import create_permanent_unique_task
from loguru import logger

from .crud import db
from .tasks import wait_for_paid_invoices
from .views import fluttr_generic_router
from .views_api import fluttr_api_router

logger.debug(
    "This logged message is from fluttr/__init__.py, you can debug in your "
    "extension using 'import logger from loguru' and 'logger.debug(<thing-to-log>)'."
)

fluttr_ext: APIRouter = APIRouter(prefix="/fluttr", tags=["Fluttr"])
fluttr_ext.include_router(fluttr_generic_router)
fluttr_ext.include_router(fluttr_api_router)

fluttr_static_files = [
    {
        "path": "/fluttr/static",
        "name": "fluttr_static",
    }
]

scheduled_tasks: list[asyncio.Task] = []


def fluttr_stop():
    for task in scheduled_tasks:
        try:
            task.cancel()
        except Exception as ex:
            logger.warning(ex)


def fluttr_start():
    task = create_permanent_unique_task("ext_fluttr", wait_for_paid_invoices)
    scheduled_tasks.append(task)


__all__ = [
    "db",
    "fluttr_ext",
    "fluttr_static_files",
    "fluttr_start",
    "fluttr_stop",
]
