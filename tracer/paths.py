#-*- coding: utf-8 -*-
# paths.py
# Module for defining paths to project directories. They are different when
# project is developed on git and when project is installed as a linux package
#
# Copyright (C) 2014 Jakub Kadlčík
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

import os
from os.path import dirname, realpath


def __(paths):
	for path in paths:
		if os.path.isdir(path):
			return path
	return paths[0]



PROJECT_DIR = dirname(dirname(realpath(__file__)))

DATA_DIR = __([
	PROJECT_DIR + '/' + 'data',
	'/usr/share/tracer',
])
