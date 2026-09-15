import pickle

import numpy as np

from camera_movement_estimator import CameraMovementEstimator


def test_get_camera_movement_returns_cached_data(tmp_path):
    cached = [[0, 0], [3.5, -1.0]]
    stub_path = tmp_path / "camera_movement.pkl"
    with stub_path.open("wb") as file:
        pickle.dump(cached, file)

    first_frame = np.zeros((64, 64, 3), dtype=np.uint8)
    estimator = CameraMovementEstimator(first_frame)

    result = estimator.get_camera_movement(
        frames=[],
        read_from_stub=True,
        stub_path=stub_path,
    )

    assert result == cached

