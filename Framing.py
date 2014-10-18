#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is a Psychopy adaptation of the experimental design of De Martino et al. (2006).

This experiment was created using PsychoPy2 Experiment Builder (v1.81.00), Thu Oct 16 13:34:11 2014
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
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=True,
    monitor='testMonitor', color='black', colorSpace='rgb',
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
    text='1',    font='Arial', units='cm', alignHoriz='center',
    pos=[0, 0], height=3, wrapWidth=20,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
FixationPoint = visual.TextStim(win=win, ori=0, name='FixationPoint',
    text='+',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
ProbabilityLeft = visual.ImageStim(win=win, name='ProbabilityLeft',
    image=u'Keep80.jpg', mask=None, units='cm',
    ori=0, pos=[-15, 0], size=[22, 17],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True)
ProbabilityRight = visual.ImageStim(win=win, name='ProbabilityRight',
    image=u'Keep80.jpg', mask=None, units='cm',
    ori=0, pos=[15, 0], size=[22, 17],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True)
FixedLeft = visual.TextStim(win=win, ori=0, name='FixedLeft',
    text=cos,    font='Arial',
    pos=[-15, 0], height=3, wrapWidth=None, units='cm',
    color='white', colorSpace='rgb', opacity=1)
FixedRight = visual.TextStim(win=win, ori=0, name='FixedRight',
    text='',    font='Arial',
    pos=[15, 0], height=3, wrapWidth=None, units='cm',
    color='white', colorSpace='rgb', opacity=1)
MiddleLine = visual.Line(win, start=(0, -14), end=(0, 14), units='cm', lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb')

# Initialize components for Routine "Outcome"
OutcomeClock = core.Clock()
SelectLeft = visual.Rect(win=win, name='SelectLeft',
    width=[17, 17][0], height=[17, 17][1], units='cm',
    ori=0, pos=[-15, 0],
    lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
    opacity=1,interpolate=True)
SelectRight = visual.Rect(win=win, name='SelectRight',
    width=[17, 17][0], height=[17, 17][1],units='cm',
    ori=0, pos=[15, 0],
    lineWidth=3, lineColor='yellow', lineColorSpace='rgb',
    opacity=1,interpolate=True)
    
# Initialize components for Routine "Slow"
SlowClock = core.Clock()
SlowText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'Too Slow', font=u'Arial', pos=[0, 0], height=3, units='cm', wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

# Instalize components for "Rest"
RestClock = core.Clock()
RestText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'Great! Now have a rest and press spacebar when you are ready to begin the next block.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)

# Instalize components for "Thank You"
ThankYouClock = core.Clock()
ThankYouText = visual.TextStim(win=win, ori=0, name='rest_prompt_txt', text=u'You have now completed this experiment. Thank you for your participation. Please inform the experimenter that you have finished.', font=u'Arial', pos=[0, 0], height=0.08, wrapWidth=None, color=u'white', colorSpace=u'rgb', opacity=1, depth=0.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
FramingLoop = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'FramingTrialHandler.csv'),
    seed=None, name='FramingLoop')
thisExp.addLoop(FramingLoop)  # add the loop to the experiment
thisFramingLoop = FramingLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFramingLoop.rgb)
if thisFramingLoop != None:
    for paramName in thisFramingLoop.keys():
        exec(paramName + '= thisFramingLoop.' + paramName)

################################ FRAMING LOOP STARTS ####################################################

# Before the loop, we set up a counter to control the rest screen between the blocks!
RestCounter = 0

for thisFramingLoop in FramingLoop:
    currentLoop = FramingLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFramingLoop.rgb)
    if thisFramingLoop != None:
        for paramName in thisFramingLoop.keys():
            exec(paramName + '= thisFramingLoop.' + paramName)
    
    # Increase the RestCounter by 1 per trial
    RestCounter += 1
    #------Prepare to start Routine "OriginalValue"-------
    # determine the text for the OriginalValueStimuli:
    BaseValueText=u'You recieve \n %s' %Full_Amount
    t = 0
    OriginalValueClock.reset()  # clock 
    frameN = -1
