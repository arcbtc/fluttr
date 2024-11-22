async def m001_initial(db):
    """
    Initial templates table.
    """
    await db.execute(
        """
        CREATE TABLE fluttr.nsec (
            boss TEXT PRIMARY KEY NOT NULL,
            nsec TEXT,
            botfather TEXT
        );
    """
    )

async def m002_initial(db):
    """
    Initial templates table.
    """
    await db.execute(
        """
        CREATE TABLE fluttr.players (
            id TEXT PRIMARY KEY NOT NULL,
            public_key TEXT NOT NULL,
            note_id TEXT NOT NULL,
            amount INTEGER DEFAULT 0,
            game TEXT NOT NULL,
            game_id TEXT NOT NULL,
            live BOOLEAN DEFAULT FALSE,
            nip_05 TEXT NOT NULL
        );
    """
    )

async def m003_initial(db):
    """
    Initial templates table.
    """
    await db.execute(
        """
        CREATE TABLE fluttr.games (
            id TEXT PRIMARY KEY NOT NULL,
            enabled BOOLEAN NOT NULL,
            game TEXT NOT NULL,
            wallet TEXT NOT NULL
        );
    """
    )


