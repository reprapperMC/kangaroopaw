(Exported by FreeCAD)
(Post Processor: linuxcnc_post)
(Output Time:2019-04-25 13:49:58.810653)
(begin preamble)
G17 G54 G40 G49 G80 G90
G21
M8
(begin operation: T17: 1/16"drill)
(machine: not set, mm/min)
(T17: 1/16"drill)
M6 T17 G43 H17
M3 S3000
(finish operation: T17: 1/16"drill)
(begin operation: Drilling)
(machine: not set, mm/min)
(Drilling)
(Begin Drilling)
G0 Z5.000
G90
G98
G83 X-2.827 Y-2.488 Z-4.000 F60.000 Q0.100 R3.000
G83 X-9.827 Y-2.488 Z-4.000 F60.000 Q0.100 R3.000
G80
G0 Z5.000
(finish operation: Drilling)
(begin postamble)
M05
G17 G54 G90 G80 G40
M2
