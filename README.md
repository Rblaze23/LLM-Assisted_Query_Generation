# LLM-Assisted Query Generation for NoSQL Databases

A natural language interface for querying multiple NoSQL database types using Large Language Models and the Model Context Protocol (MCP).

## Overview

This project enables users to interact with Redis, MongoDB, HBase, Neo4j, and RDF stores using natural language queries. The system leverages LLMs (via Groq API) and MCP to translate user queries into appropriate database-specific query languages.

## Features

- **Natural Language Query Translation**: Write queries in plain English, get database-specific queries
- **Multi-Database Support**: MongoDB, Neo4j, Redis, HBase, and RDF stores
- **Schema Exploration**: Automatically discover and utilize database schema information
- **Query Validation**: Validate queries before execution with helpful error messages
- **Query Explanation**: Understand how your natural language maps to database queries
- **Cross-Database Comparison**: Compare how the same query is expressed across different NoSQL databases
- **MCP-Based Architecture**: Modular, extensible design using Model Context Protocol

## Supported Databases

| Database | Type | Status | Phase |
|----------|------|--------|-------|
| MongoDB | Document Store | 🚧 In Progress | Phase 2 |
| Neo4j | Graph Database | 📋 Planned | Phase 4 |
| Redis | Key-Value Store | 📋 Planned | Phase 6 |
| HBase | Wide-Column Store | 📋 Planned | Phase 6 |
| Apache Jena Fuseki | RDF Triple Store | 📋 Planned | Phase 6 |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Main Application (Python)                   │
│  ┌────────────────────────────────────────────────┐    │
│  │    Query Translation Engine (LLM - Groq)       │    │
│  └────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────┐    │
│  │         MCP Client Manager                     │    │
│  └────────────────────────────────────────────────┘    │
└─────────────┬───────────────────────────────────────────┘
              │ MCP Protocol
┌─────────────┴───────────────────────────────────────────┐
│           MCP Servers (Database-Specific)                │
│  ┌──────────┐  ┌─────────┐  ┌────────┐  ┌────────┐    │
│  │ MongoDB  │  │ Neo4j   │  │ Redis  │  │ HBase  │    │
│  │   MCP    │  │  MCP    │  │  MCP   │  │  MCP   │    │
│  └──────────┘  └─────────┘  └────────┘  └────────┘    │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- Groq API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LLM-Assisted_Query_Generation
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env

   # Edit .env and add your Groq API key
   # GROQ_API_KEY=your_api_key_here
   ```

5. **Start databases with Docker**
   ```bash
   # Start MongoDB (Phase 2)
   docker-compose up -d mongodb

   # Later: Start Neo4j (Phase 4)
   docker-compose --profile phase4 up -d neo4j

   # Later: Start all databases (Phase 6)
   docker-compose --profile phase6 up -d
   ```

6. **Verify setup**
   ```bash
   # Check Docker containers
   docker ps

   # Test Python environment
   python -c "from src.utils.config import get_settings; print('Config loaded!')"
   ```

## Project Structure

```
LLM-Assisted_Query_Generation/
├── docs/                          # Documentation
│   ├── PROJECT_OVERVIEW.md        # Project overview
│   ├── TODO.md                    # Task tracking
│   ├── literature_review.md       # Research findings
│   └── architecture.md            # Detailed architecture
├── src/
│   ├── main_app/                  # Main application
│   │   ├── app.py                 # CLI entry point
│   │   ├── query_engine.py        # LLM query translation
│   │   ├── mcp_manager.py         # MCP client manager
│   │   └── cross_db_compare.py    # Cross-database comparison
│   ├── mcp_servers/               # MCP servers for each database
│   │   ├── mongodb_mcp/
│   │   ├── neo4j_mcp/
│   │   ├── redis_mcp/
│   │   ├── hbase_mcp/
│   │   └── rdf_mcp/
│   └── utils/                     # Utility modules
│       ├── config.py              # Configuration
│       └── logger.py              # Logging
├── tests/                         # Test suite
├── datasets/                      # Sample data
├── evaluation/                    # Benchmarking and evaluation
├── frontend/                      # Optional UI
├── docker-compose.yml             # Database orchestration
├── requirements.txt               # Python dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # This file
```

## Usage

### Basic Query Translation (Coming in Phase 3)

```python
from src.main_app.query_engine import QueryEngine

engine = QueryEngine()

# Translate natural language to MongoDB query
result = engine.process_query(
    "Find all users who live in New York and are over 25"
)

print(result.generated_query)
# Output: {"city": "New York", "age": {"$gt": 25}}

print(result.explanation)
# Output: "This query filters the users collection for documents where..."
```

### Cross-Database Comparison (Coming in Phase 7)

```python
from src.main_app.cross_db_compare import CrossDBCompare

comparer = CrossDBCompare()

# Compare same query across all databases
comparison = comparer.compare_query(
    "Find all products with price greater than 100"
)

for db, result in comparison.items():
    print(f"{db}: {result.query}")

# MongoDB: {"price": {"$gt": 100}}
# Neo4j: MATCH (p:Product) WHERE p.price > 100 RETURN p
# Redis: [Custom scan logic]
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_mongodb_mcp.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type checking
mypy src/
```

## Implementation Phases

- ✅ **Phase 1**: Setup & Literature Review
- 🚧 **Phase 2**: MongoDB MCP Server (In Progress)
- 📋 **Phase 3**: Main Application Core
- 📋 **Phase 4**: Neo4j MCP Server
- 📋 **Phase 5**: Query Engine Enhancement
- 📋 **Phase 6**: Additional Database Servers (Redis, HBase, RDF)
- 📋 **Phase 7**: Cross-Database Comparison
- 📋 **Phase 8**: Testing & Validation
- 📋 **Phase 9**: Documentation & Presentation

For detailed task breakdown, see [TODO.md](TODO.md).

## Contributing

This is an academic project for [Course Name]. Team members:
- [Team Member 1]
- [Team Member 2]
- [Team Member 3]
- [Team Member 4]

## Research & References

1. Qin, Zhiqian, et al. "MultiTEND: A Multilingual Benchmark for Natural Language to NoSQL Query Translation." ACL 2025.
2. Lu, Jinwei, et al. "Bridging the gap: Enabling natural language queries for nosql databases." arXiv 2025.
3. Tola, Alessandro. "Towards user-friendly nosql: A synthetic dataset approach and LLMs." Politecnico di Torino, 2024.
4. Yang, Tianhao. "LLM-Enhanced Data Management in Multi-Model Databases." 2025.

See [literature_review.md](docs/literature_review.md) for detailed analysis.

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- **Groq** for providing free LLM API access
- **Anthropic** for the Model Context Protocol specification
- Research papers and datasets from the NoSQL and NLP communities

## Contact

For questions or issues, please open an issue on GitHub or contact [your.email@example.com].

---

**Status**: Phase 1 Complete - Active Development
**Last Updated**: December 2025
