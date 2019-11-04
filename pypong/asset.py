from pathlib import Path


def get_assets_dir():
    return '{}/assets'.format(Path(__file__).parent.parent)
