######################################
#PySigil
#Written by Andy P. (Icy_Viking)
#Python 3.8.4
#Sigil 0.9.0
#Icy Viking Games
#Sigil wrapper for Python
#####################################

#import ctype
import ctypes

#sigil constants
SL_ALIGN_CENTER = 0
SL_ALIGN_RIGHT = 1
SL_ALIGN_LEFT = 2

#sigil key constants
SL_KEY_ESCAPE = 256
SL_KEY_ENTER = 257
SL_KEY_TAB = 258
SL_KEY_BACKSPACE = 259
SL_KEY_INSERT = 260
SL_KEY_DELETE = 261
SL_KEY_RIGHT = 262
SL_KEY_LEFT = 263
SL_KEY_DOWN = 264
SL_KEY_UP = 265
SL_KEY_PAGE_UP = 266
SL_KEY_PAGE_DOWN = 267
SL_KEY_HOME = 268
SL_KEY_END = 269
SL_KEY_CAPS_LOCK = 280
SL_KEY_SCROLL_LOCK = 281
SL_KEY_NUM_LOCK = 282
SL_KEY_PRINT_SCREEN = 283
SL_KEY_PAUSE = 284
SL_KEY_F1 = 290
SL_KEY_F2 = 291
SL_KEY_F3 = 292
SL_KEY_F4 = 293
SL_KEY_F5 = 294
SL_KEY_F6 = 295
SL_KEY_F7 = 296
SL_KEY_F8 = 297
SL_KEY_F9 = 298
SL_KEY_F10 = 299
SL_KEY_F11 = 300
SL_KEY_F12 = 301
SL_KEY_F13 = 302
SL_KEY_F14 = 303
SL_KEY_F15 = 304
SL_KEY_F16 = 305
SL_KEY_F17 = 306
SL_KEY_F18 = 307
SL_KEY_F19 = 308
SL_KEY_F20 = 309
SL_KEY_F21 = 310
SL_KEY_F22 = 311
SL_KEY_F23 = 312
SL_KEY_F24 = 313
SL_KEY_F25 = 314
SL_KEY_KEYPAD_0 = 320
SL_KEY_KEYPAD_1 = 321
SL_KEY_KEYPAD_2 = 322
SL_KEY_KEYPAD_3 = 323
SL_KEY_KEYPAD_4 = 324
SL_KEY_KEYPAD_5 = 325
SL_KEY_KEYPAD_6 = 326
SL_KEY_KEYPAD_7 = 327
SL_KEY_KEYPAD_8 = 328
SL_KEY_KEYPAD_9 = 329
SL_KEY_KEYPAD_DECIMAL = 330
SL_KEY_KEYPAD_DIVIDE = 331
SL_KEY_KEYPAD_MULTIPLY = 332
SL_KEY_KEYPAD_SUBTRACT = 333
SL_KEY_KEYPAD_ADD = 334
SL_KEY_KEYPAD_ENTER = 335
SL_KEY_KEYPAD_EQUAL = 336
SL_KEY_LEFT_SHIFT = 340
SL_KEY_LEFT_CONTROL = 341
SL_KEY_LEFT_ALT = 342
SL_KEY_LEFT_SUPER = 343
SL_KEY_RIGHT_SHIFT = 344
SL_KEY_RIGHT_CONTROL = 345
SL_KEY_RIGHT_ALT = 346
SL_KEY_RIGHT_SUPER = 347

#sigil mouse buttons
SL_MOUSE_BUTTON_1 = 0
SL_MOUSE_BUTTON_2 = 1
SL_MOUSE_BUTTON_3 = 2
SL_MOUSE_BUTTON_4 = 3
SL_MOUSE_BUTTON_5 = 4
SL_MOUSE_BUTTON_6 = 5
SL_MOUSE_BUTTON_7 = 6
SL_MOUSE_BUTTON_8 = 7
SL_MOUSE_BUTTON_LEFT = SL_MOUSE_BUTTON_1
SL_MOUSE_BUTTON_RIGHT = SL_MOUSE_BUTTON_2
SL_MOUSE_BUTTON_MIDDLE = SL_MOUSE_BUTTON_3

#load sigil library
sigil = ctypes.cdll.LoadLibrary('Path to 32-bit sigil DLL') #changed for security reasons. 
#simply change this to the path where the sigil DLL resides. 

#sigil init functions
slWindow = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int,ctypes.c_int,ctypes.c_char_p,ctypes.c_int)
slShowCursor = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
slClose = ctypes.CFUNCTYPE(ctypes.c_void_p)
slShouldClose = ctypes.CFUNCTYPE(ctypes.c_int)

#sigil key functions
slGetKey = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

#sigil mouse functions
slGetMouseButton = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
slGetMouseX = ctypes.CFUNCTYPE(ctypes.c_int)
slGetMouseY = ctypes.CFUNCTYPE(ctypes.c_int)

#sigil time functions
slGetDeltaTime = ctypes.CFUNCTYPE(ctypes.c_double)
slGetTime = ctypes.CFUNCTYPE(ctypes.c_double)

#sigil render functions
slRender = ctypes.CFUNCTYPE(ctypes.c_void_p)

#sigil color functions
slSetBackColor = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double)
slSetForeColor = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

#sigil blendinf function
slSetAdditiveBlend = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)

#sigil transformation functions
slPush = ctypes.CFUNCTYPE(ctypes.c_void_p)
slPop = ctypes.CFUNCTYPE(ctypes.c_void_p)

slTranslate = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double)
slRotate = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double)
slScale = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double)

#sigil texture loading
slLoadTexture = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p)

#sigil sound functions
slLoadWAV = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p)
slSoundPlay = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
slSoundLoop = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
slSoundPause = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
slSoundStop = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
slSoundPauseAll = ctypes.CFUNCTYPE(ctypes.c_void_p)
slSoundResumeAll = ctypes.CFUNCTYPE(ctypes.c_void_p)
slSoundStopAll = ctypes.CFUNCTYPE(ctypes.c_void_p)
slSoundPlaying = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
slSoundLooping = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

#sigil shape functions
slTriangleFill = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)
slTriangleOutline = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

slRectangleFill = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)
slRectangleOutline = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

slCircleFill = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_int)
slCircleOutline = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_int)

slSemiCircleFill = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double)
slSemiCircleOutline = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_int,ctypes.c_double)

slPoint = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double)

slLine = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

slSetSpriteTiling = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double)
slSetSpriteScroll = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double)
slSprite = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

#sigil text functions
slSetTextAlign = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
slGetTextWidth = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_char_p)
slGetTextHeight = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_char_p)
slLoadFont = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_char_p)
slSetFont = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int,ctypes.c_int)
slSetFontSize = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_int)
slText = ctypes.CFUNCTYPE(ctypes.c_void_p,ctypes.c_double,ctypes.c_double,ctypes.c_char_p)

#sigil example

sigil.slWindow(800,600,b"Hello World",0)

while not sigil.slShouldClose() :

   if sigil.slGetKey(SL_KEY_ESCAPE) :
       sigil.slClose()
       
   sigil.slRender()

sigil.slClose()
