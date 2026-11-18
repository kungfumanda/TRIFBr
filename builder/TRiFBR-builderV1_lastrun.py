#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.3),
    on November 10, 2026, at 17:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_2
import os

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.3'
expName = 'Teste de Reconhecimento Identidade de Faces - TRIFBr'  # from the Builder filename that created this script
expVersion = '1'
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'Participante ID': '',
    'Idade': '',
    'Gênero': '',
    'Experimento': 'TESTE',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1366, 768]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s' % (expInfo['Participante ID'], expName)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\amdas\\Documents\\Experimentos\\TRIFBr\\builder\\TRiFBR-builderV1_lastrun.py',
        savePickle=False, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='deg',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'deg'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Iniciando o teste...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcomeRoutine" ---
    text_title = visual.TextStim(win=win, name='text_title',
        text='Bem-vindo(a) ao Teste de Reconhecimento\nde Identidade de Faces.',
        font='Arial',
        units='norm', pos=(0, 0.7), draggable=False, height=0.09, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_body = visual.TextStim(win=win, name='text_body',
        text='TAREFA: \nUm vídeo com uma face aparecerá no centro. Identifique qual das 4 opções abaixo corresponde à mesma face.\n\nCOMO RESPONDER:\nUse o MOUSE para clicar na face OU Use o TECLADO (1, 2, 3, 4)\n\nDETALHES:\nO teste começará com uma breve etapa de familiarização.\nO teste é dividido em blocos. Haverá pausas automáticas entre eles.',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.07, wrapWidth=1.6, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_advance = visual.TextStim(win=win, name='text_advance',
        text='Vamos fazer um teste? \nPressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        units='norm', pos=(0, -0.7), draggable=False, height=0.06, wrapWidth=1.5, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_response_initiate = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_initiate = event.Mouse(win=win)
    x, y = [None, None]
    mouse_initiate.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code_2
    block_number = 0
    
    
    # --- Initialize components for Routine "exampleInstruction" ---
    text_example = visual.TextStim(win=win, name='text_example',
        text='Este é um exemplo deste teste',
        font='Arial',
        units='height', pos=(0, 0.8), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    video_instruction = visual.ImageStim(
        win=win,
        name='video_instruction', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    continue_keys = visual.TextStim(win=win, name='continue_keys',
        text='Clique em algum das opções ou digite o seu número para continuar.',
        font='Arial',
        units='height', pos=(0, -0.04), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_instruction_1 = visual.TextStim(win=win, name='text_instruction_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    image_instruction_1 = visual.ImageStim(
        win=win,
        name='image_instruction_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_instruction_2 = visual.TextStim(win=win, name='text_instruction_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13,-0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    image_instruction_2 = visual.ImageStim(
        win=win,
        name='image_instruction_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_instruction_3 = visual.TextStim(win=win, name='text_instruction_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    image_instruction_3 = visual.ImageStim(
        win=win,
        name='image_instruction_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    text_instruction_4 = visual.TextStim(win=win, name='text_instruction_4',
        text='4',
        font='Arial',
        units='height', pos=(0.40, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    image_instruction_4 = visual.ImageStim(
        win=win,
        name='image_instruction_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    key_response_intructions = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_instructions = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_instructions.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "blockIntro" ---
    txt_block_title = visual.TextStim(win=win, name='txt_block_title',
        text='',
        font='Arial',
        pos=(0, 1), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_response = visual.TextStim(win=win, name='text_response',
        text='Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        pos=(0, -2), draggable=False, height=0.7, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trialFaceRecognition" ---
    video_trial = visual.ImageStim(
        win=win,
        name='video_trial', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.42),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stim_image_1 = visual.ImageStim(
        win=win,
        name='stim_image_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    stim_image_2 = visual.ImageStim(
        win=win,
        name='stim_image_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stim_image_3 = visual.ImageStim(
        win=win,
        name='stim_image_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='4',
        font='Arial',
        units='height', pos=(0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    stim_image_4 = visual.ImageStim(
        win=win,
        name='stim_image_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    key_response_trial = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_trial = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_trial.mouseClock = core.Clock()
    targetID_Teste = visual.TextStim(win=win, name='targetID_Teste',
        text='',
        font='Arial',
        units='height', pos=(-0.48, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "pause" ---
    
    # --- Initialize components for Routine "blockIntro" ---
    txt_block_title = visual.TextStim(win=win, name='txt_block_title',
        text='',
        font='Arial',
        pos=(0, 1), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_response = visual.TextStim(win=win, name='text_response',
        text='Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        pos=(0, -2), draggable=False, height=0.7, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trialFaceRecognition" ---
    video_trial = visual.ImageStim(
        win=win,
        name='video_trial', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.42),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stim_image_1 = visual.ImageStim(
        win=win,
        name='stim_image_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    stim_image_2 = visual.ImageStim(
        win=win,
        name='stim_image_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stim_image_3 = visual.ImageStim(
        win=win,
        name='stim_image_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='4',
        font='Arial',
        units='height', pos=(0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    stim_image_4 = visual.ImageStim(
        win=win,
        name='stim_image_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    key_response_trial = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_trial = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_trial.mouseClock = core.Clock()
    targetID_Teste = visual.TextStim(win=win, name='targetID_Teste',
        text='',
        font='Arial',
        units='height', pos=(-0.48, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "pause_2" ---
    
    # --- Initialize components for Routine "blockIntro" ---
    txt_block_title = visual.TextStim(win=win, name='txt_block_title',
        text='',
        font='Arial',
        pos=(0, 1), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_response = visual.TextStim(win=win, name='text_response',
        text='Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        pos=(0, -2), draggable=False, height=0.7, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trialFaceRecognition" ---
    video_trial = visual.ImageStim(
        win=win,
        name='video_trial', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.42),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stim_image_1 = visual.ImageStim(
        win=win,
        name='stim_image_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    stim_image_2 = visual.ImageStim(
        win=win,
        name='stim_image_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stim_image_3 = visual.ImageStim(
        win=win,
        name='stim_image_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='4',
        font='Arial',
        units='height', pos=(0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    stim_image_4 = visual.ImageStim(
        win=win,
        name='stim_image_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    key_response_trial = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_trial = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_trial.mouseClock = core.Clock()
    targetID_Teste = visual.TextStim(win=win, name='targetID_Teste',
        text='',
        font='Arial',
        units='height', pos=(-0.48, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "pause_3" ---
    
    # --- Initialize components for Routine "blockIntro" ---
    txt_block_title = visual.TextStim(win=win, name='txt_block_title',
        text='',
        font='Arial',
        pos=(0, 1), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_response = visual.TextStim(win=win, name='text_response',
        text='Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        pos=(0, -2), draggable=False, height=0.7, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trialFaceRecognition" ---
    video_trial = visual.ImageStim(
        win=win,
        name='video_trial', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.42),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stim_image_1 = visual.ImageStim(
        win=win,
        name='stim_image_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    stim_image_2 = visual.ImageStim(
        win=win,
        name='stim_image_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stim_image_3 = visual.ImageStim(
        win=win,
        name='stim_image_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='4',
        font='Arial',
        units='height', pos=(0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    stim_image_4 = visual.ImageStim(
        win=win,
        name='stim_image_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    key_response_trial = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_trial = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_trial.mouseClock = core.Clock()
    targetID_Teste = visual.TextStim(win=win, name='targetID_Teste',
        text='',
        font='Arial',
        units='height', pos=(-0.48, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "pause_4" ---
    
    # --- Initialize components for Routine "blockIntro" ---
    txt_block_title = visual.TextStim(win=win, name='txt_block_title',
        text='',
        font='Arial',
        pos=(0, 1), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_response = visual.TextStim(win=win, name='text_response',
        text='Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
        font='Arial',
        pos=(0, -2), draggable=False, height=0.7, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_resp = event.Mouse(win=win)
    x, y = [None, None]
    mouse_resp.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trialFaceRecognition" ---
    video_trial = visual.ImageStim(
        win=win,
        name='video_trial', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(None, 0.42),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        units='height', pos=(-0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stim_image_1 = visual.ImageStim(
        win=win,
        name='stim_image_1', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        units='height', pos=(-0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    stim_image_2 = visual.ImageStim(
        win=win,
        name='stim_image_2', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        units='height', pos=(0.13, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stim_image_3 = visual.ImageStim(
        win=win,
        name='stim_image_3', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.13, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    text_4 = visual.TextStim(win=win, name='text_4',
        text='4',
        font='Arial',
        units='height', pos=(0.4, -0.10), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    stim_image_4 = visual.ImageStim(
        win=win,
        name='stim_image_4', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.40, -0.30), draggable=False, size=(None, 0.32),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    key_response_trial = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    mouse_response_trial = event.Mouse(win=win)
    x, y = [None, None]
    mouse_response_trial.mouseClock = core.Clock()
    targetID_Teste = visual.TextStim(win=win, name='targetID_Teste',
        text='',
        font='Arial',
        units='height', pos=(-0.48, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    
    # --- Initialize components for Routine "pause_5" ---
    
    # --- Initialize components for Routine "finalRoutine" ---
    text = visual.TextStim(win=win, name='text',
        text='Agradecemos por participar!',
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.09, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcomeRoutine" ---
    # create an object to store info about Routine welcomeRoutine
    welcomeRoutine = data.Routine(
        name='welcomeRoutine',
        components=[text_title, text_body, text_advance, key_response_initiate, mouse_initiate],
    )
    welcomeRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_response_initiate
    key_response_initiate.keys = []
    key_response_initiate.rt = []
    _key_response_initiate_allKeys = []
    # setup some python lists for storing info about the mouse_initiate
    gotValidClick = False  # until a click is received
    # store start times for welcomeRoutine
    welcomeRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcomeRoutine.tStart = globalClock.getTime(format='float')
    welcomeRoutine.status = STARTED
    welcomeRoutine.maxDuration = None
    # keep track of which components have finished
    welcomeRoutineComponents = welcomeRoutine.components
    for thisComponent in welcomeRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcomeRoutine" ---
    thisExp.currentRoutine = welcomeRoutine
    welcomeRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_title* updates
        
        # if text_title is starting this frame...
        if text_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_title.frameNStart = frameN  # exact frame index
            text_title.tStart = t  # local t and not account for scr refresh
            text_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_title.status = STARTED
            text_title.setAutoDraw(True)
        
        # if text_title is active this frame...
        if text_title.status == STARTED:
            # update params
            pass
        
        # *text_body* updates
        
        # if text_body is starting this frame...
        if text_body.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_body.frameNStart = frameN  # exact frame index
            text_body.tStart = t  # local t and not account for scr refresh
            text_body.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_body, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_body.status = STARTED
            text_body.setAutoDraw(True)
        
        # if text_body is active this frame...
        if text_body.status == STARTED:
            # update params
            pass
        
        # *text_advance* updates
        
        # if text_advance is starting this frame...
        if text_advance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_advance.frameNStart = frameN  # exact frame index
            text_advance.tStart = t  # local t and not account for scr refresh
            text_advance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_advance, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_advance.status = STARTED
            text_advance.setAutoDraw(True)
        
        # if text_advance is active this frame...
        if text_advance.status == STARTED:
            # update params
            pass
        
        # *key_response_initiate* updates
        waitOnFlip = False
        
        # if key_response_initiate is starting this frame...
        if key_response_initiate.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_response_initiate.frameNStart = frameN  # exact frame index
            key_response_initiate.tStart = t  # local t and not account for scr refresh
            key_response_initiate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response_initiate, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_response_initiate.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response_initiate.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response_initiate.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response_initiate.status == STARTED and not waitOnFlip:
            theseKeys = key_response_initiate.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_response_initiate_allKeys.extend(theseKeys)
            if len(_key_response_initiate_allKeys):
                key_response_initiate.keys = _key_response_initiate_allKeys[-1].name  # just the last key pressed
                key_response_initiate.rt = _key_response_initiate_allKeys[-1].rt
                key_response_initiate.duration = _key_response_initiate_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_initiate* updates
        
        # if mouse_initiate is starting this frame...
        if mouse_initiate.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_initiate.frameNStart = frameN  # exact frame index
            mouse_initiate.tStart = t  # local t and not account for scr refresh
            mouse_initiate.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_initiate, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_initiate.status = STARTED
            mouse_initiate.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_initiate.prevButtonState = mouse_initiate.getPressed()
        if mouse_initiate.status == STARTED:  # only update if started and not finished!
            buttons = mouse_initiate.getPressed()
            # button state changed?
            if buttons != mouse_initiate.prevButtonState:
                mouse_initiate.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=welcomeRoutine,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            welcomeRoutine.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if welcomeRoutine.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in welcomeRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcomeRoutine" ---
    for thisComponent in welcomeRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcomeRoutine
    welcomeRoutine.tStop = globalClock.getTime(format='float')
    welcomeRoutine.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "welcomeRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    introTrials = data.TrialHandler2(
        name='introTrials',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-intro.csv'), 
        seed=None, 
        isTrials=False, 
    )
    thisExp.addLoop(introTrials)  # add the loop to the experiment
    thisIntroTrial = introTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIntroTrial.rgb)
    if thisIntroTrial != None:
        for paramName in thisIntroTrial:
            globals()[paramName] = thisIntroTrial[paramName]
    
    for thisIntroTrial in introTrials:
        introTrials.status = STARTED
        if hasattr(thisIntroTrial, 'status'):
            thisIntroTrial.status = STARTED
        currentLoop = introTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisIntroTrial.rgb)
        if thisIntroTrial != None:
            for paramName in thisIntroTrial:
                globals()[paramName] = thisIntroTrial[paramName]
        
        # --- Prepare to start Routine "exampleInstruction" ---
        # create an object to store info about Routine exampleInstruction
        exampleInstruction = data.Routine(
            name='exampleInstruction',
            components=[text_example, video_instruction, continue_keys, text_instruction_1, image_instruction_1, text_instruction_2, image_instruction_2, text_instruction_3, image_instruction_3, text_instruction_4, image_instruction_4, key_response_intructions, mouse_response_instructions],
        )
        exampleInstruction.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames_intro
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        image_instruction_1.setImage(Image_1)
        image_instruction_2.setImage(Image_2)
        image_instruction_3.setImage(Image_3)
        image_instruction_4.setImage(Image_4)
        # create starting attributes for key_response_intructions
        key_response_intructions.keys = []
        key_response_intructions.rt = []
        _key_response_intructions_allKeys = []
        # setup some python lists for storing info about the mouse_response_instructions
        mouse_response_instructions.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for exampleInstruction
        exampleInstruction.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        exampleInstruction.tStart = globalClock.getTime(format='float')
        exampleInstruction.status = STARTED
        exampleInstruction.maxDuration = None
        # keep track of which components have finished
        exampleInstructionComponents = exampleInstruction.components
        for thisComponent in exampleInstruction.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "exampleInstruction" ---
        thisExp.currentRoutine = exampleInstruction
        exampleInstruction.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisIntroTrial, 'status') and thisIntroTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_example* updates
            
            # if text_example is starting this frame...
            if text_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_example.frameNStart = frameN  # exact frame index
                text_example.tStart = t  # local t and not account for scr refresh
                text_example.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_example, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_example.status = STARTED
                text_example.setAutoDraw(True)
            
            # if text_example is active this frame...
            if text_example.status == STARTED:
                # update params
                pass
            
            # *video_instruction* updates
            
            # if video_instruction is starting this frame...
            if video_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_instruction.frameNStart = frameN  # exact frame index
                video_instruction.tStart = t  # local t and not account for scr refresh
                video_instruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_instruction, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_instruction.status = STARTED
                video_instruction.setAutoDraw(True)
            
            # if video_instruction is active this frame...
            if video_instruction.status == STARTED:
                # update params
                video_instruction.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *continue_keys* updates
            
            # if continue_keys is starting this frame...
            if continue_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue_keys.frameNStart = frameN  # exact frame index
                continue_keys.tStart = t  # local t and not account for scr refresh
                continue_keys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_keys, 'tStartRefresh')  # time at next scr refresh
                # update status
                continue_keys.status = STARTED
                continue_keys.setAutoDraw(True)
            
            # if continue_keys is active this frame...
            if continue_keys.status == STARTED:
                # update params
                pass
            
            # *text_instruction_1* updates
            
            # if text_instruction_1 is starting this frame...
            if text_instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_instruction_1.frameNStart = frameN  # exact frame index
                text_instruction_1.tStart = t  # local t and not account for scr refresh
                text_instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instruction_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_instruction_1.status = STARTED
                text_instruction_1.setAutoDraw(True)
            
            # if text_instruction_1 is active this frame...
            if text_instruction_1.status == STARTED:
                # update params
                pass
            
            # *image_instruction_1* updates
            
            # if image_instruction_1 is starting this frame...
            if image_instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_instruction_1.frameNStart = frameN  # exact frame index
                image_instruction_1.tStart = t  # local t and not account for scr refresh
                image_instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_instruction_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_instruction_1.status = STARTED
                image_instruction_1.setAutoDraw(True)
            
            # if image_instruction_1 is active this frame...
            if image_instruction_1.status == STARTED:
                # update params
                pass
            
            # *text_instruction_2* updates
            
            # if text_instruction_2 is starting this frame...
            if text_instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_instruction_2.frameNStart = frameN  # exact frame index
                text_instruction_2.tStart = t  # local t and not account for scr refresh
                text_instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instruction_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_instruction_2.status = STARTED
                text_instruction_2.setAutoDraw(True)
            
            # if text_instruction_2 is active this frame...
            if text_instruction_2.status == STARTED:
                # update params
                pass
            
            # *image_instruction_2* updates
            
            # if image_instruction_2 is starting this frame...
            if image_instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_instruction_2.frameNStart = frameN  # exact frame index
                image_instruction_2.tStart = t  # local t and not account for scr refresh
                image_instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_instruction_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_instruction_2.status = STARTED
                image_instruction_2.setAutoDraw(True)
            
            # if image_instruction_2 is active this frame...
            if image_instruction_2.status == STARTED:
                # update params
                pass
            
            # *text_instruction_3* updates
            
            # if text_instruction_3 is starting this frame...
            if text_instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_instruction_3.frameNStart = frameN  # exact frame index
                text_instruction_3.tStart = t  # local t and not account for scr refresh
                text_instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instruction_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_instruction_3.status = STARTED
                text_instruction_3.setAutoDraw(True)
            
            # if text_instruction_3 is active this frame...
            if text_instruction_3.status == STARTED:
                # update params
                pass
            
            # *image_instruction_3* updates
            
            # if image_instruction_3 is starting this frame...
            if image_instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_instruction_3.frameNStart = frameN  # exact frame index
                image_instruction_3.tStart = t  # local t and not account for scr refresh
                image_instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_instruction_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_instruction_3.status = STARTED
                image_instruction_3.setAutoDraw(True)
            
            # if image_instruction_3 is active this frame...
            if image_instruction_3.status == STARTED:
                # update params
                pass
            
            # *text_instruction_4* updates
            
            # if text_instruction_4 is starting this frame...
            if text_instruction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_instruction_4.frameNStart = frameN  # exact frame index
                text_instruction_4.tStart = t  # local t and not account for scr refresh
                text_instruction_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_instruction_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_instruction_4.status = STARTED
                text_instruction_4.setAutoDraw(True)
            
            # if text_instruction_4 is active this frame...
            if text_instruction_4.status == STARTED:
                # update params
                pass
            
            # *image_instruction_4* updates
            
            # if image_instruction_4 is starting this frame...
            if image_instruction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_instruction_4.frameNStart = frameN  # exact frame index
                image_instruction_4.tStart = t  # local t and not account for scr refresh
                image_instruction_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_instruction_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_instruction_4.status = STARTED
                image_instruction_4.setAutoDraw(True)
            
            # if image_instruction_4 is active this frame...
            if image_instruction_4.status == STARTED:
                # update params
                pass
            
            # *key_response_intructions* updates
            waitOnFlip = False
            
            # if key_response_intructions is starting this frame...
            if key_response_intructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_intructions.frameNStart = frameN  # exact frame index
                key_response_intructions.tStart = t  # local t and not account for scr refresh
                key_response_intructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_intructions, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_intructions.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_response_intructions.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_response_intructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_response_intructions.status == STARTED and not waitOnFlip:
                theseKeys = key_response_intructions.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_intructions_allKeys.extend(theseKeys)
                if len(_key_response_intructions_allKeys):
                    key_response_intructions.keys = _key_response_intructions_allKeys[-1].name  # just the last key pressed
                    key_response_intructions.rt = _key_response_intructions_allKeys[-1].rt
                    key_response_intructions.duration = _key_response_intructions_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_instructions* updates
            
            # if mouse_response_instructions is starting this frame...
            if mouse_response_instructions.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_response_instructions.frameNStart = frameN  # exact frame index
                mouse_response_instructions.tStart = t  # local t and not account for scr refresh
                mouse_response_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_instructions, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_instructions.status = STARTED
                mouse_response_instructions.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_instructions.prevButtonState = mouse_response_instructions.getPressed()
            if mouse_response_instructions.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_instructions.getPressed()
                # button state changed?
                if buttons != mouse_response_instructions.prevButtonState:
                    mouse_response_instructions.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([image_instruction_1,image_instruction_2,image_instruction_3,image_instruction_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_instructions):
                                gotValidClick = True
                                mouse_response_instructions.clicked_name.append(obj.name)
                                mouse_response_instructions.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=exampleInstruction,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                exampleInstruction.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if exampleInstruction.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in exampleInstruction.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "exampleInstruction" ---
        for thisComponent in exampleInstruction.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for exampleInstruction
        exampleInstruction.tStop = globalClock.getTime(format='float')
        exampleInstruction.tStopRefresh = tThisFlipGlobal
        # store data for introTrials (TrialHandler)
        # the Routine "exampleInstruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisIntroTrial as finished
        if hasattr(thisIntroTrial, 'status'):
            thisIntroTrial.status = FINISHED
        # if awaiting a pause, pause now
        if introTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            introTrials.status = STARTED
    # completed 1 repeats of 'introTrials'
    introTrials.status = FINISHED
    
    
    # --- Prepare to start Routine "blockIntro" ---
    # create an object to store info about Routine blockIntro
    blockIntro = data.Routine(
        name='blockIntro',
        components=[txt_block_title, text_response, key_resp, mouse_resp],
    )
    blockIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_num
    block_number +=1
    
    block_title = f"BLOCO {block_number}"
    txt_block_title.setText(block_title)
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    gotValidClick = False  # until a click is received
    # store start times for blockIntro
    blockIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blockIntro.tStart = globalClock.getTime(format='float')
    blockIntro.status = STARTED
    blockIntro.maxDuration = None
    # keep track of which components have finished
    blockIntroComponents = blockIntro.components
    for thisComponent in blockIntro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockIntro" ---
    thisExp.currentRoutine = blockIntro
    blockIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_block_title* updates
        
        # if txt_block_title is starting this frame...
        if txt_block_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_block_title.frameNStart = frameN  # exact frame index
            txt_block_title.tStart = t  # local t and not account for scr refresh
            txt_block_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_block_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            txt_block_title.status = STARTED
            txt_block_title.setAutoDraw(True)
        
        # if txt_block_title is active this frame...
        if txt_block_title.status == STARTED:
            # update params
            pass
        
        # *text_response* updates
        
        # if text_response is starting this frame...
        if text_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_response.frameNStart = frameN  # exact frame index
            text_response.tStart = t  # local t and not account for scr refresh
            text_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_response.status = STARTED
            text_response.setAutoDraw(True)
        
        # if text_response is active this frame...
        if text_response.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        
        # if mouse_resp is starting this frame...
        if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_resp.prevButtonState = mouse_resp.getPressed()
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            # button state changed?
            if buttons != mouse_resp.prevButtonState:
                mouse_resp.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blockIntro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blockIntro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blockIntro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blockIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockIntro" ---
    for thisComponent in blockIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blockIntro
    blockIntro.tStop = globalClock.getTime(format='float')
    blockIntro.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block1Trials = data.TrialHandler2(
        name='block1Trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-B1.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(block1Trials)  # add the loop to the experiment
    thisBlock1Trial = block1Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1Trial.rgb)
    if thisBlock1Trial != None:
        for paramName in thisBlock1Trial:
            globals()[paramName] = thisBlock1Trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlock1Trial in block1Trials:
        block1Trials.status = STARTED
        if hasattr(thisBlock1Trial, 'status'):
            thisBlock1Trial.status = STARTED
        currentLoop = block1Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlock1Trial.rgb)
        if thisBlock1Trial != None:
            for paramName in thisBlock1Trial:
                globals()[paramName] = thisBlock1Trial[paramName]
        
        # --- Prepare to start Routine "trialFaceRecognition" ---
        # create an object to store info about Routine trialFaceRecognition
        trialFaceRecognition = data.Routine(
            name='trialFaceRecognition',
            components=[video_trial, text_1, stim_image_1, text_2, stim_image_2, text_3, stim_image_3, text_4, stim_image_4, key_response_trial, mouse_response_trial, targetID_Teste],
        )
        trialFaceRecognition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        stim_image_1.setImage(Image_1)
        stim_image_2.setImage(Image_2)
        stim_image_3.setImage(Image_3)
        stim_image_4.setImage(Image_4)
        # create starting attributes for key_response_trial
        key_response_trial.keys = []
        key_response_trial.rt = []
        _key_response_trial_allKeys = []
        # setup some python lists for storing info about the mouse_response_trial
        mouse_response_trial.x = []
        mouse_response_trial.y = []
        mouse_response_trial.leftButton = []
        mouse_response_trial.midButton = []
        mouse_response_trial.rightButton = []
        mouse_response_trial.time = []
        mouse_response_trial.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_handle_trial
        # Sets the ID Variable
        identificator = Bloco+Lamina_ID
        # Mapeia a posição numérica (lida do CSV) para o nome do componente visual
        correct_pos = str(Target_Correto_Posicao) 
        # Cria o nome do componente de imagem que é a resposta correta
        correct_response_name = 'stim_image_' + correct_pos
        
        # Inicializa variáveis para este trial
        is_correct = 0
        rt_value = None
        
        targetID_Teste.setText(identificator)
        # store start times for trialFaceRecognition
        trialFaceRecognition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialFaceRecognition.tStart = globalClock.getTime(format='float')
        trialFaceRecognition.status = STARTED
        trialFaceRecognition.maxDuration = None
        # keep track of which components have finished
        trialFaceRecognitionComponents = trialFaceRecognition.components
        for thisComponent in trialFaceRecognition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFaceRecognition" ---
        thisExp.currentRoutine = trialFaceRecognition
        trialFaceRecognition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock1Trial, 'status') and thisBlock1Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_trial* updates
            
            # if video_trial is starting this frame...
            if video_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_trial.frameNStart = frameN  # exact frame index
                video_trial.tStart = t  # local t and not account for scr refresh
                video_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_trial.status = STARTED
                video_trial.setAutoDraw(True)
            
            # if video_trial is active this frame...
            if video_trial.status == STARTED:
                # update params
                video_trial.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *text_1* updates
            
            # if text_1 is starting this frame...
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_1.status = STARTED
                text_1.setAutoDraw(True)
            
            # if text_1 is active this frame...
            if text_1.status == STARTED:
                # update params
                pass
            
            # *stim_image_1* updates
            
            # if stim_image_1 is starting this frame...
            if stim_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_1.frameNStart = frameN  # exact frame index
                stim_image_1.tStart = t  # local t and not account for scr refresh
                stim_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_1.status = STARTED
                stim_image_1.setAutoDraw(True)
            
            # if stim_image_1 is active this frame...
            if stim_image_1.status == STARTED:
                # update params
                pass
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *stim_image_2* updates
            
            # if stim_image_2 is starting this frame...
            if stim_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_2.frameNStart = frameN  # exact frame index
                stim_image_2.tStart = t  # local t and not account for scr refresh
                stim_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_2.status = STARTED
                stim_image_2.setAutoDraw(True)
            
            # if stim_image_2 is active this frame...
            if stim_image_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stim_image_3* updates
            
            # if stim_image_3 is starting this frame...
            if stim_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_3.frameNStart = frameN  # exact frame index
                stim_image_3.tStart = t  # local t and not account for scr refresh
                stim_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_3.status = STARTED
                stim_image_3.setAutoDraw(True)
            
            # if stim_image_3 is active this frame...
            if stim_image_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *stim_image_4* updates
            
            # if stim_image_4 is starting this frame...
            if stim_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_4.frameNStart = frameN  # exact frame index
                stim_image_4.tStart = t  # local t and not account for scr refresh
                stim_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_4.status = STARTED
                stim_image_4.setAutoDraw(True)
            
            # if stim_image_4 is active this frame...
            if stim_image_4.status == STARTED:
                # update params
                pass
            
            # *key_response_trial* updates
            
            # if key_response_trial is starting this frame...
            if key_response_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_trial.frameNStart = frameN  # exact frame index
                key_response_trial.tStart = t  # local t and not account for scr refresh
                key_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_trial.status = STARTED
                # keyboard checking is just starting
                key_response_trial.clock.reset()  # now t=0
            if key_response_trial.status == STARTED:
                theseKeys = key_response_trial.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_trial_allKeys.extend(theseKeys)
                if len(_key_response_trial_allKeys):
                    key_response_trial.keys = _key_response_trial_allKeys[-1].name  # just the last key pressed
                    key_response_trial.rt = _key_response_trial_allKeys[-1].rt
                    key_response_trial.duration = _key_response_trial_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_trial* updates
            
            # if mouse_response_trial is starting this frame...
            if mouse_response_trial.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                mouse_response_trial.frameNStart = frameN  # exact frame index
                mouse_response_trial.tStart = t  # local t and not account for scr refresh
                mouse_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_trial.status = STARTED
                mouse_response_trial.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_trial.prevButtonState = mouse_response_trial.getPressed()
            if mouse_response_trial.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_trial.getPressed()
                # button state changed?
                if buttons != mouse_response_trial.prevButtonState:
                    mouse_response_trial.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([stim_image_1,stim_image_2,stim_image_3,stim_image_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_trial):
                                gotValidClick = True
                                mouse_response_trial.clicked_name.append(obj.name)
                                mouse_response_trial.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_response_trial.getPos()
                            mouse_response_trial.x.append(float(x))
                            mouse_response_trial.y.append(float(y))
                            buttons = mouse_response_trial.getPressed()
                            mouse_response_trial.leftButton.append(buttons[0])
                            mouse_response_trial.midButton.append(buttons[1])
                            mouse_response_trial.rightButton.append(buttons[2])
                            mouse_response_trial.time.append(mouse_response_trial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *targetID_Teste* updates
            
            # if targetID_Teste is starting this frame...
            if targetID_Teste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                targetID_Teste.frameNStart = frameN  # exact frame index
                targetID_Teste.tStart = t  # local t and not account for scr refresh
                targetID_Teste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetID_Teste, 'tStartRefresh')  # time at next scr refresh
                # update status
                targetID_Teste.status = STARTED
                targetID_Teste.setAutoDraw(True)
            
            # if targetID_Teste is active this frame...
            if targetID_Teste.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialFaceRecognition,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trialFaceRecognition.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trialFaceRecognition.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trialFaceRecognition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFaceRecognition" ---
        for thisComponent in trialFaceRecognition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialFaceRecognition
        trialFaceRecognition.tStop = globalClock.getTime(format='float')
        trialFaceRecognition.tStopRefresh = tThisFlipGlobal
        # store data for block1Trials (TrialHandler)
        block1Trials.addData('mouse_response_trial.x', mouse_response_trial.x)
        block1Trials.addData('mouse_response_trial.y', mouse_response_trial.y)
        block1Trials.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton)
        block1Trials.addData('mouse_response_trial.midButton', mouse_response_trial.midButton)
        block1Trials.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton)
        block1Trials.addData('mouse_response_trial.time', mouse_response_trial.time)
        block1Trials.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name)
        # Run 'End Routine' code from code_handle_trial
        # Inicializar as variáveis de análise (default: miss/sem resposta)
        response_method = 'miss'
        selected_option = None
        
        #  Arbitragem de Resposta:
        
        # Checa se houve resposta pelo Teclado
        if len(key_response_trial.keys) > 0:
            
            response_method = 'keyboard'
            rt_value = key_response_trial.rt
            
            # Pega o primeiro dígito pressionado
            pressed_key = key_response_trial.keys[0] 
            
            # Checa o acerto
            if str(pressed_key) == str(Target_Correto_Posicao):
                is_correct = 1
            
            selected_option = f"stim_image_{pressed_key}"
        
        # Se não, checa se houve resposta pelo Mouse
        elif mouse_response_trial.clicked_name:
            
            response_method = 'mouse'
            
            # O tempo do mouse está na lista de tempos registrada pelo componente
            if mouse_response_trial.time is not None and len(mouse_response_trial.time) > 0:
                rt_value = mouse_response_trial.time[0]
            
            # O nome do componente clicado está na lista
            selected_option = mouse_response_trial.clicked_name[0] 
            
            # Checa o acerto
            if selected_option == correct_response_name:
                is_correct = 1
        
        # SALVAR APENAS AS COLUNAS ESSENCIAIS NO ARQUIVO FINAL
        thisExp.addData('ANALYSIS_Lamina_ID', (identificator))
        thisExp.addData('ANALYSIS_CR', is_correct)
        thisExp.addData('ANALYSIS_RT', (round(rt_value,3)))
        thisExp.addData('ANALYSIS_Response_Method', response_method)
        thisExp.addData('ANALYSIS_Selected_Option', selected_option)
        thisExp.addData('ANALYSIS_Target_Component', correct_response_name)
        # the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause" ---
        # create an object to store info about Routine pause
        pause = data.Routine(
            name='pause',
            components=[],
        )
        pause.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause
        pause.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause.tStart = globalClock.getTime(format='float')
        pause.status = STARTED
        pause.maxDuration = 1
        # skip Routine pause if its 'Skip if' condition is True
        pause.skipped = continueRoutine and not (block1Trials.thisTrialN == (block1Trials.nTotal - 1))
        continueRoutine = pause.skipped
        # keep track of which components have finished
        pauseComponents = pause.components
        for thisComponent in pause.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        thisExp.currentRoutine = pause
        pause.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlock1Trial, 'status') and thisBlock1Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > pause.maxDuration-frameTolerance:
                pause.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pause.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pause.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pause.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pause.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause
        pause.tStop = globalClock.getTime(format='float')
        pause.tStopRefresh = tThisFlipGlobal
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause.maxDurationReached:
            routineTimer.addTime(-pause.maxDuration)
        elif pause.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisBlock1Trial as finished
        if hasattr(thisBlock1Trial, 'status'):
            thisBlock1Trial.status = FINISHED
        # if awaiting a pause, pause now
        if block1Trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            block1Trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block1Trials'
    block1Trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blockIntro" ---
    # create an object to store info about Routine blockIntro
    blockIntro = data.Routine(
        name='blockIntro',
        components=[txt_block_title, text_response, key_resp, mouse_resp],
    )
    blockIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_num
    block_number +=1
    
    block_title = f"BLOCO {block_number}"
    txt_block_title.setText(block_title)
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    gotValidClick = False  # until a click is received
    # store start times for blockIntro
    blockIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blockIntro.tStart = globalClock.getTime(format='float')
    blockIntro.status = STARTED
    blockIntro.maxDuration = None
    # keep track of which components have finished
    blockIntroComponents = blockIntro.components
    for thisComponent in blockIntro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockIntro" ---
    thisExp.currentRoutine = blockIntro
    blockIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_block_title* updates
        
        # if txt_block_title is starting this frame...
        if txt_block_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_block_title.frameNStart = frameN  # exact frame index
            txt_block_title.tStart = t  # local t and not account for scr refresh
            txt_block_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_block_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            txt_block_title.status = STARTED
            txt_block_title.setAutoDraw(True)
        
        # if txt_block_title is active this frame...
        if txt_block_title.status == STARTED:
            # update params
            pass
        
        # *text_response* updates
        
        # if text_response is starting this frame...
        if text_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_response.frameNStart = frameN  # exact frame index
            text_response.tStart = t  # local t and not account for scr refresh
            text_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_response.status = STARTED
            text_response.setAutoDraw(True)
        
        # if text_response is active this frame...
        if text_response.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        
        # if mouse_resp is starting this frame...
        if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_resp.prevButtonState = mouse_resp.getPressed()
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            # button state changed?
            if buttons != mouse_resp.prevButtonState:
                mouse_resp.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blockIntro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blockIntro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blockIntro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blockIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockIntro" ---
    for thisComponent in blockIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blockIntro
    blockIntro.tStop = globalClock.getTime(format='float')
    blockIntro.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block2Trials = data.TrialHandler2(
        name='block2Trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-B2.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(block2Trials)  # add the loop to the experiment
    thisBlock2Trial = block2Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2Trial.rgb)
    if thisBlock2Trial != None:
        for paramName in thisBlock2Trial:
            globals()[paramName] = thisBlock2Trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlock2Trial in block2Trials:
        block2Trials.status = STARTED
        if hasattr(thisBlock2Trial, 'status'):
            thisBlock2Trial.status = STARTED
        currentLoop = block2Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlock2Trial.rgb)
        if thisBlock2Trial != None:
            for paramName in thisBlock2Trial:
                globals()[paramName] = thisBlock2Trial[paramName]
        
        # --- Prepare to start Routine "trialFaceRecognition" ---
        # create an object to store info about Routine trialFaceRecognition
        trialFaceRecognition = data.Routine(
            name='trialFaceRecognition',
            components=[video_trial, text_1, stim_image_1, text_2, stim_image_2, text_3, stim_image_3, text_4, stim_image_4, key_response_trial, mouse_response_trial, targetID_Teste],
        )
        trialFaceRecognition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        stim_image_1.setImage(Image_1)
        stim_image_2.setImage(Image_2)
        stim_image_3.setImage(Image_3)
        stim_image_4.setImage(Image_4)
        # create starting attributes for key_response_trial
        key_response_trial.keys = []
        key_response_trial.rt = []
        _key_response_trial_allKeys = []
        # setup some python lists for storing info about the mouse_response_trial
        mouse_response_trial.x = []
        mouse_response_trial.y = []
        mouse_response_trial.leftButton = []
        mouse_response_trial.midButton = []
        mouse_response_trial.rightButton = []
        mouse_response_trial.time = []
        mouse_response_trial.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_handle_trial
        # Sets the ID Variable
        identificator = Bloco+Lamina_ID
        # Mapeia a posição numérica (lida do CSV) para o nome do componente visual
        correct_pos = str(Target_Correto_Posicao) 
        # Cria o nome do componente de imagem que é a resposta correta
        correct_response_name = 'stim_image_' + correct_pos
        
        # Inicializa variáveis para este trial
        is_correct = 0
        rt_value = None
        
        targetID_Teste.setText(identificator)
        # store start times for trialFaceRecognition
        trialFaceRecognition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialFaceRecognition.tStart = globalClock.getTime(format='float')
        trialFaceRecognition.status = STARTED
        trialFaceRecognition.maxDuration = None
        # keep track of which components have finished
        trialFaceRecognitionComponents = trialFaceRecognition.components
        for thisComponent in trialFaceRecognition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFaceRecognition" ---
        thisExp.currentRoutine = trialFaceRecognition
        trialFaceRecognition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock2Trial, 'status') and thisBlock2Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_trial* updates
            
            # if video_trial is starting this frame...
            if video_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_trial.frameNStart = frameN  # exact frame index
                video_trial.tStart = t  # local t and not account for scr refresh
                video_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_trial.status = STARTED
                video_trial.setAutoDraw(True)
            
            # if video_trial is active this frame...
            if video_trial.status == STARTED:
                # update params
                video_trial.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *text_1* updates
            
            # if text_1 is starting this frame...
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_1.status = STARTED
                text_1.setAutoDraw(True)
            
            # if text_1 is active this frame...
            if text_1.status == STARTED:
                # update params
                pass
            
            # *stim_image_1* updates
            
            # if stim_image_1 is starting this frame...
            if stim_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_1.frameNStart = frameN  # exact frame index
                stim_image_1.tStart = t  # local t and not account for scr refresh
                stim_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_1.status = STARTED
                stim_image_1.setAutoDraw(True)
            
            # if stim_image_1 is active this frame...
            if stim_image_1.status == STARTED:
                # update params
                pass
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *stim_image_2* updates
            
            # if stim_image_2 is starting this frame...
            if stim_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_2.frameNStart = frameN  # exact frame index
                stim_image_2.tStart = t  # local t and not account for scr refresh
                stim_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_2.status = STARTED
                stim_image_2.setAutoDraw(True)
            
            # if stim_image_2 is active this frame...
            if stim_image_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stim_image_3* updates
            
            # if stim_image_3 is starting this frame...
            if stim_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_3.frameNStart = frameN  # exact frame index
                stim_image_3.tStart = t  # local t and not account for scr refresh
                stim_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_3.status = STARTED
                stim_image_3.setAutoDraw(True)
            
            # if stim_image_3 is active this frame...
            if stim_image_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *stim_image_4* updates
            
            # if stim_image_4 is starting this frame...
            if stim_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_4.frameNStart = frameN  # exact frame index
                stim_image_4.tStart = t  # local t and not account for scr refresh
                stim_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_4.status = STARTED
                stim_image_4.setAutoDraw(True)
            
            # if stim_image_4 is active this frame...
            if stim_image_4.status == STARTED:
                # update params
                pass
            
            # *key_response_trial* updates
            
            # if key_response_trial is starting this frame...
            if key_response_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_trial.frameNStart = frameN  # exact frame index
                key_response_trial.tStart = t  # local t and not account for scr refresh
                key_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_trial.status = STARTED
                # keyboard checking is just starting
                key_response_trial.clock.reset()  # now t=0
            if key_response_trial.status == STARTED:
                theseKeys = key_response_trial.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_trial_allKeys.extend(theseKeys)
                if len(_key_response_trial_allKeys):
                    key_response_trial.keys = _key_response_trial_allKeys[-1].name  # just the last key pressed
                    key_response_trial.rt = _key_response_trial_allKeys[-1].rt
                    key_response_trial.duration = _key_response_trial_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_trial* updates
            
            # if mouse_response_trial is starting this frame...
            if mouse_response_trial.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                mouse_response_trial.frameNStart = frameN  # exact frame index
                mouse_response_trial.tStart = t  # local t and not account for scr refresh
                mouse_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_trial.status = STARTED
                mouse_response_trial.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_trial.prevButtonState = mouse_response_trial.getPressed()
            if mouse_response_trial.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_trial.getPressed()
                # button state changed?
                if buttons != mouse_response_trial.prevButtonState:
                    mouse_response_trial.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([stim_image_1,stim_image_2,stim_image_3,stim_image_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_trial):
                                gotValidClick = True
                                mouse_response_trial.clicked_name.append(obj.name)
                                mouse_response_trial.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_response_trial.getPos()
                            mouse_response_trial.x.append(float(x))
                            mouse_response_trial.y.append(float(y))
                            buttons = mouse_response_trial.getPressed()
                            mouse_response_trial.leftButton.append(buttons[0])
                            mouse_response_trial.midButton.append(buttons[1])
                            mouse_response_trial.rightButton.append(buttons[2])
                            mouse_response_trial.time.append(mouse_response_trial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *targetID_Teste* updates
            
            # if targetID_Teste is starting this frame...
            if targetID_Teste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                targetID_Teste.frameNStart = frameN  # exact frame index
                targetID_Teste.tStart = t  # local t and not account for scr refresh
                targetID_Teste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetID_Teste, 'tStartRefresh')  # time at next scr refresh
                # update status
                targetID_Teste.status = STARTED
                targetID_Teste.setAutoDraw(True)
            
            # if targetID_Teste is active this frame...
            if targetID_Teste.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialFaceRecognition,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trialFaceRecognition.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trialFaceRecognition.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trialFaceRecognition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFaceRecognition" ---
        for thisComponent in trialFaceRecognition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialFaceRecognition
        trialFaceRecognition.tStop = globalClock.getTime(format='float')
        trialFaceRecognition.tStopRefresh = tThisFlipGlobal
        # store data for block2Trials (TrialHandler)
        block2Trials.addData('mouse_response_trial.x', mouse_response_trial.x)
        block2Trials.addData('mouse_response_trial.y', mouse_response_trial.y)
        block2Trials.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton)
        block2Trials.addData('mouse_response_trial.midButton', mouse_response_trial.midButton)
        block2Trials.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton)
        block2Trials.addData('mouse_response_trial.time', mouse_response_trial.time)
        block2Trials.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name)
        # Run 'End Routine' code from code_handle_trial
        # Inicializar as variáveis de análise (default: miss/sem resposta)
        response_method = 'miss'
        selected_option = None
        
        #  Arbitragem de Resposta:
        
        # Checa se houve resposta pelo Teclado
        if len(key_response_trial.keys) > 0:
            
            response_method = 'keyboard'
            rt_value = key_response_trial.rt
            
            # Pega o primeiro dígito pressionado
            pressed_key = key_response_trial.keys[0] 
            
            # Checa o acerto
            if str(pressed_key) == str(Target_Correto_Posicao):
                is_correct = 1
            
            selected_option = f"stim_image_{pressed_key}"
        
        # Se não, checa se houve resposta pelo Mouse
        elif mouse_response_trial.clicked_name:
            
            response_method = 'mouse'
            
            # O tempo do mouse está na lista de tempos registrada pelo componente
            if mouse_response_trial.time is not None and len(mouse_response_trial.time) > 0:
                rt_value = mouse_response_trial.time[0]
            
            # O nome do componente clicado está na lista
            selected_option = mouse_response_trial.clicked_name[0] 
            
            # Checa o acerto
            if selected_option == correct_response_name:
                is_correct = 1
        
        # SALVAR APENAS AS COLUNAS ESSENCIAIS NO ARQUIVO FINAL
        thisExp.addData('ANALYSIS_Lamina_ID', (identificator))
        thisExp.addData('ANALYSIS_CR', is_correct)
        thisExp.addData('ANALYSIS_RT', (round(rt_value,3)))
        thisExp.addData('ANALYSIS_Response_Method', response_method)
        thisExp.addData('ANALYSIS_Selected_Option', selected_option)
        thisExp.addData('ANALYSIS_Target_Component', correct_response_name)
        # the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause_2" ---
        # create an object to store info about Routine pause_2
        pause_2 = data.Routine(
            name='pause_2',
            components=[],
        )
        pause_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause_2
        pause_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause_2.tStart = globalClock.getTime(format='float')
        pause_2.status = STARTED
        thisExp.addData('pause_2.started', pause_2.tStart)
        pause_2.maxDuration = 1
        # skip Routine pause_2 if its 'Skip if' condition is True
        pause_2.skipped = continueRoutine and not (block2Trials.thisTrialN == (block2Trials.nTotal - 1))
        continueRoutine = pause_2.skipped
        # keep track of which components have finished
        pause_2Components = pause_2.components
        for thisComponent in pause_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause_2" ---
        thisExp.currentRoutine = pause_2
        pause_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlock2Trial, 'status') and thisBlock2Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > pause_2.maxDuration-frameTolerance:
                pause_2.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause_2,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pause_2.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pause_2.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pause_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_2" ---
        for thisComponent in pause_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause_2
        pause_2.tStop = globalClock.getTime(format='float')
        pause_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause_2.stopped', pause_2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause_2.maxDurationReached:
            routineTimer.addTime(-pause_2.maxDuration)
        elif pause_2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisBlock2Trial as finished
        if hasattr(thisBlock2Trial, 'status'):
            thisBlock2Trial.status = FINISHED
        # if awaiting a pause, pause now
        if block2Trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            block2Trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block2Trials'
    block2Trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blockIntro" ---
    # create an object to store info about Routine blockIntro
    blockIntro = data.Routine(
        name='blockIntro',
        components=[txt_block_title, text_response, key_resp, mouse_resp],
    )
    blockIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_num
    block_number +=1
    
    block_title = f"BLOCO {block_number}"
    txt_block_title.setText(block_title)
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    gotValidClick = False  # until a click is received
    # store start times for blockIntro
    blockIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blockIntro.tStart = globalClock.getTime(format='float')
    blockIntro.status = STARTED
    blockIntro.maxDuration = None
    # keep track of which components have finished
    blockIntroComponents = blockIntro.components
    for thisComponent in blockIntro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockIntro" ---
    thisExp.currentRoutine = blockIntro
    blockIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_block_title* updates
        
        # if txt_block_title is starting this frame...
        if txt_block_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_block_title.frameNStart = frameN  # exact frame index
            txt_block_title.tStart = t  # local t and not account for scr refresh
            txt_block_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_block_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            txt_block_title.status = STARTED
            txt_block_title.setAutoDraw(True)
        
        # if txt_block_title is active this frame...
        if txt_block_title.status == STARTED:
            # update params
            pass
        
        # *text_response* updates
        
        # if text_response is starting this frame...
        if text_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_response.frameNStart = frameN  # exact frame index
            text_response.tStart = t  # local t and not account for scr refresh
            text_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_response.status = STARTED
            text_response.setAutoDraw(True)
        
        # if text_response is active this frame...
        if text_response.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        
        # if mouse_resp is starting this frame...
        if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_resp.prevButtonState = mouse_resp.getPressed()
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            # button state changed?
            if buttons != mouse_resp.prevButtonState:
                mouse_resp.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blockIntro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blockIntro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blockIntro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blockIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockIntro" ---
    for thisComponent in blockIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blockIntro
    blockIntro.tStop = globalClock.getTime(format='float')
    blockIntro.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block3Trials = data.TrialHandler2(
        name='block3Trials',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-B3.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(block3Trials)  # add the loop to the experiment
    thisBlock3Trial = block3Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3Trial.rgb)
    if thisBlock3Trial != None:
        for paramName in thisBlock3Trial:
            globals()[paramName] = thisBlock3Trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlock3Trial in block3Trials:
        block3Trials.status = STARTED
        if hasattr(thisBlock3Trial, 'status'):
            thisBlock3Trial.status = STARTED
        currentLoop = block3Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlock3Trial.rgb)
        if thisBlock3Trial != None:
            for paramName in thisBlock3Trial:
                globals()[paramName] = thisBlock3Trial[paramName]
        
        # --- Prepare to start Routine "trialFaceRecognition" ---
        # create an object to store info about Routine trialFaceRecognition
        trialFaceRecognition = data.Routine(
            name='trialFaceRecognition',
            components=[video_trial, text_1, stim_image_1, text_2, stim_image_2, text_3, stim_image_3, text_4, stim_image_4, key_response_trial, mouse_response_trial, targetID_Teste],
        )
        trialFaceRecognition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        stim_image_1.setImage(Image_1)
        stim_image_2.setImage(Image_2)
        stim_image_3.setImage(Image_3)
        stim_image_4.setImage(Image_4)
        # create starting attributes for key_response_trial
        key_response_trial.keys = []
        key_response_trial.rt = []
        _key_response_trial_allKeys = []
        # setup some python lists for storing info about the mouse_response_trial
        mouse_response_trial.x = []
        mouse_response_trial.y = []
        mouse_response_trial.leftButton = []
        mouse_response_trial.midButton = []
        mouse_response_trial.rightButton = []
        mouse_response_trial.time = []
        mouse_response_trial.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_handle_trial
        # Sets the ID Variable
        identificator = Bloco+Lamina_ID
        # Mapeia a posição numérica (lida do CSV) para o nome do componente visual
        correct_pos = str(Target_Correto_Posicao) 
        # Cria o nome do componente de imagem que é a resposta correta
        correct_response_name = 'stim_image_' + correct_pos
        
        # Inicializa variáveis para este trial
        is_correct = 0
        rt_value = None
        
        targetID_Teste.setText(identificator)
        # store start times for trialFaceRecognition
        trialFaceRecognition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialFaceRecognition.tStart = globalClock.getTime(format='float')
        trialFaceRecognition.status = STARTED
        trialFaceRecognition.maxDuration = None
        # keep track of which components have finished
        trialFaceRecognitionComponents = trialFaceRecognition.components
        for thisComponent in trialFaceRecognition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFaceRecognition" ---
        thisExp.currentRoutine = trialFaceRecognition
        trialFaceRecognition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock3Trial, 'status') and thisBlock3Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_trial* updates
            
            # if video_trial is starting this frame...
            if video_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_trial.frameNStart = frameN  # exact frame index
                video_trial.tStart = t  # local t and not account for scr refresh
                video_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_trial.status = STARTED
                video_trial.setAutoDraw(True)
            
            # if video_trial is active this frame...
            if video_trial.status == STARTED:
                # update params
                video_trial.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *text_1* updates
            
            # if text_1 is starting this frame...
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_1.status = STARTED
                text_1.setAutoDraw(True)
            
            # if text_1 is active this frame...
            if text_1.status == STARTED:
                # update params
                pass
            
            # *stim_image_1* updates
            
            # if stim_image_1 is starting this frame...
            if stim_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_1.frameNStart = frameN  # exact frame index
                stim_image_1.tStart = t  # local t and not account for scr refresh
                stim_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_1.status = STARTED
                stim_image_1.setAutoDraw(True)
            
            # if stim_image_1 is active this frame...
            if stim_image_1.status == STARTED:
                # update params
                pass
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *stim_image_2* updates
            
            # if stim_image_2 is starting this frame...
            if stim_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_2.frameNStart = frameN  # exact frame index
                stim_image_2.tStart = t  # local t and not account for scr refresh
                stim_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_2.status = STARTED
                stim_image_2.setAutoDraw(True)
            
            # if stim_image_2 is active this frame...
            if stim_image_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stim_image_3* updates
            
            # if stim_image_3 is starting this frame...
            if stim_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_3.frameNStart = frameN  # exact frame index
                stim_image_3.tStart = t  # local t and not account for scr refresh
                stim_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_3.status = STARTED
                stim_image_3.setAutoDraw(True)
            
            # if stim_image_3 is active this frame...
            if stim_image_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *stim_image_4* updates
            
            # if stim_image_4 is starting this frame...
            if stim_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_4.frameNStart = frameN  # exact frame index
                stim_image_4.tStart = t  # local t and not account for scr refresh
                stim_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_4.status = STARTED
                stim_image_4.setAutoDraw(True)
            
            # if stim_image_4 is active this frame...
            if stim_image_4.status == STARTED:
                # update params
                pass
            
            # *key_response_trial* updates
            
            # if key_response_trial is starting this frame...
            if key_response_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_trial.frameNStart = frameN  # exact frame index
                key_response_trial.tStart = t  # local t and not account for scr refresh
                key_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_trial.status = STARTED
                # keyboard checking is just starting
                key_response_trial.clock.reset()  # now t=0
            if key_response_trial.status == STARTED:
                theseKeys = key_response_trial.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_trial_allKeys.extend(theseKeys)
                if len(_key_response_trial_allKeys):
                    key_response_trial.keys = _key_response_trial_allKeys[-1].name  # just the last key pressed
                    key_response_trial.rt = _key_response_trial_allKeys[-1].rt
                    key_response_trial.duration = _key_response_trial_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_trial* updates
            
            # if mouse_response_trial is starting this frame...
            if mouse_response_trial.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                mouse_response_trial.frameNStart = frameN  # exact frame index
                mouse_response_trial.tStart = t  # local t and not account for scr refresh
                mouse_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_trial.status = STARTED
                mouse_response_trial.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_trial.prevButtonState = mouse_response_trial.getPressed()
            if mouse_response_trial.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_trial.getPressed()
                # button state changed?
                if buttons != mouse_response_trial.prevButtonState:
                    mouse_response_trial.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([stim_image_1,stim_image_2,stim_image_3,stim_image_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_trial):
                                gotValidClick = True
                                mouse_response_trial.clicked_name.append(obj.name)
                                mouse_response_trial.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_response_trial.getPos()
                            mouse_response_trial.x.append(float(x))
                            mouse_response_trial.y.append(float(y))
                            buttons = mouse_response_trial.getPressed()
                            mouse_response_trial.leftButton.append(buttons[0])
                            mouse_response_trial.midButton.append(buttons[1])
                            mouse_response_trial.rightButton.append(buttons[2])
                            mouse_response_trial.time.append(mouse_response_trial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *targetID_Teste* updates
            
            # if targetID_Teste is starting this frame...
            if targetID_Teste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                targetID_Teste.frameNStart = frameN  # exact frame index
                targetID_Teste.tStart = t  # local t and not account for scr refresh
                targetID_Teste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetID_Teste, 'tStartRefresh')  # time at next scr refresh
                # update status
                targetID_Teste.status = STARTED
                targetID_Teste.setAutoDraw(True)
            
            # if targetID_Teste is active this frame...
            if targetID_Teste.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialFaceRecognition,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trialFaceRecognition.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trialFaceRecognition.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trialFaceRecognition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFaceRecognition" ---
        for thisComponent in trialFaceRecognition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialFaceRecognition
        trialFaceRecognition.tStop = globalClock.getTime(format='float')
        trialFaceRecognition.tStopRefresh = tThisFlipGlobal
        # store data for block3Trials (TrialHandler)
        block3Trials.addData('mouse_response_trial.x', mouse_response_trial.x)
        block3Trials.addData('mouse_response_trial.y', mouse_response_trial.y)
        block3Trials.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton)
        block3Trials.addData('mouse_response_trial.midButton', mouse_response_trial.midButton)
        block3Trials.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton)
        block3Trials.addData('mouse_response_trial.time', mouse_response_trial.time)
        block3Trials.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name)
        # Run 'End Routine' code from code_handle_trial
        # Inicializar as variáveis de análise (default: miss/sem resposta)
        response_method = 'miss'
        selected_option = None
        
        #  Arbitragem de Resposta:
        
        # Checa se houve resposta pelo Teclado
        if len(key_response_trial.keys) > 0:
            
            response_method = 'keyboard'
            rt_value = key_response_trial.rt
            
            # Pega o primeiro dígito pressionado
            pressed_key = key_response_trial.keys[0] 
            
            # Checa o acerto
            if str(pressed_key) == str(Target_Correto_Posicao):
                is_correct = 1
            
            selected_option = f"stim_image_{pressed_key}"
        
        # Se não, checa se houve resposta pelo Mouse
        elif mouse_response_trial.clicked_name:
            
            response_method = 'mouse'
            
            # O tempo do mouse está na lista de tempos registrada pelo componente
            if mouse_response_trial.time is not None and len(mouse_response_trial.time) > 0:
                rt_value = mouse_response_trial.time[0]
            
            # O nome do componente clicado está na lista
            selected_option = mouse_response_trial.clicked_name[0] 
            
            # Checa o acerto
            if selected_option == correct_response_name:
                is_correct = 1
        
        # SALVAR APENAS AS COLUNAS ESSENCIAIS NO ARQUIVO FINAL
        thisExp.addData('ANALYSIS_Lamina_ID', (identificator))
        thisExp.addData('ANALYSIS_CR', is_correct)
        thisExp.addData('ANALYSIS_RT', (round(rt_value,3)))
        thisExp.addData('ANALYSIS_Response_Method', response_method)
        thisExp.addData('ANALYSIS_Selected_Option', selected_option)
        thisExp.addData('ANALYSIS_Target_Component', correct_response_name)
        # the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause_3" ---
        # create an object to store info about Routine pause_3
        pause_3 = data.Routine(
            name='pause_3',
            components=[],
        )
        pause_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause_3
        pause_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause_3.tStart = globalClock.getTime(format='float')
        pause_3.status = STARTED
        thisExp.addData('pause_3.started', pause_3.tStart)
        pause_3.maxDuration = 1
        # skip Routine pause_3 if its 'Skip if' condition is True
        pause_3.skipped = continueRoutine and not (block3Trials.thisTrialN == (block3Trials.nTotal - 1))
        continueRoutine = pause_3.skipped
        # keep track of which components have finished
        pause_3Components = pause_3.components
        for thisComponent in pause_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause_3" ---
        thisExp.currentRoutine = pause_3
        pause_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlock3Trial, 'status') and thisBlock3Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > pause_3.maxDuration-frameTolerance:
                pause_3.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause_3,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pause_3.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pause_3.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pause_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_3" ---
        for thisComponent in pause_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause_3
        pause_3.tStop = globalClock.getTime(format='float')
        pause_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause_3.stopped', pause_3.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause_3.maxDurationReached:
            routineTimer.addTime(-pause_3.maxDuration)
        elif pause_3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisBlock3Trial as finished
        if hasattr(thisBlock3Trial, 'status'):
            thisBlock3Trial.status = FINISHED
        # if awaiting a pause, pause now
        if block3Trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            block3Trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'block3Trials'
    block3Trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blockIntro" ---
    # create an object to store info about Routine blockIntro
    blockIntro = data.Routine(
        name='blockIntro',
        components=[txt_block_title, text_response, key_resp, mouse_resp],
    )
    blockIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_num
    block_number +=1
    
    block_title = f"BLOCO {block_number}"
    txt_block_title.setText(block_title)
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    gotValidClick = False  # until a click is received
    # store start times for blockIntro
    blockIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blockIntro.tStart = globalClock.getTime(format='float')
    blockIntro.status = STARTED
    blockIntro.maxDuration = None
    # keep track of which components have finished
    blockIntroComponents = blockIntro.components
    for thisComponent in blockIntro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockIntro" ---
    thisExp.currentRoutine = blockIntro
    blockIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_block_title* updates
        
        # if txt_block_title is starting this frame...
        if txt_block_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_block_title.frameNStart = frameN  # exact frame index
            txt_block_title.tStart = t  # local t and not account for scr refresh
            txt_block_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_block_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            txt_block_title.status = STARTED
            txt_block_title.setAutoDraw(True)
        
        # if txt_block_title is active this frame...
        if txt_block_title.status == STARTED:
            # update params
            pass
        
        # *text_response* updates
        
        # if text_response is starting this frame...
        if text_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_response.frameNStart = frameN  # exact frame index
            text_response.tStart = t  # local t and not account for scr refresh
            text_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_response.status = STARTED
            text_response.setAutoDraw(True)
        
        # if text_response is active this frame...
        if text_response.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        
        # if mouse_resp is starting this frame...
        if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_resp.prevButtonState = mouse_resp.getPressed()
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            # button state changed?
            if buttons != mouse_resp.prevButtonState:
                mouse_resp.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blockIntro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blockIntro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blockIntro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blockIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockIntro" ---
    for thisComponent in blockIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blockIntro
    blockIntro.tStop = globalClock.getTime(format='float')
    blockIntro.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block4Trials = data.TrialHandler2(
        name='block4Trials',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-B4.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(block4Trials)  # add the loop to the experiment
    thisBlock4Trial = block4Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4Trial.rgb)
    if thisBlock4Trial != None:
        for paramName in thisBlock4Trial:
            globals()[paramName] = thisBlock4Trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlock4Trial in block4Trials:
        block4Trials.status = STARTED
        if hasattr(thisBlock4Trial, 'status'):
            thisBlock4Trial.status = STARTED
        currentLoop = block4Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlock4Trial.rgb)
        if thisBlock4Trial != None:
            for paramName in thisBlock4Trial:
                globals()[paramName] = thisBlock4Trial[paramName]
        
        # --- Prepare to start Routine "trialFaceRecognition" ---
        # create an object to store info about Routine trialFaceRecognition
        trialFaceRecognition = data.Routine(
            name='trialFaceRecognition',
            components=[video_trial, text_1, stim_image_1, text_2, stim_image_2, text_3, stim_image_3, text_4, stim_image_4, key_response_trial, mouse_response_trial, targetID_Teste],
        )
        trialFaceRecognition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        stim_image_1.setImage(Image_1)
        stim_image_2.setImage(Image_2)
        stim_image_3.setImage(Image_3)
        stim_image_4.setImage(Image_4)
        # create starting attributes for key_response_trial
        key_response_trial.keys = []
        key_response_trial.rt = []
        _key_response_trial_allKeys = []
        # setup some python lists for storing info about the mouse_response_trial
        mouse_response_trial.x = []
        mouse_response_trial.y = []
        mouse_response_trial.leftButton = []
        mouse_response_trial.midButton = []
        mouse_response_trial.rightButton = []
        mouse_response_trial.time = []
        mouse_response_trial.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_handle_trial
        # Sets the ID Variable
        identificator = Bloco+Lamina_ID
        # Mapeia a posição numérica (lida do CSV) para o nome do componente visual
        correct_pos = str(Target_Correto_Posicao) 
        # Cria o nome do componente de imagem que é a resposta correta
        correct_response_name = 'stim_image_' + correct_pos
        
        # Inicializa variáveis para este trial
        is_correct = 0
        rt_value = None
        
        targetID_Teste.setText(identificator)
        # store start times for trialFaceRecognition
        trialFaceRecognition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialFaceRecognition.tStart = globalClock.getTime(format='float')
        trialFaceRecognition.status = STARTED
        trialFaceRecognition.maxDuration = None
        # keep track of which components have finished
        trialFaceRecognitionComponents = trialFaceRecognition.components
        for thisComponent in trialFaceRecognition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFaceRecognition" ---
        thisExp.currentRoutine = trialFaceRecognition
        trialFaceRecognition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock4Trial, 'status') and thisBlock4Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_trial* updates
            
            # if video_trial is starting this frame...
            if video_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_trial.frameNStart = frameN  # exact frame index
                video_trial.tStart = t  # local t and not account for scr refresh
                video_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_trial.status = STARTED
                video_trial.setAutoDraw(True)
            
            # if video_trial is active this frame...
            if video_trial.status == STARTED:
                # update params
                video_trial.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *text_1* updates
            
            # if text_1 is starting this frame...
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_1.status = STARTED
                text_1.setAutoDraw(True)
            
            # if text_1 is active this frame...
            if text_1.status == STARTED:
                # update params
                pass
            
            # *stim_image_1* updates
            
            # if stim_image_1 is starting this frame...
            if stim_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_1.frameNStart = frameN  # exact frame index
                stim_image_1.tStart = t  # local t and not account for scr refresh
                stim_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_1.status = STARTED
                stim_image_1.setAutoDraw(True)
            
            # if stim_image_1 is active this frame...
            if stim_image_1.status == STARTED:
                # update params
                pass
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *stim_image_2* updates
            
            # if stim_image_2 is starting this frame...
            if stim_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_2.frameNStart = frameN  # exact frame index
                stim_image_2.tStart = t  # local t and not account for scr refresh
                stim_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_2.status = STARTED
                stim_image_2.setAutoDraw(True)
            
            # if stim_image_2 is active this frame...
            if stim_image_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stim_image_3* updates
            
            # if stim_image_3 is starting this frame...
            if stim_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_3.frameNStart = frameN  # exact frame index
                stim_image_3.tStart = t  # local t and not account for scr refresh
                stim_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_3.status = STARTED
                stim_image_3.setAutoDraw(True)
            
            # if stim_image_3 is active this frame...
            if stim_image_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *stim_image_4* updates
            
            # if stim_image_4 is starting this frame...
            if stim_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_4.frameNStart = frameN  # exact frame index
                stim_image_4.tStart = t  # local t and not account for scr refresh
                stim_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_4.status = STARTED
                stim_image_4.setAutoDraw(True)
            
            # if stim_image_4 is active this frame...
            if stim_image_4.status == STARTED:
                # update params
                pass
            
            # *key_response_trial* updates
            
            # if key_response_trial is starting this frame...
            if key_response_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_trial.frameNStart = frameN  # exact frame index
                key_response_trial.tStart = t  # local t and not account for scr refresh
                key_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_trial.status = STARTED
                # keyboard checking is just starting
                key_response_trial.clock.reset()  # now t=0
            if key_response_trial.status == STARTED:
                theseKeys = key_response_trial.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_trial_allKeys.extend(theseKeys)
                if len(_key_response_trial_allKeys):
                    key_response_trial.keys = _key_response_trial_allKeys[-1].name  # just the last key pressed
                    key_response_trial.rt = _key_response_trial_allKeys[-1].rt
                    key_response_trial.duration = _key_response_trial_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_trial* updates
            
            # if mouse_response_trial is starting this frame...
            if mouse_response_trial.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                mouse_response_trial.frameNStart = frameN  # exact frame index
                mouse_response_trial.tStart = t  # local t and not account for scr refresh
                mouse_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_trial.status = STARTED
                mouse_response_trial.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_trial.prevButtonState = mouse_response_trial.getPressed()
            if mouse_response_trial.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_trial.getPressed()
                # button state changed?
                if buttons != mouse_response_trial.prevButtonState:
                    mouse_response_trial.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([stim_image_1,stim_image_2,stim_image_3,stim_image_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_trial):
                                gotValidClick = True
                                mouse_response_trial.clicked_name.append(obj.name)
                                mouse_response_trial.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_response_trial.getPos()
                            mouse_response_trial.x.append(float(x))
                            mouse_response_trial.y.append(float(y))
                            buttons = mouse_response_trial.getPressed()
                            mouse_response_trial.leftButton.append(buttons[0])
                            mouse_response_trial.midButton.append(buttons[1])
                            mouse_response_trial.rightButton.append(buttons[2])
                            mouse_response_trial.time.append(mouse_response_trial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *targetID_Teste* updates
            
            # if targetID_Teste is starting this frame...
            if targetID_Teste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                targetID_Teste.frameNStart = frameN  # exact frame index
                targetID_Teste.tStart = t  # local t and not account for scr refresh
                targetID_Teste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetID_Teste, 'tStartRefresh')  # time at next scr refresh
                # update status
                targetID_Teste.status = STARTED
                targetID_Teste.setAutoDraw(True)
            
            # if targetID_Teste is active this frame...
            if targetID_Teste.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialFaceRecognition,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trialFaceRecognition.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trialFaceRecognition.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trialFaceRecognition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFaceRecognition" ---
        for thisComponent in trialFaceRecognition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialFaceRecognition
        trialFaceRecognition.tStop = globalClock.getTime(format='float')
        trialFaceRecognition.tStopRefresh = tThisFlipGlobal
        # store data for block4Trials (TrialHandler)
        block4Trials.addData('mouse_response_trial.x', mouse_response_trial.x)
        block4Trials.addData('mouse_response_trial.y', mouse_response_trial.y)
        block4Trials.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton)
        block4Trials.addData('mouse_response_trial.midButton', mouse_response_trial.midButton)
        block4Trials.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton)
        block4Trials.addData('mouse_response_trial.time', mouse_response_trial.time)
        block4Trials.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name)
        # Run 'End Routine' code from code_handle_trial
        # Inicializar as variáveis de análise (default: miss/sem resposta)
        response_method = 'miss'
        selected_option = None
        
        #  Arbitragem de Resposta:
        
        # Checa se houve resposta pelo Teclado
        if len(key_response_trial.keys) > 0:
            
            response_method = 'keyboard'
            rt_value = key_response_trial.rt
            
            # Pega o primeiro dígito pressionado
            pressed_key = key_response_trial.keys[0] 
            
            # Checa o acerto
            if str(pressed_key) == str(Target_Correto_Posicao):
                is_correct = 1
            
            selected_option = f"stim_image_{pressed_key}"
        
        # Se não, checa se houve resposta pelo Mouse
        elif mouse_response_trial.clicked_name:
            
            response_method = 'mouse'
            
            # O tempo do mouse está na lista de tempos registrada pelo componente
            if mouse_response_trial.time is not None and len(mouse_response_trial.time) > 0:
                rt_value = mouse_response_trial.time[0]
            
            # O nome do componente clicado está na lista
            selected_option = mouse_response_trial.clicked_name[0] 
            
            # Checa o acerto
            if selected_option == correct_response_name:
                is_correct = 1
        
        # SALVAR APENAS AS COLUNAS ESSENCIAIS NO ARQUIVO FINAL
        thisExp.addData('ANALYSIS_Lamina_ID', (identificator))
        thisExp.addData('ANALYSIS_CR', is_correct)
        thisExp.addData('ANALYSIS_RT', (round(rt_value,3)))
        thisExp.addData('ANALYSIS_Response_Method', response_method)
        thisExp.addData('ANALYSIS_Selected_Option', selected_option)
        thisExp.addData('ANALYSIS_Target_Component', correct_response_name)
        # the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause_4" ---
        # create an object to store info about Routine pause_4
        pause_4 = data.Routine(
            name='pause_4',
            components=[],
        )
        pause_4.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause_4
        pause_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause_4.tStart = globalClock.getTime(format='float')
        pause_4.status = STARTED
        thisExp.addData('pause_4.started', pause_4.tStart)
        pause_4.maxDuration = 1
        # skip Routine pause_4 if its 'Skip if' condition is True
        pause_4.skipped = continueRoutine and not (block4Trials.thisTrialN == (block4Trials.nTotal - 1))
        continueRoutine = pause_4.skipped
        # keep track of which components have finished
        pause_4Components = pause_4.components
        for thisComponent in pause_4.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause_4" ---
        thisExp.currentRoutine = pause_4
        pause_4.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlock4Trial, 'status') and thisBlock4Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > pause_4.maxDuration-frameTolerance:
                pause_4.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause_4,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pause_4.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pause_4.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pause_4.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_4" ---
        for thisComponent in pause_4.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause_4
        pause_4.tStop = globalClock.getTime(format='float')
        pause_4.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause_4.stopped', pause_4.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause_4.maxDurationReached:
            routineTimer.addTime(-pause_4.maxDuration)
        elif pause_4.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisBlock4Trial as finished
        if hasattr(thisBlock4Trial, 'status'):
            thisBlock4Trial.status = FINISHED
        # if awaiting a pause, pause now
        if block4Trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            block4Trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'block4Trials'
    block4Trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "blockIntro" ---
    # create an object to store info about Routine blockIntro
    blockIntro = data.Routine(
        name='blockIntro',
        components=[txt_block_title, text_response, key_resp, mouse_resp],
    )
    blockIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_num
    block_number +=1
    
    block_title = f"BLOCO {block_number}"
    txt_block_title.setText(block_title)
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse_resp
    gotValidClick = False  # until a click is received
    # store start times for blockIntro
    blockIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    blockIntro.tStart = globalClock.getTime(format='float')
    blockIntro.status = STARTED
    blockIntro.maxDuration = None
    # keep track of which components have finished
    blockIntroComponents = blockIntro.components
    for thisComponent in blockIntro.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blockIntro" ---
    thisExp.currentRoutine = blockIntro
    blockIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txt_block_title* updates
        
        # if txt_block_title is starting this frame...
        if txt_block_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txt_block_title.frameNStart = frameN  # exact frame index
            txt_block_title.tStart = t  # local t and not account for scr refresh
            txt_block_title.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txt_block_title, 'tStartRefresh')  # time at next scr refresh
            # update status
            txt_block_title.status = STARTED
            txt_block_title.setAutoDraw(True)
        
        # if txt_block_title is active this frame...
        if txt_block_title.status == STARTED:
            # update params
            pass
        
        # *text_response* updates
        
        # if text_response is starting this frame...
        if text_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_response.frameNStart = frameN  # exact frame index
            text_response.tStart = t  # local t and not account for scr refresh
            text_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_response.status = STARTED
            text_response.setAutoDraw(True)
        
        # if text_response is active this frame...
        if text_response.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse_resp* updates
        
        # if mouse_resp is starting this frame...
        if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_resp.frameNStart = frameN  # exact frame index
            mouse_resp.tStart = t  # local t and not account for scr refresh
            mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            mouse_resp.status = STARTED
            mouse_resp.mouseClock.reset()
            # if button is down already this ISN'T a new click
            mouse_resp.prevButtonState = mouse_resp.getPressed()
        if mouse_resp.status == STARTED:  # only update if started and not finished!
            buttons = mouse_resp.getPressed()
            # button state changed?
            if buttons != mouse_resp.prevButtonState:
                mouse_resp.prevButtonState = buttons
                # state changed to a new click
                if sum(buttons) > 0:
                    pass
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=blockIntro,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            blockIntro.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if blockIntro.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in blockIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blockIntro" ---
    for thisComponent in blockIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for blockIntro
    blockIntro.tStop = globalClock.getTime(format='float')
    blockIntro.tStopRefresh = tThisFlipGlobal
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    block5Trials = data.TrialHandler2(
        name='block5Trials',
        nReps=1, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('../conditions/conditions-B5.csv'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(block5Trials)  # add the loop to the experiment
    thisBlock5Trial = block5Trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5Trial.rgb)
    if thisBlock5Trial != None:
        for paramName in thisBlock5Trial:
            globals()[paramName] = thisBlock5Trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlock5Trial in block5Trials:
        block5Trials.status = STARTED
        if hasattr(thisBlock5Trial, 'status'):
            thisBlock5Trial.status = STARTED
        currentLoop = block5Trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisBlock5Trial.rgb)
        if thisBlock5Trial != None:
            for paramName in thisBlock5Trial:
                globals()[paramName] = thisBlock5Trial[paramName]
        
        # --- Prepare to start Routine "trialFaceRecognition" ---
        # create an object to store info about Routine trialFaceRecognition
        trialFaceRecognition = data.Routine(
            name='trialFaceRecognition',
            components=[video_trial, text_1, stim_image_1, text_2, stim_image_2, text_3, stim_image_3, text_4, stim_image_4, key_response_trial, mouse_response_trial, targetID_Teste],
        )
        trialFaceRecognition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_count_frames
        current_path = os.path.join('.', Target_Pasta_Frames)
        
        total_frames = len([f for f in os.listdir(current_path) if f.endswith('.png')])
        stim_image_1.setImage(Image_1)
        stim_image_2.setImage(Image_2)
        stim_image_3.setImage(Image_3)
        stim_image_4.setImage(Image_4)
        # create starting attributes for key_response_trial
        key_response_trial.keys = []
        key_response_trial.rt = []
        _key_response_trial_allKeys = []
        # setup some python lists for storing info about the mouse_response_trial
        mouse_response_trial.x = []
        mouse_response_trial.y = []
        mouse_response_trial.leftButton = []
        mouse_response_trial.midButton = []
        mouse_response_trial.rightButton = []
        mouse_response_trial.time = []
        mouse_response_trial.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_handle_trial
        # Sets the ID Variable
        identificator = Bloco+Lamina_ID
        # Mapeia a posição numérica (lida do CSV) para o nome do componente visual
        correct_pos = str(Target_Correto_Posicao) 
        # Cria o nome do componente de imagem que é a resposta correta
        correct_response_name = 'stim_image_' + correct_pos
        
        # Inicializa variáveis para este trial
        is_correct = 0
        rt_value = None
        
        targetID_Teste.setText(identificator)
        # store start times for trialFaceRecognition
        trialFaceRecognition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trialFaceRecognition.tStart = globalClock.getTime(format='float')
        trialFaceRecognition.status = STARTED
        trialFaceRecognition.maxDuration = None
        # keep track of which components have finished
        trialFaceRecognitionComponents = trialFaceRecognition.components
        for thisComponent in trialFaceRecognition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trialFaceRecognition" ---
        thisExp.currentRoutine = trialFaceRecognition
        trialFaceRecognition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock5Trial, 'status') and thisBlock5Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *video_trial* updates
            
            # if video_trial is starting this frame...
            if video_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                video_trial.frameNStart = frameN  # exact frame index
                video_trial.tStart = t  # local t and not account for scr refresh
                video_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(video_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                video_trial.status = STARTED
                video_trial.setAutoDraw(True)
            
            # if video_trial is active this frame...
            if video_trial.status == STARTED:
                # update params
                video_trial.setImage(f"{Target_Pasta_Frames}/frame_{(int(t * 30) % total_frames) + 1:04d}.png", log=False)
            
            # *text_1* updates
            
            # if text_1 is starting this frame...
            if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_1.frameNStart = frameN  # exact frame index
                text_1.tStart = t  # local t and not account for scr refresh
                text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_1.status = STARTED
                text_1.setAutoDraw(True)
            
            # if text_1 is active this frame...
            if text_1.status == STARTED:
                # update params
                pass
            
            # *stim_image_1* updates
            
            # if stim_image_1 is starting this frame...
            if stim_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_1.frameNStart = frameN  # exact frame index
                stim_image_1.tStart = t  # local t and not account for scr refresh
                stim_image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_1, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_1.status = STARTED
                stim_image_1.setAutoDraw(True)
            
            # if stim_image_1 is active this frame...
            if stim_image_1.status == STARTED:
                # update params
                pass
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *stim_image_2* updates
            
            # if stim_image_2 is starting this frame...
            if stim_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_2.frameNStart = frameN  # exact frame index
                stim_image_2.tStart = t  # local t and not account for scr refresh
                stim_image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_2.status = STARTED
                stim_image_2.setAutoDraw(True)
            
            # if stim_image_2 is active this frame...
            if stim_image_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stim_image_3* updates
            
            # if stim_image_3 is starting this frame...
            if stim_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_3.frameNStart = frameN  # exact frame index
                stim_image_3.tStart = t  # local t and not account for scr refresh
                stim_image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_3.status = STARTED
                stim_image_3.setAutoDraw(True)
            
            # if stim_image_3 is active this frame...
            if stim_image_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *stim_image_4* updates
            
            # if stim_image_4 is starting this frame...
            if stim_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_image_4.frameNStart = frameN  # exact frame index
                stim_image_4.tStart = t  # local t and not account for scr refresh
                stim_image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_image_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                stim_image_4.status = STARTED
                stim_image_4.setAutoDraw(True)
            
            # if stim_image_4 is active this frame...
            if stim_image_4.status == STARTED:
                # update params
                pass
            
            # *key_response_trial* updates
            
            # if key_response_trial is starting this frame...
            if key_response_trial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_response_trial.frameNStart = frameN  # exact frame index
                key_response_trial.tStart = t  # local t and not account for scr refresh
                key_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_response_trial.status = STARTED
                # keyboard checking is just starting
                key_response_trial.clock.reset()  # now t=0
            if key_response_trial.status == STARTED:
                theseKeys = key_response_trial.getKeys(keyList=['1','2','3','4'], ignoreKeys=["escape"], waitRelease=False)
                _key_response_trial_allKeys.extend(theseKeys)
                if len(_key_response_trial_allKeys):
                    key_response_trial.keys = _key_response_trial_allKeys[-1].name  # just the last key pressed
                    key_response_trial.rt = _key_response_trial_allKeys[-1].rt
                    key_response_trial.duration = _key_response_trial_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse_response_trial* updates
            
            # if mouse_response_trial is starting this frame...
            if mouse_response_trial.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                mouse_response_trial.frameNStart = frameN  # exact frame index
                mouse_response_trial.tStart = t  # local t and not account for scr refresh
                mouse_response_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_response_trial, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse_response_trial.status = STARTED
                mouse_response_trial.mouseClock.reset()
                # if button is down already this ISN'T a new click
                mouse_response_trial.prevButtonState = mouse_response_trial.getPressed()
            if mouse_response_trial.status == STARTED:  # only update if started and not finished!
                buttons = mouse_response_trial.getPressed()
                # button state changed?
                if buttons != mouse_response_trial.prevButtonState:
                    mouse_response_trial.prevButtonState = buttons
                    # state changed to a new click
                    if sum(buttons) > 0:
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([stim_image_1,stim_image_2,stim_image_3,stim_image_4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_response_trial):
                                gotValidClick = True
                                mouse_response_trial.clicked_name.append(obj.name)
                                mouse_response_trial.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_response_trial.getPos()
                            mouse_response_trial.x.append(float(x))
                            mouse_response_trial.y.append(float(y))
                            buttons = mouse_response_trial.getPressed()
                            mouse_response_trial.leftButton.append(buttons[0])
                            mouse_response_trial.midButton.append(buttons[1])
                            mouse_response_trial.rightButton.append(buttons[2])
                            mouse_response_trial.time.append(mouse_response_trial.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # *targetID_Teste* updates
            
            # if targetID_Teste is starting this frame...
            if targetID_Teste.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                targetID_Teste.frameNStart = frameN  # exact frame index
                targetID_Teste.tStart = t  # local t and not account for scr refresh
                targetID_Teste.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetID_Teste, 'tStartRefresh')  # time at next scr refresh
                # update status
                targetID_Teste.status = STARTED
                targetID_Teste.setAutoDraw(True)
            
            # if targetID_Teste is active this frame...
            if targetID_Teste.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trialFaceRecognition,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trialFaceRecognition.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trialFaceRecognition.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trialFaceRecognition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trialFaceRecognition" ---
        for thisComponent in trialFaceRecognition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trialFaceRecognition
        trialFaceRecognition.tStop = globalClock.getTime(format='float')
        trialFaceRecognition.tStopRefresh = tThisFlipGlobal
        # store data for block5Trials (TrialHandler)
        block5Trials.addData('mouse_response_trial.x', mouse_response_trial.x)
        block5Trials.addData('mouse_response_trial.y', mouse_response_trial.y)
        block5Trials.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton)
        block5Trials.addData('mouse_response_trial.midButton', mouse_response_trial.midButton)
        block5Trials.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton)
        block5Trials.addData('mouse_response_trial.time', mouse_response_trial.time)
        block5Trials.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name)
        # Run 'End Routine' code from code_handle_trial
        # Inicializar as variáveis de análise (default: miss/sem resposta)
        response_method = 'miss'
        selected_option = None
        
        #  Arbitragem de Resposta:
        
        # Checa se houve resposta pelo Teclado
        if len(key_response_trial.keys) > 0:
            
            response_method = 'keyboard'
            rt_value = key_response_trial.rt
            
            # Pega o primeiro dígito pressionado
            pressed_key = key_response_trial.keys[0] 
            
            # Checa o acerto
            if str(pressed_key) == str(Target_Correto_Posicao):
                is_correct = 1
            
            selected_option = f"stim_image_{pressed_key}"
        
        # Se não, checa se houve resposta pelo Mouse
        elif mouse_response_trial.clicked_name:
            
            response_method = 'mouse'
            
            # O tempo do mouse está na lista de tempos registrada pelo componente
            if mouse_response_trial.time is not None and len(mouse_response_trial.time) > 0:
                rt_value = mouse_response_trial.time[0]
            
            # O nome do componente clicado está na lista
            selected_option = mouse_response_trial.clicked_name[0] 
            
            # Checa o acerto
            if selected_option == correct_response_name:
                is_correct = 1
        
        # SALVAR APENAS AS COLUNAS ESSENCIAIS NO ARQUIVO FINAL
        thisExp.addData('ANALYSIS_Lamina_ID', (identificator))
        thisExp.addData('ANALYSIS_CR', is_correct)
        thisExp.addData('ANALYSIS_RT', (round(rt_value,3)))
        thisExp.addData('ANALYSIS_Response_Method', response_method)
        thisExp.addData('ANALYSIS_Selected_Option', selected_option)
        thisExp.addData('ANALYSIS_Target_Component', correct_response_name)
        # the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause_5" ---
        # create an object to store info about Routine pause_5
        pause_5 = data.Routine(
            name='pause_5',
            components=[],
        )
        pause_5.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause_5
        pause_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause_5.tStart = globalClock.getTime(format='float')
        pause_5.status = STARTED
        thisExp.addData('pause_5.started', pause_5.tStart)
        pause_5.maxDuration = 1
        # skip Routine pause_5 if its 'Skip if' condition is True
        pause_5.skipped = continueRoutine and not (block5Trials.thisTrialN == (block5Trials.nTotal - 1))
        continueRoutine = pause_5.skipped
        # keep track of which components have finished
        pause_5Components = pause_5.components
        for thisComponent in pause_5.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause_5" ---
        thisExp.currentRoutine = pause_5
        pause_5.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisBlock5Trial, 'status') and thisBlock5Trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > pause_5.maxDuration-frameTolerance:
                pause_5.maxDurationReached = True
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause_5,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                pause_5.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if pause_5.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in pause_5.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_5" ---
        for thisComponent in pause_5.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause_5
        pause_5.tStop = globalClock.getTime(format='float')
        pause_5.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause_5.stopped', pause_5.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause_5.maxDurationReached:
            routineTimer.addTime(-pause_5.maxDuration)
        elif pause_5.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisBlock5Trial as finished
        if hasattr(thisBlock5Trial, 'status'):
            thisBlock5Trial.status = FINISHED
        # if awaiting a pause, pause now
        if block5Trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            block5Trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'block5Trials'
    block5Trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "finalRoutine" ---
    # create an object to store info about Routine finalRoutine
    finalRoutine = data.Routine(
        name='finalRoutine',
        components=[text],
    )
    finalRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for finalRoutine
    finalRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    finalRoutine.tStart = globalClock.getTime(format='float')
    finalRoutine.status = STARTED
    finalRoutine.maxDuration = 2
    # keep track of which components have finished
    finalRoutineComponents = finalRoutine.components
    for thisComponent in finalRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "finalRoutine" ---
    thisExp.currentRoutine = finalRoutine
    finalRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > finalRoutine.maxDuration-frameTolerance:
            finalRoutine.maxDurationReached = True
            continueRoutine = False
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=finalRoutine,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            finalRoutine.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if finalRoutine.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in finalRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "finalRoutine" ---
    for thisComponent in finalRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for finalRoutine
    finalRoutine.tStop = globalClock.getTime(format='float')
    finalRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "finalRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='semicolon')


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
