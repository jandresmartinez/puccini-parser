import logging
import sys, puccini.tosca, ard
logger = logging.getLogger(__name__)
from . import base


@base.route("/test/")
def index():
    return "Hello"


@base.route("/parse/")
def index2():
    try:
        clout = puccini.tosca.compile(url)
        ard.write(clout, sys.stdout)
    except puccini.tosca.Problems as e:
        print('Problems:', file=sys.stderr)
        for problem in e.problems:
            ard.write(problem, sys.stderr)
