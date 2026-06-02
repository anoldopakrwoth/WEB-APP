"""Reusable validation helpers for uploaded files."""

from django.core.exceptions import ValidationError

MAX_UPLOAD_SIZE = 5 * 1024 * 1024
MAX_VIDEO_UPLOAD_SIZE = 2 * 1024 * 1024
ALLOWED_IMAGE_TYPES = {'image/gif', 'image/jpeg', 'image/png', 'image/webp'}
ALLOWED_VIDEO_TYPES = {'video/mp4', 'video/quicktime', 'video/webm'}


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


def validate_video_upload(video_file) -> None:
    """Validate uploaded harvest video type and size."""
    if video_file is None:
        return

    if video_file.size > MAX_VIDEO_UPLOAD_SIZE:
        raise ValidationError('Video size must be less than 2MB (2048KB).')

    if video_file.content_type not in ALLOWED_VIDEO_TYPES:
        raise ValidationError(
            'Only MP4, MOV, and WebM videos are allowed.'
        )
