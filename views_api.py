from http import HTTPStatus

from fastapi import APIRouter, Depends
from lnbits.core.crud import get_user
from lnbits.core.models import WalletTypeInfo
from lnbits.decorators import require_admin_key
from starlette.exceptions import HTTPException

from .crud import (
    get_players,
    get_nsec,
    get_game,
    get_games,
    update_game,
    set_nsec
)
from .models import Nsec, Players, Games

fluttr_api_router = APIRouter()

## Get games

@fluttr_api_router.get("/api/v1/games")
async def api_games(
    wallet: WalletTypeInfo = Depends(require_admin_key),
) -> list[Games]:
    wallet_ids = [wallet.wallet.id]
    user = await get_user(wallet.wallet.user)
    wallet_ids = user.wallet_ids if user else []
    games = await get_games(wallet_ids)
    return games

## Update games

@fluttr_api_router.put("/api/v1/games")
async def api_fluttr_update(
    data: Games,
    wallet: WalletTypeInfo = Depends(require_admin_key),
) -> Games:
    game = await get_game(data.id)
    if not game:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Fluttr does not exist."
        )

    if wallet.wallet.id != game.wallet:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Not your Fluttr."
        )

    for key, value in data.dict().items():
        setattr(game, key, value)

    games = await update_game(data)
    return games


## Get nsec

@fluttr_api_router.get(
    "/api/v1/nsec",
    status_code=HTTPStatus.OK
)
async def api_nsec(
    wallet: WalletTypeInfo = Depends(require_admin_key)
) -> Nsec:
    nsec = await get_nsec(wallet.wallet.user)
    return nsec

## Set nsec

@fluttr_api_router.put("/api/v1/nsec")
async def api_fluttr_update(
    data: Nsec,
    wallet: WalletTypeInfo = Depends(require_admin_key),
) -> Games:
    nsec = await get_nsec(data.boss)
    if not nsec:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Nsec does not exist."
        )

    if wallet.wallet.user != data.boss:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="You're not the boss."
        )

    for key, value in data.dict().items():
        setattr(nsec, key, value)

    nsec = await set_nsec(nsec)
    return nsec

## Get players

@fluttr_api_router.get("/api/v1/players/{boss}")
async def api_players(
    boss: str,
    wallet: WalletTypeInfo = Depends(require_admin_key),
) -> list[Players]:
    if wallet.wallet.user != boss:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="You're not the boss."
        )
    players = await get_players(boss)
    return players