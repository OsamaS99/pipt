import os
import sys
import pytest


@pytest.fixture(scope="session")
def vcr_config():
    return {
        "cassette_library_dir": os.path.join(os.path.dirname(__file__), "cassettes"),
        "record_mode": os.environ.get("VCR_RECORD_MODE", "once"),
        "filter_headers": ["authorization"],
    }
