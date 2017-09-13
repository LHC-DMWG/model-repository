# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Mon 11 Sep 2017 14:35:05


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_422_156,(0,0,1):C.R2GC_422_157})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_339_101,(2,0,1):C.R2GC_339_102,(0,0,0):C.R2GC_339_101,(0,0,1):C.R2GC_339_102,(4,0,0):C.R2GC_337_97,(4,0,1):C.R2GC_337_98,(3,0,0):C.R2GC_337_97,(3,0,1):C.R2GC_337_98,(8,0,0):C.R2GC_338_99,(8,0,1):C.R2GC_338_100,(7,0,0):C.R2GC_343_108,(7,0,1):C.R2GC_427_163,(6,0,0):C.R2GC_342_106,(6,0,1):C.R2GC_428_164,(5,0,0):C.R2GC_337_97,(5,0,1):C.R2GC_337_98,(1,0,0):C.R2GC_337_97,(1,0,1):C.R2GC_337_98,(11,3,0):C.R2GC_341_104,(11,3,1):C.R2GC_341_105,(10,3,0):C.R2GC_341_104,(10,3,1):C.R2GC_341_105,(9,3,1):C.R2GC_340_103,(2,1,0):C.R2GC_339_101,(2,1,1):C.R2GC_339_102,(0,1,0):C.R2GC_339_101,(0,1,1):C.R2GC_339_102,(6,1,0):C.R2GC_424_159,(6,1,1):C.R2GC_424_160,(4,1,0):C.R2GC_337_97,(4,1,1):C.R2GC_337_98,(3,1,0):C.R2GC_337_97,(3,1,1):C.R2GC_337_98,(8,1,0):C.R2GC_338_99,(8,1,1):C.R2GC_426_162,(7,1,0):C.R2GC_343_108,(7,1,1):C.R2GC_343_109,(5,1,0):C.R2GC_337_97,(5,1,1):C.R2GC_337_98,(1,1,0):C.R2GC_337_97,(1,1,1):C.R2GC_337_98,(2,2,0):C.R2GC_339_101,(2,2,1):C.R2GC_339_102,(0,2,0):C.R2GC_339_101,(0,2,1):C.R2GC_339_102,(4,2,0):C.R2GC_337_97,(4,2,1):C.R2GC_337_98,(3,2,0):C.R2GC_337_97,(3,2,1):C.R2GC_337_98,(8,2,0):C.R2GC_338_99,(8,2,1):C.R2GC_423_158,(6,2,0):C.R2GC_342_106,(6,2,1):C.R2GC_342_107,(7,2,0):C.R2GC_425_161,(7,2,1):C.R2GC_339_102,(5,2,0):C.R2GC_337_97,(5,2,1):C.R2GC_337_98,(1,2,0):C.R2GC_337_97,(1,2,1):C.R2GC_337_98})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_437_169,(0,1,0):C.R2GC_440_172})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_400_141,(0,1,0):C.R2GC_397_138})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_413_148,(0,1,0):C.R2GC_416_151})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.d__tilde__, P.u, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_440_172,(0,1,0):C.R2GC_437_169})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.s__tilde__, P.c, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_397_138,(0,1,0):C.R2GC_400_141})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_416_151,(0,1,0):C.R2GC_413_148})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_436_168,(0,1,0):C.R2GC_438_170})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_398_139,(0,1,0):C.R2GC_396_137})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_412_147,(0,1,0):C.R2GC_414_149})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_384_130})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_399_140})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_362_117})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_439_171})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_373_124})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_415_150})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_438_170,(0,1,0):C.R2GC_436_168})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_396_137,(0,1,0):C.R2GC_398_139})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_414_149,(0,1,0):C.R2GC_412_147})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_441_173})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_442_174})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_443_175})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_444_176})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_374_125})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_375_126})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_376_127})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_377_128})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_417_152})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_418_153})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_419_154})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_420_155})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_385_131})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_386_132})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_387_133})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_388_134})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_401_142})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_402_143})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_403_144})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_404_145})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_363_118})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_364_119})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_365_120})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_366_121})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_346_112})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_346_112})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_346_112})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_434_166,(0,1,0):C.R2GC_435_167})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_371_123,(0,1,0):C.R2GC_361_116})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_371_123,(0,1,0):C.R2GC_361_116})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_344_110})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_344_110})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_344_110})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_111})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_393_136})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_360_115,(0,1,0):C.R2GC_361_116})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_360_115,(0,1,0):C.R2GC_361_116})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_360_115,(0,1,0):C.R2GC_361_116})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_432_165,(0,1,0):C.R2GC_356_113})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_370_122,(0,1,0):C.R2GC_356_113})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_408_146,(0,1,0):C.R2GC_356_113})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_381_129,(0,1,0):C.R2GC_356_113})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_392_135,(0,1,0):C.R2GC_356_113})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_359_114,(0,1,0):C.R2GC_356_113})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,2,4):C.R2GC_310_1,(0,0,0):C.R2GC_314_7,(0,0,2):C.R2GC_314_8,(0,0,3):C.R2GC_314_9,(0,0,5):C.R2GC_314_10,(0,0,6):C.R2GC_314_11,(0,0,7):C.R2GC_314_12,(0,1,1):C.R2GC_311_2})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_319_21,(0,0,1):C.R2GC_319_22,(0,0,2):C.R2GC_319_23,(0,0,3):C.R2GC_319_24,(0,0,4):C.R2GC_319_25,(0,0,5):C.R2GC_319_26})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_320_27,(0,0,1):C.R2GC_320_28,(0,0,2):C.R2GC_320_29,(0,0,3):C.R2GC_320_30,(0,0,4):C.R2GC_320_31,(0,0,5):C.R2GC_320_32})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_330_87})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_315_13,(0,0,1):C.R2GC_315_14})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_318_19,(0,0,1):C.R2GC_318_20})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_312_3,(0,0,1):C.R2GC_312_4})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_317_17,(1,0,1):C.R2GC_317_18,(0,1,0):C.R2GC_316_15,(0,1,1):C.R2GC_316_16})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_313_5,(0,0,1):C.R2GC_313_6})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_321_33,(0,0,1):C.R2GC_321_34,(0,0,2):C.R2GC_321_35,(0,0,3):C.R2GC_321_36,(0,0,4):C.R2GC_321_37,(0,0,5):C.R2GC_321_38})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_331_88,(0,0,1):C.R2GC_331_89,(0,0,2):C.R2GC_331_90})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_333_94,(0,0,1):C.R2GC_333_95,(0,0,2):C.R2GC_333_96})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.g, P.G__plus__, P.h__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_333_94,(0,0,1):C.R2GC_333_95,(0,0,2):C.R2GC_333_96})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.g, P.g, P.h__minus__, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_332_91,(0,0,1):C.R2GC_332_92,(0,0,2):C.R2GC_332_93})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.g, P.g, P.h1, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_322_39,(0,0,1):C.R2GC_322_40,(0,0,2):C.R2GC_322_41,(0,0,3):C.R2GC_322_42,(0,0,4):C.R2GC_322_43,(0,0,5):C.R2GC_322_44})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.g, P.g, P.h1, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_323_45,(0,0,1):C.R2GC_323_46,(0,0,2):C.R2GC_323_47,(0,0,3):C.R2GC_323_48,(0,0,4):C.R2GC_323_49,(0,0,5):C.R2GC_323_50})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.g, P.g, P.h2, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_324_51,(0,0,1):C.R2GC_324_52,(0,0,2):C.R2GC_324_53,(0,0,3):C.R2GC_324_54,(0,0,4):C.R2GC_324_55,(0,0,5):C.R2GC_324_56})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_325_57,(0,0,1):C.R2GC_325_58,(0,0,2):C.R2GC_325_59,(0,0,3):C.R2GC_325_60,(0,0,4):C.R2GC_325_61,(0,0,5):C.R2GC_325_62})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.g, P.g, P.h3, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_326_63,(0,0,1):C.R2GC_326_64,(0,0,2):C.R2GC_326_65,(0,0,3):C.R2GC_326_66,(0,0,4):C.R2GC_326_67,(0,0,5):C.R2GC_326_68})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_327_69,(0,0,1):C.R2GC_327_70,(0,0,2):C.R2GC_327_71,(0,0,3):C.R2GC_327_72,(0,0,4):C.R2GC_327_73,(0,0,5):C.R2GC_327_74})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.g, P.g, P.h3, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_328_75,(0,0,1):C.R2GC_328_76,(0,0,2):C.R2GC_328_77,(0,0,3):C.R2GC_328_78,(0,0,4):C.R2GC_328_79,(0,0,5):C.R2GC_328_80})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.g, P.h4, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_329_81,(0,0,1):C.R2GC_329_82,(0,0,2):C.R2GC_329_83,(0,0,3):C.R2GC_329_84,(0,0,4):C.R2GC_329_85,(0,0,5):C.R2GC_329_86})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_422_118,(0,1,1):C.UVGC_422_119,(0,1,2):C.UVGC_422_120,(0,1,5):C.UVGC_422_121,(0,1,6):C.UVGC_422_122,(0,1,7):C.UVGC_422_123,(0,2,3):C.UVGC_334_1,(0,0,4):C.UVGC_335_2})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,4):C.UVGC_338_8,(2,0,5):C.UVGC_338_7,(0,0,4):C.UVGC_338_8,(0,0,5):C.UVGC_338_7,(4,0,4):C.UVGC_337_5,(4,0,5):C.UVGC_337_6,(3,0,4):C.UVGC_337_5,(3,0,5):C.UVGC_337_6,(8,0,4):C.UVGC_338_7,(8,0,5):C.UVGC_338_8,(7,0,0):C.UVGC_427_150,(7,0,2):C.UVGC_427_151,(7,0,3):C.UVGC_427_152,(7,0,4):C.UVGC_427_153,(7,0,5):C.UVGC_427_154,(7,0,6):C.UVGC_427_155,(7,0,7):C.UVGC_427_156,(7,0,8):C.UVGC_427_157,(6,0,0):C.UVGC_427_150,(6,0,2):C.UVGC_427_151,(6,0,3):C.UVGC_427_152,(6,0,4):C.UVGC_428_158,(6,0,5):C.UVGC_428_159,(6,0,6):C.UVGC_427_155,(6,0,7):C.UVGC_427_156,(6,0,8):C.UVGC_427_157,(5,0,4):C.UVGC_337_5,(5,0,5):C.UVGC_337_6,(1,0,4):C.UVGC_337_5,(1,0,5):C.UVGC_337_6,(11,3,4):C.UVGC_341_11,(11,3,5):C.UVGC_341_12,(10,3,4):C.UVGC_341_11,(10,3,5):C.UVGC_341_12,(9,3,4):C.UVGC_340_9,(9,3,5):C.UVGC_340_10,(2,1,4):C.UVGC_338_8,(2,1,5):C.UVGC_338_7,(0,1,4):C.UVGC_338_8,(0,1,5):C.UVGC_338_7,(6,1,0):C.UVGC_424_132,(6,1,2):C.UVGC_424_133,(6,1,3):C.UVGC_424_134,(6,1,4):C.UVGC_424_135,(6,1,5):C.UVGC_424_136,(6,1,6):C.UVGC_424_137,(6,1,7):C.UVGC_424_138,(6,1,8):C.UVGC_424_139,(4,1,4):C.UVGC_337_5,(4,1,5):C.UVGC_337_6,(3,1,4):C.UVGC_337_5,(3,1,5):C.UVGC_337_6,(8,1,0):C.UVGC_426_142,(8,1,2):C.UVGC_426_143,(8,1,3):C.UVGC_426_144,(8,1,4):C.UVGC_426_145,(8,1,5):C.UVGC_426_146,(8,1,6):C.UVGC_426_147,(8,1,7):C.UVGC_426_148,(8,1,8):C.UVGC_426_149,(7,1,1):C.UVGC_342_13,(7,1,4):C.UVGC_343_15,(7,1,5):C.UVGC_343_16,(5,1,4):C.UVGC_337_5,(5,1,5):C.UVGC_337_6,(1,1,4):C.UVGC_337_5,(1,1,5):C.UVGC_337_6,(2,2,4):C.UVGC_338_8,(2,2,5):C.UVGC_338_7,(0,2,4):C.UVGC_338_8,(0,2,5):C.UVGC_338_7,(4,2,4):C.UVGC_337_5,(4,2,5):C.UVGC_337_6,(3,2,4):C.UVGC_337_5,(3,2,5):C.UVGC_337_6,(8,2,0):C.UVGC_423_124,(8,2,2):C.UVGC_423_125,(8,2,3):C.UVGC_423_126,(8,2,4):C.UVGC_423_127,(8,2,5):C.UVGC_423_128,(8,2,6):C.UVGC_423_129,(8,2,7):C.UVGC_423_130,(8,2,8):C.UVGC_423_131,(6,2,1):C.UVGC_342_13,(6,2,4):C.UVGC_342_14,(6,2,5):C.UVGC_340_9,(7,2,0):C.UVGC_424_132,(7,2,2):C.UVGC_424_133,(7,2,3):C.UVGC_424_134,(7,2,4):C.UVGC_425_140,(7,2,5):C.UVGC_425_141,(7,2,6):C.UVGC_424_137,(7,2,7):C.UVGC_424_138,(7,2,8):C.UVGC_424_139,(5,2,4):C.UVGC_337_5,(5,2,5):C.UVGC_337_6,(1,2,4):C.UVGC_337_5,(1,2,5):C.UVGC_337_6})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_437_171,(0,0,2):C.UVGC_437_172,(0,0,1):C.UVGC_437_173,(0,1,0):C.UVGC_440_178,(0,1,2):C.UVGC_440_179,(0,1,1):C.UVGC_440_180})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_400_80,(0,0,2):C.UVGC_400_81,(0,0,1):C.UVGC_400_82,(0,1,0):C.UVGC_397_73,(0,1,2):C.UVGC_397_74,(0,1,1):C.UVGC_397_75})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_413_98,(0,0,2):C.UVGC_413_99,(0,0,1):C.UVGC_413_100,(0,1,0):C.UVGC_416_105,(0,1,2):C.UVGC_416_106,(0,1,1):C.UVGC_416_107})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_440_178,(0,0,2):C.UVGC_440_179,(0,0,1):C.UVGC_440_180,(0,1,0):C.UVGC_437_171,(0,1,2):C.UVGC_437_172,(0,1,1):C.UVGC_437_173})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_397_73,(0,0,2):C.UVGC_397_74,(0,0,1):C.UVGC_397_75,(0,1,0):C.UVGC_400_80,(0,1,2):C.UVGC_400_81,(0,1,1):C.UVGC_400_82})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_416_105,(0,0,2):C.UVGC_416_106,(0,0,1):C.UVGC_416_107,(0,1,0):C.UVGC_413_98,(0,1,2):C.UVGC_413_99,(0,1,1):C.UVGC_413_100})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_436_168,(0,0,2):C.UVGC_436_169,(0,0,1):C.UVGC_436_170,(0,1,0):C.UVGC_438_174,(0,1,2):C.UVGC_438_175,(0,1,1):C.UVGC_438_176})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_398_76,(0,0,2):C.UVGC_398_77,(0,0,1):C.UVGC_398_78,(0,1,0):C.UVGC_396_70,(0,1,2):C.UVGC_396_71,(0,1,1):C.UVGC_396_72})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_412_95,(0,0,2):C.UVGC_412_96,(0,0,1):C.UVGC_412_97,(0,1,0):C.UVGC_414_101,(0,1,2):C.UVGC_414_102,(0,1,1):C.UVGC_414_103})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_384_56})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_399_79})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_362_34})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_439_177})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_373_45})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_415_104})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_438_174,(0,0,2):C.UVGC_438_175,(0,0,1):C.UVGC_438_176,(0,1,0):C.UVGC_436_168,(0,1,2):C.UVGC_436_169,(0,1,1):C.UVGC_436_170})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_396_70,(0,0,2):C.UVGC_396_71,(0,0,1):C.UVGC_396_72,(0,1,0):C.UVGC_398_76,(0,1,2):C.UVGC_398_77,(0,1,1):C.UVGC_398_78})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_414_101,(0,0,2):C.UVGC_414_102,(0,0,1):C.UVGC_414_103,(0,1,0):C.UVGC_412_95,(0,1,2):C.UVGC_412_96,(0,1,1):C.UVGC_412_97})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_441_181})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_442_182})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_443_183})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_444_184})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_374_46})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_375_47})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_376_48})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_377_49})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_417_108})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_418_109})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_419_110})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_420_111})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_385_57})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_386_58})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_387_59})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_388_60})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_401_83})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_402_84})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_403_85})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_404_86})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_363_35})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_364_36})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_365_37})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_366_38})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_346_19,(0,1,0):C.UVGC_430_161,(0,2,0):C.UVGC_430_161})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_346_19,(0,1,0):C.UVGC_368_40,(0,2,0):C.UVGC_368_40})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_346_19,(0,1,0):C.UVGC_406_88,(0,2,0):C.UVGC_406_88})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,1):C.UVGC_358_23,(0,1,2):C.UVGC_358_24,(0,1,3):C.UVGC_358_25,(0,1,4):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,5):C.UVGC_431_162,(0,2,0):C.UVGC_358_22,(0,2,1):C.UVGC_358_23,(0,2,2):C.UVGC_358_24,(0,2,3):C.UVGC_358_25,(0,2,4):C.UVGC_358_26,(0,2,6):C.UVGC_358_27,(0,2,7):C.UVGC_358_28,(0,2,8):C.UVGC_358_29,(0,2,5):C.UVGC_431_162})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,1):C.UVGC_358_23,(0,1,3):C.UVGC_358_24,(0,1,4):C.UVGC_358_25,(0,1,5):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,2):C.UVGC_369_41,(0,2,0):C.UVGC_358_22,(0,2,1):C.UVGC_358_23,(0,2,3):C.UVGC_358_24,(0,2,4):C.UVGC_358_25,(0,2,5):C.UVGC_358_26,(0,2,6):C.UVGC_358_27,(0,2,7):C.UVGC_358_28,(0,2,8):C.UVGC_358_29,(0,2,2):C.UVGC_369_41})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,1):C.UVGC_358_23,(0,1,2):C.UVGC_358_24,(0,1,3):C.UVGC_358_25,(0,1,4):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,5):C.UVGC_407_89,(0,2,0):C.UVGC_358_22,(0,2,1):C.UVGC_358_23,(0,2,2):C.UVGC_358_24,(0,2,3):C.UVGC_358_25,(0,2,4):C.UVGC_358_26,(0,2,6):C.UVGC_358_27,(0,2,7):C.UVGC_358_28,(0,2,8):C.UVGC_358_29,(0,2,5):C.UVGC_407_89})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_433_164,(0,0,2):C.UVGC_433_165,(0,0,1):C.UVGC_393_67})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_393_65,(0,0,2):C.UVGC_393_66,(0,0,1):C.UVGC_393_67})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_409_91,(0,0,2):C.UVGC_409_92,(0,0,1):C.UVGC_393_67})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_434_166,(0,1,0):C.UVGC_435_167})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_371_43,(0,1,0):C.UVGC_372_44})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV6 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_410_93,(0,1,0):C.UVGC_411_94})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_344_17,(0,1,0):C.UVGC_379_51})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_344_17,(0,1,0):C.UVGC_390_62})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_344_17,(0,1,0):C.UVGC_357_21})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,1):C.UVGC_358_23,(0,1,2):C.UVGC_358_24,(0,1,4):C.UVGC_358_25,(0,1,5):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,3):C.UVGC_380_52})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,1):C.UVGC_358_23,(0,1,2):C.UVGC_358_24,(0,1,3):C.UVGC_358_25,(0,1,4):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,5):C.UVGC_391_63})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_345_18,(0,1,0):C.UVGC_358_22,(0,1,2):C.UVGC_358_23,(0,1,3):C.UVGC_358_24,(0,1,4):C.UVGC_358_25,(0,1,5):C.UVGC_358_26,(0,1,6):C.UVGC_358_27,(0,1,7):C.UVGC_358_28,(0,1,8):C.UVGC_358_29,(0,1,1):C.UVGC_358_30})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_433_164,(0,0,2):C.UVGC_433_165,(0,0,1):C.UVGC_393_67})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_393_65,(0,0,2):C.UVGC_393_66,(0,0,1):C.UVGC_393_67})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_409_91,(0,0,2):C.UVGC_409_92,(0,0,1):C.UVGC_393_67})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_382_54,(0,1,0):C.UVGC_383_55})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_394_68,(0,1,0):C.UVGC_395_69})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_360_32,(0,1,0):C.UVGC_361_33})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_432_163,(0,1,0):C.UVGC_429_160})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_370_42,(0,1,0):C.UVGC_367_39})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_408_90,(0,1,0):C.UVGC_405_87})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_381_53,(0,1,0):C.UVGC_378_50})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_392_64,(0,1,0):C.UVGC_389_61})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_359_31,(0,1,0):C.UVGC_356_20})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,1,0):C.UVGC_421_112,(0,1,1):C.UVGC_421_113,(0,1,2):C.UVGC_421_114,(0,1,5):C.UVGC_421_115,(0,1,6):C.UVGC_421_116,(0,1,7):C.UVGC_421_117,(0,0,3):C.UVGC_336_3,(0,0,4):C.UVGC_336_4})

