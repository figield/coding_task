import unittest


# from unittest.mock import patch


class DoSth:

    def __init__(self, some_list=[]):
        self.not_validated_list = some_list
        self.validated = []
        self.balancer_configuration = {}
        self.shorts = {}
        self.short_prefix = "https://aws.re/"

    def validate(self):
        for item in self.not_validated_list:
            if self.is_valid_url(item):
                self.validated.append(item)

    @staticmethod
    def is_valid_url(url):
        import re
        url = url.strip()
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.fullmatch(url)

    def make_balancer_configuration(self):
        for url in self.validated:
            url_parts = url.split("?")
            url_base = url_parts[0]
            counter = self.balancer_configuration.get(url_base, 0)
            self.balancer_configuration[url_base] = counter + 1

    def get_random_str(self, length=5):
        import uuid
        uuid_str = str(uuid.uuid4())
        uuid_str = uuid_str.replace('-', '')
        return uuid_str[:length]

    def generate_short_url(self, random_generator=get_random_str):
        if random_generator is None:
            unique_url = self.short_prefix + self.get_random_str()
        else:
            unique_url = self.short_prefix + random_generator()
        if unique_url not in self.shorts.keys():
            return unique_url
        return self.generate_short_url()

    def add_shorten_url(self, shorten_url, url):
        self.shorts[shorten_url] = url


class TestDoSth(unittest.TestCase):

    def test_is_valid_url(self):
        self.assertTrue(DoSth.is_valid_url("http://wp.pl"))
        self.assertTrue(DoSth.is_valid_url("http://wp.pl?q=1?a=2"))
        self.assertTrue(DoSth.is_valid_url("http://wp.pl/test"))
        self.assertTrue(DoSth.is_valid_url("http://wp.pl "))
        self.assertTrue(DoSth.is_valid_url("http://localhost"))

    def test_validate(self):
        init_list = ["http://wp.pl", "123", "http://wp.pl/test", "http://wp.pl?q=1?a=2"]
        expected_list = ["http://wp.pl", "http://wp.pl/test", "http://wp.pl?q=1?a=2"]
        dosth = DoSth(init_list)
        dosth.validate()
        self.assertListEqual(dosth.validated, expected_list)

    def test_make_balancer_configuration(self):
        init_list = ["http://wp.pl", "123", "http://wp.pl/test", "http://wp.pl?q=1?a=2"]
        dosth = DoSth(init_list)
        dosth.validate()
        dosth.make_balancer_configuration()
        expected = {"http://wp.pl": 2, "http://wp.pl/test": 1}
        self.assertDictEqual(dosth.balancer_configuration, expected)

    # def test_shortener1(self):
    #     dosth = DoSth()
    #     with patch('classes.DoSth.get_random_str') as mock:
    #         mock.return_value = "abcde"
    #         short_url = dosth.generate_short_url()
    #         self.assertEqual(short_url, "https://aws.re/abcde")

    def test_shortener2(self):
        dosth = DoSth()
        random_generator = lambda: "abcde"
        short_url = dosth.generate_short_url(random_generator)
        self.assertEqual(short_url, "https://aws.re/abcde")

    def get_random_str_gen(self, length=5):
        return "abcdef"

    def test_shortener3(self):
        dosth = DoSth()
        short_url = dosth.generate_short_url(self.get_random_str_gen)
        self.assertEqual(short_url, "https://aws.re/abcdef")


if __name__ == "__main__":
    unittest.main()
