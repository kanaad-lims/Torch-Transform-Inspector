from torchvision import transforms
from transform_inspector import inspect_transforms, inspect_random

transforms_pipeline = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomResizedCrop(224, scale=(0.3, 0.6), ratio=(0.5, 1.5)),
    transforms.RandomHorizontalFlip(p=1.0),
    transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.1, hue=0.4),
    transforms.RandomRotation(degrees=69),
    transforms.ToTensor(),
])

inspect_transforms("image-path", transforms_pipeline, cols=3)