from dataclasses import dataclass


@dataclass
class AppConfig:
    secret_key: str


@dataclass
class DBConfig:
    host: str
    port: str
    user: str
    pswd: str
    name: str


@dataclass
class Config:
    app: AppConfig
    db: DBConfig
