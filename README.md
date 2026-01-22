# DynoBIO - Dynamic Profile Biography API

DynoBIO is a simple RESTful API built with **Django** and **Django REST Framework (DRF)**. It serves as a centralized management system to maintain and serve dynamic profile and biographical data, allowing for dynamic updates to portfolio data, career history, and technical skills.

## Key Features

* **Custom Admin Interface:** Tailored Django Admin for easy content management.
* **Dynamic Skill Tracking:** Manage proficiency percentages with inline editing.
* **Focus Highlight:** Maintain a list of current focus areas in real-time.
* **Clean API Design:** Uses `ModelViewSets` for standard CRUD operations across all resources.
* **Serialized JSON Output:** Ready for integration with modern frontend frameworks like React, Vue, or Next.js.

---

## Tech Stack

* **Backend:** [Django](https://www.djangoproject.com/)
* **API:** [Django REST Framework](https://www.django-rest-framework.org/)
* **Database:** Currently MariaDB (Production)

---

## API Endpoints

`/api/profile/` Basic bio, title, and location information. |  
`/api/expertise/` Broad categories of professional mastery.  
`/api/projects/` Descriptions of past work.   
`/api/skills/` Technical skills with percentage-based values. For Spider Diagram.  
`/api/focus/` Current priorities or project status (toggleable).  
`/api/career/` Professional timeline and role history.  

## Administration
`/admin` Data admin ui.  

## Example - Using API in static profile page
By fetching the data from the API in a static html page, using JavaScript, the page can be updated dynamically from the Admin panel of this service.  
An example...

## Installation & Setup (Docker)
### 1. Build Image in Docker
```bash
docker build -t bio-api:latest .
```




There is an example stack for use with Traefik as reverse proxy, but that can be simmplified to.

```yaml
version: '3.8'

services:
  web:
    image: bio-api:latest
    container_name: bio_api_prod
    restart: always
    # Maps host port 8000 to container port 8000 - can be changed on LHS
    ports:
      - "8000:8000"
    environment:
      - DJANGO_SECRET_KEY=your-secret-key
      - DJANGO_DEBUG=False
      - DJANGO_ALLOWED_HOSTS=*
      - DB_NAME=your_db
      - DB_USER=your_user
      - DB_PASSWORD=your_password
      - DB_HOST=your_db_host_ip
      - DB_PORT=3306
      - PYTHONUNBUFFERED=1
Key Changes Explained
```
## Installation & Setup (Development)

### 1. Clone and Environment
```bash
git clone https://github.com/your-username/dynobio-backend.git
cd dynobio-backend
```
### 2. Create Venv
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install Requirements
```bash
python -m venv venv
pip install django djangorestframework django-cors-headers
```

### 4. Database Initialisation
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Administrative Setup
```bash
python manage.py createsuperuser
```
### 6. Launch
```bash
python manage.py runserver
```



## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.