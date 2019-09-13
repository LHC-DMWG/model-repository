# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 6 Jun 2019 21:52:45


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_263_73,(0,0,1):C.R2GC_263_74})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ] ],
               couplings = {(0,1,0):C.R2GC_258_68,(0,1,1):C.R2GC_258_69,(2,1,0):C.R2GC_258_68,(2,1,1):C.R2GC_258_69,(5,1,0):C.R2GC_256_64,(5,1,1):C.R2GC_256_65,(1,1,0):C.R2GC_256_64,(1,1,1):C.R2GC_256_65,(7,1,0):C.R2GC_266_79,(7,1,1):C.R2GC_266_80,(4,1,0):C.R2GC_256_64,(4,1,1):C.R2GC_256_65,(3,1,0):C.R2GC_256_64,(3,1,1):C.R2GC_256_65,(8,1,0):C.R2GC_257_66,(8,1,1):C.R2GC_257_67,(6,1,0):C.R2GC_265_77,(6,1,1):C.R2GC_265_78,(11,0,0):C.R2GC_260_71,(11,0,1):C.R2GC_260_72,(10,0,0):C.R2GC_260_71,(10,0,1):C.R2GC_260_72,(9,0,1):C.R2GC_259_70,(0,2,0):C.R2GC_258_68,(0,2,1):C.R2GC_258_69,(2,2,0):C.R2GC_258_68,(2,2,1):C.R2GC_258_69,(5,2,0):C.R2GC_256_64,(5,2,1):C.R2GC_256_65,(1,2,0):C.R2GC_256_64,(1,2,1):C.R2GC_256_65,(7,2,0):C.R2GC_266_79,(7,2,1):C.R2GC_257_67,(6,2,0):C.R2GC_271_81,(6,2,1):C.R2GC_271_82,(4,2,0):C.R2GC_256_64,(4,2,1):C.R2GC_256_65,(3,2,0):C.R2GC_256_64,(3,2,1):C.R2GC_256_65,(8,2,0):C.R2GC_257_66,(8,2,1):C.R2GC_266_80,(0,3,0):C.R2GC_258_68,(0,3,1):C.R2GC_258_69,(2,3,0):C.R2GC_258_68,(2,3,1):C.R2GC_258_69,(5,3,0):C.R2GC_256_64,(5,3,1):C.R2GC_256_65,(1,3,0):C.R2GC_256_64,(1,3,1):C.R2GC_256_65,(7,3,0):C.R2GC_264_75,(7,3,1):C.R2GC_264_76,(4,3,0):C.R2GC_256_64,(4,3,1):C.R2GC_256_65,(3,3,0):C.R2GC_256_64,(3,3,1):C.R2GC_256_65,(8,3,0):C.R2GC_257_66,(8,3,1):C.R2GC_264_76,(6,3,0):C.R2GC_265_77})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d1] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d2] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3d3] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
               couplings = {(0,0,0):C.R2GC_273_84})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
               couplings = {(0,0,0):C.R2GC_278_88})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_278_88})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_278_88})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_278_88})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_278_88})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_278_88})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_568_171})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_568_171})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_163})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_163})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_555_158})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_555_158})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_566_169})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_731_188})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_553_156})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_749_196})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_562_165})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_742_193})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_735_189})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_466_136})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_465_135})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_566_169})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_731_188})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_553_156})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_749_196})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_562_165})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_742_193})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_568_171})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_568_171})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_560_163})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_560_163})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_555_158})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_555_158})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u1] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u2] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3u3] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d1] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d2] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3d3] ] ],
                couplings = {(0,0,0):C.R2GC_274_85})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd1, P.YF3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd2, P.YF3Qu2] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.YF3Qd3, P.YF3Qu3] ] ],
                couplings = {(0,0,0):C.R2GC_558_161})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_288_91})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_563_166})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_563_166})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_290_93})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_563_166})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_563_166})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_289_92})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d1] ] ],
                couplings = {(0,0,0):C.R2GC_291_94})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d1] ] ],
                couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_288_91})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_728_186})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_728_186})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS2 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_290_93})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_728_186})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.s, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_728_186})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_289_92})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d2] ] ],
                couplings = {(0,0,0):C.R2GC_291_94})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d2] ] ],
                couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_288_91,(0,1,0):C.R2GC_314_106})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_550_153})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_550_153})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_290_93,(0,1,0):C.R2GC_317_107})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_550_153})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_550_153})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_289_92})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3d3] ] ],
                couplings = {(0,0,0):C.R2GC_291_94})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3d3] ] ],
                couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_288_91,(0,1,0):C.R2GC_314_106})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_564_167})

V_89 = CTVertex(name = 'V_89',
                type = 'R2',
                particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_564_167})

V_90 = CTVertex(name = 'V_90',
                type = 'R2',
                particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_630_182,(0,1,0):C.R2GC_628_181})

V_91 = CTVertex(name = 'V_91',
                type = 'R2',
                particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'T(1,3,2)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_290_93,(0,1,0):C.R2GC_317_107})

V_92 = CTVertex(name = 'V_92',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_564_167})

V_93 = CTVertex(name = 'V_93',
                type = 'R2',
                particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                color = [ 'Identity(1,3)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.d, P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_564_167})

V_94 = CTVertex(name = 'V_94',
                type = 'R2',
                particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_628_181,(0,1,0):C.R2GC_630_182})

V_95 = CTVertex(name = 'V_95',
                type = 'R2',
                particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_289_92})

V_96 = CTVertex(name = 'V_96',
                type = 'R2',
                particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                couplings = {(0,0,0):C.R2GC_626_179,(0,0,1):C.R2GC_626_180})

V_97 = CTVertex(name = 'V_97',
                type = 'R2',
                particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'T(2,4,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                couplings = {(0,0,0):C.R2GC_291_94})

V_98 = CTVertex(name = 'V_98',
                type = 'R2',
                particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd1] ] ],
                couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_99 = CTVertex(name = 'V_99',
                type = 'R2',
                particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VSS1, L.VSS3 ],
                loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                couplings = {(0,0,0):C.R2GC_288_91,(0,1,0):C.R2GC_314_106})

V_100 = CTVertex(name = 'V_100',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_101 = CTVertex(name = 'V_101',
                 type = 'R2',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_102 = CTVertex(name = 'V_102',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_630_182,(0,1,0):C.R2GC_628_181})

V_103 = CTVertex(name = 'V_103',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93,(0,1,0):C.R2GC_317_107})

V_104 = CTVertex(name = 'V_104',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_105 = CTVertex(name = 'V_105',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_106 = CTVertex(name = 'V_106',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_628_181,(0,1,0):C.R2GC_630_182})

V_107 = CTVertex(name = 'V_107',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_289_92})

V_108 = CTVertex(name = 'V_108',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_626_179,(0,0,1):C.R2GC_626_180})

V_109 = CTVertex(name = 'V_109',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_291_94})

V_110 = CTVertex(name = 'V_110',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_111 = CTVertex(name = 'V_111',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_288_91,(0,1,0):C.R2GC_314_106})

V_112 = CTVertex(name = 'V_112',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_113 = CTVertex(name = 'V_113',
                 type = 'R2',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_114 = CTVertex(name = 'V_114',
                 type = 'R2',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_630_182,(0,1,0):C.R2GC_628_181})

V_115 = CTVertex(name = 'V_115',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93,(0,1,0):C.R2GC_317_107})

V_116 = CTVertex(name = 'V_116',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_117 = CTVertex(name = 'V_117',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_118 = CTVertex(name = 'V_118',
                 type = 'R2',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_628_181,(0,1,0):C.R2GC_630_182})

V_119 = CTVertex(name = 'V_119',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_289_92})

V_120 = CTVertex(name = 'V_120',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_626_179,(0,0,1):C.R2GC_626_180})

V_121 = CTVertex(name = 'V_121',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_291_94})

V_122 = CTVertex(name = 'V_122',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_123 = CTVertex(name = 'V_123',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116,(0,1,0):C.R2GC_375_117})

V_124 = CTVertex(name = 'V_124',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_564_167})

V_125 = CTVertex(name = 'V_125',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_564_167})

V_126 = CTVertex(name = 'V_126',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_127 = CTVertex(name = 'V_127',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_128 = CTVertex(name = 'V_128',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93,(0,1,0):C.R2GC_317_107})

V_129 = CTVertex(name = 'V_129',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_564_167})

V_130 = CTVertex(name = 'V_130',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_564_167})

V_131 = CTVertex(name = 'V_131',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_132 = CTVertex(name = 'V_132',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_133 = CTVertex(name = 'V_133',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_134 = CTVertex(name = 'V_134',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,1):C.R2GC_626_179,(0,0,0):C.R2GC_626_180})

V_135 = CTVertex(name = 'V_135',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_136 = CTVertex(name = 'V_136',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_137 = CTVertex(name = 'V_137',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116,(0,1,0):C.R2GC_375_117})

V_138 = CTVertex(name = 'V_138',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_139 = CTVertex(name = 'V_139',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_140 = CTVertex(name = 'V_140',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_141 = CTVertex(name = 'V_141',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_142 = CTVertex(name = 'V_142',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93})

V_143 = CTVertex(name = 'V_143',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_144 = CTVertex(name = 'V_144',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_556_159})

V_145 = CTVertex(name = 'V_145',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_146 = CTVertex(name = 'V_146',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_147 = CTVertex(name = 'V_147',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_148 = CTVertex(name = 'V_148',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,1):C.R2GC_626_179,(0,0,0):C.R2GC_626_180})

V_149 = CTVertex(name = 'V_149',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_150 = CTVertex(name = 'V_150',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_151 = CTVertex(name = 'V_151',
                 type = 'R2',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116})

V_152 = CTVertex(name = 'V_152',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_153 = CTVertex(name = 'V_153',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_154 = CTVertex(name = 'V_154',
                 type = 'R2',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_155 = CTVertex(name = 'V_155',
                 type = 'R2',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_156 = CTVertex(name = 'V_156',
                 type = 'R2',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93})

V_157 = CTVertex(name = 'V_157',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_158 = CTVertex(name = 'V_158',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_551_154})

V_159 = CTVertex(name = 'V_159',
                 type = 'R2',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_632_183})

V_160 = CTVertex(name = 'V_160',
                 type = 'R2',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_633_184,(0,0,1):C.R2GC_633_185})

V_161 = CTVertex(name = 'V_161',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_162 = CTVertex(name = 'V_162',
                 type = 'R2',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,1):C.R2GC_626_179,(0,0,0):C.R2GC_626_180})

V_163 = CTVertex(name = 'V_163',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_164 = CTVertex(name = 'V_164',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_165 = CTVertex(name = 'V_165',
                 type = 'R2',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116})

V_166 = CTVertex(name = 'V_166',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_745_194})

V_167 = CTVertex(name = 'V_167',
                 type = 'R2',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_745_194})

V_168 = CTVertex(name = 'V_168',
                 type = 'R2',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93})

V_169 = CTVertex(name = 'V_169',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_745_194})

V_170 = CTVertex(name = 'V_170',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_745_194})

V_171 = CTVertex(name = 'V_171',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_172 = CTVertex(name = 'V_172',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_173 = CTVertex(name = 'V_173',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_174 = CTVertex(name = 'V_174',
                 type = 'R2',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116})

V_175 = CTVertex(name = 'V_175',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_557_160})

V_176 = CTVertex(name = 'V_176',
                 type = 'R2',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_557_160})

V_177 = CTVertex(name = 'V_177',
                 type = 'R2',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93})

V_178 = CTVertex(name = 'V_178',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_557_160})

V_179 = CTVertex(name = 'V_179',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_557_160})

V_180 = CTVertex(name = 'V_180',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_181 = CTVertex(name = 'V_181',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_182 = CTVertex(name = 'V_182',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_183 = CTVertex(name = 'V_183',
                 type = 'R2',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_374_116})

V_184 = CTVertex(name = 'V_184',
                 type = 'R2',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_738_191})

V_185 = CTVertex(name = 'V_185',
                 type = 'R2',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_738_191})

V_186 = CTVertex(name = 'V_186',
                 type = 'R2',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_290_93})

V_187 = CTVertex(name = 'V_187',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_738_191})

V_188 = CTVertex(name = 'V_188',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_738_191})

V_189 = CTVertex(name = 'V_189',
                 type = 'R2',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_376_118})

V_190 = CTVertex(name = 'V_190',
                 type = 'R2',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_379_119})

V_191 = CTVertex(name = 'V_191',
                 type = 'R2',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(2,0,0):C.R2GC_294_98,(2,0,1):C.R2GC_294_99,(1,0,0):C.R2GC_294_98,(1,0,1):C.R2GC_294_99,(0,0,0):C.R2GC_260_72,(0,0,1):C.R2GC_293_97})

V_192 = CTVertex(name = 'V_192',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_736_190})

V_193 = CTVertex(name = 'V_193',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_493_142})

V_194 = CTVertex(name = 'V_194',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_493_142})

V_195 = CTVertex(name = 'V_195',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_493_142})

V_196 = CTVertex(name = 'V_196',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_516_146})

V_197 = CTVertex(name = 'V_197',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_516_146})

V_198 = CTVertex(name = 'V_198',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_516_146})

V_199 = CTVertex(name = 'V_199',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_476_138})

V_200 = CTVertex(name = 'V_200',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_476_138})

V_201 = CTVertex(name = 'V_201',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_476_138})

V_202 = CTVertex(name = 'V_202',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_539_150})

V_203 = CTVertex(name = 'V_203',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_539_150})

V_204 = CTVertex(name = 'V_204',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_539_150})

V_205 = CTVertex(name = 'V_205',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_296_101})

V_206 = CTVertex(name = 'V_206',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_297_102})

V_207 = CTVertex(name = 'V_207',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_298_103})

V_208 = CTVertex(name = 'V_208',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_296_101})

V_209 = CTVertex(name = 'V_209',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_297_102})

V_210 = CTVertex(name = 'V_210',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_298_103})

V_211 = CTVertex(name = 'V_211',
                 type = 'R2',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_296_101})

V_212 = CTVertex(name = 'V_212',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_297_102})

V_213 = CTVertex(name = 'V_213',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_298_103})

V_214 = CTVertex(name = 'V_214',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_339_110})

V_215 = CTVertex(name = 'V_215',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_340_111})

V_216 = CTVertex(name = 'V_216',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_341_112})

V_217 = CTVertex(name = 'V_217',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_339_110})

V_218 = CTVertex(name = 'V_218',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_340_111})

V_219 = CTVertex(name = 'V_219',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_341_112})

V_220 = CTVertex(name = 'V_220',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_339_110})

V_221 = CTVertex(name = 'V_221',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_340_111})

V_222 = CTVertex(name = 'V_222',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_341_112})

V_223 = CTVertex(name = 'V_223',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_384_121})

V_224 = CTVertex(name = 'V_224',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_225 = CTVertex(name = 'V_225',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_226 = CTVertex(name = 'V_226',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_385_122})

V_227 = CTVertex(name = 'V_227',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_386_123})

V_228 = CTVertex(name = 'V_228',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_384_121})

V_229 = CTVertex(name = 'V_229',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_230 = CTVertex(name = 'V_230',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_231 = CTVertex(name = 'V_231',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_385_122})

V_232 = CTVertex(name = 'V_232',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_386_123})

V_233 = CTVertex(name = 'V_233',
                 type = 'R2',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_384_121})

V_234 = CTVertex(name = 'V_234',
                 type = 'R2',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_235 = CTVertex(name = 'V_235',
                 type = 'R2',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_623_178})

V_236 = CTVertex(name = 'V_236',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_385_122})

V_237 = CTVertex(name = 'V_237',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_386_123})

V_238 = CTVertex(name = 'V_238',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_424_128})

V_239 = CTVertex(name = 'V_239',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_425_129})

V_240 = CTVertex(name = 'V_240',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_426_130})

V_241 = CTVertex(name = 'V_241',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_424_128})

V_242 = CTVertex(name = 'V_242',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_425_129})

V_243 = CTVertex(name = 'V_243',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_426_130})

V_244 = CTVertex(name = 'V_244',
                 type = 'R2',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_424_128})

V_245 = CTVertex(name = 'V_245',
                 type = 'R2',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_425_129})

V_246 = CTVertex(name = 'V_246',
                 type = 'R2',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_426_130})

V_247 = CTVertex(name = 'V_247',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_299_104})

V_248 = CTVertex(name = 'V_248',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_299_104})

V_249 = CTVertex(name = 'V_249',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_299_104})

V_250 = CTVertex(name = 'V_250',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_342_113})

V_251 = CTVertex(name = 'V_251',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_342_113})

V_252 = CTVertex(name = 'V_252',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_342_113})

V_253 = CTVertex(name = 'V_253',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_387_124})

V_254 = CTVertex(name = 'V_254',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_387_124})

V_255 = CTVertex(name = 'V_255',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_387_124})

V_256 = CTVertex(name = 'V_256',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_427_131})

V_257 = CTVertex(name = 'V_257',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_427_131})

V_258 = CTVertex(name = 'V_258',
                 type = 'R2',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_427_131})

V_259 = CTVertex(name = 'V_259',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_567_170})

V_260 = CTVertex(name = 'V_260',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_567_170})

V_261 = CTVertex(name = 'V_261',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_162})

V_262 = CTVertex(name = 'V_262',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_162})

V_263 = CTVertex(name = 'V_263',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_554_157})

V_264 = CTVertex(name = 'V_264',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_554_157})

V_265 = CTVertex(name = 'V_265',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_278_88})

V_266 = CTVertex(name = 'V_266',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_278_88})

V_267 = CTVertex(name = 'V_267',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_278_88})

V_268 = CTVertex(name = 'V_268',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_273_84})

V_269 = CTVertex(name = 'V_269',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_273_84})

V_270 = CTVertex(name = 'V_270',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_273_84})

V_271 = CTVertex(name = 'V_271',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_272 = CTVertex(name = 'V_272',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_273 = CTVertex(name = 'V_273',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_274 = CTVertex(name = 'V_274',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_275 = CTVertex(name = 'V_275',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_276 = CTVertex(name = 'V_276',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_274_85})

V_277 = CTVertex(name = 'V_277',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_278 = CTVertex(name = 'V_278',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_279 = CTVertex(name = 'V_279',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_280 = CTVertex(name = 'V_280',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_281 = CTVertex(name = 'V_281',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_282 = CTVertex(name = 'V_282',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_558_161})

V_283 = CTVertex(name = 'V_283',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_280_89,(0,1,0):C.R2GC_276_87})

V_284 = CTVertex(name = 'V_284',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_280_89,(0,1,0):C.R2GC_276_87})

V_285 = CTVertex(name = 'V_285',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_280_89,(0,1,0):C.R2GC_276_87})

V_286 = CTVertex(name = 'V_286',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_275_86,(0,1,0):C.R2GC_276_87})

V_287 = CTVertex(name = 'V_287',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_275_86,(0,1,0):C.R2GC_276_87})

V_288 = CTVertex(name = 'V_288',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_275_86,(0,1,0):C.R2GC_276_87})

V_289 = CTVertex(name = 'V_289',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_567_170})

V_290 = CTVertex(name = 'V_290',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_567_170})

