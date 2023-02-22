import os
from utils import create_run_configs, yaml_load
from pathlib import Path
import subprocess
from tqdm import tqdm

def run_workflow(rcfg_dir=Path("./run_configs")):
    cfgs = os.listdir(rcfg_dir)

    for cfg in tqdm(cfgs, desc=f"Workflow Progress"):
        c = f"cfg={rcfg_dir.absolute().joinpath(cfg)}"
        subprocess.run(["yolo", c])

if __name__ == '__main__':
    create_run_configs()
    subprocess.run("clearml-init") # init logging
    run_workflow()









