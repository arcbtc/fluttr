from typing import List, Optional, Union

from lnbits.db import Database

from .models import Nsec, Players, Games

db = Database("ext_fluttr")

async def set_nsec(data: Nsec) -> Nsec:
    await db.update("fluttr.nsec", data)
    return Nsec(**data.dict())

async def get_nsec(boss: str) -> Optional[Nsec]:
    return await db.fetchone(
        "SELECT * FROM fluttr.nsec WHERE boss = :boss",
        {"boss": boss},
        Nsec,
    )

async def get_game(record_id: str) -> Optional[Games]:
    return await db.fetchone(
        "SELECT * FROM fluttr.games WHERE id = :id",
        {"id": record_id},
        Games,
    )

async def get_games(wallet_ids: Union[str, List[str]]) -> List[Games]:
    if isinstance(wallet_ids, str):
        wallet_ids = [wallet_ids]
    q = ",".join([f"'{w}'" for w in wallet_ids])
    return await db.fetchall(
        f"SELECT * FROM fluttr.games WHERE wallet IN ({q}) ORDER BY id",
        model=Games,
    )

async def get_players(boss: str) -> List[Players]:
    return await db.fetchall(
        "SELECT * FROM fluttr.players WHERE boss = :boss ORDER BY id",
        {"boss": boss},
        model=Players,
    )

async def get_players_by_game(game_id: str) -> List[Players]:
    return await db.fetchall(
        "SELECT * FROM fluttr.players WHERE game_id = :game_id ORDER BY game_id",
        {"game_id": game_id},
        model=Players,
    )

async def update_game(data: Games) -> Games:
    await db.update("fluttr.maintable", data)
    return Games(**data.dict())