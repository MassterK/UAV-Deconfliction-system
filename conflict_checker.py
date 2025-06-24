# === conflict_checker.py ===
from utils import euclidean_distance, interpolate_path

def check_conflicts(primary, others, min_dist=5.0):
    conflicts = []
    primary_path = interpolate_path(primary["waypoints"], primary["start_time"], primary["end_time"])

    for drone in others:
        other_path = interpolate_path(drone["waypoints"], drone["start_time"], drone["end_time"])

        for (p_pos, p_time) in primary_path:
            for (o_pos, o_time) in other_path:
                if abs(p_time - o_time) <= 1:
                    if euclidean_distance(p_pos, o_pos) < min_dist:
                        conflicts.append({
                            "location": p_pos,
                            "time": p_time,
                            "conflicting_drone": drone["id"]
                        })

    if conflicts:
        return {"status": "conflict_detected", "conflicts": conflicts}
    return {"status": "clear", "conflicts": []}

