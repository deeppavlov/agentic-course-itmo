import yaml

def load_config(path="config/app.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)
