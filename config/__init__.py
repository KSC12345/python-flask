# coding: UTF-8
import os
def load_config(env=os.environ.get('ENV')):
    """Load config."""
    try:
        if env == 'PROD':
            from .prod import Config
            return Config
        elif env == 'STAGE':
            from .stage import Config
            return Config
        elif env == 'TEST':
            from .test import Config
            return Config
        else:
            from .development import Config
            return Config
    except ImportError:
        from .development import Config
        return Config