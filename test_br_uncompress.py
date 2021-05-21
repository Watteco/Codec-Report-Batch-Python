#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test file for br_uncompress module. Should be launched with py.test"""

import pytest
from br_uncompress import (
    uncompress,
    hex_to_array,
    Buffer,
    Flag,
    find_index_of_lbl,
    to_float,
)
import constants


def test_float():
    actual = uncompress(
        3,
        [{"taglbl": 2, "lblname": "temperature", "resol": 1.0, "sampletype": 12}],
        "$10$27$00$80$03$93$20$18$00$80$10$81$83$07$0d$45$85$10$05",
    )
    expected = {
        "batch_counter": 7,
        "batch_relative_timestamp": 1944,
        "dataset": [
            {
                "data_relative_timestamp": 1830,
                "data": {"value": 11, "label": 2, "label_name": "temperature"},
            },
            {
                "data_relative_timestamp": 1845,
                "data": {"value": 13, "label": 2, "label_name": "temperature"},
            },
            {
                "data_relative_timestamp": 1860,
                "data": {"value": 14, "label": 2, "label_name": "temperature"},
            },
            {
                "data_relative_timestamp": 1875,
                "data": {"value": 21, "label": 2, "label_name": "temperature"},
            },
            {
                "data_relative_timestamp": 1876,
                "data": {"value": 100, "label": 2, "label_name": "temperature"},
            },
        ],
    }
    assert expected == actual