#    routineTimer.add(20.000000)
    # update component parameters for each repeat
    BaseValue.setText(BaseValueText)
    # keep track of which components have finished
    OriginalValueComponents = []
    OriginalValueComponents.append(BaseValue)
    for thisComponent in OriginalValueComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "OriginalValue"-------
    continueRoutine = True
    while continueRoutine:
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
        elif BaseValue.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
    # If the gamble should be shown on the right side of the screen, run the following:
    if GambleLeft == 0:
        # Creating a variable to simplify storing participants' answers at the end of the routine
        RightChoice=Gamble
        LeftChoice=Stable
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        ProbabilityRight.setImage(Gamble)
        FixedLeft.setText(Stable)
        # Update Keyboard parameters
        event.clearEvents(eventType='keyboard')
        KeyResp = event.BuilderKeyResponse()
        KeyResp.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(FixationPoint)
        trialComponents.append(ProbabilityRight)
        trialComponents.append(FixedLeft)
        trialComponents.append(MiddleLine)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
    
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine: # and routineTimer.getTime() > 0:
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
        
                # *MiddleLine* updates
            if t >= 0.5 and MiddleLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                MiddleLine.tStart = t  # underestimates by a little under one frame
                MiddleLine.frameNStart = frameN  # exact frame index
                MiddleLine.setAutoDraw(True)
            elif MiddleLine.status == STARTED and t >= (0.5 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                MiddleLine.setAutoDraw(False)
    
            # *ProbabilityRight* updates
            if t >= 0.5 and ProbabilityRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                ProbabilityRight.tStart = t  # underestimates by a little under one frame
                ProbabilityRight.frameNStart = frameN  # exact frame index
                ProbabilityRight.setAutoDraw(True)
            elif ProbabilityRight.status == STARTED and t >= (0.5 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                ProbabilityRight.setAutoDraw(False)
        
            # *FixedLeft* updates
            if t >= 0.5 and FixedLeft.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixedLeft.tStart = t  # underestimates by a little under one frame
                FixedLeft.frameNStart = frameN  # exact frame index
                FixedLeft.setAutoDraw(True)
            elif FixedLeft.status == STARTED and t >= (0.5 + (4.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                FixedLeft.setAutoDraw(False)
        
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period
        
            # *KeyResp* updates
            if t >= 0.5 and KeyResp.status == NOT_STARTED:
                KeyResp.tStart = t
                KeyResp.frameNStart = frameN
                KeyResp.status = STARTED
                KeyResp.clock.reset()
            if KeyResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
            
                # check for quit:
                if 'escape' in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:
                    KeyResp.keys = theseKeys[-1]
                    KeyResp.rt = KeyResp.clock.getTime()
                    continueRoutine = False
                
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
                    # check responses
        if KeyResp.keys in ['', [], None]:
            KeyResp.keys = None
    
    
        # Store data for experiment:
        thisExp.addData('Frame', Frame)
        thisExp.addData('Stable', Stable)
        thisExp.addData('Gamble', Gamble)
        thisExp.addData('FullAmount', Full_Amount)
        thisExp.addData('GambleLeft', GambleLeft)
        thisExp.addData('Catch', Catch)
        thisExp.addData('Response', KeyResp.keys)
        if KeyResp.keys != None:
            thisExp.addData('RT', KeyResp.rt)
        if KeyResp.keys == 'left':
            thisExp.addData('Choice', LeftChoice)
        if KeyResp.keys == 'right':
            thisExp.addData('Choice', RightChoice)
        thisExp.nextEntry()
        
        # Only do the outcome routine if there is a response of this trial
        if KeyResp.keys != None:
            #------Prepare to start Routine "Outcome"-------
            t = 0
            OutcomeClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # keep track of which components have finished
            OutcomeComponents = []
            OutcomeComponents.append(SelectLeft)
            OutcomeComponents.append(SelectRight)
            OutcomeComponents.append(ProbabilityRight)
            OutcomeComponents.append(FixedLeft)
            OutcomeComponents.append(MiddleLine)
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
    
            #-------Start Routine "Outcome"-------
            continueRoutine = True
            while continueRoutine: # and routineTimer.getTime() > 0:
                # get current time
                t = OutcomeClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
            
                # *MiddleLine* updates
                if t >= 0 and MiddleLine.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    MiddleLine.tStart = t  # underestimates by a little under one frame
                    MiddleLine.frameNStart = frameN  # exact frame index
                    MiddleLine.setAutoDraw(True)
                elif MiddleLine.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    MiddleLine.setAutoDraw(False)
    
                # *ProbabilityRight* updates
                if t >= 0 and ProbabilityRight.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ProbabilityRight.tStart = t  # underestimates by a little under one frame
                    ProbabilityRight.frameNStart = frameN  # exact frame index
                    ProbabilityRight.setAutoDraw(True)
                elif ProbabilityRight.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ProbabilityRight.setAutoDraw(False)
        
                # *FixedLeft* updates
                if t >= 0 and FixedLeft.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    FixedLeft.tStart = t  # underestimates by a little under one frame
                    FixedLeft.frameNStart = frameN  # exact frame index
                    FixedLeft.setAutoDraw(True)
                elif FixedLeft.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    FixedLeft.setAutoDraw(False)
        
                # *SelectLeft* updates
                if t >= 0 and SelectLeft.status == NOT_STARTED and KeyResp.keys =='left':
                    # keep track of start time/frame for later
                    SelectLeft.tStart = t  # underestimates by a little under one frame
                    SelectLeft.frameNStart = frameN  # exact frame index
                    SelectLeft.setAutoDraw(True)
                elif SelectLeft.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SelectLeft.setAutoDraw(False)
                    continueRoutine = False
                
                # *SelectRight* updates
                if t >= 0 and SelectRight.status == NOT_STARTED and KeyResp.keys =='right':
                    # keep track of start time/frame for later
                    SelectRight.tStart = t  # underestimates by a little under one frame
                    SelectRight.frameNStart = frameN  # exact frame index
                    SelectRight.setAutoDraw(True)
                elif SelectRight.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SelectRight.setAutoDraw(False)
                    continueRoutine = False
            
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in OutcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                    # check for quit (the Esc key)
                    if endExpNow or event.getKeys(keyList=["escape"]):
                        core.quit()
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            #-------Ending Routine "Outcome"-------
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
        
        # If people were too slow to respond start the Slow routine
        if KeyResp.keys == None:
           
           #------Prepare to start Routine "Slow"-------
            t = 0
            SlowClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # keep track of which components have finished
            SlowComponents = []
            SlowComponents.append(SlowText)
            for thisComponent in SlowComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
    
            #-------Start Routine "Slow"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = SlowClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *SlowText* updates
                if t >= 0.0 and SlowText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    SlowText.tStart = t  # underestimates by a little under one frame
                    SlowText.frameNStart = frameN  # exact frame index
                    SlowText.setAutoDraw(True)
                elif SlowText.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SlowText.setAutoDraw(False)
        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SlowComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
                #-------Ending Routine "Slow"-------
                for thisComponent in OriginalValueComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
        
# If the gamble should be shown on the left side of the screen, run the following:
    if GambleLeft == 1:
        # Creating a variable to simplify storing participants' answers at the end of the routine
        RightChoice=Stable
        LeftChoice=Gamble
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        ProbabilityLeft.setImage(Gamble)
        FixedRight.setText(Stable)
        # Update Keyboard parameters
        event.clearEvents(eventType='keyboard')
        KeyResp = event.BuilderKeyResponse()
        KeyResp.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(ISI)
        trialComponents.append(FixationPoint)
        trialComponents.append(ProbabilityLeft)
        trialComponents.append(FixedRight)
        trialComponents.append(MiddleLine)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
    
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine: # and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *MiddleLine* updates
            if t >= 0.5 and MiddleLine.status == NOT_STARTED:
                # keep track of start time/frame for later
                MiddleLine.tStart = t  # underestimates by a little under one frame
                MiddleLine.frameNStart = frameN  # exact frame index
                MiddleLine.setAutoDraw(True)
            elif MiddleLine.status == STARTED and t >= (0.5 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
                MiddleLine.setAutoDraw(False)
        
            # *FixationPoint* updates
            if t >= 0.0 and FixationPoint.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixationPoint.tStart = t  # underestimates by a little under one frame
                FixationPoint.frameNStart = frameN  # exact frame index
                FixationPoint.setAutoDraw(True)
            elif FixationPoint.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                FixationPoint.setAutoDraw(False)
        
    
           # *ProbabilityLeft* updates
            if t >= 0.5 and ProbabilityLeft.status == NOT_STARTED:
                # keep track of start time/frame for later
                ProbabilityLeft.tStart = t  # underestimates by a little under one frame
                ProbabilityLeft.frameNStart = frameN  # exact frame index
                ProbabilityLeft.setAutoDraw(True)
            elif ProbabilityLeft.status == STARTED and t >= (0.5 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
                ProbabilityLeft.setAutoDraw(False)
        
             # *FixedRight* updates
            if t >= 0.5 and FixedRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixedRight.tStart = t  # underestimates by a little under one frame
                FixedRight.frameNStart = frameN  # exact frame index
                FixedRight.setAutoDraw(True)
            elif FixedRight.status == STARTED and t >= (0.5 + (4-win.monitorFramePeriod*0.75)): #most of one frame period left
                FixedRight.setAutoDraw(False)
        
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t  # underestimates by a little under one frame
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(0.5)
            elif ISI.status == STARTED: #one frame should pass before updating params and completing
                ISI.complete() #finish the static period
            
            
            # *KeyResp* updates
            if t >= 0.5 and KeyResp.status == NOT_STARTED:
                KeyResp.tStart = t
                KeyResp.frameNStart = frameN
                KeyResp.status = STARTED
                KeyResp.clock.reset()
            if KeyResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
            
                # check for quit:
                if 'escape' in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:
                    KeyResp.keys = theseKeys[-1]
                    KeyResp.rt = KeyResp.clock.getTime()
                    continueRoutine = False
            
                
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
        # check responses
        if KeyResp.keys in ['', [], None]:
            KeyResp.keys = None
    
    
        # Store data for experiment:
        thisExp.addData('Frame', Frame)
        thisExp.addData('Stable', Stable)
        thisExp.addData('Gamble', Gamble)
        thisExp.addData('FullAmount', Full_Amount)
        thisExp.addData('GambleLeft', GambleLeft)
        thisExp.addData('Catch', Catch)
        thisExp.addData('Response', KeyResp.keys)
        if KeyResp.keys != None:
            thisExp.addData('RT', KeyResp.rt)
        if KeyResp.keys == 'left':
            thisExp.addData('Choice', LeftChoice)
        if KeyResp.keys == 'right':
            thisExp.addData('Choice', RightChoice)
        thisExp.nextEntry()
        
        # Only do the outcome routine if there is a response of this trial
        if KeyResp.keys != None:
        
            #------Prepare to start Routine "Outcome"-------
            t = 0
            OutcomeClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # keep track of which components have finished
            OutcomeComponents = []
            OutcomeComponents.append(SelectLeft)
            OutcomeComponents.append(SelectRight)
            OutcomeComponents.append(ProbabilityLeft)
            OutcomeComponents.append(FixedRight)
            OutcomeComponents.append(MiddleLine)
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            #-------Start Routine "Outcome"-------
            continueRoutine = True
            while continueRoutine: # and routineTimer.getTime() > 0:
                # get current time
                t = OutcomeClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
            
                # *MiddleLine* updates
                if t >= 0 and MiddleLine.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    MiddleLine.tStart = t  # underestimates by a little under one frame
                    MiddleLine.frameNStart = frameN  # exact frame index
                    MiddleLine.setAutoDraw(True)
                elif MiddleLine.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    MiddleLine.setAutoDraw(False)
    
                # *ProbabilityRight* updates
                if t >= 0 and ProbabilityLeft.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    ProbabilityLeft.tStart = t  # underestimates by a little under one frame
                    ProbabilityLeft.frameNStart = frameN  # exact frame index
                    ProbabilityLeft.setAutoDraw(True)
                elif ProbabilityLeft.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    ProbabilityLeft.setAutoDraw(False)
        
                # *FixedLeft* updates
                if t >= 0 and FixedRight.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    FixedRight.tStart = t  # underestimates by a little under one frame
                    FixedRight.frameNStart = frameN  # exact frame index
                    FixedRight.setAutoDraw(True)
                elif FixedRight.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    FixedRight.setAutoDraw(False)
        
                # *SelectLeft* updates
                if t >= 0 and SelectLeft.status == NOT_STARTED and KeyResp.keys=='left':
                    # keep track of start time/frame for later
                    SelectLeft.tStart = t  # underestimates by a little under one frame
                    SelectLeft.frameNStart = frameN  # exact frame index
                    SelectLeft.setAutoDraw(True)
                elif SelectLeft.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SelectLeft.setAutoDraw(False)
                    continueRoutine = False
        
                # *SelectRight* updates
                if t >= 0 and SelectRight.status == NOT_STARTED and KeyResp.keys=='right':
                    # keep track of start time/frame for later
                    SelectRight.tStart = t  # underestimates by a little under one frame
                    SelectRight.frameNStart = frameN  # exact frame index
                    SelectRight.setAutoDraw(True)
                elif SelectRight.status == STARTED and t >= (0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SelectRight.setAutoDraw(False)
                    continueRoutine = False
            
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in OutcomeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
            #-------Ending Routine "Outcome"-------
            for thisComponent in OutcomeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
        
        # If people were too slow to respond start the Slow routine
        elif KeyResp.keys == None:
           
           #------Prepare to start Routine "Slow"-------
            t = 0
            SlowClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # keep track of which components have finished
            SlowComponents = []
            SlowComponents.append(SlowText)
            for thisComponent in SlowComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
    
            #-------Start Routine "Slow"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = SlowClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        
                # *SlowText* updates
                if t >= 0.0 and SlowText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    SlowText.tStart = t  # underestimates by a little under one frame
                    SlowText.frameNStart = frameN  # exact frame index
                    SlowText.setAutoDraw(True)
                elif SlowText.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    SlowText.setAutoDraw(False)
        
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SlowComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
        
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
        
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
    
                #-------Ending Routine "Slow"-------
                for thisComponent in OriginalValueComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                
    # If the trial number is divisible by 10, display the rest prompt
    if RestCounter % 96 == 0 and RestCounter != 288:
        
        #------Prepare to start Routine "Rest"-------
        t = 0
        RestClock.reset()
        frameN = -1
        # update component parameters for each repeat
        RestResponse = event.BuilderKeyResponse()
        RestResponse.status = NOT_STARTED
        # keep track of which components have finished
        RestComponents = []
        RestComponents.append(RestText)
        RestComponents.append(RestResponse)
        for thisComponent in RestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Rest"-------
        continueRoutine = True
        while continueRoutine:
            t = RestClock.getTime()
            frameN = frameN + 1
            
            # *RestText* updates
            if t >= 0.0 and RestText.status == NOT_STARTED:
                RestText.tStart = t
                RestText.frameNStart = frameN
                RestText.setAutoDraw(True)
            
            # *RestResponse* updates
            if t >= 2.0 and RestResponse.status == NOT_STARTED:
                RestResponse.tStart = t
                RestResponse.frameNStart = frameN
                RestResponse.status = STARTED
                RestResponse.clock.reset()
                event.clearEvents(eventType='keyboard')
            if RestResponse.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if 'escape' in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:
                    RestResponse.keys = theseKeys[-1]
                    RestResponse.rt = RestResponse.clock.getTime()
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:
                routineTimer.reset()
                break
            continueRoutine = False
            for thisComponent in RestComponents:
                if hasattr(thisComponent, 'status') and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(
            keyList=['escape']):
                core.quit()
            
            # refresh the screen
            if continueRoutine:
                win.flip()
            else:
                routineTimer.reset()

        #-------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, 'setAutoDraw'):
                thisComponent.setAutoDraw(False)
        # check responses
        if RestResponse.keys in ['', [], None]:
            RestResponse.keys = None
        # store data for MainStaircase (ExperimentHandler)
        if RestResponse.keys != None:
            thisExp.addData('RestTime', RestResponse.rt)  
            thisExp.nextEntry()
            
################################ FRAMING LOOP FINISHED ####################################################

#------Prepare to start Routine "Thank You"-------
t = 0
ThankYouClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ThankYouResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
ThankYouResponse.status = NOT_STARTED
# keep track of which components have finished
ThankYouComponents = []
ThankYouComponents.append(Instructions3Text)
ThankYouComponents.append(Instructions3Response)
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "ThankYou"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ThankYouClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankYouText* updates
    if t >= 0.0 and ThankYouText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouText.tStart = t  # underestimates by a little under one frame
        ThankYouText.frameNStart = frameN  # exact frame index
        ThankYouText.setAutoDraw(True)
    
    # *ThankYouResponse* updates
    if t >= 0 and ThankYouResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThankYouResponse.tStart = t  # underestimates by a little under one frame
        ThankYouResponse.frameNStart = frameN  # exact frame index
        ThankYouResponse.status = STARTED
        # keyboard checking is just starting
        ThankYouResponse.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if ThankYouResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ThankYouResponse.keys = theseKeys[-1]  # just the last key pressed
            ThankYouResponse.rt = ThankYouResponse.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Close experimental window
win.close()
core.quit()
