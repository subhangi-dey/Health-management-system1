import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hms-super-secret-key-2026-college-project'
    
    # SQLite default database for easy zero-config execution
    # To use MySQL: 'mysql+pymysql://username:password@localhost/hms_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload Configurations
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    REPORTS_FOLDER = os.path.join(UPLOAD_FOLDER, 'reports')
    BILLS_FOLDER = os.path.join(UPLOAD_FOLDER, 'bills')
    PROFILE_FOLDER = os.path.join(UPLOAD_FOLDER, 'profile')
    
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB limit
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
