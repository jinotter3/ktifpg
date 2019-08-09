from setuptools import setup, find_packages

setup(
    name             = 'ktifpg',
    version          = '1.0',
    description      = 'Korean text input for pygame',
    author           = 'Seonghyun Jin',
    author_email     = 'jinotter@gmail.com',
    url              = 'https://github.com/jinotter3/ktifpg',
    install_requires = ['hgtk'],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['korean', 'pygame','input'],
    python_requires  = '>=2',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
