from src.signi_rest_test_runner.scenario_loader import load_scenario
from src.signi_rest_test_runner.executor import execute_scenario
from src.signi_rest_test_runner.validator import validate_scenario
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <scenario_file.yaml>")
        sys.exit(1)

    scenario_path = sys.argv[1]
    scenario = load_scenario(scenario_path)
    results = execute_scenario(scenario)

    for result in results:
        step_name = result.get("name", "Unnamed Step")
        expected = result.get("expected", {})
        actual = result.get("actual", {})

        if expected == actual:
            print(f"PASS : {step_name}")
        else:
            print(f"FAIL : {step_name}")
            print("Expected:", expected)
            print("Got     :", actual)

    validate_scenario(results)
