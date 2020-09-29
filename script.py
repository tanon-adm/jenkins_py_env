#!/usr/bin/env python3.8

import argparse
import enum
import itertools
import logging
import os
import sys
import pathlib

print ('this is python script')
passwd = os.environ.get('PASSWORD')
var1 = "sonar.password={}".format(passwd)
print(var1)
