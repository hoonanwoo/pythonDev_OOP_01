import os
from time import asctime


#fileLog = "C:\Users\Public\pythonCode\logFile_store"
fileLog = '/home/hoonanwoo/Desktop/stuff/pythonCODE/logFile_store'

timeLog_stamp = asctime()

 

class TestDMT:
    'TestDMT base class for logFile operation code storage.'
    objectCount = 0

    def __init__(self,opCode):
         self.opCode = opCode



def generateTestDMT_object(filePointer):
    testDMT_object = TestDMT(0)
    TestDMT.objectCount += 1


    try:
        opCode_input = raw_input("\n\tEnter DMT Error_opCode: ")
        setattr(testDMT_object,'opCode',opCode_input)
        filePointer.writelines(timeLog_stamp + '\t')
        log_testDMT_object_opCode = testDMT_object.opCode
        filePointer.write('_opCode: ' + log_testDMT_object_opCode + '\n')
    except IOError:
         print("testIOError: [Erno 2] No such file or directory")



def main():
    filePointer = open(fileLog,'a')
    generateTestDMT_object(filePointer)
 

if __name__ == '__main__':
    main()