def test_integer():
    actual = uncompress(
        1,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 1},
        ],
        "20100000a020a8010000004401e297ad40871b770e377b",
        "2018-11-05T10:35:09.685Z",
    )
    expected = {
        "batch_counter": 0,
        "batch_relative_timestamp": 99,
        "batch_absolute_timestamp": "2018-11-05T10:35:09.685Z",
        "dataset": [
            {
                "data_absolute_timestamp": "2018-11-05T10:34:19.685Z",
                "data_relative_timestamp": 49,
                "data": {"value": 0, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:29.685Z",
                "data_relative_timestamp": 59,
                "data": {"value": 0, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:39.685Z",
                "data_relative_timestamp": 69,
                "data": {"value": 3, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:49.685Z",
                "data_relative_timestamp": 79,
                "data": {"value": 7, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:59.685Z",
                "data_relative_timestamp": 89,
                "data": {"value": 7, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:35:09.685Z",
                "data_relative_timestamp": 99,
                "data": {"value": 10, "label": 0},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:33:35.685Z",
                "data_relative_timestamp": 5,
                "data": {"value": 1, "label": 1},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:37.685Z",
                "data_relative_timestamp": 67,
                "data": {"value": 0, "label": 1},
            },
            {
                "data_absolute_timestamp": "2018-11-05T10:34:39.685Z",
                "data_relative_timestamp": 69,
                "data": {"value": 1, "label": 1},
            },
        ],
    }
    assert expected == actual


def test_big_float_input():
    """Function comments"""
    actual = uncompress(
        1,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 12},
            {"taglbl": 1, "resol": 100, "sampletype": 6},
        ],
        "10000000404a481f000044a1d1a9d5e8353aad1042e83542afd10b8d5a557aa14aad2a21b47aa111420821d4a9d469f51aa14e2bb442af11eab442a8151abdd0aad20b8d5e23f41abd46e8b4ead46b06",
    )
    expected = {
        "batch_counter": 0,
        "batch_relative_timestamp": 166,
        "dataset": [
            {"data_relative_timestamp": 82, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 83, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 84, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 85, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 86, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 87, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 88, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 89, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 90, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 91, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 92, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 93, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 94, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 95, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 96, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 97, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 98, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 99, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 100, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 101, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 102, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 103, "data": {"value": 127, "label": 0}},
            {"data_relative_timestamp": 104, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 105, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 106, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 107, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 108, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 109, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 110, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 111, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 112, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 113, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 114, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 115, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 116, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 117, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 118, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 119, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 120, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 121, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 122, "data": {"value": 118, "label": 0}},
            {"data_relative_timestamp": 123, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 124, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 125, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 126, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 127, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 128, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 129, "data": {"value": 118, "label": 0}},
            {"data_relative_timestamp": 130, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 131, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 132, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 133, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 134, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 135, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 136, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 137, "data": {"value": 118, "label": 0}},
            {"data_relative_timestamp": 138, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 139, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 140, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 141, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 142, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 143, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 144, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 145, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 146, "data": {"value": 127, "label": 0}},
            {"data_relative_timestamp": 147, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 148, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 149, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 150, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 151, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 152, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 153, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 154, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 155, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 156, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 157, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 158, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 159, "data": {"value": 120, "label": 0}},
            {"data_relative_timestamp": 160, "data": {"value": 122, "label": 0}},
            {"data_relative_timestamp": 161, "data": {"value": 118, "label": 0}},
            {"data_relative_timestamp": 162, "data": {"value": 125, "label": 0}},
            {"data_relative_timestamp": 163, "data": {"value": 122, "label": 0}},
        ],
    }
    assert expected == actual


def test_integer_2():
    """Function comments"""
    actual = uncompress(
        1,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 1},
        ],
        "201600206018180000007ae201726c922d59920520ad",
    )
    expected = {
        "batch_counter": 6,
        "batch_relative_timestamp": 504,
        "dataset": [
            {"data_relative_timestamp": 454, "data": {"value": 61, "label": 0}},
            {"data_relative_timestamp": 455, "data": {"value": 62, "label": 0}},
            {"data_relative_timestamp": 451, "data": {"value": 0, "label": 1}},
            {"data_relative_timestamp": 452, "data": {"value": 1, "label": 1}},
            {"data_relative_timestamp": 496, "data": {"value": 0, "label": 1}},
            {"data_relative_timestamp": 497, "data": {"value": 1, "label": 1}},
            {"data_relative_timestamp": 499, "data": {"value": 0, "label": 1}},
            {"data_relative_timestamp": 500, "data": {"value": 1, "label": 1}},
            {"data_relative_timestamp": 501, "data": {"value": 0, "label": 1}},
            {"data_relative_timestamp": 502, "data": {"value": 1, "label": 1}},
        ],
    }
    assert expected == actual


def test_common_timestamp():
    actual = uncompress(
        3,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 10},
            {"taglbl": 2, "resol": 1, "sampletype": 7},
            {"taglbl": 3, "resol": 1, "sampletype": 7},
            {"taglbl": 4, "resol": 1, "sampletype": 6},
        ],
        "523000800310050AE1DEC124B41F680FEC01003802237B00008EC01080009DB08C8819AF126440382419100ED903",
    )
    expected = {
        "batch_counter": 0,
        "batch_relative_timestamp": 3624,
        "dataset": [
            {"data_relative_timestamp": 1824, "data": {"value": 7297, "label": 0}},
            {"data_relative_timestamp": 3624, "data": {"value": 14497, "label": 0}},
            {"data_relative_timestamp": 1824, "data": {"value": 7297, "label": 1}},
            {"data_relative_timestamp": 3624, "data": {"value": 14497, "label": 1}},
            {"data_relative_timestamp": 1824, "data": {"value": 1005, "label": 2}},
            {"data_relative_timestamp": 3624, "data": {"value": 1005, "label": 2}},
            {"data_relative_timestamp": 1824, "data": {"value": 2580, "label": 3}},
            {"data_relative_timestamp": 3624, "data": {"value": 2541, "label": 3}},
            {"data_relative_timestamp": 1824, "data": {"value": 3622, "label": 4}},
            {"data_relative_timestamp": 3624, "data": {"value": 3676, "label": 4}},
        ],
    }
    assert expected == actual


def test_common_timestamp_2():
    """Function comments"""
    actual = uncompress(
        2,
        [
            {"taglbl": 0, "resol": 10, "sampletype": 7},
            {"taglbl": 1, "resol": 100, "sampletype": 6},
            {"taglbl": 2, "resol": 1, "sampletype": 6},
        ],
        "322040c884854308b04f308df611942100f90649c908",
    )
    expected = {
        "batch_counter": 0,
        "batch_relative_timestamp": 2167609,
        "dataset": [
            {"data_relative_timestamp": 2167574, "data": {"value": 2470, "label": 0}},
            {"data_relative_timestamp": 2167604, "data": {"value": 2470, "label": 0}},
            {"data_relative_timestamp": 2167574, "data": {"value": 4500, "label": 1}},
            {"data_relative_timestamp": 2167604, "data": {"value": 4500, "label": 1}},
            {"data_relative_timestamp": 2167574, "data": {"value": 3617, "label": 2}},
        ],
    }
    assert expected == actual


