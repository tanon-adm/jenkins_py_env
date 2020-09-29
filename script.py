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
var2 = "value1"
var3 = "value2"
print(var1)
print("""# required metadata
sonar.projectVersion=0.x
sonar.language=c++

sonar.technicaldebt.daily.rate=680.0

# path to source directories (required)
sonar.sources=.

# credentials
sonar.forceAuthentication=true
sonar.login=tech_mcdcore
{}

sonar.cxx.errorRecoveryEnabled=true
#sonar.cxx.forceIncludes=VS10Macros.h
#sonar.cxx.includeDirectories=.

sonar.cxx.suffixes.sources=.c,.cpp
sonar.cxx.suffixes.headers=.h,.hh,.hpp,.inl,.ice
{}
{}

# Enterprise edition SonarQube has 2 different plugins for C++, we should be using the plugin which is compatible with QACPP
# So disable these suffixes explicitly, as per RBEI team's advice
sonar.c.file.suffixes=-
sonar.cpp.file.suffixes=-
sonar.objc.file.suffixes=-""".format(var1, var2, var3))
