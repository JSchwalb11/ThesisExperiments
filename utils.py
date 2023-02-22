from pathlib import Path
import os
import yaml

def create_run_configs(dcfg_dir=Path("./data_configs"),
                       mcfg_dir = Path("./model_configs"),
                       rcfg_dir = Path("./run_configs")):

    data_cfgs = os.listdir(dcfg_dir)
    model_cfgs = os.listdir(mcfg_dir)

    rcfg_fp = rcfg_dir.joinpath("default.yaml")

    with open(rcfg_fp, 'r') as rcfg:
        run_yaml = yaml.safe_load(rcfg)

    for dcfg in data_cfgs:
        dcfg_path = dcfg_dir.joinpath(dcfg)
        run_yaml['data'] = str(dcfg_path).replace("\\", "/")
        for mcfg in model_cfgs:
            mcfg_path = mcfg_dir.joinpath(mcfg)
            run_yaml['model'] = str(mcfg_path).replace("\\", "/")


            new_cfg_fn = f"{dcfg_path.stem}_{mcfg_path.stem}.yaml"
            with open(rcfg_dir.joinpath(new_cfg_fn), 'w') as f:
                yaml.safe_dump(run_yaml, f)

def yaml_load(file='data.yaml', append_filename=False):
    """
    Load YAML data from a file.
    Args:
        file (str, optional): File name. Default is 'data.yaml'.
        append_filename (bool): Add the YAML filename to the YAML dictionary. Default is False.
    Returns:
        dict: YAML data and file name.

    Function taken from ultralytics repo
    """

    with open(file, errors='ignore', encoding='utf-8') as f:
        # Add YAML filename to dict and return
        s = f.read()  # string
        if not s.isprintable():  # remove special characters
            s = re.sub(r'[^\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010ffff]+', '', s)
        return {**yaml.safe_load(s), 'yaml_file': str(file)} if append_filename else yaml.safe_load(s)