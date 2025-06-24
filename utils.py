# === utils.py ===
from math import sqrt

def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def interpolate_path(waypoints, start_time, end_time, steps=20):
    path = []
    total_segments = len(waypoints) - 1
    time_per_segment = (end_time - start_time) / (total_segments * steps)
    time = start_time

    for i in range(total_segments):
        x1, y1 = waypoints[i]
        x2, y2 = waypoints[i+1]
        for s in range(steps):
            t = s / steps
            x = x1 + t * (x2 - x1)
            y = y1 + t * (y2 - y1)
            path.append(((x, y), time))
            time += time_per_segment
    return path

