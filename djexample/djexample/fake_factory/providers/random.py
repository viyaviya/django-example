# -*- coding: utf-8 -*-

import string
import random

from faker import Faker
from faker.providers import BaseProvider


class RandomProvider(BaseProvider):

    def random_digits_string(self, length=8):
        return ''.join(random.choice(string.digits) for x in range(length))

    def random_string_dict(self):
        result = Faker().pydict()
        return {key: value for key, value in result.items() if isinstance(value, str)}

    def random_mobile_number(self):
        """随机生成国内的手机号码"""
        MOBILE_CODES_PREFIX = {'134', '135', '136', '137', '138', '139', '147',
                               '150', '151', '152', '157', '158', '159', '178',
                               '182', '183', '184', '187', '188'}
        TELECOM_CODE_PREFIX = {'133', '153', '173', '177', '180', '181', '189'}
        UNICOM_CODE_PREFIX = {'130', '131', '132', '145', '155', '156', '185', '186'}

        CHAIN_CODE_PREFIX = MOBILE_CODES_PREFIX | TELECOM_CODE_PREFIX | UNICOM_CODE_PREFIX

        valid_mobile_prefix = list(CHAIN_CODE_PREFIX)
        last_num_string = self.random_digits_string(8)
        return random.choice(valid_mobile_prefix) + last_num_string
