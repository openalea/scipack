
__all__ = ['Image', 'ImageQt', 'ImageOps']

try:
    import Image
    import ImageOps
except ImportError:
    try:
        from PIL import Image, ImageOps
    except ImportError:
        raise ImportError, "PIL not found. Please install PIL or pillow"

from openalea.image.pil.ImageQt import ImageQt