V_291 = CTVertex(name = 'V_291',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_162})

V_292 = CTVertex(name = 'V_292',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_559_162})

V_293 = CTVertex(name = 'V_293',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_554_157})

V_294 = CTVertex(name = 'V_294',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_554_157})

V_295 = CTVertex(name = 'V_295',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_565_168})

V_296 = CTVertex(name = 'V_296',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_730_187})

V_297 = CTVertex(name = 'V_297',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_552_155})

V_298 = CTVertex(name = 'V_298',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_748_195})

V_299 = CTVertex(name = 'V_299',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_561_164})

V_300 = CTVertex(name = 'V_300',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_741_192})

V_301 = CTVertex(name = 'V_301',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_565_168})

V_302 = CTVertex(name = 'V_302',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_730_187})

V_303 = CTVertex(name = 'V_303',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_552_155})

V_304 = CTVertex(name = 'V_304',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_748_195})

V_305 = CTVertex(name = 'V_305',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_561_164})

V_306 = CTVertex(name = 'V_306',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_741_192})

V_307 = CTVertex(name = 'V_307',
                 type = 'R2',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_272_83})

V_308 = CTVertex(name = 'V_308',
                 type = 'R2',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_272_83})

V_309 = CTVertex(name = 'V_309',
                 type = 'R2',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_462_134,(0,1,0):C.R2GC_272_83})

V_310 = CTVertex(name = 'V_310',
                 type = 'R2',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_272_83})

V_311 = CTVertex(name = 'V_311',
                 type = 'R2',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.R2GC_272_83})

V_312 = CTVertex(name = 'V_312',
                 type = 'R2',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.R2GC_272_83})

V_313 = CTVertex(name = 'V_313',
                 type = 'R2',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_511_145,(0,1,0):C.R2GC_272_83})

V_314 = CTVertex(name = 'V_314',
                 type = 'R2',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_520_147,(0,1,0):C.R2GC_272_83})

V_315 = CTVertex(name = 'V_315',
                 type = 'R2',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_529_148,(0,1,0):C.R2GC_272_83})

V_316 = CTVertex(name = 'V_316',
                 type = 'R2',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_490_141,(0,1,0):C.R2GC_272_83})

V_317 = CTVertex(name = 'V_317',
                 type = 'R2',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_497_143,(0,1,0):C.R2GC_272_83})

V_318 = CTVertex(name = 'V_318',
                 type = 'R2',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_504_144,(0,1,0):C.R2GC_272_83})

V_319 = CTVertex(name = 'V_319',
                 type = 'R2',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_538_149,(0,1,0):C.R2GC_272_83})

V_320 = CTVertex(name = 'V_320',
                 type = 'R2',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_543_151,(0,1,0):C.R2GC_272_83})

V_321 = CTVertex(name = 'V_321',
                 type = 'R2',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_548_152,(0,1,0):C.R2GC_272_83})

V_322 = CTVertex(name = 'V_322',
                 type = 'R2',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_475_137,(0,1,0):C.R2GC_272_83})

V_323 = CTVertex(name = 'V_323',
                 type = 'R2',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_480_139,(0,1,0):C.R2GC_272_83})

V_324 = CTVertex(name = 'V_324',
                 type = 'R2',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_485_140,(0,1,0):C.R2GC_272_83})

V_325 = CTVertex(name = 'V_325',
                 type = 'R2',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV2, L.VV3 ],
                 loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.g] ], [ [P.t] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ] ],
                 couplings = {(0,2,1):C.R2GC_112_1,(0,0,2):C.R2GC_121_13,(0,0,3):C.R2GC_121_14,(0,0,4):C.R2GC_121_15,(0,0,5):C.R2GC_121_16,(0,0,6):C.R2GC_121_17,(0,0,7):C.R2GC_121_18,(0,0,8):C.R2GC_121_19,(0,0,9):C.R2GC_121_20,(0,0,10):C.R2GC_121_21,(0,0,11):C.R2GC_121_22,(0,0,12):C.R2GC_121_23,(0,0,13):C.R2GC_121_24,(0,0,14):C.R2GC_121_25,(0,1,0):C.R2GC_118_8})

V_326 = CTVertex(name = 'V_326',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.R2GC_383_120,(0,1,0):C.R2GC_287_90})

V_327 = CTVertex(name = 'V_327',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.R2GC_397_125,(0,1,0):C.R2GC_287_90})

V_328 = CTVertex(name = 'V_328',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_410_126,(0,1,0):C.R2GC_287_90})

V_329 = CTVertex(name = 'V_329',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.R2GC_338_109,(0,1,0):C.R2GC_287_90})

V_330 = CTVertex(name = 'V_330',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.R2GC_353_114,(0,1,0):C.R2GC_287_90})

V_331 = CTVertex(name = 'V_331',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.R2GC_368_115,(0,1,0):C.R2GC_287_90})

V_332 = CTVertex(name = 'V_332',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_423_127,(0,1,0):C.R2GC_287_90})

V_333 = CTVertex(name = 'V_333',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.R2GC_436_132,(0,1,0):C.R2GC_287_90})

V_334 = CTVertex(name = 'V_334',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_449_133,(0,1,0):C.R2GC_287_90})

V_335 = CTVertex(name = 'V_335',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.R2GC_295_100,(0,1,0):C.R2GC_287_90})

V_336 = CTVertex(name = 'V_336',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.R2GC_308_105,(0,1,0):C.R2GC_287_90})

V_337 = CTVertex(name = 'V_337',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.R2GC_323_108,(0,1,0):C.R2GC_287_90})

V_338 = CTVertex(name = 'V_338',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVV1 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                 couplings = {(0,0,0):C.R2GC_116_4,(0,0,1):C.R2GC_116_5})

V_339 = CTVertex(name = 'V_339',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_113_2})

V_340 = CTVertex(name = 'V_340',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xv, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_125_44,(0,0,1):C.R2GC_125_45,(0,0,2):C.R2GC_125_46,(0,0,3):C.R2GC_125_47,(0,0,4):C.R2GC_125_48,(0,0,5):C.R2GC_125_49,(0,0,6):C.R2GC_125_50,(0,0,7):C.R2GC_125_51,(0,0,8):C.R2GC_125_52})

V_341 = CTVertex(name = 'V_341',
                 type = 'R2',
                 particles = [ P.a, P.a, P.g, P.g ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_119_9,(0,0,1):C.R2GC_119_10})

V_342 = CTVertex(name = 'V_342',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.Z ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_122_26,(0,0,1):C.R2GC_122_27,(0,0,2):C.R2GC_122_28,(0,0,3):C.R2GC_122_29,(0,0,4):C.R2GC_122_30,(0,0,5):C.R2GC_122_31})

V_343 = CTVertex(name = 'V_343',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Z, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_124_38,(0,0,1):C.R2GC_124_39,(0,0,2):C.R2GC_124_40,(0,0,3):C.R2GC_124_41,(0,0,4):C.R2GC_124_42,(0,0,5):C.R2GC_124_43})

V_344 = CTVertex(name = 'V_344',
                 type = 'R2',
                 particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ], [ [P.YF3Qd1, P.YF3Qu1], [P.YF3Qd2, P.YF3Qu2], [P.YF3Qd3, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.R2GC_127_62,(0,0,1):C.R2GC_127_63})

V_345 = CTVertex(name = 'V_345',
                 type = 'R2',
                 particles = [ P.a, P.g, P.g, P.g ],
                 color = [ 'd(2,3,4)' ],
                 lorentz = [ L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.c], [P.t], [P.u], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(0,0,0):C.R2GC_120_11,(0,0,1):C.R2GC_120_12})

V_346 = CTVertex(name = 'V_346',
                 type = 'R2',
                 particles = [ P.g, P.g, P.g, P.Z ],
                 color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                 lorentz = [ L.VVVV1, L.VVVV10 ],
                 loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.YF3d1], [P.YF3d2], [P.YF3d3] ], [ [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3] ], [ [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3] ], [ [P.YF3u1], [P.YF3u2], [P.YF3u3] ] ],
                 couplings = {(1,0,0):C.R2GC_117_6,(1,0,1):C.R2GC_117_7,(0,1,0):C.R2GC_123_32,(0,1,1):C.R2GC_123_33,(0,1,2):C.R2GC_123_34,(0,1,3):C.R2GC_123_35,(0,1,4):C.R2GC_123_36,(0,1,5):C.R2GC_123_37})

V_347 = CTVertex(name = 'V_347',
                 type = 'R2',
                 particles = [ P.g, P.g, P.H, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_114_3})

V_348 = CTVertex(name = 'V_348',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G0, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_114_3})

V_349 = CTVertex(name = 'V_349',
                 type = 'R2',
                 particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.t] ] ],
                 couplings = {(0,0,0):C.R2GC_114_3})

V_350 = CTVertex(name = 'V_350',
                 type = 'R2',
                 particles = [ P.g, P.g, P.Xs, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b, P.YF3d3] ], [ [P.b, P.YF3Qd3], [P.t, P.YF3Qu3] ], [ [P.c, P.YF3Qu2], [P.s, P.YF3Qd2] ], [ [P.c, P.YF3u2] ], [ [P.d, P.YF3d1] ], [ [P.d, P.YF3Qd1], [P.u, P.YF3Qu1] ], [ [P.s, P.YF3d2] ], [ [P.t, P.YF3u3] ], [ [P.u, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.R2GC_126_53,(0,0,1):C.R2GC_126_54,(0,0,2):C.R2GC_126_55,(0,0,3):C.R2GC_126_56,(0,0,4):C.R2GC_126_57,(0,0,5):C.R2GC_126_58,(0,0,6):C.R2GC_126_59,(0,0,7):C.R2GC_126_60,(0,0,8):C.R2GC_126_61})

V_351 = CTVertex(name = 'V_351',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_759_204,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_759_206,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_759_204,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_759_206})

V_352 = CTVertex(name = 'V_352',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_832_272,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_832_274,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_832_276,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_831_266,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_831_268,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_831_270})

V_353 = CTVertex(name = 'V_353',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_759_204,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_759_206,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_759_204,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_759_206})

V_354 = CTVertex(name = 'V_354',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_832_272,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_832_274,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_832_276,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_831_266,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_831_268,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_831_270})

V_355 = CTVertex(name = 'V_355',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_832_272,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_832_274,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_832_276,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_831_266,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_831_268,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_831_270})

V_356 = CTVertex(name = 'V_356',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_759_204,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_759_206,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_759_204,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_759_206})

V_357 = CTVertex(name = 'V_357',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,7):C.R2GC_570_176,(1,0,8):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,4):C.R2GC_765_209,(1,0,11):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,5):C.R2GC_826_261,(1,0,10):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_263,(1,0,9):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,7):C.R2GC_569_173,(0,0,8):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,4):C.R2GC_766_212,(0,0,11):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,5):C.R2GC_825_256,(0,0,10):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_258,(0,0,9):C.R2GC_825_259})

V_358 = CTVertex(name = 'V_358',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_359 = CTVertex(name = 'V_359',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_360 = CTVertex(name = 'V_360',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_756_201,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_756_202,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_756_201,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_756_202})

V_361 = CTVertex(name = 'V_361',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_362 = CTVertex(name = 'V_362',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_363 = CTVertex(name = 'V_363',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_364 = CTVertex(name = 'V_364',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,7):C.R2GC_570_176,(1,0,8):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,4):C.R2GC_765_209,(1,0,11):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,5):C.R2GC_826_261,(1,0,10):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_263,(1,0,9):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,7):C.R2GC_569_173,(0,0,8):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,4):C.R2GC_766_212,(0,0,11):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,5):C.R2GC_825_256,(0,0,10):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_258,(0,0,9):C.R2GC_825_259})

V_365 = CTVertex(name = 'V_365',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_366 = CTVertex(name = 'V_366',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_784_236,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_784_237,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_784_238,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_783_233,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_783_234,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_783_235})

V_367 = CTVertex(name = 'V_367',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_756_201,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_756_202,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_756_201,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_756_202})

V_368 = CTVertex(name = 'V_368',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_369 = CTVertex(name = 'V_369',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_370 = CTVertex(name = 'V_370',
                 type = 'R2',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_371 = CTVertex(name = 'V_371',
                 type = 'R2',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.R2GC_765_209,(1,0,1):C.R2GC_765_210,(1,0,2):C.R2GC_765_211,(0,0,0):C.R2GC_766_212,(0,0,1):C.R2GC_766_213,(0,0,2):C.R2GC_766_214})

V_372 = CTVertex(name = 'V_372',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_373 = CTVertex(name = 'V_373',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_259})

V_374 = CTVertex(name = 'V_374',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,7):C.R2GC_570_176,(1,0,8):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,4):C.R2GC_765_209,(1,0,11):C.R2GC_826_260,(1,0,1):C.R2GC_788_245,(1,0,5):C.R2GC_826_261,(1,0,10):C.R2GC_826_262,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_826_263,(1,0,9):C.R2GC_826_264,(0,0,3):C.R2GC_569_172,(0,0,7):C.R2GC_569_173,(0,0,8):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,4):C.R2GC_766_212,(0,0,11):C.R2GC_825_255,(0,0,1):C.R2GC_119_9,(0,0,5):C.R2GC_825_256,(0,0,10):C.R2GC_825_257,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_825_258,(0,0,9):C.R2GC_825_259})

V_375 = CTVertex(name = 'V_375',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_784_236,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_784_237,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_784_238,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_783_233,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_783_234,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_783_235})

V_376 = CTVertex(name = 'V_376',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_784_236,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_784_237,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_784_238,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_783_233,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_783_234,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_783_235})

V_377 = CTVertex(name = 'V_377',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_756_201,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_756_202,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_756_201,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_756_202})