def test_hex_to_array():
    assert hex_to_array(
        "$10$27$00$80$03$93$20$18$00$80$10$81$83$07$0d$45$85$10$05"
    ) == [16, 39, 0, 128, 3, 147, 32, 24, 0, 128, 16, 129, 131, 7, 13, 69, 133, 16, 5]


def test_next_sample():
    buf = Buffer(
        [16, 39, 0, 128, 3, 147, 32, 24, 0, 128, 16, 129, 131, 7, 13, 69, 133, 16, 5]
    )
    assert buf.next_sample(constants.ST_U8, 8) == 16


def test_generate_flag():
    """Function comments"""
    f = Flag(16)
    assert f.cts == 0
    assert f.no_sample == 0
    assert f.batch_req == 0
    assert f.nb_of_type_measure == 1


def test_find_index_of_lbl():
    pass
    """Function comments"""
    arglist = [
        {"taglbl": 2, "lblname": "temperature", "resol": 1.0, "sampletype": 12},
        {"taglbl": 3, "lblname": "temperature", "resol": 1.0, "sampletype": 12},
    ]
    assert find_index_of_lbl(arglist, 3) == 1


def test_find_index_of_lbl_with_a_bad_value():
    """Function comments"""
    arglist = [
        {"taglbl": 2, "lblname": "temperature", "resol": 1.0, "sampletype": 12},
        {"taglbl": 3, "lblname": "temperature", "resol": 1.0, "sampletype": 12},
    ]
    with pytest.raises(Exception, match="Cannot find index in arg_list"):
        find_index_of_lbl(arglist, 4)


def test_float_conversion():
    """Function comments"""
    assert to_float(1093664768) == float(11)


def test_timestamp_iso_format():
    """Function comments"""

    actual = uncompress(
        3,
        [
            {"taglbl": 0, "resol": 1, "sampletype": 10},
            {"taglbl": 1, "resol": 1, "sampletype": 10},
            {"taglbl": 2, "resol": 1, "sampletype": 7},
            {"taglbl": 3, "resol": 1, "sampletype": 7},
            {"taglbl": 4, "resol": 1, "sampletype": 6},
        ],
        "523000800310050AE1DEC124B41F680FEC01003802237B00008EC01080009DB08C8819AF126440382419100ED903",
        "2018-10-05T10:00:00.000Z",
    )

    expected = {
        "batch_counter": 0,
        "batch_relative_timestamp": 3624,
        "batch_absolute_timestamp": "2018-10-05T10:00:00.000Z",
        "dataset": [
            {
                "data_relative_timestamp": 1824,
                "data": {"value": 7297, "label": 0},
                "data_absolute_timestamp": "2018-10-05T09:30:00.000Z",
            },
            {
                "data_relative_timestamp": 3624,
                "data": {"value": 14497, "label": 0},
                "data_absolute_timestamp": "2018-10-05T10:00:00.000Z",
            },
            {
                "data_relative_timestamp": 1824,
                "data": {"value": 7297, "label": 1},
                "data_absolute_timestamp": "2018-10-05T09:30:00.000Z",
            },
            {
                "data_relative_timestamp": 3624,
                "data": {"value": 14497, "label": 1},
                "data_absolute_timestamp": "2018-10-05T10:00:00.000Z",
            },
            {
                "data_relative_timestamp": 1824,
                "data": {"value": 1005, "label": 2},
                "data_absolute_timestamp": "2018-10-05T09:30:00.000Z",
            },
            {
                "data_relative_timestamp": 3624,
                "data": {"value": 1005, "label": 2},
                "data_absolute_timestamp": "2018-10-05T10:00:00.000Z",
            },
            {
                "data_relative_timestamp": 1824,
                "data": {"value": 2580, "label": 3},
                "data_absolute_timestamp": "2018-10-05T09:30:00.000Z",
            },
            {
                "data_relative_timestamp": 3624,
                "data": {"value": 2541, "label": 3},
                "data_absolute_timestamp": "2018-10-05T10:00:00.000Z",
            },
            {
                "data_relative_timestamp": 1824,
                "data": {"value": 3622, "label": 4},
                "data_absolute_timestamp": "2018-10-05T09:30:00.000Z",
            },
            {
                "data_relative_timestamp": 3624,
                "data": {"value": 3676, "label": 4},
                "data_absolute_timestamp": "2018-10-05T10:00:00.000Z",
            },
        ],
    }

    assert actual == expected
