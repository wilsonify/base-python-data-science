# coding: utf-8

from __future__ import absolute_import

import math
import unittest

import pytest
from flask import json

from openapi_server.controllers.math_controller import (
    sqrt,
    variance,
    standard_deviation,
    quantile,
    mode,
    median,
    mean,
    interquartile_range,
    de_mean,
    data_range,
    covariance,
    correlation_matrix,
    correlation,
    bucketize,
    uniform_pdf,
    uniform_cdf,
    echo, distance, in_random_order, random_kid, difference_quotient, estimate_gradient, maximize_batch,
    maximize_stochastic, minimize_batch, partial_difference_quotient, get_column, dot, get_row,
    magnitude, matrix_add, scalar_multiply, shape, squared_distance, sum_of_squares, vector_mean, vector_add,
    vector_subtract, vector_sum, f1_score, accuracy, precision, recall, split_data, train_test_split,
    bernoulli_trial, binomial, inverse_normal_cdf, normal_cdf, normal_pdf, strength
)
from openapi_server.models.sqrt_input import SqrtInput
from openapi_server.models.strength_input import StrengthInput
from openapi_server.test import BaseTestCase


def test_smoke():
    print('fire?')


def test_sqrt():
    body = dict(x=10)
    result = sqrt(body)
    assert result[1] == 200
    assert result[0] == {'result': pytest.approx(3.16, abs=0.1), 'x': 10}


def test_strength():
    body = dict(expected=10, actual=6)
    result = strength(body)
    assert result[1] == 200
    assert result[0] == {'actual': 6, 'expected': 10, 'strength': pytest.approx(0.6, abs=0.01)}


def test_echo():
    body = dict(expected=10, actual=6)
    result = echo(body)
    assert result[1] == "200"
    assert result[0] == dict(expected=10, actual=6, strategy="echo")


def test_difference_quotient():
    body = dict(x=5, h=1)
    result = difference_quotient(body)
    assert result[1] == "200"
    assert result[0] == pytest.approx(11.0, abs=0.1)


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([0, 0, 0], [10, 10, 10], math.sqrt(300)),
            ([0, 0, 0], [-10, -10, -10], math.sqrt(300)))
)
def test_distance(vec1, vec2, expected):
    body = dict(v=vec1, w=vec2)
    result = distance(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_estimate_gradient():
    body = dict(v=[10.0, 2.0], h=1)
    result = estimate_gradient(body)
    assert result[1] == "200"
    assert result[0] == [[21.0, 0.0], [0.0, 5.0]]


def test_in_random_order():
    body = dict(data=[1, 2, 3, 4, 5, 6])
    result = in_random_order(body)
    assert result[1] == "200"
    assert len(result[0]) == 6


def test_maximize_batch():
    body = dict(x=[[1, 2, 3], [2, 3, 4], [5, 6, 7]])
    result = maximize_batch(body)
    assert result[1] == "200"
    assert len(result[0]) == 3


def test_maximize_stochastic():
    body = dict(
        x=[[1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0], [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0], [1, 19, 3, 0],
           [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]],
        y=[68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, ]
    )
    result = maximize_stochastic(body)
    assert result[1] == "200"
    assert len(result[0]) == 4


def test_minimize_batch():
    body = dict(
        x=[[1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0], [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0], [1, 19, 3, 0],
           [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]],
        y=[68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, ]
    )
    result = minimize_batch(body)
    assert result[1] == "200"
    assert len(result[0]) == 4


def test_partial_difference_quotient():
    body = dict(
        v=[10.0, 2.0],
        i=0,
        h=1
    )
    result = partial_difference_quotient(body)
    assert result[1] == "200"
    assert result[0] == [pytest.approx(21.0), pytest.approx(0.0)]


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([1, 1, 1], [10, 10, 10], 30),
            ([1, 1, 1], [-10, -10, -10], -30))
)
def test_dot(vec1, vec2, expected):
    body = dict(v=vec1, w=vec2)
    result = dot(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("mat1", "col", "expected"), (
            ([[1, 2, 3]], 0, [1]),
            ([[1, 2, 3]], 2, [3]))
)
def test_get_column(mat1, col, expected):
    body = dict(mat=mat1, col=col)
    result = get_column(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("mat1", "row", "expected"), (
            ([[1], [2], [3]], 0, [1]),
            ([[1], [2], [3]], 2, [3]))
)
def test_get_row(mat1, row, expected):
    body = dict(mat=mat1, row=row)
    result = get_row(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("vec1", "expected"), (
            ([10, 10, 10], math.sqrt(300)),
            ([-10, -10, -10], math.sqrt(300)))
)
def test_magnitude(vec1, expected):
    body = dict(v=vec1)
    result = magnitude(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("mat1", "mat2", "expected"), (
            ([[1]], [[1]], [[2]]),
            ([[1, 0], [0, 1]], [[1, 2], [3, 4]], [[2, 2], [3, 5]])
    ))
