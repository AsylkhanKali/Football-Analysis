from utils.bbox_utils import (
    get_bbox_width,
    get_center_of_bbox,
    get_foot_position,
    measure_distance,
    measure_xy_distance,
)


def test_bbox_geometry():
    bbox = [10, 20, 30, 60]

    assert get_center_of_bbox(bbox) == (20, 40)
    assert get_foot_position(bbox) == (20, 60)
    assert get_bbox_width(bbox) == 20


def test_point_distances():
    assert measure_distance((0, 0), (3, 4)) == 5
    assert measure_xy_distance((7, 3), (2, 5)) == (5, -2)

