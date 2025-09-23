from enum import Enum

class ArchitectureTypeEnum(str, Enum):
    fastapi = "fastapi"
    react_next = "react_next"
    react_vite = "react_vite"
    spring_boot = "spring_boot"

class DatabaseTypeEnum(str, Enum):
    sqlite = "sqlite"
    postgresql = "postgresql"
    mysql = "mysql"
    mongodb = "mongodb"
