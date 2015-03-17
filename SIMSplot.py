# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:43:45 2015

@author: acoppola
"""
import csv
from matplotlib import pyplot as plt
import numpy as np

qtypes = ['I', 'R', 'E', 'A','I', 'R', 'E', 'A','I', 'R', 'E', 'A','I', 'R', 'E', 'A'] #for standard week of SIMS
moWeights = {'I':1, 'R':.33, 'E': -.33, 'A': -1} #motivation weights for summing (aribitrary so far)

class Survey(object):
    """One survey object per week
        Attributes:
            CSVfile: the corresponding "raw" data for this survey
            week: number of week of this survey
            questions: list of questions asked this week
        Functions:
            __init__: parses a CSV to create survey (see Week1Quant.csv for formatting)
            getQuestions: adds the survey questions to the questions(object) attribute          
    """
    
    def __init__(self, CSVfile, week):
        self.questions = []
        self.CSVfile = CSVfile #see Week1Quant.csv for example formatting
        self.week = week
        self.getQuestions(CSVfile, week) #parse first line of CSV for questions
                                        #with SIMS, the questions should not change,
                                        #but this code leaves room for them to change
        
    def getQuestions(self, CSVfile, week): #create the list of questions for this week
        """parses the CSV for the questions, located on the first line
            each question is an object and must be created with its responses"""
        questions = []
        RawData = csv.reader(open(self.CSVfile, newline=''))
        qLine = RawData.__next__()
        for question in qLine[0:-1]:
            questions.append(Question(question, 
                                        qLine.index(question),
                                        CSVfile,
                                        week))
        self.questions = questions
    
class Question(object):
    """As many questions as there are on the survey
        Attributes:
            text: what the question asks
            qnumb: the question number for the week it was asked
            qtype: descriptor of the type of motivation (I, R, E, or A)
            week: the week it was asked
            responses: list of responses for this question
            moQual: average "motivation quality" of answers. 
                    spans -3 to 3, with 3 being highest intrinsic motivation,
                    and -3 being amotivation
            hist: a dictionary of the responses and frequencies
        Notable Funtions:
            getResponses: gets the corresponding responses from the CSV
            plotHist: plots a histogram of responses
        """

    def __init__(self, text, qnumb, CSVfile, week):
        self.text = text
        self.qnumb = qnumb
        self.qtype = qtypes[qnumb]
        self.responses = self.getResponses(CSVfile, week)
        self.moQual = self.defineMoQual()
        self.hist = self.makeHist()
        
    def defineMoQual(self):
        moQual = 0
        for response in self.responses:
            moQual += response.moVal
        moQual = moQual/len(self.responses)
        return(moQual)
        
    def getResponses(self, CSVfile, week):
        RawData = csv.reader(open(CSVfile, newline=''))
        qLine = RawData.__next__()
        responses = []
        try:
            while True:
                thisLine = RawData.__next__()
                responses.append(Response(
                                thisLine[-1],
                                self.qnumb,
                                week,
                                int(thisLine[self.qnumb])))
        except StopIteration:
            return (responses)
        
    def makeHist(self):
        hist = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
        for response in self.responses:
            hist[response.value] = hist.get(response.value, 0) + 1
        return(hist)
        
    def plotHist(self):
        """plots a histogram of the responses for that week"""
        X = []
        Y = []
        for item in self.hist.items():
            X.append(int(item[0]))
            Y.append(int(item[1]))
        plt.bar(X,Y, align='center')
        plt.xticks([1,2,3,4,5,6,7])
        plt.ylim(0,len(self.responses))
        plt.title(self.text)
        plt.xlabel('Number of Responses')
        plt.ylabel('Value of Response')
        for x, y in zip(X, Y):
            plt.text(x, y, str(y), ha='center', va='bottom')
        plt.show()
        
class Response(object):
    """One Response object for each response on the survey
        Attributes:
            question
            ID: ID number of the student
            value: what the response was
            week: what week was this response given?
    """
            
    def __init__(self, ID, qnumb, week, value):
        self.ID = ID
        self.qnumb = qnumb
        self.week = week
        self.value = value
        self.qtype = qtypes[qnumb]
        self.moVal = self.defineMoVal()
        
    def defineMoVal(self):
        moVal = (self.value-4)*qMoVals[self.qtype]
        return(moVal)
        
        
        
#class User(object):
#    """As many users as we have who answered the survey
#        Attributes:
#            ID: ID number of the student
#            responses: list of their responses for all questions
#    """
#    
#    def __init___(self, ID, responses = []):
#        self.ID = ID
#        self.responses = responses
#        
#    def addResponse(self, response):
#        self.responses.append(response)
        

Week1Survey = Survey('Week1Quant.csv', 1)
for question in Week1Survey.questions:
    question.plotHist()
    print(question.qtype, question.moQual)
#    for response in question.responses:
#        print(response.moVal)
#print(len(Week1Survey.questions))
#for response in Week1Survey.questions[1].responses:
#    print(response.moVal)
#

    