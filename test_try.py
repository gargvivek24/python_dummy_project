

import pytest
open('report.html','w').close()
import os
def test_try():
    assert 1 == 1, 'not equal'
current_dir = os.path.dirname(__file__)
print(current_dir)
metadata=current_dir+'\\test_try.py'
print(metadata)
os.system(f'pytest {metadata} -v --junitxml="rulemap.xml"')
os.system('pytest --html=report.html')
# os.system(f'pytest {metadata} -v --junitxml="rulemap.xml"')
