"""
Tests that do not need an ELO server. They also run locally without the TEST_ELO_IX_* environment variables.
"""
import unittest

from eloservice.file_util import _guess_mimetype


class TestGuessMimetype(unittest.TestCase):

    def test_unknown_extension_falls_back_to_octet_stream(self):
        # https://github.com/treskon/elo-indexserver-client/issues/33
        self.assertEqual("application/octet-stream", _guess_mimetype("file.unknownextension"))

    def test_no_extension_falls_back_to_octet_stream(self):
        self.assertEqual("application/octet-stream", _guess_mimetype("README"))
        self.assertEqual("application/octet-stream", _guess_mimetype(""))

    def test_jpeg_is_mapped_to_jpg(self):
        self.assertEqual("image/jpg", _guess_mimetype("mona.jpeg"))
        self.assertEqual("image/jpg", _guess_mimetype("mona.JPG"))

    def test_known_types(self):
        self.assertEqual("image/png", _guess_mimetype("testFile.png"))
        self.assertEqual("application/pdf", _guess_mimetype("chicken.pdf"))


if __name__ == '__main__':
    unittest.main()
