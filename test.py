import unittest

if __name__ == '__main__':
    
    loader = unittest.TestLoader()
    directoire = "test/"
    suite = loader.discover(directoire)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)