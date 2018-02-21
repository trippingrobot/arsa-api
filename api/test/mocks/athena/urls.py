from __future__ import unicode_literals

from .responses import AthenaHandler

url_bases = [
    "https?://athena.(.+).amazonaws.com"
]

url_paths = {
    "{0}/": AthenaHandler.dispatch,
}
