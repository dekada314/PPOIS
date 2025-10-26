import subprocess
import sys
import os
import pytest

def run_all_tests():

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    env = os.environ.copy()
    env["PYTHONPATH"] = project_root

    cmd = [
        sys.executable, "-m", "pytest",
        ".",  
        "--cov=.", 
        "--cov-report=term-missing",
        "--cov-report=html:../htmlcov_all",
        "--cov-fail-under=85",
        "--cov-branch",
        "-v"
    ]

    print("Запуск всех тестов (employee, finance, management, projects, assets)...")
    result = subprocess.run(cmd, env=env, cwd=os.path.dirname(__file__))

    if result.returncode == 0:
        print("\nУСПЕХ: Покрытие >=95% для всех модулей")
        print("Отчёт: ../htmlcov_all/index.html")
    else:
        print("\nОШИБКА: Покрытие <95% или тесты упали")
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()