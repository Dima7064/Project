"""Сборка .exe через PyInstaller (onedir режим)."""
import sys
from pathlib import Path
import PyInstaller.__main__
def main() -> None:
    root = Path(__file__).resolve().parent.parent
    required = [
        "models/plants_lstm.pt",
        "models/products_lstm.pt",
        "models/plants_classifier.pt",
        "models/products_classifier.pt",
        "models/plants_scorers.pt",
        "models/products_scorers.pt",
    ]
    for f in required:
        if not (root / f).exists():
            print(f"Отсутствует {f}.")
            sys.exit(1)
    icon_path = root / "assets" / "icon.ico"
    sep = ";" if sys.platform == "win32" else ":"
    args = [
        str(root / "app" / "main.py"),
        "--name=AgroNomen",
        "--onedir",
        "--console",
        f"--icon={icon_path}",
        f"--add-data={root / 'models'}{sep}models",
        f"--add-data={root / 'data'}{sep}data",
        f"--add-data={root / 'assets'}{sep}assets",
        "--collect-all=gradio",
        "--collect-all=gradio_client",
        "--collect-all=groovy",
        "--collect-all=safehttpx",
        "--collect-all=torch",
        "--collect-all=matplotlib",
        "--exclude-module=torchvision",
        "--exclude-module=torchaudio",
        "--exclude-module=tensorflow",
        "--exclude-module=IPython",
        "--exclude-module=jupyter",
        "--exclude-module=notebook",
        "--exclude-module=tkinter",
        "--exclude-module=pytest",
        f"--paths={root}",
        f"--distpath={root / 'dist'}",
        f"--workpath={root / 'build' / '_work'}",
        f"--specpath={root / 'build'}",
        "--noconfirm",
        "--clean",
    ]

    PyInstaller.__main__.run(args)
    print(f"\nГотово: {root / 'dist' / 'AgroNomen' / 'AgroNomen.exe'}")