def test_matrix_add(mat1, mat2, expected):
    body = dict(mat1=mat1, mat2=mat2)
    result = matrix_add(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v", "c", "expected"), (
            ([2, 1], 1.87, [3.74, 1.87]),
            ([1, 2, 3, 4], 5, [5, 10, 15, 20])
    ))
def test_scalar_multiply(v, c, expected):
    body = dict(v=v, c=c)
    result = scalar_multiply(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_shape():
    body = dict(mat=[[1, 2, 3], [3, 4, 5], [6, 7, 8]])
    result = shape(body)
    assert result[1] == "200"
    assert result[0] == [3, 3]


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], 0),
            ([1, 0, 0, 1], [1, 2, 3, 4], 22)
    ))
def test_squared_distance(v1, v2, expected):
    body = dict(v=v1, w=v2)
    result = squared_distance(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 385),
            ([1, 2, 3, 4, 5, 100, 123], 25184),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 438),
            ([1, 0, 0, 1], 2)
    ))
def test_sum_of_squares(x, expected):
    body = dict(v=x)
    result = sum_of_squares(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [2]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    ))
def test_vector_add(v1, v2, expected):
    body = dict(v=v1, w=v2)
    result = vector_add(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [1]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [1, 1, 1.5, 2.5])
    ))
def test_vector_mean(v1, v2, expected):
    body = dict(vectors=[v1, v2])
    result = vector_mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [0]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [0, -2, -3, -3])
    ))
def test_vector_subtract(v1, v2, expected):
    body = dict(v=v1, w=v2)
    result = vector_subtract(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [2]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    ))
def test_vector_sum(v1, v2, expected):
    body = dict(vectors=[v1, v2])
    result = vector_sum(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.55, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.66, abs=0.01)),
            (0, 120, 200, 303, pytest.approx(0.48, abs=0.01))
    ))
def test_accuracy(tp, fp, fn, tn, expected):
    body = dict(tp=tp, fp=fp, fn=fn, tn=tn)
    result = accuracy(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.38, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.49, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_f1_score(tp, fp, fn, tn, expected):
    body = dict(tp=tp, fp=fp, fn=fn, tn=tn)
    result = f1_score(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.45, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.99, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_precision(tp, fp, fn, tn, expected):
    body = dict(tp=tp, fp=fp, fn=fn, tn=tn)
    result = precision(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.33, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.33, abs=0.01)),
            (1, 120, 200, 303, pytest.approx(0.01, abs=0.01))
    ))
