import module

try:
    module.case(0)
except UnboundLocalError:
    pass
else:
    raise Exception('Unexpected')
