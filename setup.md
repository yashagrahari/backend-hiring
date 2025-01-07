## Initial Setup

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate
# For Unix or MacOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Redis Setup
```bash
# Using Docker
docker run -d --name redis-server -p 6379:6379 redis:6.2-alpine

# Verify Redis is running
docker ps
docker logs redis-server
```


### 3. Create Database Tables
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

## Starting Services

### 1. Start Django Server
```bash
python manage.py runserver
```

### 2. Start Celery Workers (15 workers) Examples:-
```bash
# EXAMPE 1 - Start worker for high-volume customers
celery -A config worker -l info -Q HIGH_VOLUME_FAST

# EXAMPE 2 - Start worker for medium-volume customers
celery -A config worker -l info -Q MEDIUM_VOLUME_FAST

# EXAMPE 3 - Start worker for low-volume customers
celery -A config worker -l info -Q LOW_VOLUME_FAST
```

## Debug Mode

### 1. Enable Debug Logging
```bash
# For Celery workers
celery -A config worker --loglevel=debug -Q HIGH_VOLUME_FAST --verbose

# For Redis
docker logs -f redis-server
```

### 2. Monitor Queues
```bash
# Install flower for monitoring
pip install flower

# Start flower
celery -A config flower
```