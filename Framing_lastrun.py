#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.00), Fri Oct 17 16:16:15 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Framing'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/Tomas/Documents/FramingExperiment/Framing.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "OriginalValue"
OriginalValueClock = core.Clock()
BaseValue = visual.TextStim(win=win, ori=0, name='BaseValue',
    text='The current value is...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
FixationPoint = visual.TextStim(win=win, ori=0, name='FixationPoint',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
SelectLeft = visual.Rect(win=win, name='SelectLeft',
    width=[0.3, 0.3][0], height=[0.3, 0.3][1],
    ori=0, pos=[0, -0.5],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,interpolate=True)
SelectRight = visual.Rect(win=win, name='SelectRight',
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0, 0.5],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,interpolate=True)
ProbabilityLeft = visual.Aperture(win=win, name='ProbabilityLeft',
    units='norm', size=1, pos=(0, -0.5))
ProbabilityLeft.disable()  # disable until its actually used
ProbabilityRight = visual.Aperture(win=win, name='ProbabilityRight',
    units='norm', size=1, pos=(0, 0.5))
ProbabilityRight.disable()  # disable until its actually used
FixedLeft = visual.TextStim(win=win, ori=0, name='FixedLeft',
    text='Any text\n\nincluding line breaks',    font='Arial',
    pos=[0, -0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
FixedRight = visual.TextStim(win=win, ori=0, name='FixedRight',
    text='Any text\n\nincluding line breaks',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
polygon = visual.Line(win=win, name='polygon',
    start=(-[5, 5][0]/2.0, 0), end=(+[5, 5][0]/2.0, 0),
    ori=1, pos=[0, 0],
    lineWidth=3, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
FramingLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'/Users/Tomas/Documents/FramingExperiment/Framing.psyexp',
    trialList=data.importConditions('FramingTrialHandler.csv'),
    seed=None, name='FramingLoop')
thisExp.addLoop(FramingLoop)  # add the loop to the experiment
thisFramingLoop = FramingLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFramingLoop.rgb)
if thisFramingLoop != None:
    for paramName in thisFramingLoop.keys():
        exec(paramName + '= thisFramingLoop.' + paramName)

for thisFramingLoop in FramingLoop:
    currentLoop = FramingLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFramingLoop.rgb)
    if thisFramingLoop != None:
        for paramName in thisFramingLoop.keys():
            exec(paramName + '= thisFramingLoop.' + paramName)
    
    #------Prepare to start Routine "OriginalValue"-------
    t = 0
    OriginalValueClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    OriginalValueComponents = []
    OriginalValueComponents.append(BaseValue)
    for thisComponent in OriginalValueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "OriginalValue"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = OriginalValueClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BaseValue* updates
        if t >= 0.0 and BaseValue.status == NOT_STARTED:
            # keep track of start time/frame for later
            BaseValue.tStart = t  # underestimates by a little under one frame
            BaseValue.frameNStart = frameN  # exact frame index
            BaseValue.setAutoDraw(True)
        elif BaseValue.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            BaseValue.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OriginalValueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "OriginalValue"-------
    for thisComponent in OriginalValueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(FixationPoint)
    trialComponents.append(SelectLeft)
    trialComponents.append(SelectRight)
    trialComponents.append(ProbabilityLeft)
    trialComponents.append(ProbabilityRight)
    trialComponents.append(FixedLeft)
    trialComponents.append(FixedRight)
    trialComponents.append(polygon)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationPoint* updates
        if t >= 0.0 and FixationPoint.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixationPoint.tStart = t  # underestimates by a little under one frame
            FixationPoint.frameNStart = frameN  # exact frame index
            FixationPoint.setAutoDraw(True)
        elif FixationPoint.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            FixationPoint.setAutoDraw(False)
        
        # *SelectLeft* updates
        if t >= 0.5 and SelectLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            SelectLeft.tStart = t  # underestimates by a little under one frame
            SelectLeft.frameNStart = frameN  # exact frame index
            SelectLeft.setAutoDraw(True)
        elif SelectLeft.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            SelectLeft.setAutoDraw(False)
        
        # *SelectRight* updates
        if t >= 0.5 and SelectRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            SelectRight.tStart = t  # underestimates by a little under one frame
            SelectRight.frameNStart = frameN  # exact frame index
            SelectRight.setAutoDraw(True)
        elif SelectRight.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            SelectRight.setAutoDraw(False)
        
        # *ProbabilityLeft* updates
        if t >= 0.5 and ProbabilityLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProbabilityLeft.tStart = t  # underestimates by a little under one frame
            ProbabilityLeft.frameNStart = frameN  # exact frame index
            ProbabilityLeft.enabled = True
        elif ProbabilityLeft.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            ProbabilityLeft.enabled = False
        
        # *ProbabilityRight* updates
        if t >= 0.5 and ProbabilityRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            ProbabilityRight.tStart = t  # underestimates by a little under one frame
            ProbabilityRight.frameNStart = frameN  # exact frame index
            ProbabilityRight.enabled = True
        elif ProbabilityRight.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            ProbabilityRight.enabled = False
        
        # *FixedLeft* updates
        if t >= 0.5 and FixedLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixedLeft.tStart = t  # underestimates by a little under one frame
            FixedLeft.frameNStart = frameN  # exact frame index
            FixedLeft.setAutoDraw(True)
        elif FixedLeft.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            FixedLeft.setAutoDraw(False)
        
        # *FixedRight* updates
        if t >= 0.5 and FixedRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            FixedRight.tStart = t  # underestimates by a little under one frame
            FixedRight.frameNStart = frameN  # exact frame index
            FixedRight.setAutoDraw(True)
        elif FixedRight.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            FixedRight.setAutoDraw(False)
        
        # *polygon* updates
        if t >= 0.5 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t  # underestimates by a little under one frame
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        elif polygon.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            polygon.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ProbabilityLeft.enabled = False  # just in case it was left enabled
    ProbabilityRight.enabled = False  # just in case it was left enabled
    thisExp.nextEntry()
    
# completed 1 repeats of 'FramingLoop'

win.close()
core.quit()
