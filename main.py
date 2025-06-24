# === main.py ===
from interface import check_mission_conflict
from visualizer import plot_paths, plot_4d_paths

primary_mission = {
    "waypoints": [(0, 0), (10, 10), (20, 5)],
    "start_time": 0,
    "end_time": 100
}

if __name__ == "__main__":
    result = check_mission_conflict(primary_mission)
    print(result)

    if result["status"] == "conflict_detected":
        print("Conflicts detected:")
        for c in result["conflicts"]:
            print(c)

    plot_paths(primary_mission, result["conflicts"])
    plot_4d_paths(primary_mission, result["conflicts"])

