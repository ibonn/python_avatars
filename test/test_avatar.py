import os
import random
import pytest

import python_avataaars as pa


def test_avatar_generation():
    assert pa.Avatar().render("avatar.svg") != ""
    assert os.path.isfile("avatar.svg")


def test_random_avatar():
    random.seed(123)

    avatar_1 = pa.Avatar.random()
    avatar_2 = pa.Avatar.random()

    assert avatar_1 != avatar_2


def test_not_installable():
    with pytest.raises(RuntimeError):
        pa.install_part("../examples/install/suit.svg", pa.TopType)


def test_install_installed_part():
    pa.install_part("../examples/install/suit.svg", pa.ClothingType)
    with pytest.raises(RuntimeError):
        pa.install_part("../examples/install/suit.svg", pa.ClothingType)


def test_cross_install():
    with pytest.raises(RuntimeError):
        pa.install_part("../examples/install/suit.svg", pa.HairColor)


def test_bad_install():
    with pytest.raises(RuntimeError):
        pa.install_part("this_file_does_not_exist.svg", pa.HairType)
