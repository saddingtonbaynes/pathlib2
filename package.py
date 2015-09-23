name = 'pathlib2'
uuid = '80c71c3a-9b7d-4806-ac8a-7dadc4d8b4db'
version = '2.0.1'
tools = []
authors = [
    'Python Foundation',
    'Matthias C. M. Troffaes'
]
description = ''
variants = []
requires = ['python']
build_requires = []


def commands():
    env.PYTHONPATH.append('{root}')
