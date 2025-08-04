# KPA Backend Assignment (FastAPI)

## Setup Instructions

### 1. Using Docker
```bash
docker-compose up --build
```

### 2. Manual Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpoints

- `POST /api/v1/formdata` - Submit form data
- `GET /api/v1/formdata/{form_id}` - Retrieve form data

## Notes
- Data is stored in a temporary in-memory dictionary (`fake_db.py`)
