# Mini-Taschenrechner

Dieses Projekt dient dazu, Git und Teamarbeit kennenzulernen. Ziel ist es, gemeinsam einen Taschenrechner zu entwickeln, bei dem jede Gruppe ein Rechenmodul beiträgt.

## Aufbau
- `main.py`: Führt alle Rechenfunktionen zusammen
- `features/`: Hier landen die Module der Gruppen, z. B. `add.py`, `subtract.py` etc.

## Strucktur: mini_calculator
```
mini_calculator/
├── main.py                 # Hauptprogramm mit Funktionsaufrufen
├── README.md               # Projektbeschreibung und Aufgaben
└── features/               # Hier kommen alle Rechenfunktionen rein
    ├── __init__.py         # Macht das Verzeichnis zu einem Python-Paket
    └── add.py              # Beispielmodul: Addition
```
## Aufgabe pro Gruppe
1. Hölt euch den Code (git clone oder Fork)
2. Erstellt einen Branch für euer Feature: z. B. `feature/multiply`
3. Erstellt ein neues Python-File in `features/`, z. B. `multiply.py`
4. Schreibt eine `calculate(a, b)` Funktion
5. Binde sie in `main.py` ein
6. Committen, pushen, Pull Request stellen

## Beispiel: `multiply.py`
```python
def calculate(a, b):
    return a * b