# django 例子集合

此仓库只是简易的做些演示

## 1 环境简单说明

- python: 3.5.2
- django: 1.11.1
- 数据库：postgresql 9.5.2


## 2 跑起本地服务简单步骤

-  clone 文件

`clone` 到本地，然后进入到 `djexample` 路径下 

- 创建本地数据库

数据库默认配置如下

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djexample',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

即需要创建 `djexample` 数据库，注意用户和密码，如果你使用的用户和密码，请自行更新配置文件

- 安装应用到的包

`pip install -r requirementx.txt`

- 跑起服务

`./manage.py runserver_plus`

## 3 其他说明

- 使用 factory 快速创建测试数据，针对每个模型都会声明必要的 Factory

比如 blog app 中的 Book 模型， 声明示例：

```python
# -*- coding: utf-8 -*-

from djexample.fake_factory import factory

from blog.models import Book


class BookFactory(factory.DjangoModelFactory):
    """Book factory"""

    name = factory.Faker('word')
    extra_data = factory.Faker('random_string_dict')

    class Meta:
        model = Book

    @staticmethod
    def create_book(amount=1, **kwargs):
        return BookFactory.create_batch(amount, **kwargs)
```

创建测试数据代码示例：

```python
from blog.factory.book import BookFactory

BookFactory.create_book()
```
