# === flight_schedule_loader.py ===
def load_simulated_drones():
    return [
        {
            "id": "drone_1",
            "waypoints": [(5, 5), (15, 15)],
            "start_time": 40,
            "end_time": 80
        },
        {
            "id": "drone_2",
            "waypoints": [(0, 0), (20, 5)],
            "start_time": 50,
            "end_time": 90
        }
    ]

