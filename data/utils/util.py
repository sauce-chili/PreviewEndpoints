from dataclasses import dataclass

from sqlalchemy import Engine, create_engine


@dataclass
class ParamDB:
    driver: str
    user_name: str
    password: str
    host: str
    port: int
    database_name: str


def get_postgres_db_connection(p: ParamDB) -> Engine:
    db_url = f"postgresql://{p.user_name}:{p.password}@{p.host}:{p.port}/{p.database_name}"
    engine = create_engine(db_url)
    return engine
