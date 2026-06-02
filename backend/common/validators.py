"""Reusable validation helpers for uploaded files."""

from django.core.exceptions import ValidationError

MAX_UPLOAD_SIZE = 5 * 1024 * 1024
ALLOWED_IMAGE_TYPES = {'image/gif', 'image/jpeg', 'image/png', 'image/webp'}


def validate_image_upload(image_file) -> None:
    """Validate uploaded image type and size."""
    if image_file is None:
        return

    if image_file.size > MAX_UPLOAD_SIZE:
        raise ValidationError('Image size must be less than 5MB.')

    if image_file.content_type not in ALLOWED_IMAGE_TYPES:
        raise ValidationError(
            'Only JPEG, PNG, GIF, and WebP images are allowed.'
        )
