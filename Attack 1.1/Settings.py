from pygame.locals import *
Record = True # Do you want to record every match?
Difficulty = 0 # 0 - Easy ; 1 - Medium ; 2 - Hard.
RK = [[K_F1,K_F2,K_F3,K_F4,K_F5],\
      [K_1 ,K_2 ,K_3 ,K_4 ,K_5 ],\
      [K_q ,K_w ,K_e ,K_r ,K_t ],\
      [K_a ,K_s ,K_d ,K_f ,K_g ],\
      [K_z ,K_x ,K_c ,K_v ,K_b ]]
RConfirm = K_LSHIFT
RClear   = K_LCTRL
# 红方键位
BK = [[K_F8,K_F9,K_F10,K_F11,K_F12],\
      [K_8,K_9,K_0,K_MINUS,K_EQUALS],\
      [K_i,K_o,K_p,K_LEFTBRACKET,K_RIGHTBRACKET],\
      [K_j,K_k,K_l,K_SEMICOLON,K_QUOTE],\
      [K_n,K_m,K_COMMA,K_PERIOD,K_SLASH]]
BConfirm = K_RSHIFT
BClear   = K_RCTRL
# 蓝方键位
PVPtutorial = True # Do you want to see tutorial when playing PVP game?
