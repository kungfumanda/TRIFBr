/************************************************************* 
 * Teste De Reconhecimento Identidade De Faces - Trifbr *
 *************************************************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2026.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Teste de Reconhecimento Identidade de Faces - TRIFBr';  // from the Builder filename that created this script
let expInfo = {
    'Participante ID': '',
    'Idade': '',
    'Gênero': '',
    'Experimento': 'TESTE',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code_2
import * as os from 'os';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'deg',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineRoutineBegin());
flowScheduler.add(welcomeRoutineRoutineEachFrame());
flowScheduler.add(welcomeRoutineRoutineEnd());
const introTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(introTrialsLoopBegin(introTrialsLoopScheduler));
flowScheduler.add(introTrialsLoopScheduler);
flowScheduler.add(introTrialsLoopEnd);


flowScheduler.add(blockIntroRoutineBegin());
flowScheduler.add(blockIntroRoutineEachFrame());
flowScheduler.add(blockIntroRoutineEnd());
const block1TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(block1TrialsLoopBegin(block1TrialsLoopScheduler));
flowScheduler.add(block1TrialsLoopScheduler);
flowScheduler.add(block1TrialsLoopEnd);



flowScheduler.add(blockIntroRoutineBegin());
flowScheduler.add(blockIntroRoutineEachFrame());
flowScheduler.add(blockIntroRoutineEnd());
const block2TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(block2TrialsLoopBegin(block2TrialsLoopScheduler));
flowScheduler.add(block2TrialsLoopScheduler);
flowScheduler.add(block2TrialsLoopEnd);



flowScheduler.add(blockIntroRoutineBegin());
flowScheduler.add(blockIntroRoutineEachFrame());
flowScheduler.add(blockIntroRoutineEnd());
const block3TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(block3TrialsLoopBegin(block3TrialsLoopScheduler));
flowScheduler.add(block3TrialsLoopScheduler);
flowScheduler.add(block3TrialsLoopEnd);



flowScheduler.add(blockIntroRoutineBegin());
flowScheduler.add(blockIntroRoutineEachFrame());
flowScheduler.add(blockIntroRoutineEnd());
const block4TrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(block4TrialsLoopBegin(block4TrialsLoopScheduler));
flowScheduler.add(block4TrialsLoopScheduler);
flowScheduler.add(block4TrialsLoopEnd);



flowScheduler.add(finalRoutineRoutineBegin());
flowScheduler.add(finalRoutineRoutineEachFrame());
flowScheduler.add(finalRoutineRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions-intro.csv', 'path': '../conditions/conditions-intro.csv'},
    {'name': '../stimuli/BT/Face Alternativa 1.png', 'path': '../stimuli/BT/Face Alternativa 1.png'},
    {'name': '../stimuli/BT/Face Alternativa 2.png', 'path': '../stimuli/BT/Face Alternativa 2.png'},
    {'name': '../stimuli/BT/Face Alternativa 3.png', 'path': '../stimuli/BT/Face Alternativa 3.png'},
    {'name': '../stimuli/BT/Face Alternativa 4.png', 'path': '../stimuli/BT/Face Alternativa 4.png'},
    {'name': 'conditions-B1.csv', 'path': '../conditions/conditions-B1.csv'},
    {'name': '../stimuli/B1/L1/Gabriela.png', 'path': '../stimuli/B1/L1/Gabriela.png'},
    {'name': '../stimuli/B1/L1/Mariana.png', 'path': '../stimuli/B1/L1/Mariana.png'},
    {'name': '../stimuli/B1/L1/Kaylane.png', 'path': '../stimuli/B1/L1/Kaylane.png'},
    {'name': '../stimuli/B1/L1/Nicole (Alvo).png', 'path': '../stimuli/B1/L1/Nicole (Alvo).png'},
    {'name': '../stimuli/B1/L2/Lilian.png', 'path': '../stimuli/B1/L2/Lilian.png'},
    {'name': '../stimuli/B1/L2/M. Gabriela (alvo).png', 'path': '../stimuli/B1/L2/M. Gabriela (alvo).png'},
    {'name': '../stimuli/B1/L2/Marina.png', 'path': '../stimuli/B1/L2/Marina.png'},
    {'name': '../stimuli/B1/L2/Daiane.png', 'path': '../stimuli/B1/L2/Daiane.png'},
    {'name': '../stimuli/B1/L3/Julia (alvo).png', 'path': '../stimuli/B1/L3/Julia (alvo).png'},
    {'name': '../stimuli/B1/L3/Amanda.png', 'path': '../stimuli/B1/L3/Amanda.png'},
    {'name': '../stimuli/B1/L3/Laura.png', 'path': '../stimuli/B1/L3/Laura.png'},
    {'name': '../stimuli/B1/L3/Lyvia.png', 'path': '../stimuli/B1/L3/Lyvia.png'},
    {'name': '../stimuli/B1/L4/Letras.png', 'path': '../stimuli/B1/L4/Letras.png'},
    {'name': '../stimuli/B1/L4/Andrey (alvo).png', 'path': '../stimuli/B1/L4/Andrey (alvo).png'},
    {'name': '../stimuli/B1/L4/Amigo de Will 3.png', 'path': '../stimuli/B1/L4/Amigo de Will 3.png'},
    {'name': '../stimuli/B1/L4/Fabio.png', 'path': '../stimuli/B1/L4/Fabio.png'},
    {'name': '../stimuli/B1/L5/Henrique.png', 'path': '../stimuli/B1/L5/Henrique.png'},
    {'name': '../stimuli/B1/L5/Gabriel.png', 'path': '../stimuli/B1/L5/Gabriel.png'},
    {'name': '../stimuli/B1/L5/Mateus.png', 'path': '../stimuli/B1/L5/Mateus.png'},
    {'name': '../stimuli/B1/L5/Lucas D.png', 'path': '../stimuli/B1/L5/Lucas D.png'},
    {'name': '../stimuli/B1/L6/Will (alvo).png', 'path': '../stimuli/B1/L6/Will (alvo).png'},
    {'name': '../stimuli/B1/L6/Preto.png', 'path': '../stimuli/B1/L6/Preto.png'},
    {'name': '../stimuli/B1/L6/Kayke.png', 'path': '../stimuli/B1/L6/Kayke.png'},
    {'name': '../conditions/conditions-B2.csv', 'path': '../conditions/conditions-B2.csv'},
    {'name': '../conditions/conditions-B3.csv', 'path': '../conditions/conditions-B3.csv'},
    {'name': '../conditions/conditions-B4.csv', 'path': '../conditions/conditions-B4.csv'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DATA);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["Participante ID"]}_${expName}`);
  psychoJS.experiment.field_separator = ';';


  return Scheduler.Event.NEXT;
}


var welcomeRoutineClock;
var text_title;
var text_body;
var text_advance;
var key_response_initiate;
var mouse_initiate;
var block_number;
var exampleInstructionClock;
var text_example;
var video_instruction;
var continue_keys;
var text_instruction_1;
var image_instruction_1;
var text_instruction_2;
var image_instruction_2;
var text_instruction_3;
var image_instruction_3;
var text_instruction_4;
var image_instruction_4;
var key_response_intructions;
var mouse_response_instructions;
var blockIntroClock;
var txt_block_title;
var text_response;
var key_resp;
var mouse_resp;
var trialFaceRecognitionClock;
var video_trial;
var text_1;
var stim_image_1;
var text_2;
var stim_image_2;
var text_3;
var stim_image_3;
var text_4;
var stim_image_4;
var key_response_trial;
var mouse_response_trial;
var targetID_Teste;
var pauseClock;
var finalRoutineClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcomeRoutine"
  welcomeRoutineClock = new util.Clock();
  text_title = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_title',
    text: 'Bem-vindo(a) ao Teste de Reconhecimento\nde Identidade de Faces.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0.7], draggable: false, height: 0.09,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_body = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_body',
    text: 'TAREFA: \nUm vídeo com uma face aparecerá no centro. Identifique qual das 4 opções abaixo corresponde à mesma face.\n\nCOMO RESPONDER:\nUse o MOUSE para clicar na face OU Use o TECLADO (1, 2, 3, 4)\n\nDETALHES:\nO teste começará com uma breve etapa de familiarização.\nO teste é dividido em blocos. Haverá pausas automáticas entre eles.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.07,  wrapWidth: 1.6, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_advance = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_advance',
    text: 'Vamos fazer um teste? \nPressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
    font: 'Arial',
    units: 'norm', 
    pos: [0, (- 0.7)], draggable: false, height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_response_initiate = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse_initiate = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_initiate.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  block_number = 0;
  
  // Initialize components for Routine "exampleInstruction"
  exampleInstructionClock = new util.Clock();
  text_example = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_example',
    text: 'Este é um exemplo deste teste',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.42], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  video_instruction = new visual.ImageStim({
    win : psychoJS.window,
    name : 'video_instruction', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  continue_keys = new visual.TextStim({
    win: psychoJS.window,
    name: 'continue_keys',
    text: 'Clique em algum das opções ou digite o seu número para continuar.',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.04)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_instruction_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instruction_1',
    text: '1',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.4), (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  image_instruction_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_instruction_1', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), (- 0.3)], 
    draggable: false,
    size : [0.2, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_instruction_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instruction_2',
    text: '2',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.13), (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  image_instruction_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_instruction_2', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.13), (- 0.3)], 
    draggable: false,
    size : [0.2, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  text_instruction_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instruction_3',
    text: '3',
    font: 'Arial',
    units: 'height', 
    pos: [0.13, (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  image_instruction_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_instruction_3', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.13, (- 0.3)], 
    draggable: false,
    size : [0.2, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  text_instruction_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_instruction_4',
    text: '4',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  image_instruction_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_instruction_4', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, (- 0.3)], 
    draggable: false,
    size : [0.2, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  key_response_intructions = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse_response_instructions = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_response_instructions.mouseClock = new util.Clock();
  // Initialize components for Routine "blockIntro"
  blockIntroClock = new util.Clock();
  txt_block_title = new visual.TextStim({
    win: psychoJS.window,
    name: 'txt_block_title',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 1], draggable: false, height: 1.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_response = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_response',
    text: 'Pressione a BARRA DE ESPAÇO ou o BOTÃO ESQUERDO DO MOUSE para continuar.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 2)], draggable: false, height: 0.7,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse_resp = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_resp.mouseClock = new util.Clock();
  // Initialize components for Routine "trialFaceRecognition"
  trialFaceRecognitionClock = new util.Clock();
  video_trial = new visual.ImageStim({
    win : psychoJS.window,
    name : 'video_trial', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.4, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_1',
    text: '1',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.4), (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  stim_image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim_image_1', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), (- 0.3)], 
    draggable: false,
    size : [null, 0.4],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '2',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.13), (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  stim_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim_image_2', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.13), (- 0.3)], 
    draggable: false,
    size : [null, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '3',
    font: 'Arial',
    units: 'height', 
    pos: [0.13, (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  stim_image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim_image_3', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.13, (- 0.3)], 
    draggable: false,
    size : [null, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '4',
    font: 'Arial',
    units: 'height', 
    pos: [0.4, (- 0.08)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  stim_image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stim_image_4', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, (- 0.3)], 
    draggable: false,
    size : [null, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  key_response_trial = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  mouse_response_trial = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_response_trial.mouseClock = new util.Clock();
  targetID_Teste = new visual.TextStim({
    win: psychoJS.window,
    name: 'targetID_Teste',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [(- 0.48), 0.45], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -13.0 
  });
  
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  // Initialize components for Routine "finalRoutine"
  finalRoutineClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Agradecemos por participar!',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var welcomeRoutineMaxDurationReached;
var _key_response_initiate_allKeys;
var gotValidClick;
var welcomeRoutineMaxDuration;
var welcomeRoutineComponents;
function welcomeRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcomeRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    welcomeRoutineClock.reset();
    routineTimer.reset();
    welcomeRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    key_response_initiate.keys = undefined;
    key_response_initiate.rt = undefined;
    _key_response_initiate_allKeys = [];
    // setup some python lists for storing info about the mouse_initiate
    gotValidClick = false; // until a click is received
    welcomeRoutineMaxDuration = null
    // keep track of which components have finished
    welcomeRoutineComponents = [];
    welcomeRoutineComponents.push(text_title);
    welcomeRoutineComponents.push(text_body);
    welcomeRoutineComponents.push(text_advance);
    welcomeRoutineComponents.push(key_response_initiate);
    welcomeRoutineComponents.push(mouse_initiate);
    
    for (const thisComponent of welcomeRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function welcomeRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcomeRoutine' ---
    // get current time
    t = welcomeRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_title* updates
    if (t >= 0.0 && text_title.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_title.tStart = t;  // (not accounting for frame time here)
      text_title.frameNStart = frameN;  // exact frame index
      
      text_title.setAutoDraw(true);
    }
    
    
    // if text_title is active this frame...
    if (text_title.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_body* updates
    if (t >= 0.0 && text_body.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_body.tStart = t;  // (not accounting for frame time here)
      text_body.frameNStart = frameN;  // exact frame index
      
      text_body.setAutoDraw(true);
    }
    
    
    // if text_body is active this frame...
    if (text_body.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_advance* updates
    if (t >= 0.0 && text_advance.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_advance.tStart = t;  // (not accounting for frame time here)
      text_advance.frameNStart = frameN;  // exact frame index
      
      text_advance.setAutoDraw(true);
    }
    
    
    // if text_advance is active this frame...
    if (text_advance.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_response_initiate* updates
    if (t >= 0.0 && key_response_initiate.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_response_initiate.tStart = t;  // (not accounting for frame time here)
      key_response_initiate.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_response_initiate.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_response_initiate.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_response_initiate.clearEvents(); });
    }
    
    // if key_response_initiate is active this frame...
    if (key_response_initiate.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_response_initiate.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_response_initiate_allKeys = _key_response_initiate_allKeys.concat(theseKeys);
      if (_key_response_initiate_allKeys.length > 0) {
        key_response_initiate.keys = _key_response_initiate_allKeys[_key_response_initiate_allKeys.length - 1].name;  // just the last key pressed
        key_response_initiate.rt = _key_response_initiate_allKeys[_key_response_initiate_allKeys.length - 1].rt;
        key_response_initiate.duration = _key_response_initiate_allKeys[_key_response_initiate_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse_initiate* updates
    if (t >= 0.0 && mouse_initiate.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_initiate.tStart = t;  // (not accounting for frame time here)
      mouse_initiate.frameNStart = frameN;  // exact frame index
      
      mouse_initiate.status = PsychoJS.Status.STARTED;
      mouse_initiate.mouseClock.reset();
      prevButtonState = mouse_initiate.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_initiate is active this frame...
    if (mouse_initiate.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_initiate.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcomeRoutine' ---
    for (const thisComponent of welcomeRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_response_initiate.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "welcomeRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var introTrials;
function introTrialsLoopBegin(introTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    introTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'C:/Users/amdas/Documents/Experimentos/TRIFBr/conditions/conditions-intro.csv',
      seed: undefined, name: 'introTrials'
    });
    psychoJS.experiment.addLoop(introTrials); // add the loop to the experiment
    currentLoop = introTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisIntroTrial of introTrials) {
      snapshot = introTrials.getSnapshot();
      introTrialsLoopScheduler.add(importConditions(snapshot));
      introTrialsLoopScheduler.add(exampleInstructionRoutineBegin(snapshot));
      introTrialsLoopScheduler.add(exampleInstructionRoutineEachFrame());
      introTrialsLoopScheduler.add(exampleInstructionRoutineEnd(snapshot));
      introTrialsLoopScheduler.add(introTrialsLoopEndIteration(introTrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function introTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(introTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function introTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var block1Trials;
function block1TrialsLoopBegin(block1TrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    block1Trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'C:/Users/amdas/Documents/Experimentos/TRIFBr/conditions/conditions-B1.csv',
      seed: undefined, name: 'block1Trials'
    });
    psychoJS.experiment.addLoop(block1Trials); // add the loop to the experiment
    currentLoop = block1Trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock1Trial of block1Trials) {
      snapshot = block1Trials.getSnapshot();
      block1TrialsLoopScheduler.add(importConditions(snapshot));
      block1TrialsLoopScheduler.add(trialFaceRecognitionRoutineBegin(snapshot));
      block1TrialsLoopScheduler.add(trialFaceRecognitionRoutineEachFrame());
      block1TrialsLoopScheduler.add(trialFaceRecognitionRoutineEnd(snapshot));
      block1TrialsLoopScheduler.add(pauseRoutineBegin(snapshot));
      block1TrialsLoopScheduler.add(pauseRoutineEachFrame());
      block1TrialsLoopScheduler.add(pauseRoutineEnd(snapshot));
      block1TrialsLoopScheduler.add(block1TrialsLoopEndIteration(block1TrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function block1TrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(block1Trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function block1TrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var block2Trials;
function block2TrialsLoopBegin(block2TrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    block2Trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: '../conditions/conditions-B2.csv',
      seed: undefined, name: 'block2Trials'
    });
    psychoJS.experiment.addLoop(block2Trials); // add the loop to the experiment
    currentLoop = block2Trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock2Trial of block2Trials) {
      snapshot = block2Trials.getSnapshot();
      block2TrialsLoopScheduler.add(importConditions(snapshot));
      block2TrialsLoopScheduler.add(trialFaceRecognitionRoutineBegin(snapshot));
      block2TrialsLoopScheduler.add(trialFaceRecognitionRoutineEachFrame());
      block2TrialsLoopScheduler.add(trialFaceRecognitionRoutineEnd(snapshot));
      block2TrialsLoopScheduler.add(pauseRoutineBegin(snapshot));
      block2TrialsLoopScheduler.add(pauseRoutineEachFrame());
      block2TrialsLoopScheduler.add(pauseRoutineEnd(snapshot));
      block2TrialsLoopScheduler.add(block2TrialsLoopEndIteration(block2TrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function block2TrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(block2Trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function block2TrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var block3Trials;
function block3TrialsLoopBegin(block3TrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    block3Trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: '../conditions/conditions-B3.csv',
      seed: undefined, name: 'block3Trials'
    });
    psychoJS.experiment.addLoop(block3Trials); // add the loop to the experiment
    currentLoop = block3Trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock3Trial of block3Trials) {
      snapshot = block3Trials.getSnapshot();
      block3TrialsLoopScheduler.add(importConditions(snapshot));
      block3TrialsLoopScheduler.add(trialFaceRecognitionRoutineBegin(snapshot));
      block3TrialsLoopScheduler.add(trialFaceRecognitionRoutineEachFrame());
      block3TrialsLoopScheduler.add(trialFaceRecognitionRoutineEnd(snapshot));
      block3TrialsLoopScheduler.add(pauseRoutineBegin(snapshot));
      block3TrialsLoopScheduler.add(pauseRoutineEachFrame());
      block3TrialsLoopScheduler.add(pauseRoutineEnd(snapshot));
      block3TrialsLoopScheduler.add(block3TrialsLoopEndIteration(block3TrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function block3TrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(block3Trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function block3TrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var block4Trials;
function block4TrialsLoopBegin(block4TrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    block4Trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: '../conditions/conditions-B4.csv',
      seed: undefined, name: 'block4Trials'
    });
    psychoJS.experiment.addLoop(block4Trials); // add the loop to the experiment
    currentLoop = block4Trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock4Trial of block4Trials) {
      snapshot = block4Trials.getSnapshot();
      block4TrialsLoopScheduler.add(importConditions(snapshot));
      block4TrialsLoopScheduler.add(trialFaceRecognitionRoutineBegin(snapshot));
      block4TrialsLoopScheduler.add(trialFaceRecognitionRoutineEachFrame());
      block4TrialsLoopScheduler.add(trialFaceRecognitionRoutineEnd(snapshot));
      block4TrialsLoopScheduler.add(pauseRoutineBegin(snapshot));
      block4TrialsLoopScheduler.add(pauseRoutineEachFrame());
      block4TrialsLoopScheduler.add(pauseRoutineEnd(snapshot));
      block4TrialsLoopScheduler.add(block4TrialsLoopEndIteration(block4TrialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function block4TrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(block4Trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function block4TrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var exampleInstructionMaxDurationReached;
var _key_response_intructions_allKeys;
var exampleInstructionMaxDuration;
var exampleInstructionComponents;
function exampleInstructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'exampleInstruction' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    exampleInstructionClock.reset();
    routineTimer.reset();
    exampleInstructionMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_count_frames_intro
    /* Syntax Error: Fix Python code */
    image_instruction_1.setImage(Image_1);
    image_instruction_2.setImage(Image_2);
    image_instruction_3.setImage(Image_3);
    image_instruction_4.setImage(Image_4);
    key_response_intructions.keys = undefined;
    key_response_intructions.rt = undefined;
    _key_response_intructions_allKeys = [];
    // setup some python lists for storing info about the mouse_response_instructions
    mouse_response_instructions.clicked_name = [];
    gotValidClick = false; // until a click is received
    exampleInstructionMaxDuration = null
    // keep track of which components have finished
    exampleInstructionComponents = [];
    exampleInstructionComponents.push(text_example);
    exampleInstructionComponents.push(video_instruction);
    exampleInstructionComponents.push(continue_keys);
    exampleInstructionComponents.push(text_instruction_1);
    exampleInstructionComponents.push(image_instruction_1);
    exampleInstructionComponents.push(text_instruction_2);
    exampleInstructionComponents.push(image_instruction_2);
    exampleInstructionComponents.push(text_instruction_3);
    exampleInstructionComponents.push(image_instruction_3);
    exampleInstructionComponents.push(text_instruction_4);
    exampleInstructionComponents.push(image_instruction_4);
    exampleInstructionComponents.push(key_response_intructions);
    exampleInstructionComponents.push(mouse_response_instructions);
    
    for (const thisComponent of exampleInstructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function exampleInstructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'exampleInstruction' ---
    // get current time
    t = exampleInstructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_example* updates
    if (t >= 0.0 && text_example.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_example.tStart = t;  // (not accounting for frame time here)
      text_example.frameNStart = frameN;  // exact frame index
      
      text_example.setAutoDraw(true);
    }
    
    
    // if text_example is active this frame...
    if (text_example.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *video_instruction* updates
    if (t >= 0.0 && video_instruction.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      video_instruction.setImage(f'{Target_Pasta_Frames}/frame_{((int((t * 30)) % total_frames) + 1):04d}.png', false);
      // keep track of start time/frame for later
      video_instruction.tStart = t;  // (not accounting for frame time here)
      video_instruction.frameNStart = frameN;  // exact frame index
      
      video_instruction.setAutoDraw(true);
    }
    
    
    // if video_instruction is active this frame...
    if (video_instruction.status === PsychoJS.Status.STARTED) {
      // update params
      video_instruction.setImage(f'{Target_Pasta_Frames}/frame_{((int((t * 30)) % total_frames) + 1):04d}.png', false);
    }
    
    
    // *continue_keys* updates
    if (t >= 0.0 && continue_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_keys.tStart = t;  // (not accounting for frame time here)
      continue_keys.frameNStart = frameN;  // exact frame index
      
      continue_keys.setAutoDraw(true);
    }
    
    
    // if continue_keys is active this frame...
    if (continue_keys.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_instruction_1* updates
    if (t >= 0.0 && text_instruction_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instruction_1.tStart = t;  // (not accounting for frame time here)
      text_instruction_1.frameNStart = frameN;  // exact frame index
      
      text_instruction_1.setAutoDraw(true);
    }
    
    
    // if text_instruction_1 is active this frame...
    if (text_instruction_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_instruction_1* updates
    if (t >= 0.0 && image_instruction_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_instruction_1.tStart = t;  // (not accounting for frame time here)
      image_instruction_1.frameNStart = frameN;  // exact frame index
      
      image_instruction_1.setAutoDraw(true);
    }
    
    
    // if image_instruction_1 is active this frame...
    if (image_instruction_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_instruction_2* updates
    if (t >= 0.0 && text_instruction_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instruction_2.tStart = t;  // (not accounting for frame time here)
      text_instruction_2.frameNStart = frameN;  // exact frame index
      
      text_instruction_2.setAutoDraw(true);
    }
    
    
    // if text_instruction_2 is active this frame...
    if (text_instruction_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_instruction_2* updates
    if (t >= 0.0 && image_instruction_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_instruction_2.tStart = t;  // (not accounting for frame time here)
      image_instruction_2.frameNStart = frameN;  // exact frame index
      
      image_instruction_2.setAutoDraw(true);
    }
    
    
    // if image_instruction_2 is active this frame...
    if (image_instruction_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_instruction_3* updates
    if (t >= 0.0 && text_instruction_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instruction_3.tStart = t;  // (not accounting for frame time here)
      text_instruction_3.frameNStart = frameN;  // exact frame index
      
      text_instruction_3.setAutoDraw(true);
    }
    
    
    // if text_instruction_3 is active this frame...
    if (text_instruction_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_instruction_3* updates
    if (t >= 0.0 && image_instruction_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_instruction_3.tStart = t;  // (not accounting for frame time here)
      image_instruction_3.frameNStart = frameN;  // exact frame index
      
      image_instruction_3.setAutoDraw(true);
    }
    
    
    // if image_instruction_3 is active this frame...
    if (image_instruction_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_instruction_4* updates
    if (t >= 0.0 && text_instruction_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_instruction_4.tStart = t;  // (not accounting for frame time here)
      text_instruction_4.frameNStart = frameN;  // exact frame index
      
      text_instruction_4.setAutoDraw(true);
    }
    
    
    // if text_instruction_4 is active this frame...
    if (text_instruction_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_instruction_4* updates
    if (t >= 0.0 && image_instruction_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_instruction_4.tStart = t;  // (not accounting for frame time here)
      image_instruction_4.frameNStart = frameN;  // exact frame index
      
      image_instruction_4.setAutoDraw(true);
    }
    
    
    // if image_instruction_4 is active this frame...
    if (image_instruction_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_response_intructions* updates
    if (t >= 0.0 && key_response_intructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_response_intructions.tStart = t;  // (not accounting for frame time here)
      key_response_intructions.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_response_intructions.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_response_intructions.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_response_intructions.clearEvents(); });
    }
    
    // if key_response_intructions is active this frame...
    if (key_response_intructions.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_response_intructions.getKeys({
        keyList: typeof ['1','2','3','4'] === 'string' ? [['1','2','3','4']] : ['1','2','3','4'], 
        waitRelease: false
      });
      _key_response_intructions_allKeys = _key_response_intructions_allKeys.concat(theseKeys);
      if (_key_response_intructions_allKeys.length > 0) {
        key_response_intructions.keys = _key_response_intructions_allKeys[_key_response_intructions_allKeys.length - 1].name;  // just the last key pressed
        key_response_intructions.rt = _key_response_intructions_allKeys[_key_response_intructions_allKeys.length - 1].rt;
        key_response_intructions.duration = _key_response_intructions_allKeys[_key_response_intructions_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse_response_instructions* updates
    if (t >= 0.0 && mouse_response_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_response_instructions.tStart = t;  // (not accounting for frame time here)
      mouse_response_instructions.frameNStart = frameN;  // exact frame index
      
      mouse_response_instructions.status = PsychoJS.Status.STARTED;
      mouse_response_instructions.mouseClock.reset();
      prevButtonState = mouse_response_instructions.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_response_instructions is active this frame...
    if (mouse_response_instructions.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_response_instructions.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_response_instructions.clickableObjects = eval([image_instruction_1, image_instruction_2, image_instruction_3, image_instruction_4])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_response_instructions.clickableObjects)) {
              mouse_response_instructions.clickableObjects = [mouse_response_instructions.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_response_instructions.clickableObjects) {
              if (obj.contains(mouse_response_instructions)) {
                  gotValidClick = true;
                  mouse_response_instructions.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_response_instructions.clickableObjects = eval([image_instruction_1, image_instruction_2, image_instruction_3, image_instruction_4])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_response_instructions.clickableObjects)) {
              mouse_response_instructions.clickableObjects = [mouse_response_instructions.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_response_instructions.clickableObjects) {
              if (obj.contains(mouse_response_instructions)) {
                  gotValidClick = true;
                  mouse_response_instructions.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exampleInstructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exampleInstructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'exampleInstruction' ---
    for (const thisComponent of exampleInstructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_response_intructions.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "exampleInstruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blockIntroMaxDurationReached;
var block_title;
var _key_resp_allKeys;
var blockIntroMaxDuration;
var blockIntroComponents;
function blockIntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blockIntro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    blockIntroClock.reset();
    routineTimer.reset();
    blockIntroMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from block_num
    block_number += 1;
    block_title = `BLOCO ${block_number}`;
    
    txt_block_title.setText(block_title);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // setup some python lists for storing info about the mouse_resp
    gotValidClick = false; // until a click is received
    blockIntroMaxDuration = null
    // keep track of which components have finished
    blockIntroComponents = [];
    blockIntroComponents.push(txt_block_title);
    blockIntroComponents.push(text_response);
    blockIntroComponents.push(key_resp);
    blockIntroComponents.push(mouse_resp);
    
    for (const thisComponent of blockIntroComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blockIntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blockIntro' ---
    // get current time
    t = blockIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *txt_block_title* updates
    if (t >= 0.0 && txt_block_title.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      txt_block_title.tStart = t;  // (not accounting for frame time here)
      txt_block_title.frameNStart = frameN;  // exact frame index
      
      txt_block_title.setAutoDraw(true);
    }
    
    
    // if txt_block_title is active this frame...
    if (txt_block_title.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_response* updates
    if (t >= 0.0 && text_response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_response.tStart = t;  // (not accounting for frame time here)
      text_response.frameNStart = frameN;  // exact frame index
      
      text_response.setAutoDraw(true);
    }
    
    
    // if text_response is active this frame...
    if (text_response.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({
        keyList: typeof 'space' === 'string' ? ['space'] : 'space', 
        waitRelease: false
      });
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse_resp* updates
    if (t >= 0.0 && mouse_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_resp.tStart = t;  // (not accounting for frame time here)
      mouse_resp.frameNStart = frameN;  // exact frame index
      
      mouse_resp.status = PsychoJS.Status.STARTED;
      mouse_resp.mouseClock.reset();
      prevButtonState = mouse_resp.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_resp is active this frame...
    if (mouse_resp.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_resp.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blockIntroComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blockIntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blockIntro' ---
    for (const thisComponent of blockIntroComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "blockIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialFaceRecognitionMaxDurationReached;
var _key_response_trial_allKeys;
var identificator;
var correct_pos;
var correct_response_name;
var is_correct;
var rt_value;
var trialFaceRecognitionMaxDuration;
var trialFaceRecognitionComponents;
function trialFaceRecognitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialFaceRecognition' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialFaceRecognitionClock.reset();
    routineTimer.reset();
    trialFaceRecognitionMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_count_frames
    /* Syntax Error: Fix Python code */
    stim_image_1.setImage(Image_1);
    stim_image_2.setImage(Image_2);
    stim_image_3.setImage(Image_3);
    stim_image_4.setImage(Image_4);
    key_response_trial.keys = undefined;
    key_response_trial.rt = undefined;
    _key_response_trial_allKeys = [];
    // setup some python lists for storing info about the mouse_response_trial
    // current position of the mouse:
    mouse_response_trial.x = [];
    mouse_response_trial.y = [];
    mouse_response_trial.leftButton = [];
    mouse_response_trial.midButton = [];
    mouse_response_trial.rightButton = [];
    mouse_response_trial.time = [];
    mouse_response_trial.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code_handle_trial
    identificator = (Bloco + Lamina_ID);
    correct_pos = Target_Correto_Posicao.toString();
    correct_response_name = ("stim_image_" + correct_pos);
    is_correct = 0;
    rt_value = null;
    
    targetID_Teste.setText(identificator);
    trialFaceRecognitionMaxDuration = null
    // keep track of which components have finished
    trialFaceRecognitionComponents = [];
    trialFaceRecognitionComponents.push(video_trial);
    trialFaceRecognitionComponents.push(text_1);
    trialFaceRecognitionComponents.push(stim_image_1);
    trialFaceRecognitionComponents.push(text_2);
    trialFaceRecognitionComponents.push(stim_image_2);
    trialFaceRecognitionComponents.push(text_3);
    trialFaceRecognitionComponents.push(stim_image_3);
    trialFaceRecognitionComponents.push(text_4);
    trialFaceRecognitionComponents.push(stim_image_4);
    trialFaceRecognitionComponents.push(key_response_trial);
    trialFaceRecognitionComponents.push(mouse_response_trial);
    trialFaceRecognitionComponents.push(targetID_Teste);
    
    for (const thisComponent of trialFaceRecognitionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _mouseXYs;
function trialFaceRecognitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialFaceRecognition' ---
    // get current time
    t = trialFaceRecognitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *video_trial* updates
    if (t >= 0.0 && video_trial.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      video_trial.setImage(f'{Target_Pasta_Frames}/frame_{((int((t * 30)) % total_frames) + 1):04d}.png', false);
      // keep track of start time/frame for later
      video_trial.tStart = t;  // (not accounting for frame time here)
      video_trial.frameNStart = frameN;  // exact frame index
      
      video_trial.setAutoDraw(true);
    }
    
    
    // if video_trial is active this frame...
    if (video_trial.status === PsychoJS.Status.STARTED) {
      // update params
      video_trial.setImage(f'{Target_Pasta_Frames}/frame_{((int((t * 30)) % total_frames) + 1):04d}.png', false);
    }
    
    
    // *text_1* updates
    if (t >= 0.0 && text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_1.tStart = t;  // (not accounting for frame time here)
      text_1.frameNStart = frameN;  // exact frame index
      
      text_1.setAutoDraw(true);
    }
    
    
    // if text_1 is active this frame...
    if (text_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *stim_image_1* updates
    if (t >= 0.0 && stim_image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_image_1.tStart = t;  // (not accounting for frame time here)
      stim_image_1.frameNStart = frameN;  // exact frame index
      
      stim_image_1.setAutoDraw(true);
    }
    
    
    // if stim_image_1 is active this frame...
    if (stim_image_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *stim_image_2* updates
    if (t >= 0.0 && stim_image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_image_2.tStart = t;  // (not accounting for frame time here)
      stim_image_2.frameNStart = frameN;  // exact frame index
      
      stim_image_2.setAutoDraw(true);
    }
    
    
    // if stim_image_2 is active this frame...
    if (stim_image_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // if text_3 is active this frame...
    if (text_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *stim_image_3* updates
    if (t >= 0.0 && stim_image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_image_3.tStart = t;  // (not accounting for frame time here)
      stim_image_3.frameNStart = frameN;  // exact frame index
      
      stim_image_3.setAutoDraw(true);
    }
    
    
    // if stim_image_3 is active this frame...
    if (stim_image_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // if text_4 is active this frame...
    if (text_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *stim_image_4* updates
    if (t >= 0.0 && stim_image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_image_4.tStart = t;  // (not accounting for frame time here)
      stim_image_4.frameNStart = frameN;  // exact frame index
      
      stim_image_4.setAutoDraw(true);
    }
    
    
    // if stim_image_4 is active this frame...
    if (stim_image_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_response_trial* updates
    if (t >= 0.0 && key_response_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_response_trial.tStart = t;  // (not accounting for frame time here)
      key_response_trial.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_response_trial.clock.reset();
      key_response_trial.start();
    }
    
    // if key_response_trial is active this frame...
    if (key_response_trial.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_response_trial.getKeys({
        keyList: typeof ['1','2','3','4'] === 'string' ? [['1','2','3','4']] : ['1','2','3','4'], 
        waitRelease: false
      });
      _key_response_trial_allKeys = _key_response_trial_allKeys.concat(theseKeys);
      if (_key_response_trial_allKeys.length > 0) {
        key_response_trial.keys = _key_response_trial_allKeys[_key_response_trial_allKeys.length - 1].name;  // just the last key pressed
        key_response_trial.rt = _key_response_trial_allKeys[_key_response_trial_allKeys.length - 1].rt;
        key_response_trial.duration = _key_response_trial_allKeys[_key_response_trial_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *mouse_response_trial* updates
    if (frameN >= 0.0 && mouse_response_trial.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_response_trial.tStart = t;  // (not accounting for frame time here)
      mouse_response_trial.frameNStart = frameN;  // exact frame index
      
      mouse_response_trial.status = PsychoJS.Status.STARTED;
      mouse_response_trial.mouseClock.reset();
      prevButtonState = mouse_response_trial.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_response_trial is active this frame...
    if (mouse_response_trial.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_response_trial.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_response_trial.clickableObjects = eval([stim_image_1, stim_image_2, stim_image_3, stim_image_4])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_response_trial.clickableObjects)) {
              mouse_response_trial.clickableObjects = [mouse_response_trial.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_response_trial.clickableObjects) {
              if (obj.contains(mouse_response_trial)) {
                  gotValidClick = true;
                  mouse_response_trial.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_response_trial.clickableObjects = eval([stim_image_1, stim_image_2, stim_image_3, stim_image_4])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_response_trial.clickableObjects)) {
              mouse_response_trial.clickableObjects = [mouse_response_trial.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_response_trial.clickableObjects) {
              if (obj.contains(mouse_response_trial)) {
                  gotValidClick = true;
                  mouse_response_trial.clicked_name.push(obj.name);
              }
          }
          if (gotValidClick === true) { 
            _mouseXYs = mouse_response_trial.getPos();
            mouse_response_trial.x.push(_mouseXYs[0]);
            mouse_response_trial.y.push(_mouseXYs[1]);
            mouse_response_trial.leftButton.push(_mouseButtons[0]);
            mouse_response_trial.midButton.push(_mouseButtons[1]);
            mouse_response_trial.rightButton.push(_mouseButtons[2]);
            mouse_response_trial.time.push(mouse_response_trial.mouseClock.getTime());
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *targetID_Teste* updates
    if (t >= 0.0 && targetID_Teste.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetID_Teste.tStart = t;  // (not accounting for frame time here)
      targetID_Teste.frameNStart = frameN;  // exact frame index
      
      targetID_Teste.setAutoDraw(true);
    }
    
    
    // if targetID_Teste is active this frame...
    if (targetID_Teste.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialFaceRecognitionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var response_method;
var selected_option;
var pressed_key;
function trialFaceRecognitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialFaceRecognition' ---
    for (const thisComponent of trialFaceRecognitionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_response_trial.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_response_trial.x', mouse_response_trial.x);
    psychoJS.experiment.addData('mouse_response_trial.y', mouse_response_trial.y);
    psychoJS.experiment.addData('mouse_response_trial.leftButton', mouse_response_trial.leftButton);
    psychoJS.experiment.addData('mouse_response_trial.midButton', mouse_response_trial.midButton);
    psychoJS.experiment.addData('mouse_response_trial.rightButton', mouse_response_trial.rightButton);
    psychoJS.experiment.addData('mouse_response_trial.time', mouse_response_trial.time);
    psychoJS.experiment.addData('mouse_response_trial.clicked_name', mouse_response_trial.clicked_name);
    
    // Run 'End Routine' code from code_handle_trial
    response_method = "miss";
    selected_option = null;
    if ((key_response_trial.keys.length > 0)) {
        response_method = "keyboard";
        rt_value = key_response_trial.rt;
        pressed_key = key_response_trial.keys[0];
        if ((pressed_key.toString() === Target_Correto_Posicao.toString())) {
            is_correct = 1;
        }
        selected_option = `stim_image_${pressed_key}`;
    } else {
        if (mouse_response_trial.clicked_name) {
            response_method = "mouse";
            if (((mouse_response_trial.time !== null) && (mouse_response_trial.time.length > 0))) {
                rt_value = mouse_response_trial.time[0];
            }
            selected_option = mouse_response_trial.clicked_name[0];
            if ((selected_option === correct_response_name)) {
                is_correct = 1;
            }
        }
    }
    psychoJS.experiment.addData("ANALYSIS_Lamina_ID", identificator);
    psychoJS.experiment.addData("ANALYSIS_CR", is_correct);
    psychoJS.experiment.addData("ANALYSIS_RT", util.round(rt_value, 3));
    psychoJS.experiment.addData("ANALYSIS_Response_Method", response_method);
    psychoJS.experiment.addData("ANALYSIS_Selected_Option", selected_option);
    psychoJS.experiment.addData("ANALYSIS_Target_Component", correct_response_name);
    
    // the Routine "trialFaceRecognition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pauseMaxDurationReached;
var maxDurationReached;
var pauseMaxDuration;
var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pause' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    pauseClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    pauseMaxDurationReached = false;
    // update component parameters for each repeat
    // skip this Routine if its 'Skip if' condition is True
    continueRoutine = continueRoutine && !((block1Trials.thisTrialN == (block1Trials.nTotal - 1)));
    maxDurationReached = false
    pauseMaxDuration = 1
    // keep track of which components have finished
    pauseComponents = [];
    
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pause' ---
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > pauseMaxDuration) {
        pauseMaxDurationReached = true
        continueRoutine = false
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pause' ---
    for (const thisComponent of pauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (routineForceEnded) {
        routineTimer.reset();} else if (pauseMaxDurationReached) {
        pauseClock.add(pauseMaxDuration);
    } else {
        pauseClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var finalRoutineMaxDurationReached;
var finalRoutineMaxDuration;
var finalRoutineComponents;
function finalRoutineRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'finalRoutine' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    finalRoutineClock.reset();
    routineTimer.reset();
    finalRoutineMaxDurationReached = false;
    // update component parameters for each repeat
    finalRoutineMaxDuration = 2
    // keep track of which components have finished
    finalRoutineComponents = [];
    finalRoutineComponents.push(text);
    
    for (const thisComponent of finalRoutineComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function finalRoutineRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'finalRoutine' ---
    // get current time
    t = finalRoutineClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > finalRoutineMaxDuration) {
        finalRoutineMaxDurationReached = true
        continueRoutine = false
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of finalRoutineComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function finalRoutineRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'finalRoutine' ---
    for (const thisComponent of finalRoutineComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "finalRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
