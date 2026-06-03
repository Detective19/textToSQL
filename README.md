# Enterprise Text-to-SQL API

FastAPI microservice that converts natural language database questions into executable SQL using semantic retrieval, LLM-based SQL generation, SQL validation, and database execution.

## Project Overview

This project was developed as part of the **48-Hour Enterprise Text-to-SQL Build Challenge (NST)**.

The system accepts a natural language query and produces SQL using retrieved schema context.

Example:

Input:

```json
{
  "question": "show student department information"
}
```

Output:

```json
{
  "sql": "SELECT * FROM STUDENT_DEPARTMENT LIMIT 10"
}
```

---

## System Architecture

```text
User Question
↓
Schema Retrieval (Semantic Search)
↓
Prompt Builder
↓
LLM SQL Generator
↓
SQL Validation
↓
SQL Execution Layer
↓
FastAPI Response
```

---

## Tech Stack

* FastAPI
* Python
* Sentence Transformers
* FAISS
* HuggingFace Datasets
* SQLite
* Transformers
* SQLGlot

---

## Dataset

Dataset used:

* Beaver Dataset (HuggingFace)
* Semantic retrieval performed over Beaver schema metadata.

Dataset Components:

* beaver-table
* beaver-query

---

## Features

### Semantic Schema Retrieval

* Embedding-based schema retrieval
* Top-k table selection
* Confidence scoring

### SQL Generation

* LLM-based SQL generation
* Retrieved schema context support
* Fallback SQL generation

### Validation

* SQL syntax validation
* Error-safe execution

### Database Execution

* SQLite execution layer
* Graceful execution handling

---

## API Endpoints

### POST `/retrieve`

Retrieve relevant schema tables.

Request:

```json
{
  "question": "show student information"
}
```

Response:

```json
{
  "retrieved_tables": [],
  "scores": [],
  "confidence": 0.90
}
```

---

### POST `/generate-sql`

Generate SQL from natural language.

Request:

```json
{
  "question": "show student department information",
  "use_retrieved_context": true
}
```

Response:

```json
{
  "sql": "SELECT * FROM STUDENT_DEPARTMENT LIMIT 10",
  "valid": true
}
```

---

## Project Structure

```text
app/
├── data/
├── models/
├── routes/
├── services/
├── main.py
```

---

## Installation

```bash
git clone <repo-url>

cd text-to-SQL

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* Full Beaver execution support
* Better LLM prompting
* Query optimization
* Benchmark evaluation

---

## Screenshots

Add:

* Swagger Docs
* Retrieve Endpoint
* Generate SQL Endpoint

---

## Author

Anurag Tomar