V_378 = CTVertex(name = 'V_378',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_379 = CTVertex(name = 'V_379',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_380 = CTVertex(name = 'V_380',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_381 = CTVertex(name = 'V_381',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_382 = CTVertex(name = 'V_382',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_383 = CTVertex(name = 'V_383',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_384 = CTVertex(name = 'V_384',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_762_207,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_762_208,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_762_207,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_762_208})

V_385 = CTVertex(name = 'V_385',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_386 = CTVertex(name = 'V_386',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_387 = CTVertex(name = 'V_387',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_388 = CTVertex(name = 'V_388',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_389 = CTVertex(name = 'V_389',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_390 = CTVertex(name = 'V_390',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_391 = CTVertex(name = 'V_391',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_886_290,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_886_291,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_886_292,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_885_287,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_885_288,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_885_289})

V_392 = CTVertex(name = 'V_392',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_762_207,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_762_208,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_762_207,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_762_208})

V_393 = CTVertex(name = 'V_393',
                 type = 'R2',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_394 = CTVertex(name = 'V_394',
                 type = 'R2',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_395 = CTVertex(name = 'V_395',
                 type = 'R2',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_836_280,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_836_281,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_836_282,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_835_277,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_835_278,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_835_279})

V_396 = CTVertex(name = 'V_396',
                 type = 'R2',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_397 = CTVertex(name = 'V_397',
                 type = 'R2',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_398 = CTVertex(name = 'V_398',
                 type = 'R2',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_788_244,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_788_246,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_788_248,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_787_239,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_787_240,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_787_242})

V_399 = CTVertex(name = 'V_399',
                 type = 'R2',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_886_290,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_886_291,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_886_292,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_885_287,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_885_288,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_885_289})

V_400 = CTVertex(name = 'V_400',
                 type = 'R2',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_832_271,(1,0,8):C.R2GC_886_290,(1,0,1):C.R2GC_832_273,(1,0,7):C.R2GC_886_291,(1,0,2):C.R2GC_832_275,(1,0,6):C.R2GC_886_292,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_831_265,(0,0,8):C.R2GC_885_287,(0,0,1):C.R2GC_831_267,(0,0,7):C.R2GC_885_288,(0,0,2):C.R2GC_831_269,(0,0,6):C.R2GC_885_289})

V_401 = CTVertex(name = 'V_401',
                 type = 'R2',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_759_203,(1,0,5):C.R2GC_762_207,(1,0,1):C.R2GC_759_205,(1,0,4):C.R2GC_762_208,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_759_203,(0,0,5):C.R2GC_762_207,(0,0,1):C.R2GC_759_205,(0,0,4):C.R2GC_762_208})

V_402 = CTVertex(name = 'V_402',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_403 = CTVertex(name = 'V_403',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_404 = CTVertex(name = 'V_404',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_405 = CTVertex(name = 'V_405',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_406 = CTVertex(name = 'V_406',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_407 = CTVertex(name = 'V_407',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_408 = CTVertex(name = 'V_408',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_409 = CTVertex(name = 'V_409',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_410 = CTVertex(name = 'V_410',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_411 = CTVertex(name = 'V_411',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_753_198,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_753_200,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_753_198,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_753_200})

V_412 = CTVertex(name = 'V_412',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_413 = CTVertex(name = 'V_413',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_414 = CTVertex(name = 'V_414',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_415 = CTVertex(name = 'V_415',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_416 = CTVertex(name = 'V_416',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_417 = CTVertex(name = 'V_417',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_418 = CTVertex(name = 'V_418',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_419 = CTVertex(name = 'V_419',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_420 = CTVertex(name = 'V_420',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_421 = CTVertex(name = 'V_421',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_772_222,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_772_224,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_772_226,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_771_216,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_771_218,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_771_220})

V_422 = CTVertex(name = 'V_422',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_753_198,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_753_200,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_753_198,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_753_200})

V_423 = CTVertex(name = 'V_423',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_424 = CTVertex(name = 'V_424',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_425 = CTVertex(name = 'V_425',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_820_252,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_820_253,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_820_254,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_819_249,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_819_250,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_819_251})

V_426 = CTVertex(name = 'V_426',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_427 = CTVertex(name = 'V_427',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_428 = CTVertex(name = 'V_428',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_778_230,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_778_231,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_778_232,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_777_227,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_777_228,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_777_229})

V_429 = CTVertex(name = 'V_429',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_430 = CTVertex(name = 'V_430',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_431 = CTVertex(name = 'V_431',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_788_243,(1,0,8):C.R2GC_880_284,(1,0,1):C.R2GC_788_245,(1,0,7):C.R2GC_880_285,(1,0,2):C.R2GC_788_247,(1,0,6):C.R2GC_880_286,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_753_197,(0,0,8):C.R2GC_753_198,(0,0,1):C.R2GC_119_9,(0,0,7):C.R2GC_124_40,(0,0,2):C.R2GC_787_241,(0,0,6):C.R2GC_879_283})

V_432 = CTVertex(name = 'V_432',
                 type = 'R2',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_772_222,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_772_224,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_772_226,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_771_216,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_771_218,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_771_220})

V_433 = CTVertex(name = 'V_433',
                 type = 'R2',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.R2GC_570_175,(1,0,4):C.R2GC_570_176,(1,0,5):C.R2GC_570_177,(1,0,0):C.R2GC_772_221,(1,0,8):C.R2GC_772_222,(1,0,1):C.R2GC_772_223,(1,0,7):C.R2GC_772_224,(1,0,2):C.R2GC_772_225,(1,0,6):C.R2GC_772_226,(0,0,3):C.R2GC_569_172,(0,0,4):C.R2GC_569_173,(0,0,5):C.R2GC_569_174,(0,0,0):C.R2GC_771_215,(0,0,8):C.R2GC_771_216,(0,0,1):C.R2GC_771_217,(0,0,7):C.R2GC_771_218,(0,0,2):C.R2GC_771_219,(0,0,6):C.R2GC_771_220})

V_434 = CTVertex(name = 'V_434',
                 type = 'R2',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.R2GC_292_95,(1,0,3):C.R2GC_292_96,(1,0,0):C.R2GC_753_197,(1,0,5):C.R2GC_753_198,(1,0,1):C.R2GC_753_199,(1,0,4):C.R2GC_753_200,(0,0,2):C.R2GC_292_95,(0,0,3):C.R2GC_292_96,(0,0,0):C.R2GC_753_197,(0,0,5):C.R2GC_753_198,(0,0,1):C.R2GC_753_199,(0,0,4):C.R2GC_753_200})

V_435 = CTVertex(name = 'V_435',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g ],
                 color = [ 'f(1,2,3)' ],
                 lorentz = [ L.VVV2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_263_201,(0,0,1):C.UVGC_263_202,(0,0,2):C.UVGC_263_203,(0,0,3):C.UVGC_263_204,(0,0,4):C.UVGC_263_205,(0,0,5):C.UVGC_263_206,(0,0,6):C.UVGC_263_207,(0,0,7):C.UVGC_263_208,(0,0,8):C.UVGC_263_209,(0,0,9):C.UVGC_263_210,(0,0,10):C.UVGC_263_211,(0,0,11):C.UVGC_263_212,(0,0,12):C.UVGC_263_213,(0,0,13):C.UVGC_263_214,(0,0,14):C.UVGC_263_215,(0,0,15):C.UVGC_263_216,(0,0,16):C.UVGC_263_217,(0,0,17):C.UVGC_263_218,(0,0,18):C.UVGC_263_219,(0,0,19):C.UVGC_263_220,(0,0,20):C.UVGC_263_221,(0,0,21):C.UVGC_263_222,(0,0,22):C.UVGC_263_223,(0,0,23):C.UVGC_263_224,(0,0,24):C.UVGC_263_225,(0,0,25):C.UVGC_263_226,(0,0,26):C.UVGC_263_227,(0,0,27):C.UVGC_263_228,(0,0,28):C.UVGC_263_229,(0,0,29):C.UVGC_263_230,(0,0,30):C.UVGC_263_231,(0,0,31):C.UVGC_263_232})

V_436 = CTVertex(name = 'V_436',
                 type = 'UV',
                 particles = [ P.g, P.g, P.g, P.g ],
                 color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.YF3d1], [P.YF3d2], [P.YF3d3], [P.YF3Qd1], [P.YF3Qd2], [P.YF3Qd3], [P.YF3Qu1], [P.YF3Qu2], [P.YF3Qu3], [P.YF3u1], [P.YF3u2], [P.YF3u3], [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d1], [P.YS3d2], [P.YS3d3], [P.YS3Qd1], [P.YS3Qd2], [P.YS3Qd3], [P.YS3Qu1], [P.YS3Qu2], [P.YS3Qu3], [P.YS3u1], [P.YS3u2], [P.YS3u3] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,1,5):C.UVGC_257_132,(0,1,6):C.UVGC_257_131,(2,1,5):C.UVGC_257_132,(2,1,6):C.UVGC_257_131,(5,1,5):C.UVGC_256_129,(5,1,6):C.UVGC_256_130,(1,1,5):C.UVGC_256_129,(1,1,6):C.UVGC_256_130,(7,1,0):C.UVGC_265_265,(7,1,3):C.UVGC_265_266,(7,1,4):C.UVGC_265_267,(7,1,5):C.UVGC_266_297,(7,1,6):C.UVGC_266_298,(7,1,7):C.UVGC_265_270,(7,1,8):C.UVGC_265_271,(7,1,9):C.UVGC_265_272,(7,1,10):C.UVGC_265_273,(7,1,11):C.UVGC_265_274,(7,1,12):C.UVGC_265_275,(7,1,13):C.UVGC_265_276,(7,1,14):C.UVGC_265_277,(7,1,15):C.UVGC_265_278,(7,1,16):C.UVGC_265_279,(7,1,17):C.UVGC_265_280,(7,1,18):C.UVGC_265_281,(7,1,19):C.UVGC_265_282,(7,1,20):C.UVGC_265_283,(7,1,21):C.UVGC_265_284,(7,1,22):C.UVGC_265_285,(7,1,24):C.UVGC_265_286,(7,1,25):C.UVGC_265_287,(7,1,26):C.UVGC_265_288,(7,1,27):C.UVGC_265_289,(7,1,28):C.UVGC_265_290,(7,1,29):C.UVGC_265_291,(7,1,30):C.UVGC_265_292,(7,1,31):C.UVGC_265_293,(7,1,32):C.UVGC_265_294,(7,1,33):C.UVGC_265_295,(7,1,34):C.UVGC_265_296,(4,1,5):C.UVGC_256_129,(4,1,6):C.UVGC_256_130,(3,1,5):C.UVGC_256_129,(3,1,6):C.UVGC_256_130,(8,1,5):C.UVGC_257_131,(8,1,6):C.UVGC_257_132,(6,1,0):C.UVGC_265_265,(6,1,3):C.UVGC_265_266,(6,1,4):C.UVGC_265_267,(6,1,5):C.UVGC_265_268,(6,1,6):C.UVGC_265_269,(6,1,7):C.UVGC_265_270,(6,1,8):C.UVGC_265_271,(6,1,9):C.UVGC_265_272,(6,1,10):C.UVGC_265_273,(6,1,11):C.UVGC_265_274,(6,1,12):C.UVGC_265_275,(6,1,13):C.UVGC_265_276,(6,1,14):C.UVGC_265_277,(6,1,15):C.UVGC_265_278,(6,1,16):C.UVGC_265_279,(6,1,17):C.UVGC_265_280,(6,1,18):C.UVGC_265_281,(6,1,19):C.UVGC_265_282,(6,1,20):C.UVGC_265_283,(6,1,21):C.UVGC_265_284,(6,1,22):C.UVGC_265_285,(6,1,24):C.UVGC_265_286,(6,1,25):C.UVGC_265_287,(6,1,26):C.UVGC_265_288,(6,1,27):C.UVGC_265_289,(6,1,28):C.UVGC_265_290,(6,1,29):C.UVGC_265_291,(6,1,30):C.UVGC_265_292,(6,1,31):C.UVGC_265_293,(6,1,32):C.UVGC_265_294,(6,1,33):C.UVGC_265_295,(6,1,34):C.UVGC_265_296,(11,0,5):C.UVGC_260_135,(11,0,6):C.UVGC_260_136,(10,0,5):C.UVGC_260_135,(10,0,6):C.UVGC_260_136,(9,0,5):C.UVGC_259_133,(9,0,6):C.UVGC_259_134,(0,2,5):C.UVGC_257_132,(0,2,6):C.UVGC_257_131,(2,2,5):C.UVGC_257_132,(2,2,6):C.UVGC_257_131,(5,2,5):C.UVGC_256_129,(5,2,6):C.UVGC_256_130,(1,2,5):C.UVGC_256_129,(1,2,6):C.UVGC_256_130,(7,2,2):C.UVGC_267_299,(7,2,5):C.UVGC_257_131,(7,2,6):C.UVGC_270_363,(6,2,0):C.UVGC_264_233,(6,2,3):C.UVGC_264_234,(6,2,4):C.UVGC_264_235,(6,2,5):C.UVGC_271_364,(6,2,6):C.UVGC_271_365,(6,2,7):C.UVGC_264_238,(6,2,8):C.UVGC_264_239,(6,2,9):C.UVGC_264_240,(6,2,10):C.UVGC_264_241,(6,2,11):C.UVGC_264_242,(6,2,12):C.UVGC_264_243,(6,2,13):C.UVGC_264_244,(6,2,14):C.UVGC_264_245,(6,2,15):C.UVGC_264_246,(6,2,16):C.UVGC_264_247,(6,2,17):C.UVGC_264_248,(6,2,18):C.UVGC_264_249,(6,2,19):C.UVGC_264_250,(6,2,20):C.UVGC_264_251,(6,2,21):C.UVGC_264_252,(6,2,22):C.UVGC_271_366,(6,2,24):C.UVGC_271_367,(6,2,25):C.UVGC_271_368,(6,2,26):C.UVGC_271_369,(6,2,27):C.UVGC_271_370,(6,2,28):C.UVGC_271_371,(6,2,29):C.UVGC_271_372,(6,2,30):C.UVGC_271_373,(6,2,31):C.UVGC_271_374,(6,2,32):C.UVGC_271_375,(6,2,33):C.UVGC_271_376,(6,2,34):C.UVGC_271_377,(4,2,5):C.UVGC_256_129,(4,2,6):C.UVGC_256_130,(3,2,5):C.UVGC_256_129,(3,2,6):C.UVGC_256_130,(8,2,0):C.UVGC_269_332,(8,2,3):C.UVGC_269_333,(8,2,4):C.UVGC_269_334,(8,2,5):C.UVGC_266_297,(8,2,6):C.UVGC_269_335,(8,2,7):C.UVGC_269_336,(8,2,8):C.UVGC_269_337,(8,2,9):C.UVGC_269_338,(8,2,10):C.UVGC_269_339,(8,2,11):C.UVGC_269_340,(8,2,12):C.UVGC_269_341,(8,2,13):C.UVGC_269_342,(8,2,14):C.UVGC_269_343,(8,2,15):C.UVGC_269_344,(8,2,16):C.UVGC_269_345,(8,2,17):C.UVGC_269_346,(8,2,18):C.UVGC_269_347,(8,2,19):C.UVGC_269_348,(8,2,20):C.UVGC_269_349,(8,2,21):C.UVGC_269_350,(8,2,22):C.UVGC_269_351,(8,2,24):C.UVGC_269_352,(8,2,25):C.UVGC_269_353,(8,2,26):C.UVGC_269_354,(8,2,27):C.UVGC_269_355,(8,2,28):C.UVGC_269_356,(8,2,29):C.UVGC_269_357,(8,2,30):C.UVGC_269_358,(8,2,31):C.UVGC_269_359,(8,2,32):C.UVGC_269_360,(8,2,33):C.UVGC_269_361,(8,2,34):C.UVGC_269_362,(0,3,5):C.UVGC_257_132,(0,3,6):C.UVGC_257_131,(2,3,5):C.UVGC_257_132,(2,3,6):C.UVGC_257_131,(5,3,5):C.UVGC_256_129,(5,3,6):C.UVGC_256_130,(1,3,5):C.UVGC_256_129,(1,3,6):C.UVGC_256_130,(7,3,0):C.UVGC_264_233,(7,3,3):C.UVGC_264_234,(7,3,4):C.UVGC_264_235,(7,3,5):C.UVGC_264_236,(7,3,6):C.UVGC_264_237,(7,3,7):C.UVGC_264_238,(7,3,8):C.UVGC_264_239,(7,3,9):C.UVGC_264_240,(7,3,10):C.UVGC_264_241,(7,3,11):C.UVGC_264_242,(7,3,12):C.UVGC_264_243,(7,3,13):C.UVGC_264_244,(7,3,14):C.UVGC_264_245,(7,3,15):C.UVGC_264_246,(7,3,16):C.UVGC_264_247,(7,3,17):C.UVGC_264_248,(7,3,18):C.UVGC_264_249,(7,3,19):C.UVGC_264_250,(7,3,20):C.UVGC_264_251,(7,3,21):C.UVGC_264_252,(7,3,22):C.UVGC_264_253,(7,3,24):C.UVGC_264_254,(7,3,25):C.UVGC_264_255,(7,3,26):C.UVGC_264_256,(7,3,27):C.UVGC_264_257,(7,3,28):C.UVGC_264_258,(7,3,29):C.UVGC_264_259,(7,3,30):C.UVGC_264_260,(7,3,31):C.UVGC_264_261,(7,3,32):C.UVGC_264_262,(7,3,33):C.UVGC_264_263,(7,3,34):C.UVGC_264_264,(4,3,5):C.UVGC_256_129,(4,3,6):C.UVGC_256_130,(3,3,5):C.UVGC_256_129,(3,3,6):C.UVGC_256_130,(8,3,0):C.UVGC_268_301,(8,3,3):C.UVGC_268_302,(8,3,4):C.UVGC_268_303,(8,3,5):C.UVGC_264_236,(8,3,6):C.UVGC_268_304,(8,3,7):C.UVGC_268_305,(8,3,8):C.UVGC_268_306,(8,3,9):C.UVGC_268_307,(8,3,10):C.UVGC_268_308,(8,3,11):C.UVGC_268_309,(8,3,12):C.UVGC_268_310,(8,3,13):C.UVGC_268_311,(8,3,14):C.UVGC_268_312,(8,3,15):C.UVGC_268_313,(8,3,16):C.UVGC_268_314,(8,3,17):C.UVGC_268_315,(8,3,18):C.UVGC_268_316,(8,3,19):C.UVGC_268_317,(8,3,20):C.UVGC_268_318,(8,3,21):C.UVGC_268_319,(8,3,22):C.UVGC_268_320,(8,3,24):C.UVGC_268_321,(8,3,25):C.UVGC_268_322,(8,3,26):C.UVGC_268_323,(8,3,27):C.UVGC_268_324,(8,3,28):C.UVGC_268_325,(8,3,29):C.UVGC_268_326,(8,3,30):C.UVGC_268_327,(8,3,31):C.UVGC_268_328,(8,3,32):C.UVGC_268_329,(8,3,33):C.UVGC_268_330,(8,3,34):C.UVGC_268_331,(6,3,1):C.UVGC_267_299,(6,3,6):C.UVGC_259_133,(6,3,23):C.UVGC_267_300})

V_437 = CTVertex(name = 'V_437',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_173_46,(0,2,0):C.UVGC_175_48})

V_438 = CTVertex(name = 'V_438',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_181_54,(0,2,0):C.UVGC_183_56})

V_439 = CTVertex(name = 'V_439',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_189_62,(0,2,0):C.UVGC_191_64})

V_440 = CTVertex(name = 'V_440',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_197_70,(0,2,0):C.UVGC_199_72})

V_441 = CTVertex(name = 'V_441',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_203_76,(0,2,0):C.UVGC_205_78})

V_442 = CTVertex(name = 'V_442',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_209_82,(0,2,0):C.UVGC_211_84})

V_443 = CTVertex(name = 'V_443',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_215_88,(0,2,0):C.UVGC_217_90})

V_444 = CTVertex(name = 'V_444',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_221_94,(0,2,0):C.UVGC_223_96})

V_445 = CTVertex(name = 'V_445',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_227_100,(0,2,0):C.UVGC_229_102})

V_446 = CTVertex(name = 'V_446',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_233_106,(0,2,0):C.UVGC_235_108})

V_447 = CTVertex(name = 'V_447',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_241_114,(0,2,0):C.UVGC_243_116})

V_448 = CTVertex(name = 'V_448',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_249_122,(0,2,0):C.UVGC_251_124})

V_449 = CTVertex(name = 'V_449',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_746_1019,(0,0,2):C.UVGC_747_1021,(0,0,1):C.UVGC_568_885})

V_450 = CTVertex(name = 'V_450',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_567_881,(0,0,2):C.UVGC_568_884,(0,0,1):C.UVGC_568_885})

V_451 = CTVertex(name = 'V_451',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_860,(0,0,2):C.UVGC_560_863,(0,0,1):C.UVGC_560_864})

V_452 = CTVertex(name = 'V_452',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_732_988,(0,0,2):C.UVGC_733_990,(0,0,1):C.UVGC_560_864})

V_453 = CTVertex(name = 'V_453',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1004,(0,0,2):C.UVGC_740_1006,(0,0,1):C.UVGC_555_850})

V_454 = CTVertex(name = 'V_454',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_554_846,(0,0,2):C.UVGC_555_849,(0,0,1):C.UVGC_555_850})

V_455 = CTVertex(name = 'V_455',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_565_876,(0,0,2):C.UVGC_566_879,(0,0,1):C.UVGC_566_880})

V_456 = CTVertex(name = 'V_456',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_730_983,(0,0,2):C.UVGC_731_986,(0,0,1):C.UVGC_731_987})

V_457 = CTVertex(name = 'V_457',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_552_841,(0,0,2):C.UVGC_553_844,(0,0,1):C.UVGC_553_845})

V_458 = CTVertex(name = 'V_458',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_748_1022,(0,0,2):C.UVGC_749_1025,(0,0,1):C.UVGC_749_1026})

V_459 = CTVertex(name = 'V_459',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_865,(0,0,2):C.UVGC_562_868,(0,0,1):C.UVGC_562_869})

V_460 = CTVertex(name = 'V_460',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_741_1007,(0,0,2):C.UVGC_742_1010,(0,0,1):C.UVGC_742_1011})

V_461 = CTVertex(name = 'V_461',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_735_993,(0,0,2):C.UVGC_735_994,(0,0,1):C.UVGC_735_995})

V_462 = CTVertex(name = 'V_462',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_466_793})

V_463 = CTVertex(name = 'V_463',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_465_792})

V_464 = CTVertex(name = 'V_464',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_565_876,(0,0,2):C.UVGC_566_879,(0,0,1):C.UVGC_566_880})

V_465 = CTVertex(name = 'V_465',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_730_983,(0,0,2):C.UVGC_731_986,(0,0,1):C.UVGC_731_987})

V_466 = CTVertex(name = 'V_466',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_552_841,(0,0,2):C.UVGC_553_844,(0,0,1):C.UVGC_553_845})

V_467 = CTVertex(name = 'V_467',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_748_1022,(0,0,2):C.UVGC_749_1025,(0,0,1):C.UVGC_749_1026})

V_468 = CTVertex(name = 'V_468',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_865,(0,0,2):C.UVGC_562_868,(0,0,1):C.UVGC_562_869})

V_469 = CTVertex(name = 'V_469',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_741_1007,(0,0,2):C.UVGC_742_1010,(0,0,1):C.UVGC_742_1011})

V_470 = CTVertex(name = 'V_470',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_746_1019,(0,0,2):C.UVGC_747_1021,(0,0,1):C.UVGC_568_885})

V_471 = CTVertex(name = 'V_471',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_567_881,(0,0,2):C.UVGC_568_884,(0,0,1):C.UVGC_568_885})

V_472 = CTVertex(name = 'V_472',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_860,(0,0,2):C.UVGC_560_863,(0,0,1):C.UVGC_560_864})

V_473 = CTVertex(name = 'V_473',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_732_988,(0,0,2):C.UVGC_733_990,(0,0,1):C.UVGC_560_864})

V_474 = CTVertex(name = 'V_474',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1004,(0,0,2):C.UVGC_740_1006,(0,0,1):C.UVGC_555_850})

V_475 = CTVertex(name = 'V_475',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_554_846,(0,0,2):C.UVGC_555_849,(0,0,1):C.UVGC_555_850})

