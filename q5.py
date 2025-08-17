OK_FORMAT = True

test = {   'name': 'q5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> observation = {'hot_day': 1, 'weekend': 1}\n"
                                               '>>> output = compute_posterior(data, observation)\n'
                                               ">>> expected_output = {'chocolate': 0.6667, 'strawberry': 0.3333, 'vanilla': 0.0}\n"
                                               ">>> assert all((abs(output[flavor] - expected_output[flavor]) < 0.001 for flavor in expected_output)), f'Expected {expected_output}, got {output}'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.5},
                                   {   'code': ">>> observation = {'weekend': 1}\n"
                                               '>>> output = compute_posterior(data, observation)\n'
                                               ">>> expected_output = {'chocolate': 0.3333, 'vanilla': 0.2222, 'strawberry': 0.4444}\n"
                                               ">>> assert all((abs(output[flavor] - expected_output[flavor]) < 0.001 for flavor in expected_output)), f'Expected {expected_output}, got {output}'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
