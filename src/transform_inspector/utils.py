from typing import Union, List
from PIL import Image
import torch
from torchvision.transforms.functional import to_pil_image
from torchvision.transforms import Compose


def load_image(image: Union[str, Image.Image]) -> Image.Image:
    """
    Load an image from a file path or return it if already a PIL Image.
    Always returns a RGB PIL Image.
    """
    if isinstance(image, Image.Image):
        return image.convert("RGB")

    if isinstance(image, str):
        return Image.open(image).convert("RGB")

    raise TypeError("image must be a file path or PIL.Image.Image")


def to_displayable(img):
    """
    Convert a Tensor or PIL image into a PIL image for visualization.
    """
    if isinstance(img, Image.Image):
        return img

    if torch.is_tensor(img):
        if img.ndim != 3:
            raise ValueError("Tensor image must have shape (C, H, W)")
        return to_pil_image(img)

    raise TypeError("Unsupported image type for display")


def unwrap_transforms(transform) -> List:
    """
    Extract individual transforms from torchvision.transforms.Compose
    or wrap a single transform into a list.
    """
    if isinstance(transform, Compose):
        return list(transform.transforms)

    return [transform]


def get_transform_names(transforms: List) -> List[str]:
    """
    Get readable class names for each transform.
    """
    return [t.__class__.__name__ for t in transforms]
