# Torch Transform Inspect

![GitHub stars](https://img.shields.io/github/stars/kanaad-lims/Torch-Transform-Inspector?style=flat-square)
![GitHub watchers](https://img.shields.io/github/watchers/kanaad-lims/Torch-Transform-Inspector?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/kanaad-lims/Torch-Transform-Inspector?style=flat-square)

Visualize and debug **torchvision image transforms** step-by-step using matplotlib.

This library helps you *see* exactly how each transform in your augmentation pipeline affects an image — something that is otherwise hard to reason about.

---

## Installation
```bash
pip install torch-transform-inspect
```

**Import** it in Python using:
```python
from transform_inspector import inspect_transforms, inspect_random
```

> **Note:** The PyPI package name (`torch-transform-inspect`) is different from the Python import name (`transform_inspector`). This is normal because Python module names cannot contain hyphens.

---

## Why this library?

When working with computer vision pipelines, it's often unclear:

- Which transform causes distortion
- Whether augmentation is too aggressive
- Whether transform order is correct
- How randomness affects training data

**Torch Transform Inspect** makes this visual and intuitive.

---

## Basic Usage
```python
from torchvision import transforms
from transform_inspector import inspect_transforms

transform_pipeline = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.5, contrast=0.5),
    transforms.ToTensor(),
])

inspect_transforms("image.jpg", transform_pipeline, cols=3)
```

### What this does

1. Loads the image
2. Applies each transform one by one
3. Displays intermediate outputs in a grid
4. Labels each image with the transform name

---

## Inspecting Randomness

To understand how random augmentations behave:
```python
from transform_inspector import inspect_random

inspect_random("image.jpg", transform_pipeline, n=6, cols=3)
```

This applies the full pipeline multiple times and shows different outputs.

---

## Features

- ✅ Uses native `torchvision.transforms`
- ✅ Supports `Compose` and single transforms
- ✅ Visualizes intermediate steps
- ✅ Read-only (never modifies data)
- ✅ Lightweight and simple API
- ✅ Works in scripts and notebooks

---

## API Reference

### `inspect_transforms(image, transform, cols=3)`

| Parameter | Description |
|-----------|-------------|
| `image` | Image path (str) or PIL.Image |
| `transform` | torchvision transform or transforms.Compose |
| `cols` | Number of columns in the output grid |

**Example:**
```python
inspect_transforms("image.jpg", transform_pipeline, cols=3)
```

---

### `inspect_random(image, transform, n=6, cols=3)`

| Parameter | Description |
|-----------|-------------|
| `image` | Image path (str) or PIL.Image |
| `transform` | torchvision transform or transforms.Compose |
| `n` | Number of random samples |
| `cols` | Number of columns in the grid |

**Example:**
```python
inspect_random("image.jpg", transform_pipeline, n=6, cols=3)
```

---

## Requirements

- Python ≥ 3.8
- torch
- torchvision
- pillow
- matplotlib

---

## License

MIT License

---

## Quick Start Example
```python
# Install
# pip install torch-transform-inspect

from torchvision import transforms
from transform_inspector import inspect_transforms, inspect_random

# Define your transform pipeline
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.3, contrast=0.3),
    transforms.ToTensor(),
])

# Visualize step-by-step
inspect_transforms("path/to/image.jpg", transform)

# Visualize randomness
inspect_random("path/to/image.jpg", transform, n=9)
```

---

## Use Cases

### 1. **Debugging Transform Pipelines**

See exactly which transform is causing unexpected behavior.

### 2. **Tuning Augmentation Strength**

Visually assess if your augmentations are too aggressive or too subtle.

### 3. **Educational Purposes**

Great for teaching and understanding how different transforms work.

### 4. **Dataset Preparation**

Ensure your preprocessing pipeline produces the expected results before training.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Support

For issues, questions, or feature requests, please open an issue on the GitHub repository.

---

## Acknowledgments

Built with ❤️ for the PyTorch computer vision community.
