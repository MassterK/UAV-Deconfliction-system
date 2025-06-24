# === interface.py ===
from flight_schedule_loader import load_simulated_drones
from conflict_checker import check_conflicts

def check_mission_conflict(primary_mission):
    simulated_drones = load_simulated_drones()
    return check_conflicts(primary_mission, simulated_drones)

