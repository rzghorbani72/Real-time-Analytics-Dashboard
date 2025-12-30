# Complete Setup Guide

## Quick Setup (Automated)

Run the setup script:
```bash
./scripts/setup.sh
```

This will:
- Check prerequisites
- Set up Python virtual environment
- Install backend dependencies
- Install frontend dependencies
- Create .env files
- Start Docker services (PostgreSQL & Redis)
- Create database and run migrations

## Manual Setup

### Step 1: Prerequisites

**Python 3.11+**
```bash
python3 --version  # Should be 3.11 or higher
```

**Node.js 18+**
```bash
node --version  # Should be 18 or higher
npm --version
```

**PostgreSQL 14+** (or use Docker)
```bash
psql --version
```

**Docker & Docker Compose** (optional but recommended)
```bash
docker --version
docker-compose --version
```

### Step 2: Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/analytics_db
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
EOF

# Start Docker services (if using Docker)
cd ..
docker-compose up -d
cd backend

# Create database (if not using Docker)
# sudo -u postgres createdb analytics_db
# OR
# PGPASSWORD=postgres psql -h localhost -U postgres -c "CREATE DATABASE analytics_db"

# Create initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head

# Start the server
uvicorn app.main:app --reload
```

Backend will run at: http://localhost:8000
API docs at: http://localhost:8000/docs

### Step 3: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file (optional, defaults work)
echo "API_BASE_URL=http://localhost:8000" > .env

# Start development server
npm run dev
```

Frontend will run at: http://localhost:3000

### Step 4: Verify Setup

1. **Test Backend API**
   - Visit http://localhost:8000/docs
   - Try POST `/api/v1/metrics`:
   ```json
   {
     "name": "temperature",
     "value": 23.5,
     "source": "sensor_1"
   }
   ```
   - Try GET `/api/v1/metrics` to see the created metric

2. **Test Frontend**
   - Visit http://localhost:3000
   - Check browser console for errors
   - The page should load without errors

3. **Test Database**
   ```bash
   # If using Docker
   docker-compose exec postgres psql -U postgres -d analytics_db -c "SELECT * FROM metrics;"
   
   # If using local PostgreSQL
   psql -U postgres -d analytics_db -c "SELECT * FROM metrics;"
   ```

## Troubleshooting

### Database Connection Issues

**Problem**: `connection refused` or `database does not exist`

**Solutions**:
1. Check PostgreSQL is running:
   ```bash
   # Docker
   docker-compose ps
   
   # Local
   sudo systemctl status postgresql
   ```

2. Verify database exists:
   ```bash
   psql -U postgres -l | grep analytics_db
   ```

3. Check connection string in `backend/.env`

### Port Already in Use

**Backend (8000)**:
```bash
# Find process
lsof -i :8000
# Kill process
kill -9 <PID>
# Or change port in uvicorn command
uvicorn app.main:app --reload --port 8001
```

**Frontend (3000)**:
```bash
# Find process
lsof -i :3000
# Kill process
kill -9 <PID>
# Or change in nuxt.config.ts
```

### Python Module Not Found

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
```

### Node Modules Issues

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Alembic Migration Issues

If migration fails:
```bash
cd backend
source venv/bin/activate

# Check current migration status
alembic current

# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migration
alembic upgrade head

# If you need to rollback
alembic downgrade -1
```

## Development Workflow

### Daily Development

1. **Start Services**
   ```bash
   # Terminal 1: Docker services
   docker-compose up -d
   
   # Terminal 2: Backend
   cd backend
   source venv/bin/activate
   uvicorn app.main:app --reload
   
   # Terminal 3: Frontend
   cd frontend
   npm run dev
   ```

2. **Make Changes**
   - Backend: Changes auto-reload with `--reload` flag
   - Frontend: Changes auto-reload with Nuxt dev server

3. **Database Changes**
   ```bash
   cd backend
   source venv/bin/activate
   alembic revision --autogenerate -m "Description of changes"
   alembic upgrade head
   ```

### Git Workflow

```bash
# Check status
git status

# Add changes
git add .

# Commit with meaningful message
git commit -m "feat: add new feature description"

# Push to GitHub
git push origin main
```

## Next Steps

After setup is complete:

1. ✅ Read [Learning Path](./learning-path.md) for step-by-step development
2. ✅ Review [Architecture](./architecture.md) to understand the system
3. ✅ Start with Phase 1: Foundation (Week 1-2)
4. ✅ Follow the roadmap in [Project Definition](./project-definition.md)

## Useful Commands

### Backend
```bash
# Run tests
pytest

# Check code style
black --check .
flake8 .

# Type checking
mypy app/
```

### Frontend
```bash
# Lint
npm run lint

# Type check
npm run typecheck

# Build
npm run build
```

### Database
```bash
# View tables
docker-compose exec postgres psql -U postgres -d analytics_db -c "\dt"

# View data
docker-compose exec postgres psql -U postgres -d analytics_db -c "SELECT * FROM metrics LIMIT 10;"

# Analyze query performance
docker-compose exec postgres psql -U postgres -d analytics_db -c "EXPLAIN ANALYZE SELECT * FROM metrics WHERE timestamp > NOW() - INTERVAL '1 day';"
```

