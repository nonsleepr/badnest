"""
A script to explore Nest API.

Usage:

1. Populate file `scripts/creds.json`
2. Run `python scripts/explore.py`
"""
import sys
from pathlib import Path

sys.path.append("custom_components")
from unittest.mock import patch, MagicMock
import json

KNOWN_BUCKET_TYPES = ["buckets", "delayed_topaz", "demand_response", "device",
                      "device_alert_dialog", "geofence_info", "kryptonite",
                      "link", "message", "message_center", "metadata",
                      "occupancy", "quartz", "safety", "rcs_settings",
                      "safety_summary", "schedule", "shared", "structure",
                      "structure_history", "structure_metadata", "topaz",
                      "topaz_resource", "track", "trip", "tuneups", "user",
                      "user_alert_dialog", "user_settings", "where",
                      "widget_track"]

SUBSCRIBE_WHITELIST = ["schedule", "tuneups", "metadata", "user_alert_dialog",
                       "delayed_topaz"]



def main():
    from badnest.api import NestAPI
    with open(Path(__file__).absolute().parent.joinpath("creds.json")) as f:
       creds = json.load(f)
    cookie = creds["cookie"]
    token = creds["issuetoken"]
    nest = NestAPI(None,None,token,cookie,None)
    print(nest.presence)


if __name__ == "__main__":
    mock_module = MagicMock()
    with patch.dict("sys.modules", {"voluptuous": mock_module, "homeassistant.helpers": mock_module}):
        with patch("badnest.api.KNOWN_BUCKET_TYPES", KNOWN_BUCKET_TYPES):
            main()
