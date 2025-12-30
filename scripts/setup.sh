#!/bin/bash

set -e

echo "🚀 Setting up Real-time Analytics Dashboard Project"
echo "=================================================="

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "\n${BLUE}Checking prerequisites...${NC}"

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} Python: $PYTHON_VERSION"
else
    echo -e "${YELLOW}✗${NC} Python 3 not found. Please install Python 3.11+"
    exit 1
fi

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓${NC} Node.js: $NODE_VERSION"
else
    echo -e "${YELLOW}✗${NC} Node.js not found. Please install Node.js 18+"
    exit 1
fi

# Check PostgreSQL
if command -v psql &> /dev/null; then
    echo -e "${GREEN}✓${NC} PostgreSQL found"
else
    echo -e "${YELLOW}⚠${NC} PostgreSQL not found. You can use Docker Compose instead."
fi

# Check Docker
if command -v docker &> /dev/null && command -v docker-compose &> /dev/null; then
    echo -e "${GREEN}✓${NC} Docker and Docker Compose found"
else
    echo -e "${YELLOW}⚠${NC} Docker not found. You'll need to set up PostgreSQL manually."
fi

echo -e "\n${BLUE}Setting up backend...${NC}"
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/analytics_db
REDIS_URL=redis://localhost:6379
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
EOF
    echo -e "${GREEN}✓${NC} Created .env file"
else
    echo -e "${GREEN}✓${NC} .env file already exists"
fi

# Initialize Alembic if needed
if [ ! -d "alembic/versions" ]; then
    echo "Initializing Alembic migrations..."
    alembic init alembic || echo "Alembic already initialized"
fi

cd ..

echo -e "\n${BLUE}Setting up frontend...${NC}"
cd frontend

# Install dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
    echo -e "${GREEN}✓${NC} Dependencies installed"
else
    echo -e "${GREEN}✓${NC} Dependencies already installed"
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    echo "API_BASE_URL=http://localhost:8000" > .env
    echo -e "${GREEN}✓${NC} Created .env file"
else
    echo -e "${GREEN}✓${NC} .env file already exists"
fi

cd ..

echo -e "\n${BLUE}Setting up Docker services...${NC}"
if command -v docker-compose &> /dev/null; then
    echo "Starting PostgreSQL and Redis with Docker Compose..."
    docker-compose up -d
    echo -e "${GREEN}✓${NC} Docker services started"
    echo "Waiting for PostgreSQL to be ready..."
    sleep 5
else
    echo -e "${YELLOW}⚠${NC} Docker Compose not available. Please set up PostgreSQL manually."
fi

echo -e "\n${BLUE}Creating database and running migrations...${NC}"
cd backend
source venv/bin/activate

# Create database (if using local PostgreSQL)
if command -v psql &> /dev/null; then
    echo "Creating database (if it doesn't exist)..."
    PGPASSWORD=postgres psql -h localhost -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'analytics_db'" | grep -q 1 || PGPASSWORD=postgres psql -h localhost -U postgres -c "CREATE DATABASE analytics_db" || echo "Database might already exist or using Docker"
fi

# Run migrations
echo "Running database migrations..."
alembic upgrade head || echo "Migrations might need to be created first. Run: cd backend && alembic revision --autogenerate -m 'Initial migration'"

cd ..

echo -e "\n${GREEN}✅ Setup complete!${NC}"
echo -e "\n${BLUE}Next steps:${NC}"
echo "1. Start backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "2. Start frontend: cd frontend && npm run dev"
echo "3. Visit http://localhost:8000/docs for API documentation"
echo "4. Visit http://localhost:3000 for the frontend"
echo -e "\n${BLUE}If you need to create the initial migration:${NC}"
echo "cd backend && source venv/bin/activate && alembic revision --autogenerate -m 'Initial migration' && alembic upgrade head"

