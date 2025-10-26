import subprocess
import sys
import os

def run_tests():
    try:
        import pytest
    except ImportError:
        print("ОШИБКА: pytest не установлен!")
        print("Запусти: pip install pytest pytest-cov")
        sys.exit(1)

    project_root = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["PYTHONPATH"] = project_root

    cmd = [
        sys.executable, "-m", "pytest",
        "tests/",
        "--cov=lab2",
        "--cov-report=term-missing",
        "--cov-fail-under=85",
        "-v"
    ]

    print("Запуск тестов с покрытием (lab2)...")
    result = subprocess.run(cmd, env=env)
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_tests()