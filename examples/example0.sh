# Ensure to build coverage library from source after each code update:
# $ cd /path/to/coveragepy (main directory containing setup.py)
# $ python setup.py install

# Launch coverage with a "test" module
coverage erase
coverage run --timid test_zero.py
coverage html
open htmlcov/index.html