def test_recall(tp, fp, fn, tn, expected):
    body = dict(tp=tp, fp=fp, fn=fn, tn=tn)
    result = recall(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_split_data():
    body = dict(mat=[[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]], p=0.5)
    result = split_data(body)
    assert result[1] == "200"
    assert len(result[0][0]) + len(result[0][1]) == len(body["mat"])


def test_train_test_split():
    body = dict(
        x=[[1.1316776275634766, -4.759654998779297, -0.15560150146484375, 6],
           [0.3211688995361328, -0.6198501586914062, -2.2504234313964844, 0],
           [-0.03821372985839844, -0.6946563720703125, 5.498104095458984, 6],
           [-0.1600933074951172, 1.9200515747070312, 10.169029235839844, 6],
           [-0.05995750427246094, 0.33695220947265625, -6.663417816162109, 0],
           [-0.1679706573486328, 2.493915557861328, 8.885936737060547, 6],
           [0.38908958435058594, -2.5916099548339844, -4.244575500488281, 0],
           [0.2788829803466797, -0.11791229248046875, -7.269153594970703, 0],
           [-1.212167739868164, 5.421409606933594, 11.897430419921875, 6],
           [-1.2006664276123047, 6.029815673828125, 6.235008239746094, 6],
           [0.39992332458496094, -1.7329788208007812, 4.125823974609375, 6],
           [-0.06012916564941406, 0.8364677429199219, 9.313201904296875, 6],
           [-2.1445178985595703, 11.666793823242188, 2.725391387939453, 6],
           [-1.0451412200927734, 6.041355133056641, 3.300342559814453, 6],
           [0.3055286407470703, -0.24250030517578125, -3.1299209594726562, 0],
           [-1.3082218170166016, 7.252521514892578, 4.410266876220703, 6],
           [1.492452621459961, -7.153759002685547, -5.443153381347656, 0],
           [1.1581134796142578, -5.634441375732422, -1.7660331726074219, 6],
           [-0.6119823455810547, 2.0266151428222656, 10.129070281982422, 6],
           [-0.04212379455566406, 1.4994239807128906, -1.2224769592285156, 6],
           [-0.33904075622558594, 1.1407089233398438, 6.202564239501953, 6],
           [-0.48356056213378906, 3.1785011291503906, 1.6668319702148438, 6],
           [-0.29595375061035156, 0.7853507995605469, -0.8632469177246094, 6],
           [0.25916099548339844, -2.924823760986328, -4.280948638916016, 0],
           [0.1540851593017578, -2.3513031005859375, -10.558891296386719, 0],
           [0.8454608917236328, -6.830711364746094, -3.790416717529297, 0],
           [1.5851879119873047, -8.778953552246094, -2.7120208740234375, 0],
           [-0.4101848602294922, 1.9089698791503906, -0.7268524169921875, 6],
           [-1.3624095916748047, 8.270931243896484, 5.646381378173828, 6],
           [0.5951404571533203, -2.3493385314941406, -0.057468414306640625, 6],
           [0.41823387145996094, -2.8293800354003906, -0.8535575866699219, 6],
           [0.5451679229736328, -3.3335494995117188, -2.3252296447753906, 0],
           [-0.6060123443603516, 2.693023681640625, 4.23492431640625, 6],
           [1.2329387664794922, -7.303352355957031, -7.431354522705078, 0],
           [0.3113079071044922, -1.4812660217285156, 8.57950210571289, 6],
           [-0.011587142944335938, -0.12678146362304688, 7.4033355712890625, 6],
           [-1.228017807006836, 6.160430908203125, 13.614044189453125, 6],
           [-0.4121685028076172, 2.4369430541992188, 3.5726356506347656, 6],
           [0.6995105743408203, -2.365264892578125, -8.064289093017578, 0],
           [-2.1786975860595703, 8.889713287353516, 10.76456069946289, 6],
           [-0.7229900360107422, 5.106792449951172, 14.39199447631836, 6],
           [-1.120748519897461, 5.543079376220703, -2.2624969482421875, 0],
           [0.31142234802246094, -1.7682075500488281, -4.590320587158203, 0],
           [-0.8372783660888672, 4.618587493896484, -2.158222198486328, 0],
           [-0.07723808288574219, 0.4239654541015625, -5.140190124511719, 0],
           [1.143808364868164, -5.066356658935547, -3.555908203125, 0],
           [-1.3470745086669922, 5.8251190185546875, 10.482711791992188, 6],
           [0.8372974395751953, -4.955272674560547, -11.479625701904297, 0],
           [1.5221881866455078, -6.844234466552734, -10.103530883789062, 0],
           [-0.9085178375244141, 4.543819427490234, 7.582798004150391, 6],
           [-0.9582042694091797, 3.797454833984375, 1.0918807983398438, 6],
           [-0.5344676971435547, 1.9523048400878906, 0.7156944274902344, 6],
           [0.7050228118896484, -1.0172080993652344, -2.3758888244628906, 0],
           [0.46669960021972656, -1.5128707885742188, 5.617389678955078, 6],
           [0.45340538024902344, -3.5840415954589844, -2.9229736328125, 0],
           [-2.285432815551758, 11.019039154052734, 7.876682281494141, 6],
           [1.0870838165283203, -3.8082504272460938, -10.256481170654297, 0],
           [-0.2325153350830078, 0.8565139770507812, 3.5395240783691406, 6],
           [-0.7575130462646484, 4.3814849853515625, 3.9826011657714844, 6],
           [1.5211009979248047, -7.1900177001953125, -4.18304443359375, 0],
           [1.054697036743164, -5.29083251953125, 1.7218017578125, 6],
           [-0.6432247161865234, 3.9892959594726562, 1.7551040649414062, 6],
           [0.33555030822753906, -1.0505294799804688, -0.6264305114746094, 6],
           [-0.6844997406005859, 3.9739990234375, 1.9586944580078125, 6],
           [-1.1155223846435547, 6.497688293457031, 6.753692626953125, 6],
           [0.2950572967529297, -0.8376502990722656, -1.8006324768066406, 6],
           [-1.0504627227783203, 5.185565948486328, 7.183380126953125, 6],
           [-1.8407726287841797, 11.04074478149414, 8.593578338623047, 6],
           [0.2087879180908203, -1.6827392578125, 0.957489013671875, 6],
           [-0.43831825256347656, 1.8396759033203125, 5.122642517089844, 6],
           [0.06630897521972656, 1.6608428955078125, 0.2621650695800781, 6],
           [-0.8940410614013672, 3.327503204345703, 1.0602188110351562, 6],
           [-0.6395626068115234, 3.370037078857422, 1.8988227844238281, 6],
           [-1.1476612091064453, 5.626239776611328, 4.066066741943359, 6],
           [0.16633033752441406, -0.3182029724121094, 3.9079666137695312, 6],
           [-0.21811485290527344, 1.5558815002441406, -9.04378890991211, 0],
           [0.4063892364501953, -1.9027137756347656, 2.447834014892578, 6],
           [1.0609912872314453, -4.443264007568359, -10.46630859375, 0],
           [0.3614521026611328, -3.204212188720703, 0.8072853088378906, 6],
           [-1.1270999908447266, 5.251979827880859, 14.199161529541016, 6],
           [-0.5493068695068359, 1.3205909729003906, -1.4872550964355469, 6],
           [-0.7167339324951172, 3.9739227294921875, 8.348426818847656, 6],
           [0.9803676605224609, -5.070362091064453, -5.495567321777344, 0],
           [-0.10352134704589844, 0.5245590209960938, -0.22321701049804688, 6],
           [-0.7791805267333984, 4.5169830322265625, 1.0643196105957031, 6],
           [-1.2512683868408203, 3.617076873779297, -2.7596664428710938, 0],
           [0.023012161254882812, 0.006313323974609375, -1.8956184387207031, 6],
           [-0.8350086212158203, 5.233726501464844, -0.05374908447265625, 6],
           [1.2720394134521484, -6.073131561279297, -6.212959289550781, 0],
           [0.5188274383544922, -2.623748779296875, -1.3530921936035156, 6],
           [-1.090097427368164, 5.399646759033203, -9.934768676757812, 0],
           [-0.5174922943115234, 4.210319519042969, 0.2613639831542969, 6],
           [-0.4767131805419922, 1.7911529541015625, 8.423748016357422, 6],
           [1.5734577178955078, -8.713092803955078, -9.716987609863281, 0],
           [0.33562660217285156, -2.819976806640625, -1.9648361206054688, 6],
           [0.11179924011230469, -0.9972572326660156, -5.789775848388672, 0],
           [0.5711269378662109, -3.1775474548339844, 0.58013916015625, 6],
           [-0.05795478820800781, -0.21005630493164062, -2.9288101196289062, 0],
           [0.6026935577392578, -2.8577804565429688, 2.014942169189453, 6],
           [-1.4389705657958984, 7.371711730957031, 10.729389190673828, 6]],
        y=[[1.1316776275634766, -4.759654998779297, -0.15560150146484375, 6],
           [0.3211688995361328, -0.6198501586914062, -2.2504234313964844, 0],
           [-0.03821372985839844, -0.6946563720703125, 5.498104095458984, 6],
           [-0.1600933074951172, 1.9200515747070312, 10.169029235839844, 6],
           [-0.05995750427246094, 0.33695220947265625, -6.663417816162109, 0],
           [-0.1679706573486328, 2.493915557861328, 8.885936737060547, 6],
           [0.38908958435058594, -2.5916099548339844, -4.244575500488281, 0],
           [0.2788829803466797, -0.11791229248046875, -7.269153594970703, 0],
           [-1.212167739868164, 5.421409606933594, 11.897430419921875, 6],
           [-1.2006664276123047, 6.029815673828125, 6.235008239746094, 6],
           [0.39992332458496094, -1.7329788208007812, 4.125823974609375, 6],
           [-0.06012916564941406, 0.8364677429199219, 9.313201904296875, 6],
           [-2.1445178985595703, 11.666793823242188, 2.725391387939453, 6],
           [-1.0451412200927734, 6.041355133056641, 3.300342559814453, 6],
           [0.3055286407470703, -0.24250030517578125, -3.1299209594726562, 0],
           [-1.3082218170166016, 7.252521514892578, 4.410266876220703, 6],
           [1.492452621459961, -7.153759002685547, -5.443153381347656, 0],
           [1.1581134796142578, -5.634441375732422, -1.7660331726074219, 6],
           [-0.6119823455810547, 2.0266151428222656, 10.129070281982422, 6],
           [-0.04212379455566406, 1.4994239807128906, -1.2224769592285156, 6],
           [-0.33904075622558594, 1.1407089233398438, 6.202564239501953, 6],
           [-0.48356056213378906, 3.1785011291503906, 1.6668319702148438, 6],
           [-0.29595375061035156, 0.7853507995605469, -0.8632469177246094, 6],
           [0.25916099548339844, -2.924823760986328, -4.280948638916016, 0],
           [0.1540851593017578, -2.3513031005859375, -10.558891296386719, 0],
           [0.8454608917236328, -6.830711364746094, -3.790416717529297, 0],
           [1.5851879119873047, -8.778953552246094, -2.7120208740234375, 0],
           [-0.4101848602294922, 1.9089698791503906, -0.7268524169921875, 6],
           [-1.3624095916748047, 8.270931243896484, 5.646381378173828, 6],
           [0.5951404571533203, -2.3493385314941406, -0.057468414306640625, 6],
           [0.41823387145996094, -2.8293800354003906, -0.8535575866699219, 6],
           [0.5451679229736328, -3.3335494995117188, -2.3252296447753906, 0],
           [-0.6060123443603516, 2.693023681640625, 4.23492431640625, 6],
           [1.2329387664794922, -7.303352355957031, -7.431354522705078, 0],
           [0.3113079071044922, -1.4812660217285156, 8.57950210571289, 6],
           [-0.011587142944335938, -0.12678146362304688, 7.4033355712890625, 6],
           [-1.228017807006836, 6.160430908203125, 13.614044189453125, 6],
           [-0.4121685028076172, 2.4369430541992188, 3.5726356506347656, 6],
           [0.6995105743408203, -2.365264892578125, -8.064289093017578, 0],
           [-2.1786975860595703, 8.889713287353516, 10.76456069946289, 6],
           [-0.7229900360107422, 5.106792449951172, 14.39199447631836, 6],
           [-1.120748519897461, 5.543079376220703, -2.2624969482421875, 0],
           [0.31142234802246094, -1.7682075500488281, -4.590320587158203, 0],
           [-0.8372783660888672, 4.618587493896484, -2.158222198486328, 0],
           [-0.07723808288574219, 0.4239654541015625, -5.140190124511719, 0],
           [1.143808364868164, -5.066356658935547, -3.555908203125, 0],
           [-1.3470745086669922, 5.8251190185546875, 10.482711791992188, 6],
           [0.8372974395751953, -4.955272674560547, -11.479625701904297, 0],
           [1.5221881866455078, -6.844234466552734, -10.103530883789062, 0],
           [-0.9085178375244141, 4.543819427490234, 7.582798004150391, 6],
           [-0.9582042694091797, 3.797454833984375, 1.0918807983398438, 6],
           [-0.5344676971435547, 1.9523048400878906, 0.7156944274902344, 6],
           [0.7050228118896484, -1.0172080993652344, -2.3758888244628906, 0],
           [0.46669960021972656, -1.5128707885742188, 5.617389678955078, 6],
           [0.45340538024902344, -3.5840415954589844, -2.9229736328125, 0],
           [-2.285432815551758, 11.019039154052734, 7.876682281494141, 6],
           [1.0870838165283203, -3.8082504272460938, -10.256481170654297, 0],
           [-0.2325153350830078, 0.8565139770507812, 3.5395240783691406, 6],
           [-0.7575130462646484, 4.3814849853515625, 3.9826011657714844, 6],
           [1.5211009979248047, -7.1900177001953125, -4.18304443359375, 0],
           [1.054697036743164, -5.29083251953125, 1.7218017578125, 6],
           [-0.6432247161865234, 3.9892959594726562, 1.7551040649414062, 6],
           [0.33555030822753906, -1.0505294799804688, -0.6264305114746094, 6],
           [-0.6844997406005859, 3.9739990234375, 1.9586944580078125, 6],
           [-1.1155223846435547, 6.497688293457031, 6.753692626953125, 6],
           [0.2950572967529297, -0.8376502990722656, -1.8006324768066406, 6],
           [-1.0504627227783203, 5.185565948486328, 7.183380126953125, 6],
           [-1.8407726287841797, 11.04074478149414, 8.593578338623047, 6],
           [0.2087879180908203, -1.6827392578125, 0.957489013671875, 6],
           [-0.43831825256347656, 1.8396759033203125, 5.122642517089844, 6],
           [0.06630897521972656, 1.6608428955078125, 0.2621650695800781, 6],
           [-0.8940410614013672, 3.327503204345703, 1.0602188110351562, 6],
           [-0.6395626068115234, 3.370037078857422, 1.8988227844238281, 6],
           [-1.1476612091064453, 5.626239776611328, 4.066066741943359, 6],
           [0.16633033752441406, -0.3182029724121094, 3.9079666137695312, 6],
           [-0.21811485290527344, 1.5558815002441406, -9.04378890991211, 0],
           [0.4063892364501953, -1.9027137756347656, 2.447834014892578, 6],
           [1.0609912872314453, -4.443264007568359, -10.46630859375, 0],
           [0.3614521026611328, -3.204212188720703, 0.8072853088378906, 6],
           [-1.1270999908447266, 5.251979827880859, 14.199161529541016, 6],
           [-0.5493068695068359, 1.3205909729003906, -1.4872550964355469, 6],
           [-0.7167339324951172, 3.9739227294921875, 8.348426818847656, 6],
           [0.9803676605224609, -5.070362091064453, -5.495567321777344, 0],
           [-0.10352134704589844, 0.5245590209960938, -0.22321701049804688, 6],
           [-0.7791805267333984, 4.5169830322265625, 1.0643196105957031, 6],
           [-1.2512683868408203, 3.617076873779297, -2.7596664428710938, 0],
           [0.023012161254882812, 0.006313323974609375, -1.8956184387207031, 6],
           [-0.8350086212158203, 5.233726501464844, -0.05374908447265625, 6],
           [1.2720394134521484, -6.073131561279297, -6.212959289550781, 0],
           [0.5188274383544922, -2.623748779296875, -1.3530921936035156, 6],
           [-1.090097427368164, 5.399646759033203, -9.934768676757812, 0],
           [-0.5174922943115234, 4.210319519042969, 0.2613639831542969, 6],
           [-0.4767131805419922, 1.7911529541015625, 8.423748016357422, 6],
           [1.5734577178955078, -8.713092803955078, -9.716987609863281, 0],
           [0.33562660217285156, -2.819976806640625, -1.9648361206054688, 6],
           [0.11179924011230469, -0.9972572326660156, -5.789775848388672, 0],
           [0.5711269378662109, -3.1775474548339844, 0.58013916015625, 6],
           [-0.05795478820800781, -0.21005630493164062, -2.9288101196289062, 0],
           [0.6026935577392578, -2.8577804565429688, 2.014942169189453, 6],
           [-1.4389705657958984, 7.371711730957031, 10.729389190673828, 6]],
        p=0.8
    )
    result = train_test_split(body)
    assert result[1] == "200"
    assert len(result[0]) == 4


def test_bernoulli_trial():
    body = dict(p=0.5)
    result = bernoulli_trial(body)
    assert result[1] == "200"
    assert result[0] in [0, 1]


def test_binomial():
    body = dict(n=10, p=0.6)
    result = binomial(body)
    assert result[1] == "200"
    assert result[0] < 10


@pytest.mark.parametrize(
    ("p", "mu", "sigma", "expected"), (
            (0.01, 100, 5, pytest.approx(88.36, abs=0.01)),
            (0.10, 100, 5, pytest.approx(93.59, abs=0.01)),
            (0.5, 100, 5, pytest.approx(100, abs=0.01)),
            (0.95, 100, 5, pytest.approx(108, abs=1))
    ))
def test_inverse_normal_cdf(p, mu, sigma, expected):
    body = dict(p=p, mu=mu, sigma=sigma)
    result = inverse_normal_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.16, abs=0.01)),
            (100, 100, 5, pytest.approx(0.5, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_cdf(x, mu, sigma, expected):
    body = dict(x=x, mu=mu, sigma=sigma)
    result = normal_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.05, abs=0.01)),
            (100, 100, 5, pytest.approx(0.08, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_pdf(x, mu, sigma, expected):
    body = dict(x=x, mu=mu, sigma=sigma)
    result = normal_pdf(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_random_kid():
    body = dict()
    result = random_kid(body)
    assert result[1] == "200"
    assert result[0] in ["boy", "girl"]


@pytest.mark.parametrize(
    ("x", "expected"), (
            (0.1, pytest.approx(0.1, abs=0.01)),
            (0.5, pytest.approx(0.5, abs=0.01)),
            (0.9, pytest.approx(0.9, abs=0.01)),
            (2, pytest.approx(1, abs=0.1))
    ))
def test_uniform_cdf(x, expected):
    body = dict(x=x)
    result = uniform_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            (-0.1, pytest.approx(0, abs=0.01)),
            (0.5, pytest.approx(1, abs=0.01)),
            (0.9, pytest.approx(1, abs=0.01)),
            (2, pytest.approx(0, abs=0.1))
    ))
def test_uniform_pdf(x, expected):
    body = dict(x=x)
    result = uniform_pdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("point", "bucket_size", "expected"), (
            (25.4958, 5, 25),
            (250.303, 5, 250),
            (25.9, 25, 25),
    ))