V_476 = CTVertex(name = 'V_476',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_200_73,(0,2,5):C.UVGC_201_74})

V_477 = CTVertex(name = 'V_477',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_206_79,(0,2,5):C.UVGC_207_80})

V_478 = CTVertex(name = 'V_478',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_212_85,(0,2,5):C.UVGC_213_86})

V_479 = CTVertex(name = 'V_479',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_218_91,(0,2,5):C.UVGC_219_92})

V_480 = CTVertex(name = 'V_480',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_224_97,(0,2,5):C.UVGC_225_98})

V_481 = CTVertex(name = 'V_481',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_230_103,(0,2,5):C.UVGC_231_104})

V_482 = CTVertex(name = 'V_482',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_236_109,(0,2,5):C.UVGC_237_110})

V_483 = CTVertex(name = 'V_483',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_244_117,(0,2,5):C.UVGC_245_118})

V_484 = CTVertex(name = 'V_484',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_252_125,(0,2,5):C.UVGC_253_126})

V_485 = CTVertex(name = 'V_485',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_176_49,(0,2,5):C.UVGC_177_50})

V_486 = CTVertex(name = 'V_486',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_184_57,(0,2,5):C.UVGC_185_58})

V_487 = CTVertex(name = 'V_487',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YF3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_192_65,(0,2,5):C.UVGC_193_66})

V_488 = CTVertex(name = 'V_488',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_512_810,(0,1,2):C.UVGC_512_811,(0,2,0):C.UVGC_513_812,(0,2,2):C.UVGC_513_813})

V_489 = CTVertex(name = 'V_489',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_521_818,(0,1,2):C.UVGC_521_819,(0,2,0):C.UVGC_522_820,(0,2,2):C.UVGC_522_821})

V_490 = CTVertex(name = 'V_490',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_530_825,(0,1,2):C.UVGC_530_826,(0,2,0):C.UVGC_531_827,(0,2,2):C.UVGC_531_828})

V_491 = CTVertex(name = 'V_491',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_512_810,(0,1,2):C.UVGC_512_811,(0,2,0):C.UVGC_513_812,(0,2,2):C.UVGC_513_813})

V_492 = CTVertex(name = 'V_492',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ], [ [P.g, P.YF3Qd2, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_521_818,(0,1,2):C.UVGC_521_819,(0,2,0):C.UVGC_522_820,(0,2,2):C.UVGC_522_821})

V_493 = CTVertex(name = 'V_493',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_530_825,(0,1,2):C.UVGC_530_826,(0,2,0):C.UVGC_531_827,(0,2,2):C.UVGC_531_828})

V_494 = CTVertex(name = 'V_494',
                 type = 'UV',
                 particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_288_387})

V_495 = CTVertex(name = 'V_495',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_563_870,(0,0,2):C.UVGC_563_871,(0,0,1):C.UVGC_563_872})

V_496 = CTVertex(name = 'V_496',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_563_870,(0,0,2):C.UVGC_563_871,(0,0,1):C.UVGC_563_872})

V_497 = CTVertex(name = 'V_497',
                 type = 'UV',
                 particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_290_421})

V_498 = CTVertex(name = 'V_498',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_563_870,(0,0,2):C.UVGC_563_871,(0,0,1):C.UVGC_563_872})

V_499 = CTVertex(name = 'V_499',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3d1] ], [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_563_870,(0,0,2):C.UVGC_563_871,(0,0,1):C.UVGC_563_872})

V_500 = CTVertex(name = 'V_500',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_289_388})

V_501 = CTVertex(name = 'V_501',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_291_454})

V_502 = CTVertex(name = 'V_502',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_294_491,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_294_491,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_503 = CTVertex(name = 'V_503',
                 type = 'UV',
                 particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_301_530})

V_504 = CTVertex(name = 'V_504',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_728_978,(0,0,2):C.UVGC_728_979,(0,0,1):C.UVGC_728_980})

V_505 = CTVertex(name = 'V_505',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_728_978,(0,0,2):C.UVGC_728_979,(0,0,1):C.UVGC_728_980})

V_506 = CTVertex(name = 'V_506',
                 type = 'UV',
                 particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_303_532})

V_507 = CTVertex(name = 'V_507',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_728_978,(0,0,2):C.UVGC_728_979,(0,0,1):C.UVGC_728_980})

V_508 = CTVertex(name = 'V_508',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3d2] ], [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_728_978,(0,0,2):C.UVGC_728_979,(0,0,1):C.UVGC_728_980})

V_509 = CTVertex(name = 'V_509',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_302_531})

V_510 = CTVertex(name = 'V_510',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_304_533})

V_511 = CTVertex(name = 'V_511',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_307_534,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_307_534,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_512 = CTVertex(name = 'V_512',
                 type = 'UV',
                 particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_315_542,(0,1,0):C.UVGC_314_541})

V_513 = CTVertex(name = 'V_513',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_550_835,(0,0,2):C.UVGC_550_836,(0,0,1):C.UVGC_550_837})

V_514 = CTVertex(name = 'V_514',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_550_835,(0,0,2):C.UVGC_550_836,(0,0,1):C.UVGC_550_837})

V_515 = CTVertex(name = 'V_515',
                 type = 'UV',
                 particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_318_545,(0,1,0):C.UVGC_261_137,(0,1,1):C.UVGC_261_138,(0,1,2):C.UVGC_261_139,(0,1,3):C.UVGC_261_140,(0,1,4):C.UVGC_261_141,(0,1,6):C.UVGC_261_142,(0,1,7):C.UVGC_261_143,(0,1,8):C.UVGC_261_144,(0,1,9):C.UVGC_261_145,(0,1,10):C.UVGC_261_146,(0,1,11):C.UVGC_261_147,(0,1,12):C.UVGC_261_148,(0,1,13):C.UVGC_261_149,(0,1,14):C.UVGC_261_150,(0,1,15):C.UVGC_261_151,(0,1,16):C.UVGC_261_152,(0,1,17):C.UVGC_261_153,(0,1,18):C.UVGC_261_154,(0,1,19):C.UVGC_261_155,(0,1,20):C.UVGC_261_156,(0,1,21):C.UVGC_261_157,(0,1,22):C.UVGC_261_158,(0,1,23):C.UVGC_261_159,(0,1,24):C.UVGC_261_160,(0,1,25):C.UVGC_261_161,(0,1,26):C.UVGC_261_162,(0,1,27):C.UVGC_261_163,(0,1,28):C.UVGC_261_164,(0,1,29):C.UVGC_261_165,(0,1,30):C.UVGC_261_166,(0,1,31):C.UVGC_261_167,(0,1,32):C.UVGC_261_168,(0,1,5):C.UVGC_317_544})

V_516 = CTVertex(name = 'V_516',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_550_835,(0,0,2):C.UVGC_550_836,(0,0,1):C.UVGC_550_837})

V_517 = CTVertex(name = 'V_517',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3d3] ], [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_550_835,(0,0,2):C.UVGC_550_836,(0,0,1):C.UVGC_550_837})

V_518 = CTVertex(name = 'V_518',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_316_543})

V_519 = CTVertex(name = 'V_519',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_319_546})

V_520 = CTVertex(name = 'V_520',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_322_547,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_322_547,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_521 = CTVertex(name = 'V_521',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_330_555,(0,1,0):C.UVGC_329_554})

V_522 = CTVertex(name = 'V_522',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_564_873,(0,0,2):C.UVGC_564_874,(0,0,1):C.UVGC_564_875})

V_523 = CTVertex(name = 'V_523',
                 type = 'UV',
                 particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_564_873,(0,0,2):C.UVGC_564_874,(0,0,1):C.UVGC_564_875})

V_524 = CTVertex(name = 'V_524',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_630_903,(0,0,2):C.UVGC_630_904,(0,0,1):C.UVGC_630_905,(0,1,0):C.UVGC_629_901,(0,1,2):C.UVGC_629_902,(0,1,1):C.UVGC_558_859})

V_525 = CTVertex(name = 'V_525',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_333_558,(0,1,0):C.UVGC_261_137,(0,1,1):C.UVGC_261_138,(0,1,2):C.UVGC_261_139,(0,1,3):C.UVGC_261_140,(0,1,4):C.UVGC_261_141,(0,1,6):C.UVGC_261_142,(0,1,7):C.UVGC_261_143,(0,1,8):C.UVGC_261_144,(0,1,9):C.UVGC_261_145,(0,1,10):C.UVGC_261_146,(0,1,11):C.UVGC_261_147,(0,1,12):C.UVGC_261_148,(0,1,13):C.UVGC_261_149,(0,1,14):C.UVGC_261_150,(0,1,15):C.UVGC_261_151,(0,1,16):C.UVGC_261_152,(0,1,17):C.UVGC_261_153,(0,1,18):C.UVGC_261_154,(0,1,19):C.UVGC_261_155,(0,1,20):C.UVGC_261_156,(0,1,21):C.UVGC_261_157,(0,1,22):C.UVGC_261_158,(0,1,23):C.UVGC_261_159,(0,1,24):C.UVGC_261_160,(0,1,25):C.UVGC_261_161,(0,1,26):C.UVGC_261_162,(0,1,27):C.UVGC_261_163,(0,1,28):C.UVGC_261_164,(0,1,29):C.UVGC_261_165,(0,1,30):C.UVGC_261_166,(0,1,31):C.UVGC_261_167,(0,1,32):C.UVGC_261_168,(0,1,5):C.UVGC_332_557})

V_526 = CTVertex(name = 'V_526',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_564_873,(0,0,2):C.UVGC_564_874,(0,0,1):C.UVGC_564_875})

V_527 = CTVertex(name = 'V_527',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_564_873,(0,0,2):C.UVGC_564_874,(0,0,1):C.UVGC_564_875})

V_528 = CTVertex(name = 'V_528',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_628_899,(0,0,2):C.UVGC_628_900,(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_631_906,(0,1,2):C.UVGC_631_907,(0,1,1):C.UVGC_630_905})

V_529 = CTVertex(name = 'V_529',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_331_556})

V_530 = CTVertex(name = 'V_530',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_627_898,(0,0,2):C.UVGC_626_895,(0,0,1):C.UVGC_626_897})

V_531 = CTVertex(name = 'V_531',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_334_559})

V_532 = CTVertex(name = 'V_532',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_337_560,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_337_560,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_533 = CTVertex(name = 'V_533',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_345_600,(0,1,0):C.UVGC_344_599})

V_534 = CTVertex(name = 'V_534',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_729_981,(0,0,2):C.UVGC_729_982,(0,0,1):C.UVGC_556_853})

V_535 = CTVertex(name = 'V_535',
                 type = 'UV',
                 particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_729_981,(0,0,2):C.UVGC_729_982,(0,0,1):C.UVGC_556_853})

V_536 = CTVertex(name = 'V_536',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_663_954,(0,0,2):C.UVGC_663_955,(0,0,1):C.UVGC_630_905,(0,1,0):C.UVGC_662_952,(0,1,2):C.UVGC_662_953,(0,1,1):C.UVGC_558_859})

V_537 = CTVertex(name = 'V_537',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_348_603,(0,1,0):C.UVGC_261_137,(0,1,1):C.UVGC_261_138,(0,1,2):C.UVGC_261_139,(0,1,3):C.UVGC_261_140,(0,1,4):C.UVGC_261_141,(0,1,6):C.UVGC_261_142,(0,1,7):C.UVGC_261_143,(0,1,8):C.UVGC_261_144,(0,1,9):C.UVGC_261_145,(0,1,10):C.UVGC_261_146,(0,1,11):C.UVGC_261_147,(0,1,12):C.UVGC_261_148,(0,1,13):C.UVGC_261_149,(0,1,14):C.UVGC_261_150,(0,1,15):C.UVGC_261_151,(0,1,16):C.UVGC_261_152,(0,1,17):C.UVGC_261_153,(0,1,18):C.UVGC_261_154,(0,1,19):C.UVGC_261_155,(0,1,20):C.UVGC_261_156,(0,1,21):C.UVGC_261_157,(0,1,22):C.UVGC_261_158,(0,1,23):C.UVGC_261_159,(0,1,24):C.UVGC_261_160,(0,1,25):C.UVGC_261_161,(0,1,26):C.UVGC_261_162,(0,1,27):C.UVGC_261_163,(0,1,28):C.UVGC_261_164,(0,1,29):C.UVGC_261_165,(0,1,30):C.UVGC_261_166,(0,1,31):C.UVGC_261_167,(0,1,32):C.UVGC_261_168,(0,1,5):C.UVGC_347_602})

V_538 = CTVertex(name = 'V_538',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_729_981,(0,0,2):C.UVGC_729_982,(0,0,1):C.UVGC_556_853})

V_539 = CTVertex(name = 'V_539',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YS3Qd2] ], [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_729_981,(0,0,2):C.UVGC_729_982,(0,0,1):C.UVGC_556_853})

V_540 = CTVertex(name = 'V_540',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_661_950,(0,0,2):C.UVGC_661_951,(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_664_956,(0,1,2):C.UVGC_664_957,(0,1,1):C.UVGC_630_905})

V_541 = CTVertex(name = 'V_541',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_346_601})

V_542 = CTVertex(name = 'V_542',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_660_949,(0,0,2):C.UVGC_626_895,(0,0,1):C.UVGC_626_897})

V_543 = CTVertex(name = 'V_543',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_349_604})

V_544 = CTVertex(name = 'V_544',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_352_605,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_352_605,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_545 = CTVertex(name = 'V_545',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_360_613,(0,1,0):C.UVGC_359_612})

V_546 = CTVertex(name = 'V_546',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_551_838,(0,0,2):C.UVGC_551_839,(0,0,1):C.UVGC_551_840})

V_547 = CTVertex(name = 'V_547',
                 type = 'UV',
                 particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_551_838,(0,0,2):C.UVGC_551_839,(0,0,1):C.UVGC_551_840})

V_548 = CTVertex(name = 'V_548',
                 type = 'UV',
                 particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_694_970,(0,0,2):C.UVGC_694_971,(0,0,1):C.UVGC_630_905,(0,1,0):C.UVGC_693_968,(0,1,2):C.UVGC_693_969,(0,1,1):C.UVGC_558_859})

V_549 = CTVertex(name = 'V_549',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_363_616,(0,1,0):C.UVGC_261_137,(0,1,1):C.UVGC_261_138,(0,1,2):C.UVGC_261_139,(0,1,3):C.UVGC_261_140,(0,1,4):C.UVGC_261_141,(0,1,6):C.UVGC_261_142,(0,1,7):C.UVGC_261_143,(0,1,8):C.UVGC_261_144,(0,1,9):C.UVGC_261_145,(0,1,10):C.UVGC_261_146,(0,1,11):C.UVGC_261_147,(0,1,12):C.UVGC_261_148,(0,1,13):C.UVGC_261_149,(0,1,14):C.UVGC_261_150,(0,1,15):C.UVGC_261_151,(0,1,16):C.UVGC_261_152,(0,1,17):C.UVGC_261_153,(0,1,18):C.UVGC_261_154,(0,1,19):C.UVGC_261_155,(0,1,20):C.UVGC_261_156,(0,1,21):C.UVGC_261_157,(0,1,22):C.UVGC_261_158,(0,1,23):C.UVGC_261_159,(0,1,24):C.UVGC_261_160,(0,1,25):C.UVGC_261_161,(0,1,26):C.UVGC_261_162,(0,1,27):C.UVGC_261_163,(0,1,28):C.UVGC_261_164,(0,1,29):C.UVGC_261_165,(0,1,30):C.UVGC_261_166,(0,1,31):C.UVGC_261_167,(0,1,32):C.UVGC_261_168,(0,1,5):C.UVGC_362_615})

V_550 = CTVertex(name = 'V_550',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_551_838,(0,0,2):C.UVGC_551_839,(0,0,1):C.UVGC_551_840})

V_551 = CTVertex(name = 'V_551',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_551_838,(0,0,2):C.UVGC_551_839,(0,0,1):C.UVGC_551_840})

V_552 = CTVertex(name = 'V_552',
                 type = 'UV',
                 particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_692_966,(0,0,2):C.UVGC_692_967,(0,0,1):C.UVGC_558_859,(0,1,0):C.UVGC_695_972,(0,1,2):C.UVGC_695_973,(0,1,1):C.UVGC_630_905})

V_553 = CTVertex(name = 'V_553',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_361_614})

V_554 = CTVertex(name = 'V_554',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_691_965,(0,0,2):C.UVGC_626_895,(0,0,1):C.UVGC_626_897})

V_555 = CTVertex(name = 'V_555',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_291_422,(0,0,1):C.UVGC_291_423,(0,0,2):C.UVGC_291_424,(0,0,3):C.UVGC_291_425,(0,0,4):C.UVGC_291_426,(0,0,6):C.UVGC_291_427,(0,0,7):C.UVGC_291_428,(0,0,8):C.UVGC_291_429,(0,0,9):C.UVGC_291_430,(0,0,10):C.UVGC_291_431,(0,0,11):C.UVGC_291_432,(0,0,12):C.UVGC_291_433,(0,0,13):C.UVGC_291_434,(0,0,14):C.UVGC_291_435,(0,0,15):C.UVGC_291_436,(0,0,16):C.UVGC_291_437,(0,0,17):C.UVGC_291_438,(0,0,18):C.UVGC_291_439,(0,0,19):C.UVGC_291_440,(0,0,20):C.UVGC_291_441,(0,0,21):C.UVGC_291_442,(0,0,22):C.UVGC_291_443,(0,0,23):C.UVGC_291_444,(0,0,24):C.UVGC_291_445,(0,0,25):C.UVGC_291_446,(0,0,26):C.UVGC_291_447,(0,0,27):C.UVGC_291_448,(0,0,28):C.UVGC_291_449,(0,0,29):C.UVGC_291_450,(0,0,30):C.UVGC_291_451,(0,0,31):C.UVGC_291_452,(0,0,32):C.UVGC_291_453,(0,0,5):C.UVGC_364_617})

V_556 = CTVertex(name = 'V_556',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_367_618,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_367_618,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_557 = CTVertex(name = 'V_557',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_374_625,(0,1,0):C.UVGC_375_626})

V_558 = CTVertex(name = 'V_558',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_744_1014,(0,0,2):C.UVGC_744_1015,(0,0,1):C.UVGC_564_875})

V_559 = CTVertex(name = 'V_559',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_744_1014,(0,0,2):C.UVGC_744_1015,(0,0,1):C.UVGC_564_875})

V_560 = CTVertex(name = 'V_560',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_632_908,(0,0,2):C.UVGC_632_909,(0,0,1):C.UVGC_632_910})

V_561 = CTVertex(name = 'V_561',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_633_943,(0,0,7):C.UVGC_633_944,(0,0,6):C.UVGC_633_945})

