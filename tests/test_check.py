import os
import shutil
import nose.tools as n

from _helpers import setup, teardown
from george import check

def test_test_has_data_submodule():
    n.assert_raises(AssertionError, check.test_has_data_submodule)
    open('.gitmodules', 'w').write('foo')
    os.mkdir('data')
    open(os.path.join('data', '.git'), 'w').write('bar')
    check.test_has_data_submodule()

def test_check_has_directory():
    n.assert_raises(AssertionError, check.check_has_directory)
    os.mkdir('code')
    check.check_has_directory('code')

def test_test_has_directories():
    n.assert_raises(AssertionError, check.test_has_directories)
    for directory_name in ['code', 'data', 'lib', 'test']:
        os.mkdir(directory_name)
    check.test_has_directories()

def test_test_has_readme():
    n.assert_raises(AssertionError, check.test_has_readme)
    open('readme.md', 'w').write('foo')
    check.test_has_readme()

def test_check_readme_has_section():
    n.assert_raises(AssertionError, check.check_readme_has_section)

    open('readme.md', 'w').write('Foo')
    n.assert_raises(AssertionError, check.check_readme_has_section)

    open('readme.md', 'w').write('## Foo')
    check.check_readme_has_section('Foo')

def test_test_python_init():
    os.mkdir('code')
    os.mkdir('test')
    check.test_python_init()

    open(os.path.join('test', 'test_foo.py'), 'w').write('foo')
    n.assert_raises(AssertionError, check.test_python_init)
    os.remove(os.path.join('test', 'test_foo.py'))

    open(os.path.join('code', 'foo.py'), 'w').write('foo')
    n.assert_raises(AssertionError, check.test_python_init)
    os.remove(os.path.join('code', 'foo.py'))

    open(os.path.join('test', 'test_foo.py'), 'w').write('foo')
    open(os.path.join('code', 'foo.py'), 'w').write('foo')
    n.assert_raises(AssertionError, check.test_python_init)

    open(os.path.join('code', '__init__.py'), 'w').write('foo')
    check.test_python_init()

def test_test_has_a_test():
    n.assert_raises(AssertionError, check.test_has_a_test)
    open(os.path.join('test', 'foo'))
    check.test_has_a_test()
