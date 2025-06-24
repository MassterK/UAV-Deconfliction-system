# === visualizer.py ===
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from flight_schedule_loader import load_simulated_drones
from utils import interpolate_path


def plot_paths(primary, conflicts):
    drones = load_simulated_drones()

    plt.figure(figsize=(10, 6))

    # Plot primary mission
    px, py = zip(*primary["waypoints"])
    plt.plot(px, py, 'b-o', label="Primary Drone")

    # Plot other drones
    for drone in drones:
        dx, dy = zip(*drone["waypoints"])
        plt.plot(dx, dy, 'g--', alpha=0.6, label=f"{drone['id']}")

    # Plot conflicts
    shown = set()
    for conflict in conflicts:
        x, y = conflict["location"]
        label = f"{conflict['conflicting_drone']} @ {int(conflict['time'])}"
        key = (round(x, 1), round(y, 1), conflict['conflicting_drone'])
        if key not in shown:
            plt.plot(x, y, 'rx')
            plt.text(x, y, label, fontsize=8)
            shown.add(key)

    plt.legend()
    plt.title("Drone Deconfliction Visualization")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_4d_paths(primary, conflicts):
    drones = load_simulated_drones()
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot primary mission in 3D (X, Y, Time)
    primary_path = interpolate_path(primary["waypoints"], primary["start_time"], primary["end_time"])
    px, py, pt = zip(*[(x, y, t) for (x, y), t in primary_path])
    ax.plot(px, py, pt, label="Primary Drone", color='blue')

    # Plot other drones
    for drone in drones:
        drone_path = interpolate_path(drone["waypoints"], drone["start_time"], drone["end_time"])
        dx, dy, dt = zip(*[(x, y, t) for (x, y), t in drone_path])
        ax.plot(dx, dy, dt, linestyle='--', alpha=0.5, label=drone["id"])

    # Plot conflicts
    for conflict in conflicts:
        x, y = conflict["location"]
        z = conflict["time"]
        ax.scatter(x, y, z, c='r', marker='x')
        ax.text(x, y, z, f"{conflict['conflicting_drone']} @ {int(z)}", fontsize=8)

    ax.set_title("4D Spatio-Temporal Drone Conflict Visualization")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Time")
    ax.legend()
    plt.tight_layout()
    plt.show()
