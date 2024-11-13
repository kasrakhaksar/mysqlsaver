from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

packages = \
['mysqlSaver']

package_data = \
{'': ['*']}


setup_kwargs = {
    'name' :'mysqlSaver',
    'version':'0.1.9',
    'author':'Kasra Khaksar',
    'author_email':'kasrakhaksar17@gmail.com',
    'description':'This Is MySQL Package That You Can Save DataFrame As Table, Partition, Update , Primarykey And Unique In MySQL',
    "long_description" : long_description,
    "long_description_content_type" :'text/markdown',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)