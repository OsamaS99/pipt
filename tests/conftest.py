import os
import sys
import pytest

# Ensure local src/ takes precedence over any installed pipt
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "cassette_library_dir": os.path.join(os.path.dirname(__file__), "cassettes"),
        "record_mode": os.environ.get("VCR_RECORD_MODE", "once"),
        "filter_headers": ["authorization"],
    }
