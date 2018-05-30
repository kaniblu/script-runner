from setuptools import setup

__VERSION__ = "0.1"

setup(
    name='script-runner',
    version=__VERSION__,
    license="GPL",
    description='A wrapper for running scripts',
    author='Kang Min Yoo',
    author_email='kaniblurous@gmail.com',
    url='https://github.com/kaniblu/script-runner',
    packages=['runscript'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Java",
        "Programming Language :: Python",
    ],
    platforms=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ]
)
