# Fastboiler
A FastAPI + Celery + Redis skeleton/example project


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