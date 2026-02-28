from pathlib import Path
import sys


LAB1_DIR = Path(__file__).resolve().parents[1]
ENTITIES_DIR = LAB1_DIR / "Entities"

if str(LAB1_DIR) not in sys.path:
    sys.path.insert(0, str(LAB1_DIR))

if str(ENTITIES_DIR) not in sys.path:
    sys.path.insert(0, str(ENTITIES_DIR))
