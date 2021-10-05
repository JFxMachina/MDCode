#!/bin/bash

sphinx-apidoc -o source/ ../mdcode
sphinx-build 'source' 'build'