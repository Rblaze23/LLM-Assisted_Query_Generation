"""Configuration management using pydantic-settings."""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow"
    )

    # LLM API Configuration
    groq_api_key: str = Field(..., description="Groq API key for LLM calls")

    # MongoDB Configuration
    mongodb_host: str = Field(default="localhost", description="MongoDB host")
    mongodb_port: int = Field(default=27017, description="MongoDB port")
    mongodb_username: str = Field(default="admin", description="MongoDB username")
    mongodb_password: str = Field(default="adminpass", description="MongoDB password")
    mongodb_database: str = Field(default="test_db", description="MongoDB default database")
    mongodb_auth_source: str = Field(default="admin", description="MongoDB auth source")

    # Neo4j Configuration
    neo4j_uri: str = Field(default="bolt://localhost:7687", description="Neo4j connection URI")
    neo4j_username: str = Field(default="neo4j", description="Neo4j username")
    neo4j_password: str = Field(default="password123", description="Neo4j password")

    # Redis Configuration
    redis_host: str = Field(default="localhost", description="Redis host")
    redis_port: int = Field(default=6379, description="Redis port")
    redis_password: Optional[str] = Field(default=None, description="Redis password")
    redis_db: int = Field(default=0, description="Redis database number")

    # HBase Configuration
    hbase_host: str = Field(default="localhost", description="HBase host")
    hbase_port: int = Field(default=9090, description="HBase Thrift port")
    hbase_thrift_protocol: str = Field(default="compact", description="HBase Thrift protocol")

    # RDF/Fuseki Configuration
    fuseki_endpoint: str = Field(
        default="http://localhost:3030",
        description="Fuseki SPARQL endpoint"
    )
    fuseki_dataset: str = Field(default="ds", description="Fuseki dataset name")
    fuseki_username: Optional[str] = Field(default="admin", description="Fuseki username")
    fuseki_password: Optional[str] = Field(default="admin123", description="Fuseki password")

    # Application Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    max_query_results: int = Field(default=100, description="Maximum query results to return")
    query_timeout: int = Field(default=30, description="Query timeout in seconds")

    # MCP Server Configuration
    mcp_server_timeout: int = Field(default=60, description="MCP server timeout in seconds")
    mcp_max_retries: int = Field(default=3, description="Maximum MCP retry attempts")

    @property
    def mongodb_uri(self) -> str:
        """Construct MongoDB connection URI."""
        return (
            f"mongodb://{self.mongodb_username}:{self.mongodb_password}"
            f"@{self.mongodb_host}:{self.mongodb_port}/"
            f"?authSource={self.mongodb_auth_source}"
        )


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings: Application settings loaded from environment.
    """
    return Settings()
