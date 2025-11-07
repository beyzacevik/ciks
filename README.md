<img src="./images/logo.png" alt="CIKS Logo" style="border: 2px solid #F48FB1; border-radius: 8px; padding: 10px; background-color: #ffffff;">

# ciks

CIKS is a backend API for managing outfit photos and metadata.

## Features

- Upload outfit photos with metadata (date, occasion, notes)
- Store and serve outfit images
- Health check endpoint

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
cd ciks-backend
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /outfits` - Upload a new outfit photo with metadata
- `GET /docs` - Interactive API documentation (Swagger UI)

## Project Structure

```
ciks/
├── ciks-backend/
│   ├── app/
│   │   └── main.py
│   └── media/
│       └── outfits/
├── images/
│   └── logo.png
└── requirements.txt
```

