from mylib.logistics import CITIES, distance_between_two_points, print_cities


def test_distance_between_two_points():
    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 2450.9503446683375


def test_print_cities():
    assert "Dallas" in print_cities()
