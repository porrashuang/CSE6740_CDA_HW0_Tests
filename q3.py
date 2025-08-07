OK_FORMAT = True

test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]\n>>> assert gauss_jordan_inverse(A) == [[4, 3, -1], [-2, -2, 1], [5, 4, -1]]\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> C = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]\n>>> assert gauss_jordan_inverse(C) is None\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
