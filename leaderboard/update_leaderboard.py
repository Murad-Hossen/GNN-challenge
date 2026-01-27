import json
import os

from calculate_scores import get_leaderboard_data


def main() -> None:
    leaderboard_data = get_leaderboard_data()
    output_path = os.path.join(os.path.dirname(__file__), "leaderboard.json")
    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(leaderboard_data, output_file, indent=4)
    print(f"Updated leaderboard at {output_path}")


if __name__ == "__main__":
    main()
