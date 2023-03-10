# 1) Register instances
#
# It should be possible to register an instance, identified by an address
#
# Each address should be unique, it should not be possible to register the same address more than once
#
# Load Balancer should accept up to 10 addresses
import random
# 2) Random invocation
#
# Develop an algorithm that, when invoking the Load Balancer 's get() method multiple times,
# should return one backend-instance choosing between the registered ones randomly.

# 3) Round-Robin invocation
#
# Develop an algorithm that, when invoking multiple times the Load Balancer on its get() method,
# should  return one backend-instance choosing between the registered one sequentially (round-robin).

import unittest


class BalancerInstance:

    def __init__(self, url):
        self.url_address = url


def get_random_value(values: list):
    random.shuffle(values)
    return values[0]


class LoadBalancer:

    def __init__(self):
        self.reistered_urls = {}
        self.current_position = 0

    def register_address(self, url):
        # make validation of the url
        # raise Exception("Validation Error")

        url_obj = self.reistered_urls.get(url, {})
        if not url_obj:
            self.reistered_urls[url] = BalancerInstance(url)

    def get(self, random_value=None):
        keys = list(self.reistered_urls.keys())
        if not keys:
            raise Exception("Empty Balancer")
        if random_value is None:
            # get items sequentially
            r_value = list(self.reistered_urls.values())[self.current_position]
            temp = self.current_position
            self.current_position = (temp + 1) % len(keys)
            return r_value
        else:
            r_value = random_value(keys)
            return self.reistered_urls[r_value]


class TestLoadBalancer(unittest.TestCase):

    def test_regiter_address(self):
        loadBalancer = LoadBalancer()
        url = "http://addr.com"
        loadBalancer.register_address(url)
        url_obj = loadBalancer.reistered_urls.get(url)
        self.assertIsNotNone(url_obj)
        self.assertEqual(url_obj.url_address, url)

    def test_get(self):
        loadBalancer = LoadBalancer()
        url = "http://addr.com"
        loadBalancer.register_address(url)
        url = "http://addr2.com"
        loadBalancer.register_address(url)
        url_obj = loadBalancer.get()

        self.assertIsNotNone(url_obj)
        all_keys = loadBalancer.reistered_urls.keys()
        self.assertTrue(url_obj.url_address in all_keys)
        self.assertTrue(url_obj.url_address == list(all_keys)[0])

    def test_random(self):
        loadBalancer = LoadBalancer()
        url = "http://addr.com"
        loadBalancer.register_address(url)
        url = "http://addr2.com"
        loadBalancer.register_address(url)

        random_value = lambda l: l[0]
        url_obj = loadBalancer.get(random_value=random_value)

        self.assertIsNotNone(url_obj)
        all_keys = loadBalancer.reistered_urls.keys()
        self.assertTrue(url_obj.url_address == list(all_keys)[0])

    def test_sequential(self):
        loadBalancer = LoadBalancer()
        url = "http://addr.com"
        loadBalancer.register_address(url)
        url = "http://addr2.com"
        loadBalancer.register_address(url)
        url = "http://addr3.com"
        loadBalancer.register_address(url)

        self.assertEqual(loadBalancer.current_position, 0)
        url_obj = loadBalancer.get()
        self.assertEqual(loadBalancer.current_position, 1)
        url_obj = loadBalancer.get()
        self.assertEqual(loadBalancer.current_position, 2)
        url_obj = loadBalancer.get()
        self.assertEqual(loadBalancer.current_position, 0)

        # self.assertIsNotNone(url_obj)
        # all_keys = loadBalancer.reistered_urls.keys()
        # self.assertTrue(url_obj.url_address == list(all_keys)[0])
