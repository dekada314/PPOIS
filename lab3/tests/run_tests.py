# import subprocess
# import sys
# import os

# def run_all_tests():
#     project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     env = os.environ.copy()
#     env["PYTHONPATH"] = project_root

#     cmd = [
#         sys.executable, "-m", "pytest",
#         "tests/",
#         "--cov=lab3",
#         "--cov-report=term-missing",
#         "--cov-report=html:coverage_html",
#         "--cov-fail-under=85",
#         "--cov-branch",
#         "-v"
#     ]

#     print("Запуск тестов для module_medical...")
#     result = subprocess.run(cmd, env=env, cwd=project_root)

#     if result.returncode == 0:
#         print("\nУСПЕХ: Тесты прошли, покрытие ≥85%")
#     else:
#         print("\nОШИБКА: Тесты упали или покрытие <85%")
#         sys.exit(1)

# if __name__ == "__main__":
#     run_all_tests()