V_562 = CTVertex(name = 'V_562',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_378_629,(0,1,0):C.UVGC_261_137,(0,1,1):C.UVGC_261_138,(0,1,2):C.UVGC_261_139,(0,1,3):C.UVGC_261_140,(0,1,4):C.UVGC_261_141,(0,1,6):C.UVGC_261_142,(0,1,7):C.UVGC_261_143,(0,1,8):C.UVGC_261_144,(0,1,9):C.UVGC_261_145,(0,1,10):C.UVGC_261_146,(0,1,11):C.UVGC_261_147,(0,1,12):C.UVGC_261_148,(0,1,13):C.UVGC_261_149,(0,1,14):C.UVGC_261_150,(0,1,15):C.UVGC_261_151,(0,1,16):C.UVGC_261_152,(0,1,17):C.UVGC_261_153,(0,1,18):C.UVGC_261_154,(0,1,19):C.UVGC_261_155,(0,1,20):C.UVGC_261_156,(0,1,21):C.UVGC_261_157,(0,1,22):C.UVGC_261_158,(0,1,23):C.UVGC_261_159,(0,1,24):C.UVGC_261_160,(0,1,25):C.UVGC_261_161,(0,1,26):C.UVGC_261_162,(0,1,27):C.UVGC_261_163,(0,1,28):C.UVGC_261_164,(0,1,29):C.UVGC_261_165,(0,1,30):C.UVGC_261_166,(0,1,31):C.UVGC_261_167,(0,1,32):C.UVGC_261_168,(0,1,5):C.UVGC_377_628})

V_563 = CTVertex(name = 'V_563',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_744_1014,(0,0,2):C.UVGC_744_1015,(0,0,1):C.UVGC_564_875})

V_564 = CTVertex(name = 'V_564',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_744_1014,(0,0,2):C.UVGC_744_1015,(0,0,1):C.UVGC_564_875})

V_565 = CTVertex(name = 'V_565',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_632_908,(0,0,2):C.UVGC_632_909,(0,0,1):C.UVGC_632_910})

V_566 = CTVertex(name = 'V_566',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_633_943,(0,0,7):C.UVGC_633_944,(0,0,6):C.UVGC_633_945})

V_567 = CTVertex(name = 'V_567',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_376_627})

V_568 = CTVertex(name = 'V_568',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_626_895,(0,0,2):C.UVGC_626_896,(0,0,1):C.UVGC_626_897})

V_569 = CTVertex(name = 'V_569',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_379_662})

V_570 = CTVertex(name = 'V_570',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_382_663,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_382_663,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_571 = CTVertex(name = 'V_571',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS1, L.VSS3 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_389_702,(0,1,0):C.UVGC_390_703})

V_572 = CTVertex(name = 'V_572',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_556_851,(0,0,2):C.UVGC_556_852,(0,0,1):C.UVGC_556_853})

V_573 = CTVertex(name = 'V_573',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_556_851,(0,0,2):C.UVGC_556_852,(0,0,1):C.UVGC_556_853})

V_574 = CTVertex(name = 'V_574',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_665_958,(0,0,2):C.UVGC_665_959,(0,0,1):C.UVGC_632_910})

V_575 = CTVertex(name = 'V_575',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_666_960,(0,0,7):C.UVGC_666_961,(0,0,6):C.UVGC_633_945})

V_576 = CTVertex(name = 'V_576',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_392_705})

V_577 = CTVertex(name = 'V_577',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_556_851,(0,0,2):C.UVGC_556_852,(0,0,1):C.UVGC_556_853})

V_578 = CTVertex(name = 'V_578',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_556_851,(0,0,2):C.UVGC_556_852,(0,0,1):C.UVGC_556_853})

V_579 = CTVertex(name = 'V_579',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_665_958,(0,0,2):C.UVGC_665_959,(0,0,1):C.UVGC_632_910})

V_580 = CTVertex(name = 'V_580',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_666_960,(0,0,7):C.UVGC_666_961,(0,0,6):C.UVGC_633_945})

V_581 = CTVertex(name = 'V_581',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_391_704})

V_582 = CTVertex(name = 'V_582',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_626_895,(0,0,2):C.UVGC_659_948,(0,0,1):C.UVGC_626_897})

V_583 = CTVertex(name = 'V_583',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_393_706})

V_584 = CTVertex(name = 'V_584',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_396_707,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_396_707,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_585 = CTVertex(name = 'V_585',
                 type = 'UV',
                 particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_403_714})

V_586 = CTVertex(name = 'V_586',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_737_999,(0,0,2):C.UVGC_737_1000,(0,0,1):C.UVGC_551_840})

V_587 = CTVertex(name = 'V_587',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_737_999,(0,0,2):C.UVGC_737_1000,(0,0,1):C.UVGC_551_840})

V_588 = CTVertex(name = 'V_588',
                 type = 'UV',
                 particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_696_974,(0,0,2):C.UVGC_696_975,(0,0,1):C.UVGC_632_910})

V_589 = CTVertex(name = 'V_589',
                 type = 'UV',
                 particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'T(1,3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_697_976,(0,0,7):C.UVGC_697_977,(0,0,6):C.UVGC_633_945})

V_590 = CTVertex(name = 'V_590',
                 type = 'UV',
                 particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_405_716})

V_591 = CTVertex(name = 'V_591',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_737_999,(0,0,2):C.UVGC_737_1000,(0,0,1):C.UVGC_551_840})

V_592 = CTVertex(name = 'V_592',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_737_999,(0,0,2):C.UVGC_737_1000,(0,0,1):C.UVGC_551_840})

V_593 = CTVertex(name = 'V_593',
                 type = 'UV',
                 particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_696_974,(0,0,2):C.UVGC_696_975,(0,0,1):C.UVGC_632_910})

V_594 = CTVertex(name = 'V_594',
                 type = 'UV',
                 particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_633_911,(0,0,1):C.UVGC_633_912,(0,0,2):C.UVGC_633_913,(0,0,3):C.UVGC_633_914,(0,0,4):C.UVGC_633_915,(0,0,8):C.UVGC_633_916,(0,0,9):C.UVGC_633_917,(0,0,10):C.UVGC_633_918,(0,0,11):C.UVGC_633_919,(0,0,12):C.UVGC_633_920,(0,0,13):C.UVGC_633_921,(0,0,14):C.UVGC_633_922,(0,0,15):C.UVGC_633_923,(0,0,16):C.UVGC_633_924,(0,0,17):C.UVGC_633_925,(0,0,18):C.UVGC_633_926,(0,0,19):C.UVGC_633_927,(0,0,20):C.UVGC_633_928,(0,0,21):C.UVGC_633_929,(0,0,22):C.UVGC_633_930,(0,0,23):C.UVGC_633_931,(0,0,24):C.UVGC_633_932,(0,0,25):C.UVGC_633_933,(0,0,26):C.UVGC_633_934,(0,0,27):C.UVGC_633_935,(0,0,28):C.UVGC_633_936,(0,0,29):C.UVGC_633_937,(0,0,30):C.UVGC_633_938,(0,0,31):C.UVGC_633_939,(0,0,32):C.UVGC_633_940,(0,0,33):C.UVGC_633_941,(0,0,34):C.UVGC_633_942,(0,0,5):C.UVGC_697_976,(0,0,7):C.UVGC_697_977,(0,0,6):C.UVGC_633_945})

V_595 = CTVertex(name = 'V_595',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_404_715})

V_596 = CTVertex(name = 'V_596',
                 type = 'UV',
                 particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_626_895,(0,0,2):C.UVGC_690_964,(0,0,1):C.UVGC_626_897})

V_597 = CTVertex(name = 'V_597',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_406_717})

V_598 = CTVertex(name = 'V_598',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_409_718,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_409_718,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_599 = CTVertex(name = 'V_599',
                 type = 'UV',
                 particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_416_725})

V_600 = CTVertex(name = 'V_600',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_745_1016,(0,0,2):C.UVGC_745_1017,(0,0,1):C.UVGC_745_1018})

V_601 = CTVertex(name = 'V_601',
                 type = 'UV',
                 particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_745_1016,(0,0,2):C.UVGC_745_1017,(0,0,1):C.UVGC_745_1018})

V_602 = CTVertex(name = 'V_602',
                 type = 'UV',
                 particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_418_727})

V_603 = CTVertex(name = 'V_603',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_745_1016,(0,0,2):C.UVGC_745_1017,(0,0,1):C.UVGC_745_1018})

V_604 = CTVertex(name = 'V_604',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YS3u1] ], [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_745_1016,(0,0,2):C.UVGC_745_1017,(0,0,1):C.UVGC_745_1018})

V_605 = CTVertex(name = 'V_605',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_417_726})

V_606 = CTVertex(name = 'V_606',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_419_728})

V_607 = CTVertex(name = 'V_607',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_422_729,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_422_729,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_608 = CTVertex(name = 'V_608',
                 type = 'UV',
                 particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_429_768})

V_609 = CTVertex(name = 'V_609',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_557_854,(0,0,2):C.UVGC_557_855,(0,0,1):C.UVGC_557_856})

V_610 = CTVertex(name = 'V_610',
                 type = 'UV',
                 particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_557_854,(0,0,2):C.UVGC_557_855,(0,0,1):C.UVGC_557_856})

V_611 = CTVertex(name = 'V_611',
                 type = 'UV',
                 particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_431_770})

V_612 = CTVertex(name = 'V_612',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_557_854,(0,0,2):C.UVGC_557_855,(0,0,1):C.UVGC_557_856})

V_613 = CTVertex(name = 'V_613',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YS3u2] ], [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_557_854,(0,0,2):C.UVGC_557_855,(0,0,1):C.UVGC_557_856})

V_614 = CTVertex(name = 'V_614',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_430_769})

V_615 = CTVertex(name = 'V_615',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_432_771})

V_616 = CTVertex(name = 'V_616',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_435_772,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_435_772,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_617 = CTVertex(name = 'V_617',
                 type = 'UV',
                 particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_442_779})

V_618 = CTVertex(name = 'V_618',
                 type = 'UV',
                 particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1001,(0,0,2):C.UVGC_738_1002,(0,0,1):C.UVGC_738_1003})

V_619 = CTVertex(name = 'V_619',
                 type = 'UV',
                 particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.FFS3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1001,(0,0,2):C.UVGC_738_1002,(0,0,1):C.UVGC_738_1003})

V_620 = CTVertex(name = 'V_620',
                 type = 'UV',
                 particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,3,2)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_290_389,(0,0,1):C.UVGC_290_390,(0,0,2):C.UVGC_290_391,(0,0,3):C.UVGC_290_392,(0,0,4):C.UVGC_290_393,(0,0,6):C.UVGC_290_394,(0,0,7):C.UVGC_290_395,(0,0,8):C.UVGC_290_396,(0,0,9):C.UVGC_290_397,(0,0,10):C.UVGC_290_398,(0,0,11):C.UVGC_290_399,(0,0,12):C.UVGC_290_400,(0,0,13):C.UVGC_290_401,(0,0,14):C.UVGC_290_402,(0,0,15):C.UVGC_290_403,(0,0,16):C.UVGC_290_404,(0,0,17):C.UVGC_290_405,(0,0,18):C.UVGC_290_406,(0,0,19):C.UVGC_290_407,(0,0,20):C.UVGC_290_408,(0,0,21):C.UVGC_290_409,(0,0,22):C.UVGC_290_410,(0,0,23):C.UVGC_290_411,(0,0,24):C.UVGC_290_412,(0,0,25):C.UVGC_290_413,(0,0,26):C.UVGC_290_414,(0,0,27):C.UVGC_290_415,(0,0,28):C.UVGC_290_416,(0,0,29):C.UVGC_290_417,(0,0,30):C.UVGC_290_418,(0,0,31):C.UVGC_290_419,(0,0,32):C.UVGC_290_420,(0,0,5):C.UVGC_444_781})

V_621 = CTVertex(name = 'V_621',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1001,(0,0,2):C.UVGC_738_1002,(0,0,1):C.UVGC_738_1003})

V_622 = CTVertex(name = 'V_622',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
                 color = [ 'Identity(1,3)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YS3u3] ], [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_738_1001,(0,0,2):C.UVGC_738_1002,(0,0,1):C.UVGC_738_1003})

V_623 = CTVertex(name = 'V_623',
                 type = 'UV',
                 particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_443_780})

V_624 = CTVertex(name = 'V_624',
                 type = 'UV',
                 particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(2,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_379_630,(0,0,1):C.UVGC_379_631,(0,0,2):C.UVGC_379_632,(0,0,3):C.UVGC_379_633,(0,0,4):C.UVGC_379_634,(0,0,6):C.UVGC_379_635,(0,0,7):C.UVGC_379_636,(0,0,8):C.UVGC_379_637,(0,0,9):C.UVGC_379_638,(0,0,10):C.UVGC_379_639,(0,0,11):C.UVGC_379_640,(0,0,12):C.UVGC_379_641,(0,0,13):C.UVGC_379_642,(0,0,14):C.UVGC_379_643,(0,0,15):C.UVGC_379_644,(0,0,16):C.UVGC_379_645,(0,0,17):C.UVGC_379_646,(0,0,18):C.UVGC_379_647,(0,0,19):C.UVGC_379_648,(0,0,20):C.UVGC_379_649,(0,0,21):C.UVGC_379_650,(0,0,22):C.UVGC_379_651,(0,0,23):C.UVGC_379_652,(0,0,24):C.UVGC_379_653,(0,0,25):C.UVGC_379_654,(0,0,26):C.UVGC_379_655,(0,0,27):C.UVGC_379_656,(0,0,28):C.UVGC_379_657,(0,0,29):C.UVGC_379_658,(0,0,30):C.UVGC_379_659,(0,0,31):C.UVGC_379_660,(0,0,32):C.UVGC_379_661,(0,0,5):C.UVGC_445_782})

V_625 = CTVertex(name = 'V_625',
                 type = 'UV',
                 particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(2,0,0):C.UVGC_294_459,(2,0,1):C.UVGC_294_460,(2,0,2):C.UVGC_294_461,(2,0,3):C.UVGC_294_462,(2,0,4):C.UVGC_294_463,(2,0,6):C.UVGC_294_464,(2,0,7):C.UVGC_294_465,(2,0,8):C.UVGC_294_466,(2,0,9):C.UVGC_294_467,(2,0,10):C.UVGC_294_468,(2,0,11):C.UVGC_294_469,(2,0,12):C.UVGC_294_470,(2,0,13):C.UVGC_294_471,(2,0,14):C.UVGC_294_472,(2,0,15):C.UVGC_294_473,(2,0,16):C.UVGC_294_474,(2,0,17):C.UVGC_294_475,(2,0,18):C.UVGC_294_476,(2,0,19):C.UVGC_294_477,(2,0,20):C.UVGC_294_478,(2,0,21):C.UVGC_294_479,(2,0,22):C.UVGC_294_480,(2,0,23):C.UVGC_294_481,(2,0,24):C.UVGC_294_482,(2,0,25):C.UVGC_294_483,(2,0,26):C.UVGC_294_484,(2,0,27):C.UVGC_294_485,(2,0,28):C.UVGC_294_486,(2,0,29):C.UVGC_294_487,(2,0,30):C.UVGC_294_488,(2,0,31):C.UVGC_294_489,(2,0,32):C.UVGC_294_490,(2,0,5):C.UVGC_448_783,(1,0,0):C.UVGC_294_459,(1,0,1):C.UVGC_294_460,(1,0,2):C.UVGC_294_461,(1,0,3):C.UVGC_294_462,(1,0,4):C.UVGC_294_463,(1,0,6):C.UVGC_294_464,(1,0,7):C.UVGC_294_465,(1,0,8):C.UVGC_294_466,(1,0,9):C.UVGC_294_467,(1,0,10):C.UVGC_294_468,(1,0,11):C.UVGC_294_469,(1,0,12):C.UVGC_294_470,(1,0,13):C.UVGC_294_471,(1,0,14):C.UVGC_294_472,(1,0,15):C.UVGC_294_473,(1,0,16):C.UVGC_294_474,(1,0,17):C.UVGC_294_475,(1,0,18):C.UVGC_294_476,(1,0,19):C.UVGC_294_477,(1,0,20):C.UVGC_294_478,(1,0,21):C.UVGC_294_479,(1,0,22):C.UVGC_294_480,(1,0,23):C.UVGC_294_481,(1,0,24):C.UVGC_294_482,(1,0,25):C.UVGC_294_483,(1,0,26):C.UVGC_294_484,(1,0,27):C.UVGC_294_485,(1,0,28):C.UVGC_294_486,(1,0,29):C.UVGC_294_487,(1,0,30):C.UVGC_294_488,(1,0,31):C.UVGC_294_489,(1,0,32):C.UVGC_294_490,(1,0,5):C.UVGC_448_783,(0,0,3):C.UVGC_293_457,(0,0,5):C.UVGC_293_458})

V_626 = CTVertex(name = 'V_626',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS5 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_736_996,(0,0,2):C.UVGC_736_997,(0,0,1):C.UVGC_736_998})

V_627 = CTVertex(name = 'V_627',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_493_802,(0,1,0):C.UVGC_491_800,(0,2,0):C.UVGC_492_801})

V_628 = CTVertex(name = 'V_628',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_493_802,(0,1,0):C.UVGC_498_804,(0,2,0):C.UVGC_499_805})

V_629 = CTVertex(name = 'V_629',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_493_802,(0,1,0):C.UVGC_505_807,(0,2,0):C.UVGC_506_808})

V_630 = CTVertex(name = 'V_630',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_516_816,(0,1,0):C.UVGC_514_814,(0,2,0):C.UVGC_515_815})

V_631 = CTVertex(name = 'V_631',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_516_816,(0,1,0):C.UVGC_523_822,(0,2,0):C.UVGC_524_823})

V_632 = CTVertex(name = 'V_632',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_516_816,(0,1,0):C.UVGC_532_829,(0,2,0):C.UVGC_533_830})

V_633 = CTVertex(name = 'V_633',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_476_796,(0,1,0):C.UVGC_178_51,(0,2,0):C.UVGC_179_52})

V_634 = CTVertex(name = 'V_634',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_476_796,(0,1,0):C.UVGC_186_59,(0,2,0):C.UVGC_187_60})

V_635 = CTVertex(name = 'V_635',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_476_796,(0,1,0):C.UVGC_194_67,(0,2,0):C.UVGC_195_68})

V_636 = CTVertex(name = 'V_636',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_539_832,(0,1,0):C.UVGC_238_111,(0,2,0):C.UVGC_239_112})

V_637 = CTVertex(name = 'V_637',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_539_832,(0,1,0):C.UVGC_246_119,(0,2,0):C.UVGC_247_120})

V_638 = CTVertex(name = 'V_638',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_539_832,(0,1,0):C.UVGC_254_127,(0,2,0):C.UVGC_255_128})

V_639 = CTVertex(name = 'V_639',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_296_493})

V_640 = CTVertex(name = 'V_640',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_297_494})

