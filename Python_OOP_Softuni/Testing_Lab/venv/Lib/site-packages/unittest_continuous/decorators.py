import sys
import time
import traceback
import socket
import json
import unittest
from xml.sax.saxutils import escape

RECEIVER_HOST = "buildserver.continuous.io"
RECEIVER_PORT = 8001

class ContinuousTestResultWrapper(object):
    """Prepare data from continuous.io
    
    Based on _XmlTextTestResult by Gareth Rushgrove:
    https://github.com/garethr/django-test-extensions
    """
    
    def __init__(self, stream, build_id, build_secret):
        self.stream = stream
        self.descriptions = True
        self._lastWas = 'success'
        self._errorsAndFailures = ""
        self._startTime = 0.0
        self.params=""
        
        self.build_id = build_id
        self.build_secret = build_secret
        self.conn = self.getStreamConnection()

    def getDescription(self, test):
        if self.descriptions:
            return test.shortDescription() or str(test)
        else:
            return str(test)

    def startTest(self, result, test):
        self.startTestXml(result, test)
    
    def stopTest(self, result, test):
        self.stopTestXml(result, test)
    
    def addSuccess(self, result, test):
        self.addSuccessXml(result, test)
        self.streamSuccess(result, test)
    
    def addError(self, result, test, err):
        self.addErrorXml(result, test, err)
        self.streamError(result, test, err)
    
    def addFailure(self, result, test, err):
        self.addFailureXml(result, test, err)
        self.streamFailure(result, test, err)
    
    # XML recording methods
    
    def startTestXml(self, result, test):
        self._startTime = time.time()
        test._extraXML = ''
        test._extraAssertions = []
        self.stream.write('<testcase classname="%s.%s" name="%s"' % (test.__class__.__module__, test.__class__.__name__, test.id().split('.')[-1]))
        desc = test.shortDescription()

        if desc:
            desc = _cleanHTML(desc)
            self.stream.write(' desc="%s"' % desc)
    
    def stopTestXml(self, result, test):
        stopTime = time.time()
        deltaTime = stopTime - self._startTime
        self.stream.write(' time="%.3f"' % deltaTime)
        self.stream.write(">")
        if self._lastWas != 'success':
            if self._lastWas == 'error':
                self.stream.write(self._errorsAndFailures)
            elif self._lastWas == 'failure':
                self.stream.write(self._errorsAndFailures)
            else:
                assert(False)

        seen = {}

        for assertion in test._extraAssertions:
            if not seen.has_key(assertion):
                self._addAssertion(assertion[:110]) # :110 avoids tl;dr TODO use a lexical truncator
                seen[assertion] = True

        self.stream.write("</testcase>\n")
        self._errorsAndFailures = ""

        if test._extraXML != '':
            self.stream.write(test._extraXML)
    
    def _addAssertion(self, diagnostic):
        diagnostic = _cleanHTML(diagnostic)
        self.stream.write('<assert>' + diagnostic + "</assert>\n")

    def addSuccessXml(self, result, test):
        self._lastWas = 'success'

    def addErrorXml(self, result, test, err):
        if err[0] is KeyboardInterrupt:
            self.shouldStop = 1
        self._lastWas = 'error'
        self._errorsAndFailures += """\n<error type="%s">""" % err[0].__name__
        ex_string = traceback.format_exception(*err)
        self._errorsAndFailures += escape("".join(ex_string))
        self._errorsAndFailures += "</error>\n"

    def addFailureXml(self, result, test, err):
        if err[0] is KeyboardInterrupt:
            self.shouldStop = 1
        self._lastWas = 'failure'
        self._errorsAndFailures += """\n<failure type="%s">""" % err[0].__name__
        ex_string = traceback.format_exception(*err)
        self._errorsAndFailures += escape("".join(ex_string))
        self._errorsAndFailures += "</failure>\n"
    
    # Data streaming methods
    
    def getStreamConnection(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(5)
        try:
            connection.connect((RECEIVER_HOST, RECEIVER_PORT))
            connection.settimeout(1800)
        except socket.timeout:
            # Errors are no big deal - the result XML should be posted 
            # to continuous.io when done anyway
            connection.settimeout(1)
    
        return connection
    
    def streamSuccess(self, result, test):
        name = ".".join((test.__module__, test.__class__.__name__, test._testMethodName))
        self._streamResult(name, result="S", test=test)
    
    def streamFailure(self, result, test, err):
        name = ".".join((test.__module__, test.__class__.__name__, test._testMethodName))
        self._streamResult(name, result="F", test=test, err=err)
    
    def streamError(self, result, test, err):
        name = ".".join((test.__module__, test.__class__.__name__, test._testMethodName))
        self._streamResult(name, result="F", test=test, err=err)
    
    def _streamResult(self, name, result, test, err=None):
        result = {
            "name": name,
            "result": result[:1].upper(),
            "build_secret": self.build_secret,
            "build_id": self.build_id,
        }
        
        if err:
            result.update({
                "logs": "\n".join(getattr(test, "capturedLogging", []) or []),
                "stdout": "\n".join(getattr(test, "capturedOutput", []) or []),
                "trace": traceback.print_exception(*err),
            })
        
        try:
            self.conn.send(json.dumps(result) + "\r\n")
        except socket.error:
            # Errors are no big deal - the result XML should be posted 
            # to continuous.io when done anyway
            pass
        
    

def _cleanHTML(whut):
    return whut.replace('"', '&quot;'). \
                replace('<', '&lt;').  \
                replace('>', '&gt;')
    

def wrap(f, result, call):
    def inner(*args, **kwargs):
        call(result, *args, **kwargs)
        return f(*args, **kwargs)
    
    return inner

def _makeResultWrap(f, build_id, build_secret):
    def _makeResult(self, *args, **kwargs):
        result = f(self, *args, **kwargs)
        
        fh = open("results.xml", "w")
        wrapper = ContinuousTestResultWrapper(fh, build_id, build_secret)
        
        result.startTest = wrap(result.startTest, result, wrapper.startTest)
        result.stopTest = wrap(result.stopTest, result, wrapper.stopTest)
        result.addSuccess = wrap(result.addSuccess, result, wrapper.addSuccess)
        result.addError = wrap(result.addError, result, wrapper.addError)
        result.addFailure = wrap(result.addFailure, result, wrapper.addFailure)
        
        return result
    
    return _makeResult

