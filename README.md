# Fastboiler
A FastAPI + Celery + Redis skeleton/example project

| Service       | Port |
|---------------|------|
| Frontend      | 8000 |
| Dashboard     | 5555 |
| Backend/Redis | 6379 |

## Project structure

```
project 
│   docker-compose.yml [Docker Compose build/deployment]
│
└───ansible [Playbooks and roles for automated deployment]
│
└───src [Application source code root]
    │   Dockerfile [Docker image build instructions]
    │   main.py [Application entrypoint]
    │   requirements.txt [Python dependencies]
    │
    └───api [REST API source code root]
        │   
        └───core [General/Core application code]
        │   │   config.py [Application configuration definitions]
        │   │
        │   └───logic [General/Background tasks/logic]
        │   │   
        │   │
        │   └───models [Core data objects definitions]
        │   
        └───api_vX
        │   │   api.py [APIRouter definition and endpoint routing]
        │   │
        │   └───endpoints [API endpoint definitions]
        ...
```

## Setup and running locally

### Install dependencies

```bash
# Python
sudo apt install python3 python3-dev python3-venv -y
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3
# Redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt update
sudo apt install redis -y
sudo systemctl enable redis
sudo systemctl start redis
```

### Setup virtualenv

```bash
python3 -m venv venv
. ./venv/bin/activate
pip install -r ./src/requirements.txt
deactivate
```

### Running
Open two (three if you want to run the monitoring dashboard) terminal windows

#### Frontend
Start the frontend in one of the terminals by running the following

```bash
. ./venv/bin/activate
cd src
uvicorn main:app --host 0.0.0.0 --reload
```

#### Backend
Start the backend in one of the terminals by running the following

```bash
. ./venv/bin/activate
cd src
celery -A worker.celery worker --loglevel=info --logfile=logs/celery.log
```

#### Monitoring Dashboard (optional)
Start the backend monitoring dashboard by running the following

```bash
. ./venv/bin/activate
cd src
celery -A worker.celery flower --port=5555 --broker=redis://localhost:6379/0
```
