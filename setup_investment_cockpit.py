import os
from zipfile import ZipFile

PROJECT_NAME = "investment_cockpit"

FILES = {
    "README.md": """# Intelligentes Investment Cockpit by Missalla

Modulare Plattform zur Vermögensanalyse und Entscheidungsunterstützung.
""",

    ".gitignore": """__pycache__/
*.pyc
.env
venv/
.vscode/
.DS_Store
""",

    "requirements.txt": """fastapi
uvicorn
streamlit
pandas
numpy
plotly
sqlalchemy
psycopg2-binary
""",

    "app.py": """import streamlit as st

st.set_page_config(page_title=\"Investment Cockpit\", layout=\"wide\")

st.title(\"📊 Intelligentes Investment Cockpit\")

st.write(\"MVP läuft – Plattform bereit für Erweiterung.\")
""",

    "modules/portfolio.py": """class Portfolio:
    def __init__(self):
        self.positions = []

    def add_position(self, asset, amount, price):
        self.positions.append({
            \"asset\": asset,
            \"amount\": amount,
            \"price\": price
        })

    def total_value(self):
        return sum(p[\"amount\"] * p[\"price\"] for p in self.positions)
""",

    "core/.gitkeep": "",
    "api/.gitkeep": "",
    "data/.gitkeep": "",

    "docs/vision.md": """# Vision

Intelligentes Investment Cockpit – zentrale Plattform für Investmententscheidungen.
""",

    "docs/PRD.md": """# PRD

MVP: Portfolio + Dashboard + Analyse + KI-Unterstützung
""",

    "docs/ROADMAP.md": """# Roadmap

Phase 1: Fundament
Phase 2: Analyse
Phase 3: KI
Phase 4: Plattform
""",

    "docs/SOFTWARE_ARCHITECTURE.md": """# Architecture

Data Layer → Analysis Layer → AI Layer → Cockpit Layer
"""
}


def create_project():
    base = PROJECT_NAME

    for path, content in FILES.items():
        full_path = os.path.join(base, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Projektstruktur '{PROJECT_NAME}' erstellt.")


def create_zip():
    zip_name = f"{PROJECT_NAME}.zip"

    with ZipFile(zip_name, "w") as zipf:
        for root, _, files in os.walk(PROJECT_NAME):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, PROJECT_NAME)
                zipf.write(file_path, arcname)

    print(f"ZIP erstellt: {zip_name}")


if __name__ == "__main__":
    create_project()
    create_zip()