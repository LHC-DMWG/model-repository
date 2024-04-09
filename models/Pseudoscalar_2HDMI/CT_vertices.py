# This file was automatically created by FeynRules 2.3.43
# Mathematica version: 12.1.0 for Mac OS X x86 (64-bit) (March 14, 2020)
# Date: Wed 3 May 2023 19:36:57


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
               couplings = {(0,0,0):C.R2GC_409_158,(0,0,1):C.R2GC_409_159})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_325_99,(2,1,1):C.R2GC_325_100,(0,1,0):C.R2GC_325_99,(0,1,1):C.R2GC_325_100,(6,1,0):C.R2GC_328_104,(6,1,1):C.R2GC_415_166,(4,1,0):C.R2GC_323_95,(4,1,1):C.R2GC_323_96,(3,1,0):C.R2GC_323_95,(3,1,1):C.R2GC_323_96,(8,1,0):C.R2GC_324_97,(8,1,1):C.R2GC_324_98,(7,1,0):C.R2GC_329_106,(7,1,1):C.R2GC_414_165,(5,1,0):C.R2GC_323_95,(5,1,1):C.R2GC_323_96,(1,1,0):C.R2GC_323_95,(1,1,1):C.R2GC_323_96,(11,0,0):C.R2GC_327_102,(11,0,1):C.R2GC_327_103,(10,0,0):C.R2GC_327_102,(10,0,1):C.R2GC_327_103,(9,0,1):C.R2GC_326_101,(2,2,0):C.R2GC_325_99,(2,2,1):C.R2GC_325_100,(0,2,0):C.R2GC_325_99,(0,2,1):C.R2GC_325_100,(4,2,0):C.R2GC_323_95,(4,2,1):C.R2GC_323_96,(3,2,0):C.R2GC_323_95,(3,2,1):C.R2GC_323_96,(8,2,0):C.R2GC_324_97,(8,2,1):C.R2GC_413_164,(6,2,0):C.R2GC_411_161,(6,2,1):C.R2GC_411_162,(7,2,0):C.R2GC_329_106,(7,2,1):C.R2GC_329_107,(5,2,0):C.R2GC_323_95,(5,2,1):C.R2GC_323_96,(1,2,0):C.R2GC_323_95,(1,2,1):C.R2GC_323_96,(2,3,0):C.R2GC_325_99,(2,3,1):C.R2GC_325_100,(0,3,0):C.R2GC_325_99,(0,3,1):C.R2GC_325_100,(4,3,0):C.R2GC_323_95,(4,3,1):C.R2GC_323_96,(3,3,0):C.R2GC_323_95,(3,3,1):C.R2GC_323_96,(8,3,0):C.R2GC_324_97,(8,3,1):C.R2GC_410_160,(6,3,0):C.R2GC_328_104,(6,3,1):C.R2GC_328_105,(7,3,0):C.R2GC_412_163,(7,3,1):C.R2GC_325_100,(5,3,0):C.R2GC_323_95,(5,3,1):C.R2GC_323_96,(1,3,0):C.R2GC_323_95,(1,3,1):C.R2GC_323_96})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.d__tilde__, P.u, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_425_170,(0,1,0):C.R2GC_424_169})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.s__tilde__, P.c, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_383_137,(0,1,0):C.R2GC_384_138})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.h__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_400_148,(0,1,0):C.R2GC_399_147})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_424_169,(0,1,0):C.R2GC_425_170})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_384_138,(0,1,0):C.R2GC_383_137})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.h__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_399_147,(0,1,0):C.R2GC_400_148})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_423_168,(0,1,0):C.R2GC_428_173})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_387_141,(0,1,0):C.R2GC_382_136})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_398_146,(0,1,0):C.R2GC_403_151})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_370_129})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_388_142})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_348_115})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_428_173,(0,1,0):C.R2GC_423_168})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_382_136,(0,1,0):C.R2GC_387_141})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_403_151,(0,1,0):C.R2GC_398_146})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_429_174})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_359_123})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_404_152})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_430_175})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_431_176})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_426_171})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_427_172})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_360_124})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_361_125})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_362_126})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_363_127})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_405_153})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_406_154})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_401_149})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_402_150})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_371_130})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_372_131})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_373_132})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_374_133})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_389_143})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_390_144})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_385_139})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_386_140})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_349_116})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_350_117})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_351_118})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_352_119})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_332_110})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_332_110})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_332_110})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_330_108})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_330_108})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_330_108})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_331_109})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_379_135})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_357_121,(0,1,0):C.R2GC_358_122})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_357_121,(0,1,0):C.R2GC_358_122})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_357_121,(0,1,0):C.R2GC_358_122})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_346_113,(0,1,0):C.R2GC_347_114})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_346_113,(0,1,0):C.R2GC_347_114})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_346_113,(0,1,0):C.R2GC_347_114})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_419_167,(0,2,0):C.R2GC_419_167,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_356_120,(0,2,0):C.R2GC_356_120,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_394_145,(0,2,0):C.R2GC_394_145,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_367_128,(0,2,0):C.R2GC_367_128,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_378_134,(0,2,0):C.R2GC_378_134,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_345_112,(0,2,0):C.R2GC_345_112,(0,1,0):C.R2GC_342_111,(0,3,0):C.R2GC_342_111})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,4):C.R2GC_408_157,(0,1,0):C.R2GC_301_5,(0,1,2):C.R2GC_301_6,(0,1,3):C.R2GC_301_7,(0,1,5):C.R2GC_301_8,(0,1,6):C.R2GC_301_9,(0,1,7):C.R2GC_301_10,(0,2,1):C.R2GC_407_155,(0,2,4):C.R2GC_407_156})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_309_37,(0,0,1):C.R2GC_309_38,(0,0,2):C.R2GC_309_39,(0,0,3):C.R2GC_309_40,(0,0,4):C.R2GC_309_41,(0,0,5):C.R2GC_309_42})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_310_43,(0,0,1):C.R2GC_310_44,(0,0,2):C.R2GC_310_45,(0,0,3):C.R2GC_310_46,(0,0,4):C.R2GC_310_47,(0,0,5):C.R2GC_310_48})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_317_85,(0,1,0):C.R2GC_317_85,(0,2,0):C.R2GC_317_85})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_302_11,(0,0,1):C.R2GC_302_12,(0,1,0):C.R2GC_302_11,(0,1,1):C.R2GC_302_12,(0,2,0):C.R2GC_302_11,(0,2,1):C.R2GC_302_12})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_305_17,(0,0,1):C.R2GC_305_18,(0,1,0):C.R2GC_305_17,(0,1,1):C.R2GC_305_18,(0,2,0):C.R2GC_305_17,(0,2,1):C.R2GC_305_18})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_299_1,(0,0,1):C.R2GC_299_2,(0,1,0):C.R2GC_299_1,(0,1,1):C.R2GC_299_2,(0,2,0):C.R2GC_299_1,(0,2,1):C.R2GC_299_2})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_304_15,(1,0,1):C.R2GC_304_16,(0,1,0):C.R2GC_303_13,(0,1,1):C.R2GC_303_14,(0,2,0):C.R2GC_303_13,(0,2,1):C.R2GC_303_14,(0,3,0):C.R2GC_303_13,(0,3,1):C.R2GC_303_14})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_300_3,(0,0,1):C.R2GC_300_4,(0,1,0):C.R2GC_300_3,(0,1,1):C.R2GC_300_4,(0,2,0):C.R2GC_300_3,(0,2,1):C.R2GC_300_4})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_313_61,(0,0,1):C.R2GC_313_62,(0,0,2):C.R2GC_313_63,(0,0,3):C.R2GC_313_64,(0,0,4):C.R2GC_313_65,(0,0,5):C.R2GC_313_66})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_320_92,(0,0,1):C.R2GC_320_93,(0,0,2):C.R2GC_320_94})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_319_89,(0,0,1):C.R2GC_319_90,(0,0,2):C.R2GC_319_91})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.g, P.G__plus__, P.h__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_319_89,(0,0,1):C.R2GC_319_90,(0,0,2):C.R2GC_319_91})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.g, P.g, P.h__minus__, P.h__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.s] ], [ [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_318_86,(0,0,1):C.R2GC_318_87,(0,0,2):C.R2GC_318_88})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.g, P.g, P.h1, P.h1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_314_67,(0,0,1):C.R2GC_314_68,(0,0,2):C.R2GC_314_69,(0,0,3):C.R2GC_314_70,(0,0,4):C.R2GC_314_71,(0,0,5):C.R2GC_314_72})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.g, P.g, P.h1, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_315_73,(0,0,1):C.R2GC_315_74,(0,0,2):C.R2GC_315_75,(0,0,3):C.R2GC_315_76,(0,0,4):C.R2GC_315_77,(0,0,5):C.R2GC_315_78})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.g, P.g, P.h2, P.h2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_316_79,(0,0,1):C.R2GC_316_80,(0,0,2):C.R2GC_316_81,(0,0,3):C.R2GC_316_82,(0,0,4):C.R2GC_316_83,(0,0,5):C.R2GC_316_84})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_311_49,(0,0,1):C.R2GC_311_50,(0,0,2):C.R2GC_311_51,(0,0,3):C.R2GC_311_52,(0,0,4):C.R2GC_311_53,(0,0,5):C.R2GC_311_54})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.g, P.g, P.h3, P.h3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_306_19,(0,0,1):C.R2GC_306_20,(0,0,2):C.R2GC_306_21,(0,0,3):C.R2GC_306_22,(0,0,4):C.R2GC_306_23,(0,0,5):C.R2GC_306_24})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_312_55,(0,0,1):C.R2GC_312_56,(0,0,2):C.R2GC_312_57,(0,0,3):C.R2GC_312_58,(0,0,4):C.R2GC_312_59,(0,0,5):C.R2GC_312_60})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.g, P.g, P.h3, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_307_25,(0,0,1):C.R2GC_307_26,(0,0,2):C.R2GC_307_27,(0,0,3):C.R2GC_307_28,(0,0,4):C.R2GC_307_29,(0,0,5):C.R2GC_307_30})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.g, P.g, P.h4, P.h4 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_308_31,(0,0,1):C.R2GC_308_32,(0,0,2):C.R2GC_308_33,(0,0,3):C.R2GC_308_34,(0,0,4):C.R2GC_308_35,(0,0,5):C.R2GC_308_36})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_409_124,(0,1,1):C.UVGC_409_125,(0,1,2):C.UVGC_409_126,(0,1,5):C.UVGC_409_127,(0,1,6):C.UVGC_409_128,(0,1,7):C.UVGC_409_129,(0,2,3):C.UVGC_321_1,(0,0,4):C.UVGC_322_2})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,1,4):C.UVGC_324_6,(2,1,5):C.UVGC_324_5,(0,1,4):C.UVGC_324_6,(0,1,5):C.UVGC_324_5,(6,1,0):C.UVGC_414_156,(6,1,2):C.UVGC_414_157,(6,1,3):C.UVGC_414_158,(6,1,4):C.UVGC_415_164,(6,1,5):C.UVGC_415_165,(6,1,6):C.UVGC_414_161,(6,1,7):C.UVGC_414_162,(6,1,8):C.UVGC_414_163,(4,1,4):C.UVGC_323_3,(4,1,5):C.UVGC_323_4,(3,1,4):C.UVGC_323_3,(3,1,5):C.UVGC_323_4,(8,1,4):C.UVGC_324_5,(8,1,5):C.UVGC_324_6,(7,1,0):C.UVGC_414_156,(7,1,2):C.UVGC_414_157,(7,1,3):C.UVGC_414_158,(7,1,4):C.UVGC_414_159,(7,1,5):C.UVGC_414_160,(7,1,6):C.UVGC_414_161,(7,1,7):C.UVGC_414_162,(7,1,8):C.UVGC_414_163,(5,1,4):C.UVGC_323_3,(5,1,5):C.UVGC_323_4,(1,1,4):C.UVGC_323_3,(1,1,5):C.UVGC_323_4,(11,0,4):C.UVGC_327_9,(11,0,5):C.UVGC_327_10,(10,0,4):C.UVGC_327_9,(10,0,5):C.UVGC_327_10,(9,0,4):C.UVGC_326_7,(9,0,5):C.UVGC_326_8,(2,2,4):C.UVGC_324_6,(2,2,5):C.UVGC_324_5,(0,2,4):C.UVGC_324_6,(0,2,5):C.UVGC_324_5,(4,2,4):C.UVGC_323_3,(4,2,5):C.UVGC_323_4,(3,2,4):C.UVGC_323_3,(3,2,5):C.UVGC_323_4,(8,2,0):C.UVGC_413_148,(8,2,2):C.UVGC_413_149,(8,2,3):C.UVGC_413_150,(8,2,4):C.UVGC_413_151,(8,2,5):C.UVGC_413_152,(8,2,6):C.UVGC_413_153,(8,2,7):C.UVGC_413_154,(8,2,8):C.UVGC_413_155,(6,2,0):C.UVGC_411_138,(6,2,2):C.UVGC_411_139,(6,2,3):C.UVGC_411_140,(6,2,4):C.UVGC_411_141,(6,2,5):C.UVGC_411_142,(6,2,6):C.UVGC_411_143,(6,2,7):C.UVGC_411_144,(6,2,8):C.UVGC_411_145,(7,2,1):C.UVGC_328_11,(7,2,4):C.UVGC_329_13,(7,2,5):C.UVGC_329_14,(5,2,4):C.UVGC_323_3,(5,2,5):C.UVGC_323_4,(1,2,4):C.UVGC_323_3,(1,2,5):C.UVGC_323_4,(2,3,4):C.UVGC_324_6,(2,3,5):C.UVGC_324_5,(0,3,4):C.UVGC_324_6,(0,3,5):C.UVGC_324_5,(4,3,4):C.UVGC_323_3,(4,3,5):C.UVGC_323_4,(3,3,4):C.UVGC_323_3,(3,3,5):C.UVGC_323_4,(8,3,0):C.UVGC_410_130,(8,3,2):C.UVGC_410_131,(8,3,3):C.UVGC_410_132,(8,3,4):C.UVGC_410_133,(8,3,5):C.UVGC_410_134,(8,3,6):C.UVGC_410_135,(8,3,7):C.UVGC_410_136,(8,3,8):C.UVGC_410_137,(6,3,1):C.UVGC_328_11,(6,3,4):C.UVGC_328_12,(6,3,5):C.UVGC_326_7,(7,3,0):C.UVGC_411_138,(7,3,2):C.UVGC_411_139,(7,3,3):C.UVGC_411_140,(7,3,4):C.UVGC_412_146,(7,3,5):C.UVGC_412_147,(7,3,6):C.UVGC_411_143,(7,3,7):C.UVGC_411_144,(7,3,8):C.UVGC_411_145,(5,3,4):C.UVGC_323_3,(5,3,5):C.UVGC_323_4,(1,3,4):C.UVGC_323_3,(1,3,5):C.UVGC_323_4})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.h__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_425_180,(0,0,2):C.UVGC_425_181,(0,0,1):C.UVGC_425_182,(0,1,0):C.UVGC_424_177,(0,1,2):C.UVGC_424_178,(0,1,1):C.UVGC_424_179})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_383_71,(0,0,2):C.UVGC_383_72,(0,0,1):C.UVGC_383_73,(0,1,0):C.UVGC_384_74,(0,1,2):C.UVGC_384_75,(0,1,1):C.UVGC_384_76})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.h__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_400_99,(0,0,2):C.UVGC_400_100,(0,0,1):C.UVGC_400_101,(0,1,0):C.UVGC_399_96,(0,1,2):C.UVGC_399_97,(0,1,1):C.UVGC_399_98})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_424_177,(0,0,2):C.UVGC_424_178,(0,0,1):C.UVGC_424_179,(0,1,0):C.UVGC_425_180,(0,1,2):C.UVGC_425_181,(0,1,1):C.UVGC_425_182})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_384_74,(0,0,2):C.UVGC_384_75,(0,0,1):C.UVGC_384_76,(0,1,0):C.UVGC_383_71,(0,1,2):C.UVGC_383_72,(0,1,1):C.UVGC_383_73})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.h__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_399_96,(0,0,2):C.UVGC_399_97,(0,0,1):C.UVGC_399_98,(0,1,0):C.UVGC_400_99,(0,1,2):C.UVGC_400_100,(0,1,1):C.UVGC_400_101})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_423_174,(0,0,2):C.UVGC_423_175,(0,0,1):C.UVGC_423_176,(0,1,0):C.UVGC_428_185,(0,1,2):C.UVGC_428_186,(0,1,1):C.UVGC_428_187})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_387_79,(0,0,2):C.UVGC_387_80,(0,0,1):C.UVGC_387_81,(0,1,0):C.UVGC_382_68,(0,1,2):C.UVGC_382_69,(0,1,1):C.UVGC_382_70})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_398_93,(0,0,2):C.UVGC_398_94,(0,0,1):C.UVGC_398_95,(0,1,0):C.UVGC_403_104,(0,1,2):C.UVGC_403_105,(0,1,1):C.UVGC_403_106})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_370_54})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_388_82})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_348_32})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_428_185,(0,0,2):C.UVGC_428_186,(0,0,1):C.UVGC_428_187,(0,1,0):C.UVGC_423_174,(0,1,2):C.UVGC_423_175,(0,1,1):C.UVGC_423_176})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_382_68,(0,0,2):C.UVGC_382_69,(0,0,1):C.UVGC_382_70,(0,1,0):C.UVGC_387_79,(0,1,2):C.UVGC_387_80,(0,1,1):C.UVGC_387_81})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_403_104,(0,0,2):C.UVGC_403_105,(0,0,1):C.UVGC_403_106,(0,1,0):C.UVGC_398_93,(0,1,2):C.UVGC_398_94,(0,1,1):C.UVGC_398_95})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_429_188})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_359_43})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_404_107})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_430_189})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_431_190})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_426_183})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_427_184})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_360_44})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_361_45})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_362_46})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_363_47})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_405_108})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_406_109})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_401_102})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_402_103})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_371_55})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_372_56})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_373_57})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_374_58})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_389_83})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_390_84})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_385_77})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_386_78})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_349_33})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_350_34})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_351_35})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.h4 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_352_36})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_332_17,(0,1,0):C.UVGC_417_167})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_332_17,(0,1,0):C.UVGC_354_38,(0,2,0):C.UVGC_354_38})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_332_17,(0,1,0):C.UVGC_392_86,(0,2,0):C.UVGC_392_86})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_330_15,(0,1,0):C.UVGC_365_49,(0,2,0):C.UVGC_365_49})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_330_15,(0,1,0):C.UVGC_376_60,(0,2,0):C.UVGC_376_60})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_330_15,(0,1,0):C.UVGC_343_19,(0,2,0):C.UVGC_343_19})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,1):C.UVGC_344_21,(0,1,2):C.UVGC_344_22,(0,1,3):C.UVGC_344_23,(0,1,4):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,5):C.UVGC_418_168,(0,2,0):C.UVGC_344_20,(0,2,1):C.UVGC_344_21,(0,2,2):C.UVGC_344_22,(0,2,3):C.UVGC_344_23,(0,2,4):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,5):C.UVGC_418_168})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,1):C.UVGC_344_21,(0,1,3):C.UVGC_344_22,(0,1,4):C.UVGC_344_23,(0,1,5):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,2):C.UVGC_355_39,(0,2,0):C.UVGC_344_20,(0,2,1):C.UVGC_344_21,(0,2,3):C.UVGC_344_22,(0,2,4):C.UVGC_344_23,(0,2,5):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,2):C.UVGC_355_39})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,1):C.UVGC_344_21,(0,1,2):C.UVGC_344_22,(0,1,3):C.UVGC_344_23,(0,1,4):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,5):C.UVGC_393_87,(0,2,0):C.UVGC_344_20,(0,2,1):C.UVGC_344_21,(0,2,2):C.UVGC_344_22,(0,2,3):C.UVGC_344_23,(0,2,4):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,5):C.UVGC_393_87})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,1):C.UVGC_344_21,(0,1,2):C.UVGC_344_22,(0,1,4):C.UVGC_344_23,(0,1,5):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,3):C.UVGC_366_50,(0,2,0):C.UVGC_344_20,(0,2,1):C.UVGC_344_21,(0,2,2):C.UVGC_344_22,(0,2,4):C.UVGC_344_23,(0,2,5):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,3):C.UVGC_366_50})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,1):C.UVGC_344_21,(0,1,2):C.UVGC_344_22,(0,1,3):C.UVGC_344_23,(0,1,4):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,5):C.UVGC_377_61,(0,2,0):C.UVGC_344_20,(0,2,1):C.UVGC_344_21,(0,2,2):C.UVGC_344_22,(0,2,3):C.UVGC_344_23,(0,2,4):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,5):C.UVGC_377_61})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_331_16,(0,1,0):C.UVGC_344_20,(0,1,2):C.UVGC_344_21,(0,1,3):C.UVGC_344_22,(0,1,4):C.UVGC_344_23,(0,1,5):C.UVGC_344_24,(0,1,6):C.UVGC_344_25,(0,1,7):C.UVGC_344_26,(0,1,8):C.UVGC_344_27,(0,1,1):C.UVGC_344_28,(0,2,0):C.UVGC_344_20,(0,2,2):C.UVGC_344_21,(0,2,3):C.UVGC_344_22,(0,2,4):C.UVGC_344_23,(0,2,5):C.UVGC_344_24,(0,2,6):C.UVGC_344_25,(0,2,7):C.UVGC_344_26,(0,2,8):C.UVGC_344_27,(0,2,1):C.UVGC_344_28})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_420_170,(0,0,2):C.UVGC_420_171,(0,0,1):C.UVGC_379_65})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_379_63,(0,0,2):C.UVGC_379_64,(0,0,1):C.UVGC_379_65})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_89,(0,0,2):C.UVGC_395_90,(0,0,1):C.UVGC_379_65})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_420_170,(0,0,2):C.UVGC_420_171,(0,0,1):C.UVGC_379_65})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_379_63,(0,0,2):C.UVGC_379_64,(0,0,1):C.UVGC_379_65})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_395_89,(0,0,2):C.UVGC_395_90,(0,0,1):C.UVGC_379_65})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_421_172,(0,1,0):C.UVGC_422_173})

