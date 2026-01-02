def test_public_api_imports():
    from transform_inspector import inspect_transforms, inspect_random
    assert callable(inspect_transforms)
    assert callable(inspect_random)


def test_utils_imports():
    from transform_inspector.utils import (
        load_image,
        unwrap_transforms,
        to_displayable,
        get_transform_names,
    )
    assert callable(load_image)
    assert callable(unwrap_transforms)
    assert callable(to_displayable)
    assert callable(get_transform_names)
