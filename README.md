# Real-time Analytics Dashboard

A full-stack learning project demonstrating modern web development with Vue 3, Nuxt 3, Pinia, D3.js, Python, and FastAPI.

## 🎯 Goals

This project is designed with:
- **Frontend**: Vue 3 Composition API, Nuxt 3 SSR/SSG, Pinia state management, D3.js visualizations
- **Backend**: Python, FastAPI, SQLAlchemy, database query optimization
- **Architecture**: Clean architecture patterns, scalability, maintainability

## 🚀 Project Features

- Real-time data ingestion and visualization
- Interactive D3.js charts and dashboards
- Optimized database queries with PostgreSQL
- WebSocket support for live updates
- RESTful API with FastAPI
- Modern Nuxt 3 frontend with SSR

## 📁 Project Structure

```
VuePy/
├── frontend/          # Nuxt 3 application
├── backend/           # FastAPI application
├── docs/              # Project documentation
├── .github/           # GitHub Actions workflows
└── docker-compose.yml # Development environment
```

## 🛠️ Tech Stack

### Frontend
- Vue 3 (Composition API)
- Nuxt 3
- Pinia
- D3.js
- TypeScript
- Tailwind CSS (optional)

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (migrations)
- Redis (caching)

## 📦 Setup Instructions

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Docker & Docker Compose (optional)

### Quick Start

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd VuePy
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

4. **Database Setup**
```bash
# Create PostgreSQL database
createdb analytics_db

# Run migrations
cd backend
alembic upgrade head
```

5. **Run Development Servers**
```bash
# Terminal 1 - Backend
cd backend
uvicorn app.main:app --reload

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## 📚 Documentation

Detailed documentation is available in the `/docs` directory:
- [Project Definition](./docs/project-definition.md)
- Architecture decisions
- API documentation
- Development guides

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm run test
```

## 🚢 Deployment

The project includes GitHub Actions workflows for:
- Automated testing
- Code quality checks
- Deployment automation

## 📝 Development Roadmap

See [Project Definition](./docs/project-definition.md) for detailed feature roadmap and learning phases.

## 🤝 Contributing

This is a learning project. Feel free to:
- Report issues
- Suggest improvements
- Share learning resources

## 📄 License

MIT License - Feel free to use this project for learning purposes.

