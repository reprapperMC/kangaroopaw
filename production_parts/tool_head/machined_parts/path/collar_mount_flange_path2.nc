(Exported by FreeCAD)
(Post Processor: linuxcnc_post)
(Output Time:2019-05-30 11:04:36.366226)
(begin preamble)
G17 G54 G40 G49 G80 G90
G21
M8
(begin operation: T6: 4mm Endmill)
(machine: not set, mm/min)
(T6: 4mm Endmill)
M6 T6 G43 H6
M3 S3000
(finish operation: T6: 4mm Endmill)
(begin operation: Profile_Edges)
(machine: not set, mm/min)
(Profile_Edges)
(Compensated Tool Path. Diameter: 4.0)
G0 Z5.000
G0 X15.150 Y1.995
G0 Z3.000
G1 X15.150 Y1.995 Z-0.200 F12.000
G1 X15.150 Y-27.694 Z-0.200 F180.000
G1 X14.650 Y-27.694 Z-0.200 F180.000
G1 X14.650 Y1.995 Z-0.200 F180.000
G1 X15.150 Y1.995 Z-0.200 F180.000
G1 X15.150 Y1.995 Z-0.400 F12.000
G1 X15.150 Y-27.694 Z-0.400 F180.000
G1 X14.650 Y-27.694 Z-0.400 F180.000
G1 X14.650 Y1.995 Z-0.400 F180.000
G1 X15.150 Y1.995 Z-0.400 F180.000
G1 X15.150 Y1.995 Z-0.600 F12.000
G1 X15.150 Y-27.694 Z-0.600 F180.000
G1 X14.650 Y-27.694 Z-0.600 F180.000
G1 X14.650 Y1.995 Z-0.600 F180.000
G1 X15.150 Y1.995 Z-0.600 F180.000
G1 X15.150 Y1.995 Z-0.800 F12.000
G1 X15.150 Y-27.694 Z-0.800 F180.000
G1 X14.650 Y-27.694 Z-0.800 F180.000
G1 X14.650 Y1.995 Z-0.800 F180.000
G1 X15.150 Y1.995 Z-0.800 F180.000
G1 X15.150 Y1.995 Z-1.000 F12.000
G1 X15.150 Y-27.694 Z-1.000 F180.000
G1 X14.650 Y-27.694 Z-1.000 F180.000
G1 X14.650 Y1.995 Z-1.000 F180.000
G1 X15.150 Y1.995 Z-1.000 F180.000
G0 Z5.000
(finish operation: Profile_Edges)
(begin postamble)
M05
G17 G54 G90 G80 G40
M2