def test_bucketize(point, bucket_size, expected):
    body = dict(point=point, bucket_size=bucket_size)
    result = bucketize(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-1, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_correlation(v1, v2, expected):
    body = dict(x=v1, y=v2)
    result = correlation(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-1, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_correlation(v1, v2, expected):
    body = dict(x=v1, y=v2)
    result = correlation(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1, 2], [2, 1], pytest.approx(-0.5, abs=0.01)),
            ([1, 2], [1, 2], pytest.approx(0.5, abs=0.01)),
            ([1, 2, 3, 4, 5], [1, 1.5, 2, 2.5], pytest.approx(0.6, abs=0.1)),
            ([1, 0, 0, 1], [1, 2, 3, 4], pytest.approx(0, abs=0.01))
    ))
def test_covariance(v1, v2, expected):
    body = dict(x=v1, y=v2)
    result = covariance(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 10], pytest.approx(9, abs=0.01)),
            ([1, 2, 3, 4, 5], pytest.approx(4, abs=0.1)),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_data_range(x, expected):
    body = dict(x=x)
    result = data_range(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], [-0.5, 0.5]),
            ([1, 2, 12], [-4.0, -3.0, 7.0]),
            ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0]),
            ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    ))
def test_de_mean(x, expected):
    body = dict(x=x)
    result = de_mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
            ([1, 2, 3, 4, 5, 100, 123], 98),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_interquartile_range(x, expected):
    body = dict(x=x)
    result = interquartile_range(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 100, 123], 34),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(5.27, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.5, abs=0.01))
    ))
