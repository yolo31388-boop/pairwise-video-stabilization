import pytest
from media import video_stabilization as mod

CASES = [
    ("feature", 'm.feature_confidence(0.2, 0.1) is True'),
    ("window", 'm.window_frames(1.0, 24) == 24'),
    ("crop", 'm.crop_scale(0.5, 1.0) == approx(0.5)'),
    ("rolling", 'm.rolling_shutter_offset(10, 0.01, 2) == approx(0.2)'),
    ("reset", 'm.reset_trajectory(True, [1, 2]) is True'),
    ("key", 'm.camera_trajectory_key("L") == "L"'),
    ("depth", 'm.bit_depth(0.5, 10) == approx(511.5)'),
    ("border", 'm.black_border_fill("reflect") == "reflect"'),
    ("phase", 'm.phase_match(1, 1) is True'),
    ("degrade", 'm.degrade_smoothing(0.5) == approx(0.5)'),
    ("smooth", 'm.smooth_path([0, 2, 4], 2) == approx(3.0)'),
    ("translation", 'm.translation_only((1, 2, 3)) == (1, 2)'),
    ("offset", 'm.stabilize_offset(5, 4) == approx(4.0)'),
    ("cut", 'm.scene_cut_score(0.5, 0.3) is True'),
    ("time", 'm.frame_time(12, 24) == approx(0.5)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
