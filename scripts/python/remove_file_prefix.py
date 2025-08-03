import os
import shutil
import random

from pathlib import Path

image_dir = "../damn-yankee-data/yolo/labels/"

for old_name in os.listdir(image_dir):
    new_name = old_name.split("-", maxsplit=1)[-1]
    old_path = Path(image_dir).joinpath(old_name)
    new_path = Path(image_dir).joinpath(new_name)
    os.rename(old_path, new_path)