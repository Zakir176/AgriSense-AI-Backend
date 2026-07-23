# AgriSense AI — Backend API

FastAPI backend service for **AgriSense AI** — an intelligent poultry farm management platform.

Provides REST API endpoints for offline-first synchronization, YOLOv8 visual audits, audio telemetry, and daily farm metric logging.

## Related Repository

- **Frontend**: [AgriSense-AI-Frontend](https://github.com/Zakir176/AgriSense-AI-Frontend)

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL + SQLAlchemy ORM
- **Auth**: JWT via python-jose + passlib/bcrypt
- **AI/ML**: YOLOv8 (ultralytics), OpenCV, librosa
- **Real-time**: WebSocket (RTSP simulator)

## Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL 15+ (or use the included `docker-compose.yml`)

### Setup

```bash
# 1. Start the database
docker compose up -d

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
# For AI/CV features:
pip install -r requirements-full.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your database URL and secrets

# 5. Run the server
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000` with interactive docs at `/docs`.

### Seed Data

```bash
python seed_data.py
```

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `FRONTEND_URL` | Comma-separated frontend origins for CORS | _(empty)_ |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:postgrespassword@localhost:5432/agrisense` |
| `SECRET_KEY` | JWT signing key | _(change in production!)_ |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifetime | `1440` (24h) |
| `UPLOAD_DIR` | Directory for uploaded files | `uploads` |

## API Endpoints

| Tag | Prefix | Description |
|---|---|---|
| Auth | `/api/v1/auth` | JWT login, register, user info |
| Farms | `/api/v1/farms` | Farm CRUD + member management |
| Batches | `/api/v1/batches` | Poultry batch lifecycle |
| Readings | `/api/v1/readings` | Daily feed/water/mortality logs |
| Growth | `/api/v1/growth` | Weight sampling + Cobb 500 tracking |
| Medications | `/api/v1/medications` | Medical/vaccination history |
| Schedules | `/api/v1/schedules` | Treatment calendar |
| Alerts | `/api/v1/alerts` | Anomaly detection alerts |
| Inference | `/api/v1/inference` | YOLOv8 video analysis |
| Spatial Trends | `/api/v1/spatial-trends` | Heatmap distribution |
| Audio | `/api/v1/audio` | Audio distress classification |

## Testing

```bash
pytest
```

## License

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
