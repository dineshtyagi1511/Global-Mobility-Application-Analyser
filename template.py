import os 
from pathlib import Path


project_name = "Visa"

list_of_Files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline",
    f"{project_name}/pipeline/prediction_pipeline",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/mains_utils.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "demo.py",
    "config/models.yaml",
    "config/schema.yaml"

    
]



for filepath in list_of_Files:
    filepath = Path(filepath)
    file_dir , file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
    if (not os.path.exists(filepath)) or os.path.getsize(filepath)==0:
        with open(filepath,"w") as f:
            pass 
    else :
        print(f"{file_name}is already preseent in {file_dir}and has some content skipping creation .")