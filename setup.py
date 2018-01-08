from distutils.core import setup

VERSION = '0.1.0'

setup(
    name='nikto_batch_scanner',
    version=VERSION,
    author='Randy Lastinger',
    author_email='rlastinger@gmail.com',
    url='https://github.com/zerstoeren/nikto_batch_scanner',
    description='library to run nikto web scanner in batches',
    long_description=open('README.md').read(),
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows', # XP
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
    packages=['nikto_batch_scanner'],

)
