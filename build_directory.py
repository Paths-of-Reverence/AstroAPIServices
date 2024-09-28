import os

# Define the directory structure
dirs = [
    "astro_api_project/app",
    "astro_api_project/app/models",
    "astro_api_project/app/services",
    "astro_api_project/app/utils",
    "astro_api_project/app/routes",
    "astro_api_project/app/templates",
    "astro_api_project/tests"
]

files = [
    "astro_api_project/app/__init__.py",
    "astro_api_project/app/main.py",
    "astro_api_project/app/config.py",
    "astro_api_project/app/models/__init__.py",
    "astro_api_project/app/models/celestial_bodies.py",
    "astro_api_project/app/models/aspects.py",
    "astro_api_project/app/models/readings.py",
    "astro_api_project/app/services/__init__.py",
    "astro_api_project/app/services/webhook_receiver.py",
    "astro_api_project/app/services/data_conversion.py",
    "astro_api_project/app/services/swiss_ephemeris_integration.py",
    "astro_api_project/app/services/aspect_calculations.py",
    "astro_api_project/app/services/neo4j_integration.py",
    "astro_api_project/app/services/email_service.py",
    "astro_api_project/app/utils/__init__.py",
    "astro_api_project/app/utils/error_handling.py",
    "astro_api_project/app/utils/logging.py",
    "astro_api_project/app/utils/helpers.py",
    "astro_api_project/app/routes/__init__.py",
    "astro_api_project/app/routes/api_routes.py",
    "astro_api_project/app/templates/email_template.html",
    "astro_api_project/tests/__init__.py",
    "astro_api_project/tests/test_webhook_receiver.py",
    "astro_api_project/tests/test_data_conversion.py",
    "astro_api_project/tests/test_swiss_ephemeris_integration.py",
    "astro_api_project/tests/test_aspect_calculations.py",
    "astro_api_project/tests/test_neo4j_integration.py",
    "astro_api_project/requirements.txt",
    "astro_api_project/Dockerfile",
    "astro_api_project/docker-compose.yml",
    "astro_api_project/.env",
    "astro_api_project/.gitignore",
    "astro_api_project/README.md",
    "astro_api_project/setup.py",  # or "astro_api_project/pyproject.toml"
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass  # Create an empty file

print("Directory structure created successfully!")
