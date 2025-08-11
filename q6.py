OK_FORMAT = True

test = {   'name': 'q6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> assert np.array_equal(q1_array_creation([1, 2, 3]), np.array([1, 2, 3])), 'Test failed for input [1, 2, 3]'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2},
                                   {   'code': '>>> assert np.array_equal(q2_basic_slicing(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])), np.array([[7, 6], [11, 10]])), '
                                               "'Test failed for input [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2},
                                   {   'code': ">>> assert np.array_equal(q3_boolean_indexing(np.array([1, 2, 3, 4, 5])), np.array([1, 2])), 'Test failed for input [1, 2, 3, 4, 5]'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2},
                                   {   'code': '>>> A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n'
                                               ">>> assert np.array_equal(q4_axis_operations(A), np.array([6, 0, -6])), 'Test failed for input [[1,2,3],[4,5,6],[7,8,9]]'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 3},
                                   {   'code': '>>> """" # BEGIN TEST CONFIG\n'
                                               '>>> points: 3\n'
                                               '>>> """\n'
                                               '>>> transpose, inverse = q5_matrix_operations(np.array([[1, 2], [3, 4]]))\n'
                                               ">>> assert np.array_equal(transpose, np.array([[1, 3], [2, 4]])), 'Transpose test failed'\n"
                                               ">>> assert np.allclose(inverse, np.array([[-2, 1], [1.5, -0.5]])), 'Inverse test failed for input [[1, 2], [3, 4]]'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> """" # BEGIN TEST CONFIG\n'
                                               '>>> points: 3\n'
                                               '>>> """\n'
                                               '>>> rank, (U, S, Vt) = q6_more_matrix_operations(np.array([[1, 2], [3, 4]]))\n'
                                               ">>> assert rank == 2, 'Rank test failed for input [[1, 2], [3, 4]]'\n"
                                               '>>> A_hat = U @ np.diag(S) @ Vt\n'
                                               ">>> assert np.allclose(A_hat, np.array([[1, 2], [3, 4]])), 'SVD reconstruction failed'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