V_641 = CTVertex(name = 'V_641',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_298_495,(0,0,1):C.UVGC_298_496,(0,0,2):C.UVGC_298_497,(0,0,3):C.UVGC_298_498,(0,0,4):C.UVGC_298_499,(0,0,6):C.UVGC_298_500,(0,0,7):C.UVGC_298_501,(0,0,8):C.UVGC_298_502,(0,0,9):C.UVGC_298_503,(0,0,10):C.UVGC_298_504,(0,0,11):C.UVGC_298_505,(0,0,12):C.UVGC_298_506,(0,0,13):C.UVGC_298_507,(0,0,14):C.UVGC_298_508,(0,0,15):C.UVGC_298_509,(0,0,16):C.UVGC_298_510,(0,0,17):C.UVGC_298_511,(0,0,18):C.UVGC_298_512,(0,0,19):C.UVGC_298_513,(0,0,20):C.UVGC_298_514,(0,0,21):C.UVGC_298_515,(0,0,22):C.UVGC_298_516,(0,0,23):C.UVGC_298_517,(0,0,24):C.UVGC_298_518,(0,0,25):C.UVGC_298_519,(0,0,26):C.UVGC_298_520,(0,0,27):C.UVGC_298_521,(0,0,28):C.UVGC_298_522,(0,0,29):C.UVGC_298_523,(0,0,30):C.UVGC_298_524,(0,0,31):C.UVGC_298_525,(0,0,32):C.UVGC_298_526,(0,0,5):C.UVGC_298_527})

V_642 = CTVertex(name = 'V_642',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_309_536})

V_643 = CTVertex(name = 'V_643',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_310_537})

V_644 = CTVertex(name = 'V_644',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_298_495,(0,0,1):C.UVGC_298_496,(0,0,2):C.UVGC_298_497,(0,0,3):C.UVGC_298_498,(0,0,4):C.UVGC_298_499,(0,0,6):C.UVGC_298_500,(0,0,7):C.UVGC_298_501,(0,0,8):C.UVGC_298_502,(0,0,9):C.UVGC_298_503,(0,0,10):C.UVGC_298_504,(0,0,11):C.UVGC_298_505,(0,0,12):C.UVGC_298_506,(0,0,13):C.UVGC_298_507,(0,0,14):C.UVGC_298_508,(0,0,15):C.UVGC_298_509,(0,0,16):C.UVGC_298_510,(0,0,17):C.UVGC_298_511,(0,0,18):C.UVGC_298_512,(0,0,19):C.UVGC_298_513,(0,0,20):C.UVGC_298_514,(0,0,21):C.UVGC_298_515,(0,0,22):C.UVGC_298_516,(0,0,23):C.UVGC_298_517,(0,0,24):C.UVGC_298_518,(0,0,25):C.UVGC_298_519,(0,0,26):C.UVGC_298_520,(0,0,27):C.UVGC_298_521,(0,0,28):C.UVGC_298_522,(0,0,29):C.UVGC_298_523,(0,0,30):C.UVGC_298_524,(0,0,31):C.UVGC_298_525,(0,0,32):C.UVGC_298_526,(0,0,5):C.UVGC_311_538})

V_645 = CTVertex(name = 'V_645',
                 type = 'UV',
                 particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_324_549})

V_646 = CTVertex(name = 'V_646',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_325_550})

V_647 = CTVertex(name = 'V_647',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3d3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_298_495,(0,0,1):C.UVGC_298_496,(0,0,2):C.UVGC_298_497,(0,0,3):C.UVGC_298_498,(0,0,4):C.UVGC_298_499,(0,0,6):C.UVGC_298_500,(0,0,7):C.UVGC_298_501,(0,0,8):C.UVGC_298_502,(0,0,9):C.UVGC_298_503,(0,0,10):C.UVGC_298_504,(0,0,11):C.UVGC_298_505,(0,0,12):C.UVGC_298_506,(0,0,13):C.UVGC_298_507,(0,0,14):C.UVGC_298_508,(0,0,15):C.UVGC_298_509,(0,0,16):C.UVGC_298_510,(0,0,17):C.UVGC_298_511,(0,0,18):C.UVGC_298_512,(0,0,19):C.UVGC_298_513,(0,0,20):C.UVGC_298_514,(0,0,21):C.UVGC_298_515,(0,0,22):C.UVGC_298_516,(0,0,23):C.UVGC_298_517,(0,0,24):C.UVGC_298_518,(0,0,25):C.UVGC_298_519,(0,0,26):C.UVGC_298_520,(0,0,27):C.UVGC_298_521,(0,0,28):C.UVGC_298_522,(0,0,29):C.UVGC_298_523,(0,0,30):C.UVGC_298_524,(0,0,31):C.UVGC_298_525,(0,0,32):C.UVGC_298_526,(0,0,5):C.UVGC_326_551})

V_648 = CTVertex(name = 'V_648',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_339_562})

V_649 = CTVertex(name = 'V_649',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_340_563})

V_650 = CTVertex(name = 'V_650',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_341_564,(0,0,1):C.UVGC_341_565,(0,0,2):C.UVGC_341_566,(0,0,3):C.UVGC_341_567,(0,0,4):C.UVGC_341_568,(0,0,6):C.UVGC_341_569,(0,0,7):C.UVGC_341_570,(0,0,8):C.UVGC_341_571,(0,0,9):C.UVGC_341_572,(0,0,10):C.UVGC_341_573,(0,0,11):C.UVGC_341_574,(0,0,12):C.UVGC_341_575,(0,0,13):C.UVGC_341_576,(0,0,14):C.UVGC_341_577,(0,0,15):C.UVGC_341_578,(0,0,16):C.UVGC_341_579,(0,0,17):C.UVGC_341_580,(0,0,18):C.UVGC_341_581,(0,0,19):C.UVGC_341_582,(0,0,20):C.UVGC_341_583,(0,0,21):C.UVGC_341_584,(0,0,22):C.UVGC_341_585,(0,0,23):C.UVGC_341_586,(0,0,24):C.UVGC_341_587,(0,0,25):C.UVGC_341_588,(0,0,26):C.UVGC_341_589,(0,0,27):C.UVGC_341_590,(0,0,28):C.UVGC_341_591,(0,0,29):C.UVGC_341_592,(0,0,30):C.UVGC_341_593,(0,0,31):C.UVGC_341_594,(0,0,32):C.UVGC_341_595,(0,0,5):C.UVGC_341_596})

V_651 = CTVertex(name = 'V_651',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_354_607})

V_652 = CTVertex(name = 'V_652',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_355_608})

V_653 = CTVertex(name = 'V_653',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_341_564,(0,0,1):C.UVGC_341_565,(0,0,2):C.UVGC_341_566,(0,0,3):C.UVGC_341_567,(0,0,4):C.UVGC_341_568,(0,0,6):C.UVGC_341_569,(0,0,7):C.UVGC_341_570,(0,0,8):C.UVGC_341_571,(0,0,9):C.UVGC_341_572,(0,0,10):C.UVGC_341_573,(0,0,11):C.UVGC_341_574,(0,0,12):C.UVGC_341_575,(0,0,13):C.UVGC_341_576,(0,0,14):C.UVGC_341_577,(0,0,15):C.UVGC_341_578,(0,0,16):C.UVGC_341_579,(0,0,17):C.UVGC_341_580,(0,0,18):C.UVGC_341_581,(0,0,19):C.UVGC_341_582,(0,0,20):C.UVGC_341_583,(0,0,21):C.UVGC_341_584,(0,0,22):C.UVGC_341_585,(0,0,23):C.UVGC_341_586,(0,0,24):C.UVGC_341_587,(0,0,25):C.UVGC_341_588,(0,0,26):C.UVGC_341_589,(0,0,27):C.UVGC_341_590,(0,0,28):C.UVGC_341_591,(0,0,29):C.UVGC_341_592,(0,0,30):C.UVGC_341_593,(0,0,31):C.UVGC_341_594,(0,0,32):C.UVGC_341_595,(0,0,5):C.UVGC_356_609})

V_654 = CTVertex(name = 'V_654',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_369_620})

V_655 = CTVertex(name = 'V_655',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_370_621})

V_656 = CTVertex(name = 'V_656',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qd3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_341_564,(0,0,1):C.UVGC_341_565,(0,0,2):C.UVGC_341_566,(0,0,3):C.UVGC_341_567,(0,0,4):C.UVGC_341_568,(0,0,6):C.UVGC_341_569,(0,0,7):C.UVGC_341_570,(0,0,8):C.UVGC_341_571,(0,0,9):C.UVGC_341_572,(0,0,10):C.UVGC_341_573,(0,0,11):C.UVGC_341_574,(0,0,12):C.UVGC_341_575,(0,0,13):C.UVGC_341_576,(0,0,14):C.UVGC_341_577,(0,0,15):C.UVGC_341_578,(0,0,16):C.UVGC_341_579,(0,0,17):C.UVGC_341_580,(0,0,18):C.UVGC_341_581,(0,0,19):C.UVGC_341_582,(0,0,20):C.UVGC_341_583,(0,0,21):C.UVGC_341_584,(0,0,22):C.UVGC_341_585,(0,0,23):C.UVGC_341_586,(0,0,24):C.UVGC_341_587,(0,0,25):C.UVGC_341_588,(0,0,26):C.UVGC_341_589,(0,0,27):C.UVGC_341_590,(0,0,28):C.UVGC_341_591,(0,0,29):C.UVGC_341_592,(0,0,30):C.UVGC_341_593,(0,0,31):C.UVGC_341_594,(0,0,32):C.UVGC_341_595,(0,0,5):C.UVGC_371_622})

V_657 = CTVertex(name = 'V_657',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_384_665})

V_658 = CTVertex(name = 'V_658',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_623_892,(0,0,2):C.UVGC_623_893,(0,0,1):C.UVGC_623_894})

V_659 = CTVertex(name = 'V_659',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_623_892,(0,0,2):C.UVGC_623_893,(0,0,1):C.UVGC_623_894})

V_660 = CTVertex(name = 'V_660',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_385_666})

V_661 = CTVertex(name = 'V_661',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_667,(0,0,1):C.UVGC_386_668,(0,0,2):C.UVGC_386_669,(0,0,3):C.UVGC_386_670,(0,0,4):C.UVGC_386_671,(0,0,6):C.UVGC_386_672,(0,0,7):C.UVGC_386_673,(0,0,8):C.UVGC_386_674,(0,0,9):C.UVGC_386_675,(0,0,10):C.UVGC_386_676,(0,0,11):C.UVGC_386_677,(0,0,12):C.UVGC_386_678,(0,0,13):C.UVGC_386_679,(0,0,14):C.UVGC_386_680,(0,0,15):C.UVGC_386_681,(0,0,16):C.UVGC_386_682,(0,0,17):C.UVGC_386_683,(0,0,18):C.UVGC_386_684,(0,0,19):C.UVGC_386_685,(0,0,20):C.UVGC_386_686,(0,0,21):C.UVGC_386_687,(0,0,22):C.UVGC_386_688,(0,0,23):C.UVGC_386_689,(0,0,24):C.UVGC_386_690,(0,0,25):C.UVGC_386_691,(0,0,26):C.UVGC_386_692,(0,0,27):C.UVGC_386_693,(0,0,28):C.UVGC_386_694,(0,0,29):C.UVGC_386_695,(0,0,30):C.UVGC_386_696,(0,0,31):C.UVGC_386_697,(0,0,32):C.UVGC_386_698,(0,0,5):C.UVGC_386_699})

V_662 = CTVertex(name = 'V_662',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_398_709})

V_663 = CTVertex(name = 'V_663',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_656_946,(0,0,2):C.UVGC_656_947,(0,0,1):C.UVGC_623_894})

V_664 = CTVertex(name = 'V_664',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_656_946,(0,0,2):C.UVGC_656_947,(0,0,1):C.UVGC_623_894})

V_665 = CTVertex(name = 'V_665',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_399_710})

V_666 = CTVertex(name = 'V_666',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_667,(0,0,1):C.UVGC_386_668,(0,0,2):C.UVGC_386_669,(0,0,3):C.UVGC_386_670,(0,0,4):C.UVGC_386_671,(0,0,6):C.UVGC_386_672,(0,0,7):C.UVGC_386_673,(0,0,8):C.UVGC_386_674,(0,0,9):C.UVGC_386_675,(0,0,10):C.UVGC_386_676,(0,0,11):C.UVGC_386_677,(0,0,12):C.UVGC_386_678,(0,0,13):C.UVGC_386_679,(0,0,14):C.UVGC_386_680,(0,0,15):C.UVGC_386_681,(0,0,16):C.UVGC_386_682,(0,0,17):C.UVGC_386_683,(0,0,18):C.UVGC_386_684,(0,0,19):C.UVGC_386_685,(0,0,20):C.UVGC_386_686,(0,0,21):C.UVGC_386_687,(0,0,22):C.UVGC_386_688,(0,0,23):C.UVGC_386_689,(0,0,24):C.UVGC_386_690,(0,0,25):C.UVGC_386_691,(0,0,26):C.UVGC_386_692,(0,0,27):C.UVGC_386_693,(0,0,28):C.UVGC_386_694,(0,0,29):C.UVGC_386_695,(0,0,30):C.UVGC_386_696,(0,0,31):C.UVGC_386_697,(0,0,32):C.UVGC_386_698,(0,0,5):C.UVGC_400_711})

V_667 = CTVertex(name = 'V_667',
                 type = 'UV',
                 particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_411_720})

V_668 = CTVertex(name = 'V_668',
                 type = 'UV',
                 particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_687_962,(0,0,2):C.UVGC_687_963,(0,0,1):C.UVGC_623_894})

V_669 = CTVertex(name = 'V_669',
                 type = 'UV',
                 particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_687_962,(0,0,2):C.UVGC_687_963,(0,0,1):C.UVGC_623_894})

V_670 = CTVertex(name = 'V_670',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_412_721})

V_671 = CTVertex(name = 'V_671',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3Qu3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_386_667,(0,0,1):C.UVGC_386_668,(0,0,2):C.UVGC_386_669,(0,0,3):C.UVGC_386_670,(0,0,4):C.UVGC_386_671,(0,0,6):C.UVGC_386_672,(0,0,7):C.UVGC_386_673,(0,0,8):C.UVGC_386_674,(0,0,9):C.UVGC_386_675,(0,0,10):C.UVGC_386_676,(0,0,11):C.UVGC_386_677,(0,0,12):C.UVGC_386_678,(0,0,13):C.UVGC_386_679,(0,0,14):C.UVGC_386_680,(0,0,15):C.UVGC_386_681,(0,0,16):C.UVGC_386_682,(0,0,17):C.UVGC_386_683,(0,0,18):C.UVGC_386_684,(0,0,19):C.UVGC_386_685,(0,0,20):C.UVGC_386_686,(0,0,21):C.UVGC_386_687,(0,0,22):C.UVGC_386_688,(0,0,23):C.UVGC_386_689,(0,0,24):C.UVGC_386_690,(0,0,25):C.UVGC_386_691,(0,0,26):C.UVGC_386_692,(0,0,27):C.UVGC_386_693,(0,0,28):C.UVGC_386_694,(0,0,29):C.UVGC_386_695,(0,0,30):C.UVGC_386_696,(0,0,31):C.UVGC_386_697,(0,0,32):C.UVGC_386_698,(0,0,5):C.UVGC_413_722})

V_672 = CTVertex(name = 'V_672',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_424_731})

V_673 = CTVertex(name = 'V_673',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_425_732})

V_674 = CTVertex(name = 'V_674',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_426_733,(0,0,1):C.UVGC_426_734,(0,0,2):C.UVGC_426_735,(0,0,3):C.UVGC_426_736,(0,0,4):C.UVGC_426_737,(0,0,6):C.UVGC_426_738,(0,0,7):C.UVGC_426_739,(0,0,8):C.UVGC_426_740,(0,0,9):C.UVGC_426_741,(0,0,10):C.UVGC_426_742,(0,0,11):C.UVGC_426_743,(0,0,12):C.UVGC_426_744,(0,0,13):C.UVGC_426_745,(0,0,14):C.UVGC_426_746,(0,0,15):C.UVGC_426_747,(0,0,16):C.UVGC_426_748,(0,0,17):C.UVGC_426_749,(0,0,18):C.UVGC_426_750,(0,0,19):C.UVGC_426_751,(0,0,20):C.UVGC_426_752,(0,0,21):C.UVGC_426_753,(0,0,22):C.UVGC_426_754,(0,0,23):C.UVGC_426_755,(0,0,24):C.UVGC_426_756,(0,0,25):C.UVGC_426_757,(0,0,26):C.UVGC_426_758,(0,0,27):C.UVGC_426_759,(0,0,28):C.UVGC_426_760,(0,0,29):C.UVGC_426_761,(0,0,30):C.UVGC_426_762,(0,0,31):C.UVGC_426_763,(0,0,32):C.UVGC_426_764,(0,0,5):C.UVGC_426_765})

V_675 = CTVertex(name = 'V_675',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_437_774})

V_676 = CTVertex(name = 'V_676',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_438_775})

V_677 = CTVertex(name = 'V_677',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u2] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_426_733,(0,0,1):C.UVGC_426_734,(0,0,2):C.UVGC_426_735,(0,0,3):C.UVGC_426_736,(0,0,4):C.UVGC_426_737,(0,0,6):C.UVGC_426_738,(0,0,7):C.UVGC_426_739,(0,0,8):C.UVGC_426_740,(0,0,9):C.UVGC_426_741,(0,0,10):C.UVGC_426_742,(0,0,11):C.UVGC_426_743,(0,0,12):C.UVGC_426_744,(0,0,13):C.UVGC_426_745,(0,0,14):C.UVGC_426_746,(0,0,15):C.UVGC_426_747,(0,0,16):C.UVGC_426_748,(0,0,17):C.UVGC_426_749,(0,0,18):C.UVGC_426_750,(0,0,19):C.UVGC_426_751,(0,0,20):C.UVGC_426_752,(0,0,21):C.UVGC_426_753,(0,0,22):C.UVGC_426_754,(0,0,23):C.UVGC_426_755,(0,0,24):C.UVGC_426_756,(0,0,25):C.UVGC_426_757,(0,0,26):C.UVGC_426_758,(0,0,27):C.UVGC_426_759,(0,0,28):C.UVGC_426_760,(0,0,29):C.UVGC_426_761,(0,0,30):C.UVGC_426_762,(0,0,31):C.UVGC_426_763,(0,0,32):C.UVGC_426_764,(0,0,5):C.UVGC_439_776})

V_678 = CTVertex(name = 'V_678',
                 type = 'UV',
                 particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(2,3)' ],
                 lorentz = [ L.VSS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_450_785})

V_679 = CTVertex(name = 'V_679',
                 type = 'UV',
                 particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_451_786})

V_680 = CTVertex(name = 'V_680',
                 type = 'UV',
                 particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'T(1,4,3)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.YS3u3] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_426_733,(0,0,1):C.UVGC_426_734,(0,0,2):C.UVGC_426_735,(0,0,3):C.UVGC_426_736,(0,0,4):C.UVGC_426_737,(0,0,6):C.UVGC_426_738,(0,0,7):C.UVGC_426_739,(0,0,8):C.UVGC_426_740,(0,0,9):C.UVGC_426_741,(0,0,10):C.UVGC_426_742,(0,0,11):C.UVGC_426_743,(0,0,12):C.UVGC_426_744,(0,0,13):C.UVGC_426_745,(0,0,14):C.UVGC_426_746,(0,0,15):C.UVGC_426_747,(0,0,16):C.UVGC_426_748,(0,0,17):C.UVGC_426_749,(0,0,18):C.UVGC_426_750,(0,0,19):C.UVGC_426_751,(0,0,20):C.UVGC_426_752,(0,0,21):C.UVGC_426_753,(0,0,22):C.UVGC_426_754,(0,0,23):C.UVGC_426_755,(0,0,24):C.UVGC_426_756,(0,0,25):C.UVGC_426_757,(0,0,26):C.UVGC_426_758,(0,0,27):C.UVGC_426_759,(0,0,28):C.UVGC_426_760,(0,0,29):C.UVGC_426_761,(0,0,30):C.UVGC_426_762,(0,0,31):C.UVGC_426_763,(0,0,32):C.UVGC_426_764,(0,0,5):C.UVGC_452_787})

V_681 = CTVertex(name = 'V_681',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_299_528})

