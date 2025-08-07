OK_FORMAT = True

test = {   'name': 'q5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> observation = {'hot_day': 1, 'weekend': 1}\n"
                                               '>>> output = compute_posterior(data, observation)\n'
                                               ">>> expected_output = {'chocolate': 0.6667, 'strawberry': 0.3333, 'vanilla': 0.0}\n"
                                               '>>> for flavor in expected_output:\n'
                                               "...     assert abs(output[flavor] - expected_output[flavor]) < 0.001, f'Expected {expected_output[flavor]} for {flavor}, got {output[flavor]}'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> observation = {'weekend': 1}\n"
                                               '>>> output = compute_posterior(data, observation)\n'
                                               ">>> expected_output = {'chocolate': 0.3333, 'vanilla': 0.2222, 'strawberry': 0.4444}\n"
                                               '>>> for flavor in expected_output:\n'
                                               "...     assert abs(output[flavor] - expected_output[flavor]) < 0.001, f'Expected {expected_output[flavor]} for {flavor}, got {output[flavor]}'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
