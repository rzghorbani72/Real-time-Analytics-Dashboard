# Getting Started Guide

## Initial Setup

### 1. Prerequisites Installation

**Install Node.js (18+)**
```bash
# Using nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 18
nvm use 18
```

**Install Python (3.11+)**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip

# Verify installation
python3 --version
```

**Install PostgreSQL**
```bash
# Ubuntu/Debian
sudo apt install postgresql postgresql-contrib

# Start PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database
sudo -u postgres createdb analytics_db
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your database credentials

# Initialize database migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# Run the server
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env
# Edit .env if needed (default should work)

# Run development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

### 4. Using Docker (Optional)

```bash
# Start PostgreSQL and Redis
docker-compose up -d

# Verify services are running
docker-compose ps
```

## First Steps

1. **Test Backend API**
   - Visit `http://localhost:8000/docs`
   - Try creating a metric: POST `/api/v1/metrics`
   - Try fetching metrics: GET `/api/v1/metrics`

2. **Test Frontend**
   - Visit `http://localhost:3000`
   - Check browser console for any errors
   - Verify API connection

3. **Create Your First Metric**
   ```bash
   curl -X POST "http://localhost:8000/api/v1/metrics" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "temperature",
       "value": 23.5,
       "source": "sensor_1"
     }'
   ```

## Common Issues

### Database Connection Error
- Ensure PostgreSQL is running: `sudo systemctl status postgresql`
- Check database exists: `psql -l | grep analytics_db`
- Verify connection string in `.env`

### Port Already in Use
- Backend (8000): Change in `uvicorn` command or kill process
- Frontend (3000): Change in `nuxt.config.ts` or kill process

### Python Module Not Found
- Ensure virtual environment is activated
- Reinstall: `pip install -r requirements.txt`

### Node Modules Issues
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again

## Next Steps

1. Read [Learning Path](./learning-path.md) for step-by-step guidance
2. Review [Project Definition](./project-definition.md) for project goals
3. Start implementing features following the roadmap

