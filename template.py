import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/trainer_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",  # Root file
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "main.py"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:  
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"✅ Creating empty file: {filepath}")
    else:
        logging.info(f"⚠️ {filename} already exists")

# ✅ After script runs, check the existence of app.py
app_file = "app.py"
if os.path.exists(app_file):
    logging.info(f"✅ app.py successfully created at: {os.path.abspath(app_file)}")
else:
    logging.warning(f"❌ app.py NOT found! Check script execution.")
