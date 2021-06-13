import unittest
from prepareEnv import prepareEnviroment
import test_db
import test_API
import test_iFrame
import os
from unittest.suite import TestSuite

prepareEnviroment()

suite = TestSuite()
tests = unittest.TestLoader()

suite.addTests(tests.loadTestsFromTestCase(test_API.APITestCase))
suite.addTests(tests.loadTestsFromTestCase(test_db.SqliteTestCase))
suite.addTests(tests.loadTestsFromTestCase(test_iFrame.iFrameTestCase))

runner = unittest.TextTestRunner()
runner.run(suite)

if os.path.exists("example.jpg"):
    os.remove("example.jpg")
if os.path.exists("database.db"):
    os.remove("database.db")