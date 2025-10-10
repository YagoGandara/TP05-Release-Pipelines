# TP05 - CI/CD (Angular + FastApi)

App mínima para establecer **CI/CD** con Azure DevOps, y desplegarlo en **Azure App Service** en entorno de **QA** y **Producción**

** Stack (Estructura)
- **Frontend**: Angular 18 (SPA)
- **Backend**: FastAPI (Python 3.12)
- **Infra**: Azure Web Apps (Linux, App Service Plan)
- **CI/CD**: Azure DevOps Pipelines (multi-stage)
- **Healthchecks**: `/`, `/healtz`, `/readyz`

---

## Acceso a los servicios (URLS)

**QA**
- Frontend (SPA): 
- Backend API: 

**PROD**
- Frontend (SPA): 
- Backend API: 

---

## Endpoints Útiles (API)

- `GET /`
- `GET /healtz` -> Estado de la app
- `GET /readyz` -> el pipeline o usa como health / gate
- `GET /api/todos` -> lista todos
- `POST /api/todos` -> crea (body : `{ "title": "texto" }`)

---

## Local (Docker)

```bash
docker compose down -v
docker compose build
docker compose up 

```
- Front http://localhost:4200
- API http://localhost:8080

Para testear el backend con Docker
```bash
docker compose run --rm api-tests
```

---

## CI(Build) - Azure DevOps

El pipeline `azure-pipelines.yml`:
- Front: `npm ci && ng build` -> publica `front/front-dist.zip`
- Back: instala dependencias y `pytest` -> publica `back/backend.zip`

Se dispara cada vez que haya un push a main

---

## CD (Release) - QA y PROD

**Stages**
1) **DeployQA**
    - Despliega front y API a Web Apps QA (zipDeploy)
    - Smoke tests `GET /readyz`, `GET /healtz`, `GET /` del front

2) **DeployPROD**
    - Requiere aprobación manual en el Environment PROD
    - Tiene los mismos checks que QA

**Variables de Azure Web App**
- ENV = `qa` o `prod`
- API_PORT = `8080`
- `CORS_ORIGINS` = URL del front correspondiente (QA o PROD)

**S