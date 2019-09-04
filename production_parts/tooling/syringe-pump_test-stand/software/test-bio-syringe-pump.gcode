; This gcode is was formulated for production use with a Syringe Pump Test Stand for LulzBot Bio
; Use of this gcode outside of the testing process may result in damage or unexpected behavior
M75           ;start print timer
G112          ;home syringe pump carriage 
M400          ;wait for moves to finish
G1 E60 F120   ;move syringe pump carriage to bottom travel limit
M400          ;wait for moves to finish
G112          ;home syringe pump carriage 
M400          ;wait for moves to finish
M77           ;end print timer
