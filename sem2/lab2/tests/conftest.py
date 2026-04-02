from pathlib import Path
import sys


LAB2_ROOT = Path(__file__).resolve().parents[1]

if str(LAB2_ROOT) not in sys.path:
    sys.path.insert(0, str(LAB2_ROOT))
