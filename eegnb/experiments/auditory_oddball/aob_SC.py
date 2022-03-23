import numpy as np
from pandas import DataFrame
#from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from time import time

__title__ = "Auditory oddball (SC)"


def present(
    save_fn = None,
    eeg=None,
    duration=120,
    n_trials=2010,
    iti=0.3,
    soa=0.2,
    jitter=0.2,
    secs=0.2,
    volume=0.8,
    random_state=42,
    s1_freq="C",
    s2_freq="D",
    s1_octave=5,
    s2_octave=6,
):

    record_duration = np.float32(duration)
    subject_nr = int(subject)
    # Ensure that relative paths start from the same directory as this script
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    info = StreamInfo("Markers", "Markers", 1, 0, "int32", "myuidw43536")
    outlet = StreamOutlet(info)  # Broadcast the stream.

    # Store info about the experiment session
    psychopyVersion = '3.0.6'
    expName = 'MMN_Modified_ver10'  # from the Builder filename that created this script
    expInfo = {'participant': ''}
    # dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    # if dlg.OK == False:
    #    core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName
    expInfo['psychopyVersion'] = psychopyVersion

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\ricercasc\\PATHS\\03_MMN\\MMN_ver10.py',
        savePickle=True, saveWideText=True,
        dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    # Start Code - component code to be run before the window creation

    # Setup the Window
    win = visual.Window(
        size=[1920, 1080], fullscr=True, screen=0,
        allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='height')
    # store frame rate of monitor if we can measure it
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess


        # start the EEG stream, will delay 5 seconds to let signal settle
        if eeg:
            eeg.start(save_fn, duration=record_duration)

        show_instructions(10)

        # Start EEG Stream, wait for signal to settle, and then pull timestamp for start point
        start = time()

    # Initialize components for Routine "Istruzioni"
    IstruzioniClock = core.Clock()
    Istr_text = visual.TextStim(win=win, name='Istr_text',
        text='Istruzioni',
        font='Arial',
        pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # -*- coding: utf-8 -*-
    '''Use this script in order to counterbalance the levels of two variables in Psychopy'''
    #In this case we want to counterbalance for:
        #1, Which sound is the deviant (500hz vs 550 hz)
        #2. Which is the first run ISI (short=500ms, long = 3000s)
    subject_nr = int(1);
    ##   Variables defined from GUI
    # subject_nr = int(expInfo.get('participant'));  
    # uncomment for 2 ISI MMN
    # you must also add a session Input in the initial GUI
    #run_nr = int(expInfo.get('session'));                

    ##   Variables defined in script
    pitch_cond = [500, 550];  
                           
    # uncomment for two ISI MMN
    #if run_nr == 1:
    #    isi_cond = [0.5, 2]; #ISI of MMN
    #elif run_nr == 2:
    #    isi_cond = [2, 0.5];

    run_nr=1
    isi_cond = [0.5, 0.5]
         
                  
    ## Create possible combinations of levels of variable 1 and variable 2.
    combination = [(x,y) for x in pitch_cond for y in isi_cond];
                                                  
    ## Assign the subject at the appropriate combination of levels
    #  Example with 2 x 2
    #  subject    1 2 3 4 5 6 7 8
    #  balancing  A B C D A B C D

    tot_levels = len(combination);

    # k can assume tot_levels values (from 0 to tot_levels -1). Can therefore be used to randomise.
    import math;
    k = subject_nr - (tot_levels*(math.floor(subject_nr/tot_levels)));
    counterbalance_cond = combination[int(k)]


    # assign values to variables to be used in Psychopy
    Duration = counterbalance_cond[1]; # set duration of ISI
    deviant = counterbalance_cond[0];
    if deviant == pitch_cond[0]:
        standard = pitch_cond[1];
    elif deviant == pitch_cond[1]:
        standard = pitch_cond[0];

    ### constraints

    ''' This script generate the sequence of trials for a MMN paradigm. 
    It starts from a series of "sequences of trials" divided in blocks.
    The aim is to scramble these blocks and return a single list that will be used
    to generate the trials in the Psychopy experiment. In this way a pseudorandom sequence
    will be generated (the trials are not scrambled, the blocks are.
    '''

    #####################
    # GENERATE TRIAL LIST
    ######################


    import numpy
    from operator import itemgetter 


    # step 1 create a list with all possible vectors (combination)
    # this allows to generate a series of deviant with at least two standard after

    dev1 = [[0,0,1]] * 20
    dev2 = [[0,0,0,1]] * 20 
    dev3 = [[0,0,0,0,1]] * 20 

    stand2 = [[0,0]] * 15 
    stand3 = [[0,0,0]] * 10

    seq_list= dev1 + dev2 + dev3 + stand2 + stand3


    # get indices
    Ind = range(len(seq_list))

    # scramble indices
    Ind_s=numpy.random.permutation(Ind)


    # scramble seq_list
    seq_list_s = itemgetter(*Ind_s)(seq_list)


    # "flatten" the list (taken from http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python)
    trial_list = [item for sublist in seq_list_s for item in sublist]

    if True:
        from collections import Counter
        freq = Counter(trial_list)
        #print freq

    if expInfo.get('Duration') == 'short':
        Duration = 0.5

    if expInfo.get('Duration') == 'long':
        Duration = 2.0

    # determine number of catch trials
    n_catch=10

    # try outside the following code. It's fairly simple.
    catch_trials = range( int((len(trial_list)/ (n_catch+1))), len(trial_list), int((len(trial_list)/ (n_catch+1))))

    # Initialize components for Routine "catch_trial"
    catch_trialClock = core.Clock()
    text_4_catch = visual.TextStim(win=win, name='text_4_catch',
        text='Premi un pulsante!',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);


    # Initialize components for Routine "ISI_post_catch"
    ISI_post_catchClock = core.Clock()

    ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

    # Initialize components for Routine "set_sound_3"
    set_sound_3Clock = core.Clock()


    # Initialize components for Routine "trial"
    trialClock = core.Clock()
    sound_1 = sound.Sound('A', secs=-1, stereo=True)
    sound_1.setVolume(0.02)
    Fix_trial = visual.TextStim(win=win, name='Fix_trial',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    ISI_3 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')
    Ntrial=0
    # p_port = parallel.ParallelPort(address='0x0378')
    text_4 = visual.TextStim(win=win, name='text_4',
        text='+',
        font='Arial',
        pos=(1, 1), height=0.01, wrapWidth=None, ori=0, 
        color='grey', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-5.0);

    # Initialize components for Routine "trial_info"
    trial_infoClock = core.Clock()


    # Initialize components for Routine "blank"
    blankClock = core.Clock()
    text_3 = visual.TextStim(win=win, name='text_3',
        text='\n',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Initialize components for Routine "Fine"
    FineClock = core.Clock()
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Fine!',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

    # ------Prepare to start Routine "Istruzioni"-------
    t = 0
    IstruzioniClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Instr_key_resp_2 = event.BuilderKeyResponse()


    # keep track of which components have finished
    IstruzioniComponents = [Istr_text, Instr_key_resp_2]
    for thisComponent in IstruzioniComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Istruzioni"-------
    while continueRoutine:
    #    print("In the while loop")
        # get current time
        t = IstruzioniClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Istr_text* updates
        if t >= 0.0 and Istr_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Istr_text.tStart = t
            Istr_text.frameNStart = frameN  # exact frame index
            Istr_text.setAutoDraw(True)
        
        # *Instr_key_resp_2* updates
        if t >= 0.0 and Instr_key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instr_key_resp_2.tStart = t
            Instr_key_resp_2.frameNStart = frameN  # exact frame index
            Instr_key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if Instr_key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IstruzioniComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Istruzioni"-------
    for thisComponent in IstruzioniComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)




    # the Routine "Istruzioni" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=len(trial_list), method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "catch_trial"-------
        t = 0
        catch_trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        catch_key_resp_2 = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        catch_trialComponents = [text_4_catch, catch_key_resp_2]
        for thisComponent in catch_trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "catch_trial"-------
        while continueRoutine:
            # get current time
            t = catch_trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4_catch* updates
            if t >= 0.0 and text_4_catch.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4_catch.tStart = t
                text_4_catch.frameNStart = frameN  # exact frame index
                text_4_catch.setAutoDraw(True)
            
            # *catch_key_resp_2* updates
            if t >= 0.0 and catch_key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                catch_key_resp_2.tStart = t
                catch_key_resp_2.frameNStart = frameN  # exact frame index
                catch_key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(catch_key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if catch_key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    catch_key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    catch_key_resp_2.rt = catch_key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            if Ntrial not in catch_trials:
                continueRoutine=False
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in catch_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "catch_trial"-------
        for thisComponent in catch_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if catch_key_resp_2.keys in ['', [], None]:  # No response was made
            catch_key_resp_2.keys=None
        trials.addData('catch_key_resp_2.keys',catch_key_resp_2.keys)
        if catch_key_resp_2.keys != None:  # we had a response
            trials.addData('catch_key_resp_2.rt', catch_key_resp_2.rt)
        
        # the Routine "catch_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI_post_catch"-------
        t = 0
        ISI_post_catchClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        # keep track of which components have finished
        ISI_post_catchComponents = [ISI]
        for thisComponent in ISI_post_catchComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI_post_catch"-------
        while continueRoutine:
            # get current time
            t = ISI_post_catchClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if Ntrial not in catch_trials:
                continueRoutine=False
            # *ISI* period
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t
                ISI.frameNStart = frameN  # exact frame index
                ISI.start(Duration)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI_post_catchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI_post_catch"-------
        for thisComponent in ISI_post_catchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "ISI_post_catch" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "set_sound_3"-------
        t = 0
        set_sound_3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # select appropriate sound filename.
        
        
        if trial_list[Ntrial] == 0:
            my_sound = 'sound_'+ str(standard) +'.wav'
            myTrig=2
        
        elif trial_list[Ntrial] == 1:
            my_sound = 'sound_'+ str(deviant) +'.wav'
            myTrig=22
        
        # keep track of which components have finished
        set_sound_3Components = []
        for thisComponent in set_sound_3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "set_sound_3"-------
        while continueRoutine:
            # get current time
            t = set_sound_3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in set_sound_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "set_sound_3"-------
        for thisComponent in set_sound_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "set_sound_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        sound_1.setSound(my_sound)
        sound_1.setVolume(0.02, log=False)
        
        # keep track of which components have finished
        # trialComponents = [sound_1, Fix_trial, ISI_3, p_port, text_4]
        trialComponents = [sound_1, Fix_trial, ISI_3, text_4] # should outlet be a component?
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop sound_1
            if t >= 0.0 and sound_1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sound_1.tStart = t
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.play()  # start the sound (it finishes automatically)
                outlet.push_sample([int(myTrig)])
            
            # *Fix_trial* updates
            if t >= 0.0 and Fix_trial.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fix_trial.tStart = t
                Fix_trial.frameNStart = frameN  # exact frame index
                Fix_trial.setAutoDraw(True)
            frameRemains = 0.0 + Duration+0.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Fix_trial.status == STARTED and t >= frameRemains:
                Fix_trial.setAutoDraw(False)
            # if t >= 0.0:
                # outlet.push_sample([int(myTrig)])
            # if t >= frameRemains:
                # outlet.push_sample([int(0)])
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 0.0 + 0.10- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            # *ISI_3* period
            if t >= 0.1 and ISI_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_3.tStart = t
                ISI_3.frameNStart = frameN  # exact frame index
                ISI_3.start(Duration)
            elif ISI_3.status == STARTED:  # one frame should pass before updating params and completing
                ISI_3.complete()  # finish the static period
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        sound_1.stop()  # ensure sound has stopped at end of routine
        Ntrial=Ntrial+1
        # if p_port.status == STARTED:
            # p_port.setData(int(0))
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial_info"-------
        t = 0
        trial_infoClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        
        
        # keep track of which components have finished
        trial_infoComponents = []
        for thisComponent in trial_infoComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_info"-------
        while continueRoutine:
            # get current time
            t = trial_infoClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_infoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_info"-------
        for thisComponent in trial_infoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if trial_list[Ntrial] == 0:
            thisExp.addData('TrialType', 'standard')
        
        elif trial_list[Ntrial] == 1:
                thisExp.addData('TrialType', 'deviant')
        
        
        
        # the Routine "trial_info" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed len(trial_list) repeats of 'trials'


    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text_3]
    for thisComponent in blankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "Fine"-------
    t = 0
    FineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FineComponents = [text_2]
    for thisComponent in FineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "Fine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Fine"-------
    for thisComponent in FineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)



    win.mouseVisible = True
    win.close()
