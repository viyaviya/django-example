# -*- coding: utf-8 -*-

import os
import re
from importlib import import_module

from django.conf import settings

from faker import Faker
import factory as origin_factory


origin_fake = Faker()


def autoload_providers(factory, fake):
    """自动装载 providers"""

    path = os.path.join(settings.BASE_DIR, 'djexample/fake_factory/providers')

    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break

    pattern = re.compile(r'^[^\_]\w+\.py$')

    for item in files:
        result = pattern.match(item)
        if result:
            file_name = result.group().split('.')[0]
            module_path = 'djexample.fake_factory.providers.' + file_name
            module = import_module(module_path)
            provider = getattr(module, file_name.title() + 'Provider')
            factory.Faker.add_provider(provider)
            fake.add_provider(provider)


autoload_providers(origin_factory, origin_fake)

factory = origin_factory
fake = origin_fake