V_160 = CTVertex(name = 'V_160',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_357_41,(0,1,0):C.UVGC_358_42})

V_161 = CTVertex(name = 'V_161',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_396_91,(0,1,0):C.UVGC_397_92})

V_162 = CTVertex(name = 'V_162',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_368_52,(0,1,0):C.UVGC_369_53})

V_163 = CTVertex(name = 'V_163',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_380_66,(0,1,0):C.UVGC_381_67})

V_164 = CTVertex(name = 'V_164',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_346_30,(0,1,0):C.UVGC_347_31})

V_165 = CTVertex(name = 'V_165',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_419_169,(0,2,0):C.UVGC_419_169,(0,1,0):C.UVGC_416_166,(0,3,0):C.UVGC_416_166})

V_166 = CTVertex(name = 'V_166',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_356_40,(0,2,0):C.UVGC_356_40,(0,1,0):C.UVGC_353_37,(0,3,0):C.UVGC_353_37})

V_167 = CTVertex(name = 'V_167',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_394_88,(0,2,0):C.UVGC_394_88,(0,1,0):C.UVGC_391_85,(0,3,0):C.UVGC_391_85})

V_168 = CTVertex(name = 'V_168',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_367_51,(0,2,0):C.UVGC_367_51,(0,1,0):C.UVGC_364_48,(0,3,0):C.UVGC_364_48})

V_169 = CTVertex(name = 'V_169',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_378_62,(0,2,0):C.UVGC_378_62,(0,1,0):C.UVGC_375_59,(0,3,0):C.UVGC_375_59})

V_170 = CTVertex(name = 'V_170',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_345_29,(0,2,0):C.UVGC_345_29,(0,1,0):C.UVGC_342_18,(0,3,0):C.UVGC_342_18})

V_171 = CTVertex(name = 'V_171',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_408_116,(0,0,1):C.UVGC_408_117,(0,0,2):C.UVGC_408_118,(0,0,3):C.UVGC_408_119,(0,0,4):C.UVGC_408_120,(0,0,5):C.UVGC_408_121,(0,0,6):C.UVGC_408_122,(0,0,7):C.UVGC_408_123,(0,1,0):C.UVGC_407_110,(0,1,1):C.UVGC_407_111,(0,1,2):C.UVGC_407_112,(0,1,5):C.UVGC_407_113,(0,1,6):C.UVGC_407_114,(0,1,7):C.UVGC_407_115})

