"""
Input validation functions for form data
"""

import re
from datetime import datetime


class ValidationError(Exception):
    """Custom validation error"""
    pass


def validate_username(username):
    """
    Validate username
    Rules: 3-20 characters, alphanumeric and underscore only
    """
    if not username:
        raise ValidationError("Username is required")
    
    if len(username) < 3:
        raise ValidationError("Username must be at least 3 characters")
    
    if len(username) > 20:
        raise ValidationError("Username must not exceed 20 characters")
    
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        raise ValidationError("Username can only contain letters, numbers, and underscores")
    
    return True


def validate_email_format(email):
    """Validate email format"""
    if not email:
        raise ValidationError("Email is required")
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError("Invalid email format")
    
    if len(email) > 100:
        raise ValidationError("Email is too long")
    
    return True


def validate_password_complexity(password):
    """
    Validate password complexity
    Rules: min 8 chars, uppercase, lowercase, digit
    """
    if not password:
        raise ValidationError("Password is required")
    
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters")
    
    if len(password) > 128:
        raise ValidationError("Password is too long")
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        raise ValidationError("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        raise ValidationError("Password must contain at least one digit")
    
    return True


def validate_phone_number(phone):
    """Validate phone number (basic validation)"""
    if not phone:
        return True  # Phone is optional
    
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    
    if not re.match(r'^\+?[0-9]{10,15}$', cleaned):
        raise ValidationError("Invalid phone number format")
    
    return True


def validate_date_format(date_string, format_str='%Y-%m-%d'):
    """Validate date string format"""
    if not date_string:
        raise ValidationError("Date is required")
    
    try:
        datetime.strptime(date_string, format_str)
        return True
    except ValueError:
        raise ValidationError(f"Invalid date format. Expected: {format_str}")


def validate_future_date(date_string, format_str='%Y-%m-%d'):
    """Validate that date is in the future"""
    validate_date_format(date_string, format_str)
    date_obj = datetime.strptime(date_string, format_str)
    
    if date_obj <= datetime.now():
        raise ValidationError("Date must be in the future")
    
    return True


def validate_integer_range(value, min_val=None, max_val=None, field_name="Value"):
    """Validate integer is within range"""
    try:
        int_value = int(value)
    except (ValueError, TypeError):
        raise ValidationError(f"{field_name} must be a valid integer")
    
    if min_val is not None and int_value < min_val:
        raise ValidationError(f"{field_name} must be at least {min_val}")
    
    if max_val is not None and int_value > max_val:
        raise ValidationError(f"{field_name} must not exceed {max_val}")
    
    return True


def validate_file_size(file_size, max_size_mb=10):
    """Validate file size in bytes"""
    max_bytes = max_size_mb * 1024 * 1024
    
    if file_size > max_bytes:
        raise ValidationError(f"File size must not exceed {max_size_mb}MB")
    
    return True


def validate_file_extension(filename, allowed_extensions):
    """Validate file extension"""
    if not filename:
        raise ValidationError("Filename is required")
    
    if '.' not in filename:
        raise ValidationError("File must have an extension")
    
    ext = filename.rsplit('.', 1)[1].lower()
    
    if ext not in allowed_extensions:
        raise ValidationError(f"File type not allowed. Allowed types: {', '.join(allowed_extensions)}")
    
    return True


def validate_url(url):
    """Basic URL validation"""
    if not url:
        raise ValidationError("URL is required")
    
    url_pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not url_pattern.match(url):
        raise ValidationError("Invalid URL format")
    
    return True


def sanitize_string(input_string, max_length=None):
    """Sanitize string input"""
    if not input_string:
        return ""
    
    # Remove leading/trailing whitespace
    cleaned = input_string.strip()
    
    # Remove potentially dangerous characters
    cleaned = re.sub(r'[<>"\';(){}]', '', cleaned)
    
    if max_length and len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    return cleaned