import os
from pathlib import Path

input_paths_dict = {
    "main_path": "C:/Utente/Doc/1",
    "cal_plans_folder_name": "Pdb/goddamn"
}

# Ora usa Path senza preoccuparti dei backslash
cal_maintenance_plans_path = Path(input_paths_dict['main_path'], input_paths_dict['cal_plans_folder_name'])

print(cal_maintenance_plans_path)