from pathlib import Path
from setuptools import setup


def find_data_files():
    local_base_dir = Path("dll")
    remote_base_dir = Path("Library/bin")
    files = (f for f in local_base_dir.glob("**/*") if f.is_file())
    data_files_tree = {}
    for file in files:
        remote_file = remote_base_dir / file.relative_to(local_base_dir)
        remote_dir = str(remote_file.parent)
        if remote_dir not in data_files_tree:
            data_files_tree[remote_dir] = []
        data_files_tree[remote_dir].append(str(file))
    return list(data_files_tree.items())


print(find_data_files())

setup(name="openvino_rt",
      version="2019.1.148",
      packages=["sample"],
      package_dir={"sample": "src/sample"},
      data_files=find_data_files())
