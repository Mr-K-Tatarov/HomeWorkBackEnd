from db.config import PostgresConfig
from transport.sanic.config import SanicConfig


class ApplicationConfig:
    sanic: SanicConfig
    database: PostgresConfig

    def __init__(self):
        self.sanic = SanicConfig()
        self.database = PostgresConfig()
