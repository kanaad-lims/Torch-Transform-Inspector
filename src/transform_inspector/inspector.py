from typing import Union
from PIL import Image

from torchvision.transforms import Compose

from .utils import (
    load_image,
    unwrap_transforms,
    to_displayable,
    get_transform_names,
)
from .visualization import show_image_grid


def inspect_transforms(
    image: Union[str, Image.Image],
    transform,
    cols: int = 3,
):
    """
    Visualize step-by-step effects of torchvision transforms on an image.

    Args:
        image: Image file path or PIL.Image.Image.
        transform: torchvision transform or transforms.Compose.
        cols: Number of columns in the visualization grid.
    """
    # 1. Load and normalize image
    img = load_image(image)

    # 2. Unwrap transform pipeline
    transforms_list = unwrap_transforms(transform)
    transform_names = get_transform_names(transforms_list)

    # 3. Apply transforms one-by-one and collect images
    images = [to_displayable(img)]
    current = img

    for t in transforms_list:
        current = t(current)
        images.append(to_displayable(current))

    # 4. Titles: Original + transform names
    titles = ["Original"] + transform_names

    # 5. Display
    show_image_grid(images=images, titles=titles, cols=cols)


def inspect_random(
    image: Union[str, Image.Image],
    transform,
    n: int = 6,
    cols: int = 3,
):
    """
    Visualize randomness by applying the full transform pipeline multiple times.

    Args:
        image: Image file path or PIL.Image.Image.
        transform: torchvision transform or transforms.Compose.
        n: Number of random samples to generate.
        cols: Number of columns in the visualization grid.
    """
    # Load and normalize image
    img = load_image(image)

    images = []
    titles = []

    for i in range(n):
        out = transform(img)
        images.append(to_displayable(out))
        titles.append(f"Sample {i+1}")

    show_image_grid(images=images, titles=titles, cols=cols)
