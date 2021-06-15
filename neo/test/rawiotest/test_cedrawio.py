import unittest

from neo.rawio.cedrawio import CedRawIO

from neo.test.rawiotest.common_rawio_test import BaseTestRawIO


class TestCedRawIO(BaseTestRawIO, unittest.TestCase, ):
    rawioclass = CedRawIO
    entities_to_test = [
        'spike2/m365_1sec.smrx'
    ]
    entities_to_download = [
        'spike2'
    ]


if __name__ == "__main__":
    unittest.main()
