import server_status as stats
import unittest


class TestServerStatus(unittest.TestCase):

    def test_get_disck_usage(self):
        # Test Case 1
        resualt = stats.get_disk_usage()
        self.assertTrue(isinstance(resualt, dict))

        self.assertTrue('total' in resualt)
        self.assertTrue(isinstance(resualt['total'], int))
        self.assertTrue('used' in resualt)
        self.assertTrue(isinstance(resualt['used'], int))
        self.assertTrue('free' in resualt)
        self.assertTrue(isinstance(resualt['free'], int))

    def test_get_memory_usage(self):
        # Test Case 1
        resualt = stats.get_memory_usage()
        self.assertTrue(isinstance(resualt, dict))

        self.assertTrue('total' in resualt)
        self.assertTrue(isinstance(resualt['total'], int))
        self.assertTrue('used' in resualt)
        self.assertTrue(isinstance(resualt['used'], int))
        self.assertTrue('free' in resualt)
        self.assertTrue(isinstance(resualt['free'], int))

    def test_get_cpu_usage(self):
        # Test Case 1
        resualt = stats.get_cpu_usage()
        self.assertTrue(isinstance(resualt, float))


if __name__ == '__main__':
    unittest.main()

