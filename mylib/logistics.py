"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel between two points and other logistics related questions
for a given speed.

For example this module can be used to calculate the distance between two cities
from geopy import distance
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)
"""
from geopy import distance

# build a list of cities with their coordinates
# make a list of cities
CITIES = [
    ("New York", (40.7128, -74.0060)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Chicago", (41.8781, -87.6298)),
    ("Houston", (29.7604, -95.3698)),
    ("Phoenix", (33.4484, -112.0740)),
    ("Philadelphia", (39.9526, -75.1652)),
    ("San Antonio", (29.4241, -98.4936)),
    ("San Diego", (32.7157, -117.1611)),
    ("Dallas", (32.7767, -96.7970)),
    ("San Jose", (37.3382, -121.8863)),
    ("Austin", (30.2672, -97.7431)),
    ("Jacksonville", (30.3322, -81.6557)),
    ("San Francisco", (37.7749, -122.4194)),
    ("Indianapolis", (39.7684, -86.1581)),
    ("Columbus", (39.9612, -82.9988)),
    ("Fort Worth", (32.7555, -97.3308)),
    ("Charlotte", (35.2271, -80.8431)),
    ("Detroit", (42.3314, -83.0458)),
    ("El Paso", (31.7776, -106.4424)),
]


def distance_between_two_points(point1, point2):
    """
    Calculate the distance between two points
    """
    return distance.distance(point1, point2).miles


# calculate the total distance between a list of cities
def total_distance(cities):
    """
    Calculate the total distance between a list of cities
    """
    total = 0
    for i in range(len(cities) - 1):
        total += distance_between_two_points(cities[i], cities[i + 1])
    return total