V_682 = CTVertex(name = 'V_682',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_312_539})

V_683 = CTVertex(name = 'V_683',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_327_552})

V_684 = CTVertex(name = 'V_684',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_342_597})

V_685 = CTVertex(name = 'V_685',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_357_610})

V_686 = CTVertex(name = 'V_686',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_372_623})

V_687 = CTVertex(name = 'V_687',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_387_700})

V_688 = CTVertex(name = 'V_688',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_401_712})

V_689 = CTVertex(name = 'V_689',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_414_723})

V_690 = CTVertex(name = 'V_690',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_427_766})

V_691 = CTVertex(name = 'V_691',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_440_777})

V_692 = CTVertex(name = 'V_692',
                 type = 'UV',
                 particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(3,4)' ],
                 lorentz = [ L.VVSS1 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_453_788})

V_693 = CTVertex(name = 'V_693',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_746_1019,(0,0,2):C.UVGC_746_1020,(0,0,1):C.UVGC_567_883})

V_694 = CTVertex(name = 'V_694',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_567_881,(0,0,2):C.UVGC_567_882,(0,0,1):C.UVGC_567_883})

V_695 = CTVertex(name = 'V_695',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_860,(0,0,2):C.UVGC_559_861,(0,0,1):C.UVGC_559_862})

V_696 = CTVertex(name = 'V_696',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_732_988,(0,0,2):C.UVGC_732_989,(0,0,1):C.UVGC_559_862})

V_697 = CTVertex(name = 'V_697',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1004,(0,0,2):C.UVGC_739_1005,(0,0,1):C.UVGC_554_848})

V_698 = CTVertex(name = 'V_698',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_554_846,(0,0,2):C.UVGC_554_847,(0,0,1):C.UVGC_554_848})

V_699 = CTVertex(name = 'V_699',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_166_39,(0,2,0):C.UVGC_168_41})

V_700 = CTVertex(name = 'V_700',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_138_11,(0,2,0):C.UVGC_140_13})

V_701 = CTVertex(name = 'V_701',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_278_383,(0,1,0):C.UVGC_159_32,(0,2,0):C.UVGC_161_34})

V_702 = CTVertex(name = 'V_702',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_145_18,(0,2,0):C.UVGC_147_20})

V_703 = CTVertex(name = 'V_703',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_152_25,(0,2,0):C.UVGC_154_27})

V_704 = CTVertex(name = 'V_704',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_273_379,(0,1,0):C.UVGC_131_4,(0,2,0):C.UVGC_133_6})

V_705 = CTVertex(name = 'V_705',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_169_42,(0,2,5):C.UVGC_170_43})

V_706 = CTVertex(name = 'V_706',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,2):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,3):C.UVGC_261_139,(0,3,4):C.UVGC_261_140,(0,3,5):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,2):C.UVGC_141_14,(0,2,2):C.UVGC_142_15})

V_707 = CTVertex(name = 'V_707',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_162_35,(0,2,5):C.UVGC_163_36})

V_708 = CTVertex(name = 'V_708',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,3):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,4):C.UVGC_261_140,(0,3,5):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,3):C.UVGC_148_21,(0,2,3):C.UVGC_149_22})

V_709 = CTVertex(name = 'V_709',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,5):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,1):C.UVGC_261_138,(0,3,2):C.UVGC_261_139,(0,3,3):C.UVGC_261_140,(0,3,4):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,5):C.UVGC_155_28,(0,2,5):C.UVGC_156_29})

V_710 = CTVertex(name = 'V_710',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,1):C.UVGC_274_380,(0,3,0):C.UVGC_261_137,(0,3,2):C.UVGC_261_138,(0,3,3):C.UVGC_261_139,(0,3,4):C.UVGC_261_140,(0,3,5):C.UVGC_261_141,(0,3,6):C.UVGC_261_142,(0,3,7):C.UVGC_261_143,(0,3,8):C.UVGC_261_144,(0,3,9):C.UVGC_261_145,(0,3,10):C.UVGC_261_146,(0,3,11):C.UVGC_261_147,(0,3,12):C.UVGC_261_148,(0,3,13):C.UVGC_261_149,(0,3,14):C.UVGC_261_150,(0,3,15):C.UVGC_261_151,(0,3,16):C.UVGC_261_152,(0,3,17):C.UVGC_261_153,(0,3,18):C.UVGC_261_154,(0,3,19):C.UVGC_261_155,(0,3,20):C.UVGC_261_156,(0,3,21):C.UVGC_261_157,(0,3,22):C.UVGC_261_158,(0,3,23):C.UVGC_261_159,(0,3,24):C.UVGC_261_160,(0,3,25):C.UVGC_261_161,(0,3,26):C.UVGC_261_162,(0,3,27):C.UVGC_261_163,(0,3,28):C.UVGC_261_164,(0,3,29):C.UVGC_261_165,(0,3,30):C.UVGC_261_166,(0,3,31):C.UVGC_261_167,(0,3,32):C.UVGC_261_168,(0,1,1):C.UVGC_134_7,(0,2,1):C.UVGC_135_8})

V_711 = CTVertex(name = 'V_711',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_743_1012,(0,0,2):C.UVGC_743_1013,(0,0,1):C.UVGC_558_859})

V_712 = CTVertex(name = 'V_712',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_558_857,(0,0,2):C.UVGC_558_858,(0,0,1):C.UVGC_558_859})

V_713 = CTVertex(name = 'V_713',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_734_991,(0,0,2):C.UVGC_734_992,(0,0,1):C.UVGC_558_859})

V_714 = CTVertex(name = 'V_714',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_743_1012,(0,0,2):C.UVGC_743_1013,(0,0,1):C.UVGC_558_859})

V_715 = CTVertex(name = 'V_715',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_558_857,(0,0,2):C.UVGC_558_858,(0,0,1):C.UVGC_558_859})

V_716 = CTVertex(name = 'V_716',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_734_991,(0,0,2):C.UVGC_734_992,(0,0,1):C.UVGC_558_859})

V_717 = CTVertex(name = 'V_717',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_470_794,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_171_44})

V_718 = CTVertex(name = 'V_718',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_280_384,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_143_16})

V_719 = CTVertex(name = 'V_719',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV7 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_463_791,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_164_37})

V_720 = CTVertex(name = 'V_720',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_285_385,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_150_23})

V_721 = CTVertex(name = 'V_721',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_457_789,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_157_30})

V_722 = CTVertex(name = 'V_722',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_275_381,(0,2,0):C.UVGC_276_382,(0,1,0):C.UVGC_136_9})

V_723 = CTVertex(name = 'V_723',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3Qu1] ], [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_746_1019,(0,0,2):C.UVGC_746_1020,(0,0,1):C.UVGC_567_883})

V_724 = CTVertex(name = 'V_724',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3Qd1] ], [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_567_881,(0,0,2):C.UVGC_567_882,(0,0,1):C.UVGC_567_883})

V_725 = CTVertex(name = 'V_725',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3Qu2] ], [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_559_860,(0,0,2):C.UVGC_559_861,(0,0,1):C.UVGC_559_862})

V_726 = CTVertex(name = 'V_726',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3Qd2] ], [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_732_988,(0,0,2):C.UVGC_732_989,(0,0,1):C.UVGC_559_862})

V_727 = CTVertex(name = 'V_727',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3Qu3] ], [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_739_1004,(0,0,2):C.UVGC_739_1005,(0,0,1):C.UVGC_554_848})

V_728 = CTVertex(name = 'V_728',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3Qd3] ], [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_554_846,(0,0,2):C.UVGC_554_847,(0,0,1):C.UVGC_554_848})

V_729 = CTVertex(name = 'V_729',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_565_876,(0,0,2):C.UVGC_565_877,(0,0,1):C.UVGC_565_878})

V_730 = CTVertex(name = 'V_730',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_730_983,(0,0,2):C.UVGC_730_984,(0,0,1):C.UVGC_730_985})

V_731 = CTVertex(name = 'V_731',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_552_841,(0,0,2):C.UVGC_552_842,(0,0,1):C.UVGC_552_843})

V_732 = CTVertex(name = 'V_732',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_748_1022,(0,0,2):C.UVGC_748_1023,(0,0,1):C.UVGC_748_1024})

V_733 = CTVertex(name = 'V_733',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_865,(0,0,2):C.UVGC_561_866,(0,0,1):C.UVGC_561_867})

V_734 = CTVertex(name = 'V_734',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_741_1007,(0,0,2):C.UVGC_741_1008,(0,0,1):C.UVGC_741_1009})

V_735 = CTVertex(name = 'V_735',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.YF3d1] ], [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_565_876,(0,0,2):C.UVGC_565_877,(0,0,1):C.UVGC_565_878})

V_736 = CTVertex(name = 'V_736',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.YF3d2] ], [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_730_983,(0,0,2):C.UVGC_730_984,(0,0,1):C.UVGC_730_985})

V_737 = CTVertex(name = 'V_737',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.YF3d3] ], [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_552_841,(0,0,2):C.UVGC_552_842,(0,0,1):C.UVGC_552_843})

V_738 = CTVertex(name = 'V_738',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.YF3u1] ], [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_748_1022,(0,0,2):C.UVGC_748_1023,(0,0,1):C.UVGC_748_1024})

V_739 = CTVertex(name = 'V_739',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.YF3u2] ], [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_561_865,(0,0,2):C.UVGC_561_866,(0,0,1):C.UVGC_561_867})

V_740 = CTVertex(name = 'V_740',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.YF3u3] ], [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_741_1007,(0,0,2):C.UVGC_741_1008,(0,0,1):C.UVGC_741_1009})

V_741 = CTVertex(name = 'V_741',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_272_378,(0,1,0):C.UVGC_165_38,(0,2,0):C.UVGC_167_40})

V_742 = CTVertex(name = 'V_742',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_378,(0,1,0):C.UVGC_137_10,(0,2,0):C.UVGC_139_12})

V_743 = CTVertex(name = 'V_743',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_462_790,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_158_31,(0,2,0):C.UVGC_160_33})

V_744 = CTVertex(name = 'V_744',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_378,(0,1,0):C.UVGC_144_17,(0,2,0):C.UVGC_146_19})

V_745 = CTVertex(name = 'V_745',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_272_378,(0,1,0):C.UVGC_151_24,(0,2,0):C.UVGC_153_26})

V_746 = CTVertex(name = 'V_746',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_272_378,(0,1,0):C.UVGC_130_3,(0,2,0):C.UVGC_132_5})

V_747 = CTVertex(name = 'V_747',
                 type = 'UV',
                 particles = [ P.YF3Qu1__tilde__, P.YF3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu1] ] ],
                 couplings = {(0,1,0):C.UVGC_511_809,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_214_87,(0,2,0):C.UVGC_216_89})

V_748 = CTVertex(name = 'V_748',
                 type = 'UV',
                 particles = [ P.YF3Qu2__tilde__, P.YF3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu2] ] ],
                 couplings = {(0,1,0):C.UVGC_520_817,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_220_93,(0,2,0):C.UVGC_222_95})

V_749 = CTVertex(name = 'V_749',
                 type = 'UV',
                 particles = [ P.YF3Qu3__tilde__, P.YF3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qu3] ] ],
                 couplings = {(0,1,0):C.UVGC_529_824,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_226_99,(0,2,0):C.UVGC_228_101})

V_750 = CTVertex(name = 'V_750',
                 type = 'UV',
                 particles = [ P.YF3Qd1__tilde__, P.YF3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd1] ] ],
                 couplings = {(0,1,0):C.UVGC_490_799,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_196_69,(0,2,0):C.UVGC_198_71})

V_751 = CTVertex(name = 'V_751',
                 type = 'UV',
                 particles = [ P.YF3Qd2__tilde__, P.YF3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd2] ] ],
                 couplings = {(0,1,0):C.UVGC_497_803,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_202_75,(0,2,0):C.UVGC_204_77})

V_752 = CTVertex(name = 'V_752',
                 type = 'UV',
                 particles = [ P.YF3Qd3__tilde__, P.YF3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3Qd3] ] ],
                 couplings = {(0,1,0):C.UVGC_504_806,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_208_81,(0,2,0):C.UVGC_210_83})

V_753 = CTVertex(name = 'V_753',
                 type = 'UV',
                 particles = [ P.YF3u1__tilde__, P.YF3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u1] ] ],
                 couplings = {(0,1,0):C.UVGC_538_831,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_232_105,(0,2,0):C.UVGC_234_107})

V_754 = CTVertex(name = 'V_754',
                 type = 'UV',
                 particles = [ P.YF3u2__tilde__, P.YF3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u2] ] ],
                 couplings = {(0,1,0):C.UVGC_543_833,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_240_113,(0,2,0):C.UVGC_242_115})

V_755 = CTVertex(name = 'V_755',
                 type = 'UV',
                 particles = [ P.YF3u3__tilde__, P.YF3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3u3] ] ],
                 couplings = {(0,1,0):C.UVGC_548_834,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_248_121,(0,2,0):C.UVGC_250_123})

V_756 = CTVertex(name = 'V_756',
                 type = 'UV',
                 particles = [ P.YF3d1__tilde__, P.YF3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d1] ] ],
                 couplings = {(0,1,0):C.UVGC_475_795,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_172_45,(0,2,0):C.UVGC_174_47})

V_757 = CTVertex(name = 'V_757',
                 type = 'UV',
                 particles = [ P.YF3d2__tilde__, P.YF3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d2] ] ],
                 couplings = {(0,1,0):C.UVGC_480_797,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_180_53,(0,2,0):C.UVGC_182_55})

V_758 = CTVertex(name = 'V_758',
                 type = 'UV',
                 particles = [ P.YF3d3__tilde__, P.YF3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.YF3d3] ] ],
                 couplings = {(0,1,0):C.UVGC_485_798,(0,3,0):C.UVGC_272_378,(0,0,0):C.UVGC_188_61,(0,2,0):C.UVGC_190_63})

V_759 = CTVertex(name = 'V_759',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV4, L.VV5, L.VV6 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.YF3d1] ], [ [P.YF3d2] ], [ [P.YF3d3] ], [ [P.YF3Qd1] ], [ [P.YF3Qd2] ], [ [P.YF3Qd3] ], [ [P.YF3Qu1] ], [ [P.YF3Qu2] ], [ [P.YF3Qu3] ], [ [P.YF3u1] ], [ [P.YF3u2] ], [ [P.YF3u3] ], [ [P.YS3d1] ], [ [P.YS3d2] ], [ [P.YS3d3] ], [ [P.YS3Qd1] ], [ [P.YS3Qd2] ], [ [P.YS3Qd3] ], [ [P.YS3Qu1] ], [ [P.YS3Qu2] ], [ [P.YS3Qu3] ], [ [P.YS3u1] ], [ [P.YS3u2] ], [ [P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_262_169,(0,0,1):C.UVGC_262_170,(0,0,2):C.UVGC_262_171,(0,0,3):C.UVGC_262_172,(0,0,4):C.UVGC_262_173,(0,0,5):C.UVGC_262_174,(0,0,6):C.UVGC_262_175,(0,0,7):C.UVGC_262_176,(0,0,8):C.UVGC_262_177,(0,0,9):C.UVGC_262_178,(0,0,10):C.UVGC_262_179,(0,0,11):C.UVGC_262_180,(0,0,12):C.UVGC_262_181,(0,0,13):C.UVGC_262_182,(0,0,14):C.UVGC_262_183,(0,0,15):C.UVGC_262_184,(0,0,16):C.UVGC_262_185,(0,0,17):C.UVGC_262_186,(0,0,18):C.UVGC_262_187,(0,0,19):C.UVGC_262_188,(0,0,20):C.UVGC_262_189,(0,0,21):C.UVGC_262_190,(0,0,22):C.UVGC_262_191,(0,0,23):C.UVGC_262_192,(0,0,24):C.UVGC_262_193,(0,0,25):C.UVGC_262_194,(0,0,26):C.UVGC_262_195,(0,0,27):C.UVGC_262_196,(0,0,28):C.UVGC_262_197,(0,0,29):C.UVGC_262_198,(0,0,30):C.UVGC_262_199,(0,0,31):C.UVGC_262_200,(0,1,3):C.UVGC_128_1,(0,2,4):C.UVGC_129_2})

V_760 = CTVertex(name = 'V_760',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu1] ] ],
                 couplings = {(0,0,0):C.UVGC_383_664,(0,1,0):C.UVGC_373_624})

V_761 = CTVertex(name = 'V_761',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu2] ] ],
                 couplings = {(0,0,0):C.UVGC_397_708,(0,1,0):C.UVGC_388_701})

V_762 = CTVertex(name = 'V_762',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qu3] ] ],
                 couplings = {(0,0,0):C.UVGC_410_719,(0,1,0):C.UVGC_402_713})

V_763 = CTVertex(name = 'V_763',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd1] ] ],
                 couplings = {(0,0,0):C.UVGC_338_561,(0,1,0):C.UVGC_328_553})

V_764 = CTVertex(name = 'V_764',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd2] ] ],
                 couplings = {(0,0,0):C.UVGC_353_606,(0,1,0):C.UVGC_343_598})

V_765 = CTVertex(name = 'V_765',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3Qd3] ] ],
                 couplings = {(0,0,0):C.UVGC_368_619,(0,1,0):C.UVGC_358_611})

V_766 = CTVertex(name = 'V_766',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u1] ] ],
                 couplings = {(0,0,0):C.UVGC_423_730,(0,1,0):C.UVGC_415_724})

V_767 = CTVertex(name = 'V_767',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u2] ] ],
                 couplings = {(0,0,0):C.UVGC_436_773,(0,1,0):C.UVGC_428_767})

V_768 = CTVertex(name = 'V_768',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3u3] ] ],
                 couplings = {(0,0,0):C.UVGC_449_784,(0,1,0):C.UVGC_441_778})

V_769 = CTVertex(name = 'V_769',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d1] ] ],
                 couplings = {(0,0,0):C.UVGC_295_492,(0,1,0):C.UVGC_287_386})

V_770 = CTVertex(name = 'V_770',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d2] ] ],
                 couplings = {(0,0,0):C.UVGC_308_535,(0,1,0):C.UVGC_300_529})

V_771 = CTVertex(name = 'V_771',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.SS1, L.SS2 ],
                 loop_particles = [ [ [P.g, P.YS3d3] ] ],
                 couplings = {(0,0,0):C.UVGC_323_548,(0,1,0):C.UVGC_313_540})

