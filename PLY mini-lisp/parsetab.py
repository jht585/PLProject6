
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '4526C71606710A3D3491B70259092D49'
    
_lr_action_items = {'FALSE':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,33,],[5,-24,-20,-23,-17,-19,-18,-22,-6,5,5,-12,5,-13,-11,-14,-7,-15,]),'NIL':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,33,],[2,-24,-20,-23,-17,-19,-18,-22,-6,2,2,-12,2,-13,-11,-14,-7,-15,]),'TEXT':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,33,],[4,-24,-20,-23,-17,-19,-18,-22,-6,4,4,-12,4,-13,-11,-14,-7,-15,]),'SIMB':([0,2,4,5,6,7,9,12,13,14,15,17,19,21,22,23,24,25,26,30,33,],[6,-24,-20,-23,-17,-19,17,-18,-22,-6,6,6,-12,6,-13,17,-11,-14,32,-7,-15,]),'NUM':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,32,33,],[7,-24,-20,-23,-17,-19,-18,-22,-6,7,7,-12,7,-13,-11,-14,-7,35,-15,]),'LET':([9,],[16,]),'LPAREN':([0,2,4,5,6,7,8,12,13,14,15,16,17,18,19,21,22,24,25,30,33,36,],[9,-24,-20,-23,-17,-19,15,-18,-22,-6,23,26,23,23,-12,23,-13,-11,-14,-7,-15,-16,]),'QUOTE':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,33,],[8,-24,-20,-23,-17,-19,-18,-22,-6,8,8,-12,8,-13,-11,-14,-7,-15,]),'RPAREN':([2,4,5,6,7,12,13,14,15,17,18,19,20,21,22,24,25,27,29,30,31,33,35,36,],[-24,-20,-23,-17,-19,-18,-22,-6,-10,-10,28,-12,30,-10,-13,-11,-9,33,34,-7,-8,-15,36,-16,]),'TRUE':([0,2,4,5,6,7,12,13,14,15,17,19,21,22,24,25,30,33,],[13,-24,-20,-23,-17,-19,-18,-22,-6,13,13,-12,13,-13,-11,-14,-7,-15,]),'$end':([0,1,2,3,4,5,6,7,10,11,12,13,14,28,30,33,34,],[-21,0,-24,-2,-20,-23,-17,-19,-1,-3,-18,-22,-6,-5,-7,-15,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'let':([9,],[18,]),'quoted_list':([0,15,17,21,],[3,19,19,19,]),'items':([15,17,21,],[20,27,31,]),'list':([8,],[14,]),'item':([15,17,21,],[21,21,21,]),'call':([0,15,17,18,21,],[11,22,22,29,22,]),'exp':([0,],[1,]),'atom':([0,15,17,21,],[10,24,24,24,]),'bool':([0,15,17,21,],[12,12,12,12,]),'empty':([15,17,21,],[25,25,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',158),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',162),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',166),
  ('exp -> LPAREN let call RPAREN','exp',4,'p_exp_let_ass','yacc.py',171),
  ('exp -> LPAREN let RPAREN','exp',3,'p_exp_let','yacc.py',176),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',181),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',185),
  ('items -> item items','items',2,'p_items','yacc.py',189),
  ('items -> empty','items',1,'p_items_empty','yacc.py',193),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',197),
  ('item -> atom','item',1,'p_item_atom','yacc.py',201),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',209),
  ('item -> call','item',1,'p_item_call','yacc.py',213),
  ('item -> empty','item',1,'p_item_empty','yacc.py',217),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',221),
  ('let -> LET LPAREN SIMB NUM RPAREN','let',5,'p_let','yacc.py',226),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',231),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',235),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',239),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',243),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',247),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',251),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',255),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',259),
]
