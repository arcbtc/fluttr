import asyncio

from lnbits.core.models import Payment
from lnbits.tasks import register_invoice_listener

from .crud import get_players_by_game

async def wait_for_paid_invoices():
    invoice_queue = asyncio.Queue()
    register_invoice_listener(invoice_queue, "ext_fluttr")
    while True:
        payment = await invoice_queue.get()
        await on_invoice_paid(payment)

async def on_invoice_paid(payment: Payment) -> None:
    if payment.extra.get("tag") != "Satsdice":
        return

    game_id = payment.extra.get("id")
    players = await get_players_by_game(game_id)
    if not players:
        return

    # Update stuff and post to nostrclient