V_772 = CTVertex(name = 'V_772',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_759_1034,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_759_1036,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_759_1034,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_759_1036})

V_773 = CTVertex(name = 'V_773',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2] ], [ [P.g, P.YS3Qu1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_832_1100,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_832_1102,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_832_1103,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_831_1095,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_831_1097,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_831_1098})

V_774 = CTVertex(name = 'V_774',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_759_1034,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_759_1036,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_759_1034,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_759_1036})

V_775 = CTVertex(name = 'V_775',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3] ], [ [P.g, P.YS3Qu1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_832_1100,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_832_1102,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_832_1103,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_831_1095,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_831_1097,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_831_1098})

V_776 = CTVertex(name = 'V_776',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3] ], [ [P.g, P.YS3Qu2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_832_1100,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_832_1102,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_832_1103,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_831_1095,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_831_1097,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_831_1098})

V_777 = CTVertex(name = 'V_777',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3Qu3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_759_1034,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_759_1036,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_759_1034,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_759_1036})

V_778 = CTVertex(name = 'V_778',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qu1] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1] ], [ [P.g, P.YS3Qd1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,7):C.UVGC_570_890,(1,0,8):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,4):C.UVGC_765_1039,(1,0,11):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,5):C.UVGC_766_1044,(1,0,10):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1092,(1,0,9):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,7):C.UVGC_569_887,(0,0,8):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,4):C.UVGC_766_1042,(0,0,11):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,5):C.UVGC_825_1086,(0,0,10):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1088,(0,0,9):C.UVGC_825_1089})

V_779 = CTVertex(name = 'V_779',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2] ], [ [P.g, P.YS3Qd1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_780 = CTVertex(name = 'V_780',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3] ], [ [P.g, P.YS3Qd1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_781 = CTVertex(name = 'V_781',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3Qd1] ], [ [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_756_1031,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_756_1032,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_756_1031,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_756_1032})

V_782 = CTVertex(name = 'V_782',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd2, P.YS3Qu1, P.YS3Qu2__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_783 = CTVertex(name = 'V_783',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qu1__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu2] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_784 = CTVertex(name = 'V_784',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1] ], [ [P.g, P.YS3Qd2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_785 = CTVertex(name = 'V_785',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qu2] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2] ], [ [P.g, P.YS3Qd2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,7):C.UVGC_570_890,(1,0,8):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,4):C.UVGC_765_1039,(1,0,11):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,5):C.UVGC_766_1044,(1,0,10):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1092,(1,0,9):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,7):C.UVGC_569_887,(0,0,8):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,4):C.UVGC_766_1042,(0,0,11):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,5):C.UVGC_825_1086,(0,0,10):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1088,(0,0,9):C.UVGC_825_1089})

V_786 = CTVertex(name = 'V_786',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3] ], [ [P.g, P.YS3Qd2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_787 = CTVertex(name = 'V_787',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2] ], [ [P.g, P.YS3Qd1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_784_1066,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_784_1067,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_784_1068,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_783_1063,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_783_1064,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_783_1065})

V_788 = CTVertex(name = 'V_788',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3Qd2] ], [ [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_756_1031,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_756_1032,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_756_1031,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_756_1032})

V_789 = CTVertex(name = 'V_789',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd3, P.YS3Qu1, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_790 = CTVertex(name = 'V_790',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd3, P.YS3Qu2, P.YS3Qu3__tilde__ ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_791 = CTVertex(name = 'V_791',
                 type = 'UV',
                 particles = [ P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qu1__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd1], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu1], [P.g, P.W__plus__, P.YS3Qu1, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_792 = CTVertex(name = 'V_792',
                 type = 'UV',
                 particles = [ P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qu2__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd2], [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu3], [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu2], [P.g, P.W__plus__, P.YS3Qu2, P.YS3Qu3] ] ],
                 couplings = {(1,0,0):C.UVGC_765_1039,(1,0,1):C.UVGC_765_1040,(1,0,2):C.UVGC_765_1041,(0,0,0):C.UVGC_766_1042,(0,0,1):C.UVGC_766_1043,(0,0,2):C.UVGC_766_1044})

V_793 = CTVertex(name = 'V_793',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1] ], [ [P.g, P.YS3Qd3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_794 = CTVertex(name = 'V_794',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2] ], [ [P.g, P.YS3Qd3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1089})

V_795 = CTVertex(name = 'V_795',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.W__plus__] ], [ [P.g, P.W__plus__, P.YS3Qd3], [P.g, P.W__plus__, P.YS3Qu3] ], [ [P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3] ], [ [P.g, P.YS3Qd3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,7):C.UVGC_570_890,(1,0,8):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,4):C.UVGC_765_1039,(1,0,11):C.UVGC_826_1090,(1,0,1):C.UVGC_788_1075,(1,0,5):C.UVGC_766_1044,(1,0,10):C.UVGC_826_1091,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_826_1092,(1,0,9):C.UVGC_826_1093,(0,0,3):C.UVGC_569_886,(0,0,7):C.UVGC_569_887,(0,0,8):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,4):C.UVGC_766_1042,(0,0,11):C.UVGC_825_1085,(0,0,1):C.UVGC_753_1029,(0,0,5):C.UVGC_825_1086,(0,0,10):C.UVGC_825_1087,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_825_1088,(0,0,9):C.UVGC_825_1089})

V_796 = CTVertex(name = 'V_796',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3] ], [ [P.g, P.YS3Qd1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_784_1066,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_784_1067,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_784_1068,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_783_1063,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_783_1064,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_783_1065})

V_797 = CTVertex(name = 'V_797',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3] ], [ [P.g, P.YS3Qd2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_784_1066,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_784_1067,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_784_1068,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_783_1063,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_783_1064,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_783_1065})

V_798 = CTVertex(name = 'V_798',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3Qd3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3Qd3] ], [ [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_756_1031,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_756_1032,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_756_1031,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_756_1032})

V_799 = CTVertex(name = 'V_799',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1] ], [ [P.g, P.YS3Qu1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_800 = CTVertex(name = 'V_800',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1] ], [ [P.g, P.YS3Qu2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_801 = CTVertex(name = 'V_801',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1] ], [ [P.g, P.YS3Qu3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_802 = CTVertex(name = 'V_802',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1] ], [ [P.g, P.YS3Qd1, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_803 = CTVertex(name = 'V_803',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1] ], [ [P.g, P.YS3Qd2, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_804 = CTVertex(name = 'V_804',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1] ], [ [P.g, P.YS3Qd3, P.YS3u1, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_805 = CTVertex(name = 'V_805',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1__tilde__, P.YS3u1, P.YS3u1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3u1] ], [ [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_762_1037,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_762_1038,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_762_1037,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_762_1038})

V_806 = CTVertex(name = 'V_806',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2] ], [ [P.g, P.YS3Qu1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_807 = CTVertex(name = 'V_807',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2] ], [ [P.g, P.YS3Qu2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_808 = CTVertex(name = 'V_808',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2] ], [ [P.g, P.YS3Qu3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_809 = CTVertex(name = 'V_809',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2] ], [ [P.g, P.YS3Qd1, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_810 = CTVertex(name = 'V_810',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2] ], [ [P.g, P.YS3Qd2, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_811 = CTVertex(name = 'V_811',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2] ], [ [P.g, P.YS3Qd3, P.YS3u2, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_812 = CTVertex(name = 'V_812',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3u1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2] ], [ [P.g, P.YS3u1, P.YS3u2, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_886_1116,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_886_1117,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_772_1052,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_885_1114,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_885_1115,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_771_1046})

V_813 = CTVertex(name = 'V_813',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2__tilde__, P.YS3u2, P.YS3u2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3u2] ], [ [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_762_1037,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_762_1038,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_762_1037,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_762_1038})

V_814 = CTVertex(name = 'V_814',
                 type = 'UV',
                 particles = [ P.YS3Qu1__tilde__, P.YS3Qu1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3] ], [ [P.g, P.YS3Qu1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_815 = CTVertex(name = 'V_815',
                 type = 'UV',
                 particles = [ P.YS3Qu2__tilde__, P.YS3Qu2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3] ], [ [P.g, P.YS3Qu2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_816 = CTVertex(name = 'V_816',
                 type = 'UV',
                 particles = [ P.YS3Qu3__tilde__, P.YS3Qu3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qu3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qu3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3] ], [ [P.g, P.YS3Qu3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qu3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_836_1107,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_836_1108,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_836_1109,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_835_1104,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_835_1105,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_835_1106})

V_817 = CTVertex(name = 'V_817',
                 type = 'UV',
                 particles = [ P.YS3Qd1__tilde__, P.YS3Qd1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd1], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3] ], [ [P.g, P.YS3Qd1, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_818 = CTVertex(name = 'V_818',
                 type = 'UV',
                 particles = [ P.YS3Qd2__tilde__, P.YS3Qd2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd2], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3] ], [ [P.g, P.YS3Qd2, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_819 = CTVertex(name = 'V_819',
                 type = 'UV',
                 particles = [ P.YS3Qd3__tilde__, P.YS3Qd3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3Qd3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3Qd3], [P.g, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3] ], [ [P.g, P.YS3Qd3, P.YS3u3, P.Z] ], [ [P.g, P.YS3Qd3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_788_1074,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_788_1076,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_788_1078,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_787_1069,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_787_1070,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_787_1072})

V_820 = CTVertex(name = 'V_820',
                 type = 'UV',
                 particles = [ P.YS3u1__tilde__, P.YS3u1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u1], [P.g, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3] ], [ [P.g, P.YS3u1, P.YS3u3, P.Z] ], [ [P.g, P.YS3u1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_886_1116,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_886_1117,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_772_1052,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_885_1114,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_885_1115,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_771_1046})

V_821 = CTVertex(name = 'V_821',
                 type = 'UV',
                 particles = [ P.YS3u2__tilde__, P.YS3u2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3u2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u2], [P.g, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3] ], [ [P.g, P.YS3u2, P.YS3u3, P.Z] ], [ [P.g, P.YS3u2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_832_1099,(1,0,8):C.UVGC_886_1116,(1,0,1):C.UVGC_832_1101,(1,0,7):C.UVGC_886_1117,(1,0,2):C.UVGC_772_1051,(1,0,6):C.UVGC_772_1052,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_831_1094,(0,0,8):C.UVGC_885_1114,(0,0,1):C.UVGC_831_1096,(0,0,7):C.UVGC_885_1115,(0,0,2):C.UVGC_771_1045,(0,0,6):C.UVGC_771_1046})

V_822 = CTVertex(name = 'V_822',
                 type = 'UV',
                 particles = [ P.YS3u3__tilde__, P.YS3u3__tilde__, P.YS3u3, P.YS3u3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3u3] ], [ [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_759_1033,(1,0,5):C.UVGC_762_1037,(1,0,1):C.UVGC_759_1035,(1,0,4):C.UVGC_762_1038,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_759_1033,(0,0,5):C.UVGC_762_1037,(0,0,1):C.UVGC_759_1035,(0,0,4):C.UVGC_762_1038})

V_823 = CTVertex(name = 'V_823',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1] ], [ [P.g, P.YS3d1, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_824 = CTVertex(name = 'V_824',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2] ], [ [P.g, P.YS3d1, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_825 = CTVertex(name = 'V_825',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3] ], [ [P.g, P.YS3d1, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_826 = CTVertex(name = 'V_826',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1] ], [ [P.g, P.YS3d1, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_827 = CTVertex(name = 'V_827',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2] ], [ [P.g, P.YS3d1, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_828 = CTVertex(name = 'V_828',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3] ], [ [P.g, P.YS3d1, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_829 = CTVertex(name = 'V_829',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d1, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1] ], [ [P.g, P.YS3d1, P.YS3u1, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_830 = CTVertex(name = 'V_830',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d1, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2] ], [ [P.g, P.YS3d1, P.YS3u2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_831 = CTVertex(name = 'V_831',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d1, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3] ], [ [P.g, P.YS3d1, P.YS3u3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_832 = CTVertex(name = 'V_832',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1__tilde__, P.YS3d1, P.YS3d1 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1] ], [ [P.g] ], [ [P.g, P.YS3d1] ], [ [P.g, P.YS3d1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_753_1028,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_753_1030,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_753_1030})

V_833 = CTVertex(name = 'V_833',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1] ], [ [P.g, P.YS3d2, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_834 = CTVertex(name = 'V_834',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2] ], [ [P.g, P.YS3d2, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_835 = CTVertex(name = 'V_835',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3] ], [ [P.g, P.YS3d2, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_836 = CTVertex(name = 'V_836',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1] ], [ [P.g, P.YS3d2, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_837 = CTVertex(name = 'V_837',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2] ], [ [P.g, P.YS3d2, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_838 = CTVertex(name = 'V_838',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3] ], [ [P.g, P.YS3d2, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_839 = CTVertex(name = 'V_839',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d2, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1] ], [ [P.g, P.YS3d2, P.YS3u1, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_840 = CTVertex(name = 'V_840',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d2, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2] ], [ [P.g, P.YS3d2, P.YS3u2, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_841 = CTVertex(name = 'V_841',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d2, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3] ], [ [P.g, P.YS3d2, P.YS3u3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_842 = CTVertex(name = 'V_842',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d2__tilde__, P.YS3d2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d2] ], [ [P.a, P.g, P.YS3d1, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2] ], [ [P.g, P.YS3d1, P.YS3d2, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_772_1052,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_772_1054,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_772_1056,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_771_1046,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_771_1048,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_771_1050})

V_843 = CTVertex(name = 'V_843',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2__tilde__, P.YS3d2, P.YS3d2 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2] ], [ [P.g] ], [ [P.g, P.YS3d2] ], [ [P.g, P.YS3d2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_753_1028,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_753_1030,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_753_1030})

V_844 = CTVertex(name = 'V_844',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu1__tilde__, P.YS3Qu1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1] ], [ [P.g, P.YS3d3, P.YS3Qu1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_845 = CTVertex(name = 'V_845',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu2__tilde__, P.YS3Qu2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2] ], [ [P.g, P.YS3d3, P.YS3Qu2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_846 = CTVertex(name = 'V_846',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qu3__tilde__, P.YS3Qu3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qu3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3] ], [ [P.g, P.YS3d3, P.YS3Qu3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qu3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_820_1082,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_820_1083,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_820_1084,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_819_1079,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_819_1080,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_819_1081})

V_847 = CTVertex(name = 'V_847',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd1__tilde__, P.YS3Qd1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd1] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1] ], [ [P.g, P.YS3d3, P.YS3Qd1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_848 = CTVertex(name = 'V_848',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd2__tilde__, P.YS3Qd2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd2] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2] ], [ [P.g, P.YS3d3, P.YS3Qd2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_849 = CTVertex(name = 'V_849',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3Qd3__tilde__, P.YS3Qd3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3Qd3] ], [ [P.a, P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3] ], [ [P.g, P.YS3d3, P.YS3Qd3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3Qd3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_778_1060,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_778_1061,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_778_1062,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_777_1057,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_777_1058,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_777_1059})

V_850 = CTVertex(name = 'V_850',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u1__tilde__, P.YS3u1 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u1] ], [ [P.a, P.g, P.YS3d3, P.YS3u1] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1] ], [ [P.g, P.YS3d3, P.YS3u1, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u1, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_851 = CTVertex(name = 'V_851',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u2__tilde__, P.YS3u2 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u2] ], [ [P.a, P.g, P.YS3d3, P.YS3u2] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2] ], [ [P.g, P.YS3d3, P.YS3u2, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u2, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_852 = CTVertex(name = 'V_852',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3, P.YS3u3__tilde__, P.YS3u3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3], [P.a, P.g, P.YS3u3] ], [ [P.a, P.g, P.YS3d3, P.YS3u3] ], [ [P.g] ], [ [P.g, P.YS3d3], [P.g, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3] ], [ [P.g, P.YS3d3, P.YS3u3, P.Z] ], [ [P.g, P.YS3d3, P.Z], [P.g, P.YS3u3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_788_1073,(1,0,8):C.UVGC_880_1111,(1,0,1):C.UVGC_788_1075,(1,0,7):C.UVGC_880_1112,(1,0,2):C.UVGC_788_1077,(1,0,6):C.UVGC_880_1113,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_753_1027,(0,0,8):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,7):C.UVGC_753_1030,(0,0,2):C.UVGC_787_1071,(0,0,6):C.UVGC_879_1110})

V_853 = CTVertex(name = 'V_853',
                 type = 'UV',
                 particles = [ P.YS3d1__tilde__, P.YS3d1, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d1], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d1, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d1], [P.g, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3] ], [ [P.g, P.YS3d1, P.YS3d3, P.Z] ], [ [P.g, P.YS3d1, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_772_1052,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_772_1054,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_772_1056,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_771_1046,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_771_1048,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_771_1050})

V_854 = CTVertex(name = 'V_854',
                 type = 'UV',
                 particles = [ P.YS3d2__tilde__, P.YS3d2, P.YS3d3__tilde__, P.YS3d3 ],
                 color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d2], [P.a, P.g, P.YS3d3] ], [ [P.a, P.g, P.YS3d2, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d2], [P.g, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3] ], [ [P.g, P.YS3d2, P.YS3d3, P.Z] ], [ [P.g, P.YS3d2, P.Z], [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,3):C.UVGC_570_889,(1,0,4):C.UVGC_570_890,(1,0,5):C.UVGC_570_891,(1,0,0):C.UVGC_772_1051,(1,0,8):C.UVGC_772_1052,(1,0,1):C.UVGC_772_1053,(1,0,7):C.UVGC_772_1054,(1,0,2):C.UVGC_772_1055,(1,0,6):C.UVGC_772_1056,(0,0,3):C.UVGC_569_886,(0,0,4):C.UVGC_569_887,(0,0,5):C.UVGC_569_888,(0,0,0):C.UVGC_771_1045,(0,0,8):C.UVGC_771_1046,(0,0,1):C.UVGC_771_1047,(0,0,7):C.UVGC_771_1048,(0,0,2):C.UVGC_771_1049,(0,0,6):C.UVGC_771_1050})

V_855 = CTVertex(name = 'V_855',
                 type = 'UV',
                 particles = [ P.YS3d3__tilde__, P.YS3d3__tilde__, P.YS3d3, P.YS3d3 ],
                 color = [ 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                 lorentz = [ L.SSSS1 ],
                 loop_particles = [ [ [P.a, P.g] ], [ [P.a, P.g, P.YS3d3] ], [ [P.g] ], [ [P.g, P.YS3d3] ], [ [P.g, P.YS3d3, P.Z] ], [ [P.g, P.Z] ] ],
                 couplings = {(1,0,2):C.UVGC_292_455,(1,0,3):C.UVGC_292_456,(1,0,0):C.UVGC_753_1027,(1,0,5):C.UVGC_753_1028,(1,0,1):C.UVGC_753_1029,(1,0,4):C.UVGC_753_1030,(0,0,2):C.UVGC_292_455,(0,0,3):C.UVGC_292_456,(0,0,0):C.UVGC_753_1027,(0,0,5):C.UVGC_753_1028,(0,0,1):C.UVGC_753_1029,(0,0,4):C.UVGC_753_1030})

