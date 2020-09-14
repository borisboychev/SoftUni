import os

__version__ = "0.1.0"

def setup(build_id=None, build_secret=None):
    from unittest_continuous.decorators import _makeResultWrap
    
    build_id = build_id or os.environ.get("BUILD_ID", None)
    build_secret = build_secret or os.environ.get("BUILD_SECRET", None)
    
    if not build_id:
        raise Exception("Could not determine the build ID. Make sure the BUILD_ID environment variable is set.")
    
    if not build_secret:
        raise Exception("Could not determine the build secret. Make sure the BUILD_SECRET environment variable is set.")
    
    # Now do the patching (TODO: clean this up)
    
    # Monkey-patch unitest module
    try:
        import unittest
        unittest.TextTestRunner._makeResult = _makeResultWrap(unittest.TextTestRunner._makeResult, build_id, build_secret)
    except ImportError:
        pass
    
    # Monkey-patch unitest2 module
    try:
        import unittest2
        unittest2.TextTestRunner._makeResult = _makeResultWrap(unittest2.TextTestRunner._makeResult, build_id, build_secret)
    except ImportError:
        pass
    
    # Monkey-patch nose
    try:
        import nose.core
        nose.core.TextTestRunner._makeResult = _makeResultWrap(nose.core.TextTestRunner._makeResult, build_id, build_secret)
    except ImportError:
        pass
    
    # Disable django-nose if present
    try:
        from django.conf import settings
        # Nose does not play well with continuous, as it's TestTextRunner never 
        # calls the unittest.TestTextRunner._makeResult (i.e. super) method, so 
        # lets make sure we set it back to the default if it is present
        test_runner = getattr(settings, "TEST_RUNNER", "")
        if test_runner and "nose" in test_runner.lower():
            import django.conf.global_settings
            settings.TEST_RUNNER = django.conf.global_settings.TEST_RUNNER
        
    except ImportError:
        pass