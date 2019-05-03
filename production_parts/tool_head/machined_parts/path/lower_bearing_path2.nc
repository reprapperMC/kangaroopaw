(Exported by FreeCAD)
(Post Processor: linuxcnc_post)
(Output Time:2019-04-18 12:28:32.455955)
(begin preamble)
G17 G54 G40 G49 G80 G90
G21
(begin operation: T17: 1/16"drill)
(machine: not set, mm/min)
(T17: 1/16"drill)
M6 T17 G43 H17
M3 S800
(finish operation: T17: 1/16"drill)
(begin operation: Drilling)
(machine: not set, mm/min)
(Drilling)
(Begin Drilling)
G0 Z6.000
G90
G98
G83 X1.705 Y-11.605 Z-8.000 F60.000 Q0.200 R3.000
G83 X5.705 Y-11.605 Z-8.000 F60.000 Q0.200 R3.000
G80
G0 Z6.000
(finish operation: Drilling)
(begin postamble)
M05
G17 G54 G90 G80 G40
M2