def test_mean(x, expected):
    body = dict(x=x)
    result = mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 100, 123], 4),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4),
            ([1, 0, 0, 1], 0.5)
    ))
def test_median(x, expected):
    body = dict(x=x)
    result = median(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5]),
            ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98]),
            ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3]),
            ([1, 0, 0, 1], [1, 0])
    ))
def test_mode(x, expected):
    body = dict(x=x)
    result = mode(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("p", "x", "expected"), (
            (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            (0.5, [1, 2, 3, 4, 5, 100, 123], 4),
            (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6),
            (0.99, [1, 0, 0, 1], 1)
    ))
def test_quantile(p, x, expected):
    body = dict(x=x, p=p)
    result = quantile(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(3.03, abs=0.01)),
            ([1, 2, 3, 4, 5, 100, 123], pytest.approx(53.37, abs=0.01)),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(3.64, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.577, abs=0.01))
    ))
def test_standard_deviation(x, expected):
    body = dict(x=x)
    result = standard_deviation(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_variance():
    body = dict(x=[1, 2, 3, 4])
    result = variance(body)
    assert result[1] == "200"
    assert result[0] == pytest.approx(1.67, abs=0.1)


class TestMathController(BaseTestCase):
    """MathController integration test stubs"""

    def test_mysqrt(self):
        """Test case for sqrt"""
        sqrt_input = SqrtInput(x=10)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/sqrt',
            method='POST',
            headers=headers,
            data=json.dumps(sqrt_input),
            content_type='application/json')
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )

    def test_mystrength(self):
        """Test case for strength"""
        strength_input = StrengthInput(expected=10, actual=6)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/strength',
            method='POST',
            headers=headers,
            data=json.dumps(strength_input),
            content_type='application/json')
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )


if __name__ == '__main__':
    unittest.main()
