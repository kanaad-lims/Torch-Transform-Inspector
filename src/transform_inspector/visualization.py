from typing import List, Optional
import math
import matplotlib.pyplot as plt
from PIL import Image


def show_image_grid(
    images: List[Image.Image],
    titles: List[str],
    cols: int = 3,
    figsize: Optional[tuple] = None,
):
    """
    Display images in a matplotlib grid with titles.

    Args:
        images: List of PIL Images.
        titles: List of titles corresponding to images.
        cols: Number of columns in the grid.
        figsize: Optional matplotlib figsize.
    """
    if len(images) != len(titles):
        raise ValueError("Number of images and titles must match")

    num_images = len(images)
    cols = min(cols, num_images)
    rows = math.ceil(num_images / cols)

    if figsize is None:
        figsize = (4 * cols, 4 * rows)

    fig, axes = plt.subplots(rows, cols, figsize=figsize)

    # Normalize axes to a flat list
    if rows == 1 and cols == 1:
        axes = [axes]
    elif rows == 1 or cols == 1:
        axes = axes.flatten()
    else:
        axes = axes.ravel()

    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img)
        ax.set_title(title, fontsize=10)
        ax.axis("off")

    # Disable unused axes
    for ax in axes[len(images):]:
        ax.axis("off")

    plt.tight_layout()
    plt.show()
