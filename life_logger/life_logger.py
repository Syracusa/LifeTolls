from collections import deque
from random import lognormvariate
from time import time
import json

class LogType:
    def __init__(self, log_name, log_interval_sec, selector):
        self.logName = log_name
        self.logRequestIntervalSec = log_interval_sec
        self.selector = selector
        self.lastAnswerTime = None
        
    def setRequestInverval(self, interval):
        self.logRequestInterval = interval

class LogTypeManager:
    def __init__(self):
        self.logNameDict = {}
        pass

    def readLogTypeListFromFile():
        pass

    def addLogType(self, log_type:LogType):
        self.logNameDict[log_type.logName] = log_type
        pass

    def addLogTypeList(self, logtype_list):
        for ltype in logtype_list:
            self.logNameDict[ltype.logName] = ltype
        pass
    def getLogTypeList(self):
        pass

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, ensure_ascii = False)

    def getJson(self):
        for lt in self.logNameDict:
            pass
        return json.dumps(self.logNameDict)
        pass

    def setJson(self, json_input):
        parsed = json.loads(json_input)
        self.logNameDict = parsed['logNameDict']
        pass

class LifeLog:
    def __init__(self, log_name, log_datatype, log_data):
        self.logName = log_name
        self.logDatatype = log_datatype
        self.logData = log_data
        self.logTime = time
        self.logTimeZone = 'KST'
        pass

class Life:
    def __init__(self):
        self.lifeLogList = deque([])
        pass

class RequestType:
    pass

class LogRequester:
    def __init__(self):
        self.requestList = []
        pass
    
    def checkRequestTime():
        pass

    def doRequest():
        pass

class LifeLogger:
    def __init__(self):
        pass

    def do_question():
        pass