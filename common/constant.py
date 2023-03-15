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
@time: 2022/8/2
@file: constant.py
@desc:
"""


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


const = _const()

const.OB_INSTALL_DIR_DEFAULT = "/home/admin/oceanbase"
const.OB_LOG_DIR_DEFAULT = "/home/admin/oceanbase/log"
const.OBPROXY_LOG_DIR_DEFAULT = "/home/admin/obproxy/log"

const.GATHER_LOG_TEMPORARY_DIR_DEFAULT = "/tmp"

# 限制收集任务的并发线程数量 10
const.GATHER_THREADS_LIMIT = 10
# 限制收集任务的并发线程单个线程的执行超时时间 15分钟
const.GATHER_THREAD_TIMEOUT = 15 * 60
# obstack2收集堆栈信息支持的最小版本
const.MIN_OB_VERSION_SUPPORT_GATHER_OBSTACK = "2.0.0"

const.MAX_OB_VERSION_SUPPORT_GATHER_OBADMIN = "4.0.0"