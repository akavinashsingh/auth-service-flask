"""
Utility functions for the application
These functions can be used for future enhancements
"""

import hashlib
import secrets
import string
from datetime import datetime, timedelta
import re


def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password, hashed_password):
    """Verify a password against its hash"""
    return hash_password(plain_password) == hashed_password


def generate_random_token(length=32):
    """Generate a secure random token"""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password_strength(password):
    """
    Check password strength
    Returns tuple (is_valid, message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain lowercase letter"
    if not re.search(r'\d', password):
        return False, "Password must contain a digit"
    return True, "Password is strong"


def sanitize_input(input_string):
    """Remove potentially harmful characters from input"""
    return re.sub(r'[<>"\';(){}]', '', input_string)


def format_timestamp(dt=None):
    """Format datetime object to string"""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def parse_timestamp(timestamp_str):
    """Parse timestamp string to datetime object"""
    try:
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def is_expired(timestamp, hours=24):
    """Check if timestamp is expired"""
    if isinstance(timestamp, str):
        timestamp = parse_timestamp(timestamp)
    if timestamp is None:
        return True
    expiry = timestamp + timedelta(hours=hours)
    return datetime.now() > expiry


def generate_verification_code(length=6):
    """Generate numeric verification code"""
    return ''.join(secrets.choice(string.digits) for _ in range(length))


def mask_email(email):
    """Mask email for privacy (show only first char and domain)"""
    if '@' not in email:
        return email
    local, domain = email.split('@')
    if len(local) <= 2:
        masked_local = local[0] + '*'
    else:
        masked_local = local[0] + '*' * (len(local) - 2) + local[-1]
    return f"{masked_local}@{domain}"


def calculate_percentage(value, total):
    """Calculate percentage with 2 decimal places"""
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)


def truncate_text(text, max_length=100, suffix='...'):
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def get_file_extension(filename):
    """Get file extension from filename"""
    if '.' not in filename:
        return ''
    return filename.rsplit('.', 1)[1].lower()


def is_allowed_file(filename, allowed_extensions):
    """Check if file has allowed extension"""
    ext = get_file_extension(filename)
    return ext in allowed_extensions


def generate_unique_filename(original_filename):
    """Generate unique filename with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = original_filename.rsplit('.', 1) if '.' in original_filename else (original_filename, '')
    return f"{name}_{timestamp}.{ext}" if ext else f"{name}_{timestamp}"