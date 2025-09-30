from enum import Enum


class ArchitectureTypeEnum(str, Enum):
    fastapi = "fastapi"
    react_next = "react_next"
    react_vite = "react_vite"
    spring_boot = "spring_boot"
    fullstack = "fullstack"
    dashboard = "dashboard"
    rag = "rag"
    ecommerce = "ecommerce"
    saas = "saas"
    microservices = "microservices"


class DatabaseTypeEnum(str, Enum):
    sqlite = "sqlite"
    postgresql = "postgresql"
    mysql = "mysql"
    mongodb = "mongodb"
    redis = "redis"
    oracle = "oracle"
    mssql = "mssql"
    cassandra = "cassandra"
    dynamodb = "dynamodb"
    neo4j = "neo4j"
