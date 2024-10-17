import unittest


def run_all_tests():
    """Run all tests in the tests directory."""
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='*.py')
    
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_all_tests()
