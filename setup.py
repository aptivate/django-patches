from setuptools import setup

long_description = '''\
- Don't catch exceptions in views, so that tests throw useful stacktraces.
- Provides extra debugging if queryset get method returns no results
- Allows redo-ing test post requests with file attachments
... needs full method documentation
'''

setup(
    author="Chris Wilson",
    author_email="chrisw@aptivate.org",
    name='django-patches',
    version='1.0',git 
    description='Add specific bugfixes and improvements to django',
    long_description=long_description,
    url='https://github.com/aptivate/django-patches',
    platforms=['OS Independent'],
    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
    ],
    install_requires=[
        'django>=1.4',
        'aptivate-monkeypatch',
    ],
    include_package_data=True,
    zip_safe=False
)
