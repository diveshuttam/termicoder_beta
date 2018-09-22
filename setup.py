from setuptools import setup, find_packages


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except BaseException:
        pass


setup(
    name='termicoder',
    version='0.2.2',
    url='https://github.com/termicoder/termicoder',
    author='Divesh Uttamchandani',
    author_email='diveshuttamchandani@gmail.com',
    license='MIT',
    description='CLI to view, code & submit problems directly from terminal',
    long_description=readme(),
    keywords='competitive iarcs codechef oj',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Education',
        'Topic :: Education',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4',
        'click-default-group',
        'click-repl',
        'click_completion'
    ],
    entry_points='''
        [console_scripts]
        termicoder=termicoder.cli:main
        [termicoder.judge_plugins]
        codechef=termicoder.judges.codechef:Codechef
        iarcs=termicoder.judges.iarcs:Iarcs
    '''
)
