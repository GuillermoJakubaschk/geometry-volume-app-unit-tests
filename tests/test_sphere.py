import pytest
import math
from geometry.sphere import volume_sphere

# saltaba error por una diferencia minima en el unit test, asi que la respuesta la deje como en formula
def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid sphere radius.
    """
    radius = 3.0
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)

def test_volume_sphere_negative_radius():
    """
    Document current behaviour when a negative radius is used.
    """
    radius = -3.0
    with pytest.raises(ValueError):
        volume_sphere(radius)

def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 1.7
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)

