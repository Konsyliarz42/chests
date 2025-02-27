from pathlib import Path
from typing import Final
from zipfile import ZipFile

PACKAGE_NAME: Final = "Chests"
REQUIRED_PATHS: Final = [
    Path("assets"),
    Path("pack.png"),
    Path("pack.mcmeta"),
]
IGNORED_SUFFIXES: Final = [
    ".pfi",
]


def check_required_paths(paths: list[Path]) -> None:
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Required path: `{path.name}` not found.")


def add_file_to_zip(zip: ZipFile, file: Path) -> None:
    if file.suffix not in IGNORED_SUFFIXES:
        zip.write(file)


def create_zip_file(zip_name: str, zip_content: list[Path]) -> None:
    with ZipFile(zip_name, "w") as zip:
        for target in zip_content:
            if target.is_dir():
                [add_file_to_zip(zip, file) for file in target.glob("**/*") if file.is_file()]
            else:
                add_file_to_zip(zip, target)


if __name__ == "__main__":
    print("Create a new zip file")
    check_required_paths(REQUIRED_PATHS)

    version = input("Version: ")
    zip_name = f"{PACKAGE_NAME}-{version}.zip"
    create_zip_file(zip_name, REQUIRED_PATHS)
    print("Zip created:", zip_name)
