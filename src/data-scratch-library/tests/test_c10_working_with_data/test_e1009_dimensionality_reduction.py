from dsl.c10_working_with_data.e1009_dimensionality_reduction import first_principal_component, project, \
    remove_projection_from_vector


def test_first_principal_component():
    data = [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5]
    ]
    pca_direction = first_principal_component(data)
    assert len(pca_direction) == 2
    assert abs(pca_direction[0]) > 0  # Ensure nonzero direction found


def test_project():
    v = [3, 4]
    w = [1, 0]
    projection = project(v, w)
    assert projection == [3, 0], f"Unexpected projection: {projection}"


def test_remove_projection():
    v = [3, 4]
    w = [1, 0]
    new_v = remove_projection_from_vector(v, w)
    assert new_v == [0, 4], f"Unexpected result after removing projection: {new_v}"
