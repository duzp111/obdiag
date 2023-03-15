#!/usr/bin/env python
# -*- coding: UTF-8 -*
# Copyright (c) 2022 OceanBase
# OceanBase Diagnostic Tool is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

"""
@time: 2022/6/22
@file: version_utils.py
@desc:
"""


def compare_versions_greater(v1, v2):
    for i, j in zip(map(int, v1.split(".")), map(int, v2.split("."))):
        if i == j:
            continue
        return i > j
    return len(v1.split(".")) > len(v2.split("."))


def compare_versions_lower(v1, v2):
    for i, j in zip(map(int, v1.split(".")), map(int, v2.split("."))):
        if i == j:
            continue
        return i < j
    return len(v1.split(".")) < len(v2.split("."))