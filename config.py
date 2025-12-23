"""
Configuration settings for the application
"""

import os
from datetime import timedelta


class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # File upload configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt'}
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    
    # Security settings
    BCRYPT_LOG_ROUNDS = 12
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_REQUIRE_UPPERCASE = True
    PASSWORD_REQUIRE_LOWERCASE = True
    PASSWORD_REQUIRE_DIGITS = True
    PASSWORD_REQUIRE_SPECIAL = False
    
    # Email configuration (for future use)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')
    
    # Pagination
    ITEMS_PER_PAGE = 20
    
    # Rate limiting
    RATELIMIT_ENABLED = True
    RATELIMIT_STORAGE_URL = os.getenv('REDIS_URL', 'memory://')
    RATELIMIT_DEFAULT = "100 per hour"
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = 'app.log'
    
    # Encryption settings
    ENCRYPTION_ALGORITHM = 'AES-256'
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
    
    # Token expiration times
    ACCESS_TOKEN_EXPIRY = timedelta(hours=1)
    REFRESH_TOKEN_EXPIRY = timedelta(days=30)
    RESET_TOKEN_EXPIRY = timedelta(hours=2)
    VERIFICATION_CODE_EXPIRY = timedelta(minutes=15)


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    
    # More strict settings for production
    PERMANENT_SESSION_LIFETIME = timedelta(hours=12)


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'
    SESSION_COOKIE_SECURE = False
    BCRYPT_LOG_ROUNDS = 4  # Faster for testing


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(config_name=None):
    """Get configuration based on environment"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    return config.get(config_name, config['default'])