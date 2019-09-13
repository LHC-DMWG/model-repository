# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 6 Jun 2019 21:52:44


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_23})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_21})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_22})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G0, P.G0, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_21})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_21})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_23})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G0, P.G0, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_90})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__minus__, P.G__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_90})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_91})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_5})

V_12 = Vertex(name = 'V_12',
              particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_14 = Vertex(name = 'V_14',
              particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_97})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ghWm, P.ghWm__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_92})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_93})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_53})

V_20 = Vertex(name = 'V_20',
              particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_100})

V_21 = Vertex(name = 'V_21',
              particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_52})

V_22 = Vertex(name = 'V_22',
              particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_96})

V_23 = Vertex(name = 'V_23',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_24 = Vertex(name = 'V_24',
              particles = [ P.ghWp, P.ghWp__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_95})

V_25 = Vertex(name = 'V_25',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_93})

V_26 = Vertex(name = 'V_26',
              particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_5})

V_27 = Vertex(name = 'V_27',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_52})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_99})

V_29 = Vertex(name = 'V_29',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_53})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_101})

V_31 = Vertex(name = 'V_31',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_52})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_98})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_53})

V_34 = Vertex(name = 'V_34',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_102})

V_35 = Vertex(name = 'V_35',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_15})

V_36 = Vertex(name = 'V_36',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_15})

V_37 = Vertex(name = 'V_37',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV4, L.VVVV7, L.VVVV8 ],
              couplings = {(1,1):C.GC_20,(0,0):C.GC_20,(2,2):C.GC_20})

V_38 = Vertex(name = 'V_38',
              particles = [ P.YF3d1__tilde__, P.YF3d1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_39 = Vertex(name = 'V_39',
              particles = [ P.YF3d2__tilde__, P.YF3d2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_40 = Vertex(name = 'V_40',
              particles = [ P.YF3d3__tilde__, P.YF3d3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_41 = Vertex(name = 'V_41',
              particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_42 = Vertex(name = 'V_42',
              particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_43 = Vertex(name = 'V_43',
              particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_44 = Vertex(name = 'V_44',
              particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_45 = Vertex(name = 'V_45',
              particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_46 = Vertex(name = 'V_46',
              particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_47 = Vertex(name = 'V_47',
              particles = [ P.YF3u1__tilde__, P.YF3u1, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_48 = Vertex(name = 'V_48',
              particles = [ P.YF3u2__tilde__, P.YF3u2, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_49 = Vertex(name = 'V_49',
              particles = [ P.YF3u3__tilde__, P.YF3u3, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_4})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.YF3Qu1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_27})

V_51 = Vertex(name = 'V_51',
              particles = [ P.d__tilde__, P.YF3Qd1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_27})

V_52 = Vertex(name = 'V_52',
              particles = [ P.c__tilde__, P.YF3Qu2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_28})

V_53 = Vertex(name = 'V_53',
              particles = [ P.s__tilde__, P.YF3Qd2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_28})

V_54 = Vertex(name = 'V_54',
              particles = [ P.t__tilde__, P.YF3Qu3, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_29})

V_55 = Vertex(name = 'V_55',
              particles = [ P.b__tilde__, P.YF3Qd3, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_29})

V_56 = Vertex(name = 'V_56',
              particles = [ P.YF3d1__tilde__, P.d, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_24})

V_57 = Vertex(name = 'V_57',
              particles = [ P.YF3d2__tilde__, P.s, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_25})

V_58 = Vertex(name = 'V_58',
              particles = [ P.YF3d3__tilde__, P.b, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_26})

V_59 = Vertex(name = 'V_59',
              particles = [ P.YF3u1__tilde__, P.u, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_30})

V_60 = Vertex(name = 'V_60',
              particles = [ P.YF3u2__tilde__, P.c, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_31})

V_61 = Vertex(name = 'V_61',
              particles = [ P.YF3u3__tilde__, P.t, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_32})

V_62 = Vertex(name = 'V_62',
              particles = [ P.b__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_105})

V_63 = Vertex(name = 'V_63',
              particles = [ P.t__tilde__, P.t, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_107})

V_64 = Vertex(name = 'V_64',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6 ],
              couplings = {(0,0):C.GC_106})

V_65 = Vertex(name = 'V_65',
              particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_109})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_110})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS6 ],
              couplings = {(0,0):C.GC_111})

V_68 = Vertex(name = 'V_68',
              particles = [ P.d__tilde__, P.YF3d1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_24})

V_69 = Vertex(name = 'V_69',
              particles = [ P.s__tilde__, P.YF3d2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_25})

V_70 = Vertex(name = 'V_70',
              particles = [ P.b__tilde__, P.YF3d3, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_26})

V_71 = Vertex(name = 'V_71',
              particles = [ P.u__tilde__, P.YF3u1, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_30})

V_72 = Vertex(name = 'V_72',
              particles = [ P.c__tilde__, P.YF3u2, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_31})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.YF3u3, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_32})

V_74 = Vertex(name = 'V_74',
              particles = [ P.YF3Qu1__tilde__, P.u, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_27})

V_75 = Vertex(name = 'V_75',
              particles = [ P.YF3Qd1__tilde__, P.d, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_27})

V_76 = Vertex(name = 'V_76',
              particles = [ P.YF3Qu2__tilde__, P.c, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_28})

V_77 = Vertex(name = 'V_77',
              particles = [ P.YF3Qd2__tilde__, P.s, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_28})

V_78 = Vertex(name = 'V_78',
              particles = [ P.YF3Qu3__tilde__, P.t, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_29})

V_79 = Vertex(name = 'V_79',
              particles = [ P.YF3Qd3__tilde__, P.b, P.Xs ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_29})

V_80 = Vertex(name = 'V_80',
              particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_81 = Vertex(name = 'V_81',
              particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_82 = Vertex(name = 'V_82',
              particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_83 = Vertex(name = 'V_83',
              particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_84 = Vertex(name = 'V_84',
              particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_85 = Vertex(name = 'V_85',
              particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_86 = Vertex(name = 'V_86',
              particles = [ P.YF3u1__tilde__, P.YF3u1, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_87 = Vertex(name = 'V_87',
              particles = [ P.YF3u2__tilde__, P.YF3u2, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_88 = Vertex(name = 'V_88',
              particles = [ P.YF3u3__tilde__, P.YF3u3, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_89 = Vertex(name = 'V_89',
              particles = [ P.YF3d1__tilde__, P.YF3d1, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_90 = Vertex(name = 'V_90',
              particles = [ P.YF3d2__tilde__, P.YF3d2, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_91 = Vertex(name = 'V_91',
              particles = [ P.YF3d3__tilde__, P.YF3d3, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_17})

V_92 = Vertex(name = 'V_92',
              particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_93 = Vertex(name = 'V_93',
              particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_94 = Vertex(name = 'V_94',
              particles = [ P.a, P.W__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_96})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_47})

V_96 = Vertex(name = 'V_96',
              particles = [ P.W__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS2 ],
              couplings = {(0,0):C.GC_45})

V_97 = Vertex(name = 'V_97',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_6})

V_98 = Vertex(name = 'V_98',
              particles = [ P.YF3Qd1__tilde__, P.YF3Qu1, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_49})

V_99 = Vertex(name = 'V_99',
              particles = [ P.YF3Qd2__tilde__, P.YF3Qu2, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_49})

V_100 = Vertex(name = 'V_100',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qu3, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_49})

V_101 = Vertex(name = 'V_101',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_55})

V_102 = Vertex(name = 'V_102',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_56})

V_103 = Vertex(name = 'V_103',
               particles = [ P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_97})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_46})

V_105 = Vertex(name = 'V_105',
               particles = [ P.W__plus__, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_45})

V_106 = Vertex(name = 'V_106',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qd1, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_49})

V_107 = Vertex(name = 'V_107',
               particles = [ P.YF3Qu2__tilde__, P.YF3Qd2, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_49})

V_108 = Vertex(name = 'V_108',
               particles = [ P.YF3Qu3__tilde__, P.YF3Qd3, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_49})

V_109 = Vertex(name = 'V_109',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_110 = Vertex(name = 'V_110',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_111 = Vertex(name = 'V_111',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_112 = Vertex(name = 'V_112',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_94})

V_113 = Vertex(name = 'V_113',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_9})

V_114 = Vertex(name = 'V_114',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_53})

V_115 = Vertex(name = 'V_115',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_43})

V_116 = Vertex(name = 'V_116',
               particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_108})

V_117 = Vertex(name = 'V_117',
               particles = [ P.a, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_118 = Vertex(name = 'V_118',
               particles = [ P.Xd__tilde__, P.d, P.YS3d1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_33})

V_119 = Vertex(name = 'V_119',
               particles = [ P.Xm, P.d, P.YS3d1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_33})

V_120 = Vertex(name = 'V_120',
               particles = [ P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_121 = Vertex(name = 'V_121',
               particles = [ P.d__tilde__, P.Xd, P.YS3d1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_33})

V_122 = Vertex(name = 'V_122',
               particles = [ P.d__tilde__, P.Xm, P.YS3d1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_33})

V_123 = Vertex(name = 'V_123',
               particles = [ P.a, P.a, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_124 = Vertex(name = 'V_124',
               particles = [ P.a, P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_125 = Vertex(name = 'V_125',
               particles = [ P.g, P.g, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_126 = Vertex(name = 'V_126',
               particles = [ P.a, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_2})

V_127 = Vertex(name = 'V_127',
               particles = [ P.Xd__tilde__, P.s, P.YS3d2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_34})

V_128 = Vertex(name = 'V_128',
               particles = [ P.Xm, P.s, P.YS3d2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_34})

V_129 = Vertex(name = 'V_129',
               particles = [ P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_130 = Vertex(name = 'V_130',
               particles = [ P.s__tilde__, P.Xd, P.YS3d2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_34})

V_131 = Vertex(name = 'V_131',
               particles = [ P.s__tilde__, P.Xm, P.YS3d2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_34})

V_132 = Vertex(name = 'V_132',
               particles = [ P.a, P.a, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_133 = Vertex(name = 'V_133',
               particles = [ P.a, P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_134 = Vertex(name = 'V_134',
               particles = [ P.g, P.g, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_135 = Vertex(name = 'V_135',
               particles = [ P.a, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_1})

V_136 = Vertex(name = 'V_136',
               particles = [ P.Xd__tilde__, P.b, P.YS3d3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_35})

V_137 = Vertex(name = 'V_137',
               particles = [ P.Xm, P.b, P.YS3d3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_35})

V_138 = Vertex(name = 'V_138',
               particles = [ P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_139 = Vertex(name = 'V_139',
               particles = [ P.b__tilde__, P.Xd, P.YS3d3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_35})

V_140 = Vertex(name = 'V_140',
               particles = [ P.b__tilde__, P.Xm, P.YS3d3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_35})

V_141 = Vertex(name = 'V_141',
               particles = [ P.a, P.a, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_143 = Vertex(name = 'V_143',
               particles = [ P.g, P.g, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_1})

V_145 = Vertex(name = 'V_145',
               particles = [ P.Xd__tilde__, P.d, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_36})

V_146 = Vertex(name = 'V_146',
               particles = [ P.Xm, P.d, P.YS3Qd1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_36})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_48,(0,1):C.GC_49})

V_148 = Vertex(name = 'V_148',
               particles = [ P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_149 = Vertex(name = 'V_149',
               particles = [ P.d__tilde__, P.Xd, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_36})

V_150 = Vertex(name = 'V_150',
               particles = [ P.d__tilde__, P.Xm, P.YS3Qd1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_36})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_49,(0,1):C.GC_48})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.a, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_155 = Vertex(name = 'V_155',
               particles = [ P.g, P.g, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_156 = Vertex(name = 'V_156',
               particles = [ P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_1})

V_157 = Vertex(name = 'V_157',
               particles = [ P.Xd__tilde__, P.s, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_37})

V_158 = Vertex(name = 'V_158',
               particles = [ P.Xm, P.s, P.YS3Qd2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_37})

V_159 = Vertex(name = 'V_159',
               particles = [ P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_48,(0,1):C.GC_49})

V_160 = Vertex(name = 'V_160',
               particles = [ P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_161 = Vertex(name = 'V_161',
               particles = [ P.s__tilde__, P.Xd, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_37})

V_162 = Vertex(name = 'V_162',
               particles = [ P.s__tilde__, P.Xm, P.YS3Qd2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_37})

V_163 = Vertex(name = 'V_163',
               particles = [ P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_49,(0,1):C.GC_48})

V_164 = Vertex(name = 'V_164',
               particles = [ P.a, P.a, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_165 = Vertex(name = 'V_165',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_167 = Vertex(name = 'V_167',
               particles = [ P.g, P.g, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_1})

V_169 = Vertex(name = 'V_169',
               particles = [ P.Xd__tilde__, P.b, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_38})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Xm, P.b, P.YS3Qd3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_38})

V_171 = Vertex(name = 'V_171',
               particles = [ P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_48,(0,1):C.GC_49})

V_172 = Vertex(name = 'V_172',
               particles = [ P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_173 = Vertex(name = 'V_173',
               particles = [ P.b__tilde__, P.Xd, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_38})

V_174 = Vertex(name = 'V_174',
               particles = [ P.b__tilde__, P.Xm, P.YS3Qd3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_38})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_49,(0,1):C.GC_48})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.a, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_7})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_18})

V_179 = Vertex(name = 'V_179',
               particles = [ P.g, P.g, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_3,(0,1):C.GC_4})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Xd__tilde__, P.u, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_36})

V_182 = Vertex(name = 'V_182',
               particles = [ P.Xm, P.u, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_36})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_184 = Vertex(name = 'V_184',
               particles = [ P.g, P.W__plus__, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_185 = Vertex(name = 'V_185',
               particles = [ P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_186 = Vertex(name = 'V_186',
               particles = [ P.u__tilde__, P.Xd, P.YS3Qu1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_36})

V_187 = Vertex(name = 'V_187',
               particles = [ P.u__tilde__, P.Xm, P.YS3Qu1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_36})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_189 = Vertex(name = 'V_189',
               particles = [ P.g, P.W__minus__, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.a, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_191 = Vertex(name = 'V_191',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_193 = Vertex(name = 'V_193',
               particles = [ P.g, P.g, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS1, L.VSS3 ],
               couplings = {(0,0):C.GC_3,(0,1):C.GC_4})

V_195 = Vertex(name = 'V_195',
               particles = [ P.Xd__tilde__, P.c, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_37})

V_196 = Vertex(name = 'V_196',
               particles = [ P.Xm, P.c, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_37})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_198 = Vertex(name = 'V_198',
               particles = [ P.g, P.W__plus__, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_199 = Vertex(name = 'V_199',
               particles = [ P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_200 = Vertex(name = 'V_200',
               particles = [ P.c__tilde__, P.Xd, P.YS3Qu2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_37})

V_201 = Vertex(name = 'V_201',
               particles = [ P.c__tilde__, P.Xm, P.YS3Qu2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_37})

V_202 = Vertex(name = 'V_202',
               particles = [ P.a, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_203 = Vertex(name = 'V_203',
               particles = [ P.g, P.W__minus__, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_204 = Vertex(name = 'V_204',
               particles = [ P.a, P.a, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_206 = Vertex(name = 'V_206',
               particles = [ P.a, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_207 = Vertex(name = 'V_207',
               particles = [ P.g, P.g, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_208 = Vertex(name = 'V_208',
               particles = [ P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_209 = Vertex(name = 'V_209',
               particles = [ P.Xd__tilde__, P.t, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_38})

V_210 = Vertex(name = 'V_210',
               particles = [ P.Xm, P.t, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_38})

V_211 = Vertex(name = 'V_211',
               particles = [ P.a, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_212 = Vertex(name = 'V_212',
               particles = [ P.g, P.W__plus__, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'T(1,3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_213 = Vertex(name = 'V_213',
               particles = [ P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_214 = Vertex(name = 'V_214',
               particles = [ P.t__tilde__, P.Xd, P.YS3Qu3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_38})

V_215 = Vertex(name = 'V_215',
               particles = [ P.t__tilde__, P.Xm, P.YS3Qu3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_38})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_57})

V_217 = Vertex(name = 'V_217',
               particles = [ P.g, P.W__minus__, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_59})

V_218 = Vertex(name = 'V_218',
               particles = [ P.a, P.a, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.W__plus__, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_42})

V_220 = Vertex(name = 'V_220',
               particles = [ P.a, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_221 = Vertex(name = 'V_221',
               particles = [ P.g, P.g, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_222 = Vertex(name = 'V_222',
               particles = [ P.a, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_223 = Vertex(name = 'V_223',
               particles = [ P.Xd__tilde__, P.u, P.YS3u1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_39})

V_224 = Vertex(name = 'V_224',
               particles = [ P.Xm, P.u, P.YS3u1__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_39})

V_225 = Vertex(name = 'V_225',
               particles = [ P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_226 = Vertex(name = 'V_226',
               particles = [ P.u__tilde__, P.Xd, P.YS3u1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_39})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.Xm, P.YS3u1 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_39})

V_228 = Vertex(name = 'V_228',
               particles = [ P.a, P.a, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_229 = Vertex(name = 'V_229',
               particles = [ P.a, P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_230 = Vertex(name = 'V_230',
               particles = [ P.g, P.g, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_231 = Vertex(name = 'V_231',
               particles = [ P.a, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_232 = Vertex(name = 'V_232',
               particles = [ P.Xd__tilde__, P.c, P.YS3u2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_40})

V_233 = Vertex(name = 'V_233',
               particles = [ P.Xm, P.c, P.YS3u2__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_40})

V_234 = Vertex(name = 'V_234',
               particles = [ P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_235 = Vertex(name = 'V_235',
               particles = [ P.c__tilde__, P.Xd, P.YS3u2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_40})

V_236 = Vertex(name = 'V_236',
               particles = [ P.c__tilde__, P.Xm, P.YS3u2 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_40})

V_237 = Vertex(name = 'V_237',
               particles = [ P.a, P.a, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_238 = Vertex(name = 'V_238',
               particles = [ P.a, P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_239 = Vertex(name = 'V_239',
               particles = [ P.g, P.g, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_240 = Vertex(name = 'V_240',
               particles = [ P.a, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_3})

V_241 = Vertex(name = 'V_241',
               particles = [ P.Xd__tilde__, P.t, P.YS3u3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_41})

V_242 = Vertex(name = 'V_242',
               particles = [ P.Xm, P.t, P.YS3u3__tilde__ ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_41})

V_243 = Vertex(name = 'V_243',
               particles = [ P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,3,2)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_16})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.Xd, P.YS3u3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_41})

V_245 = Vertex(name = 'V_245',
               particles = [ P.t__tilde__, P.Xm, P.YS3u3 ],
               color = [ 'Identity(1,3)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_41})

V_246 = Vertex(name = 'V_246',
               particles = [ P.a, P.a, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_8})

V_247 = Vertex(name = 'V_247',
               particles = [ P.a, P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(2,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_19})

V_248 = Vertex(name = 'V_248',
               particles = [ P.g, P.g, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(1,0):C.GC_20,(0,0):C.GC_20})

V_249 = Vertex(name = 'V_249',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_104})

V_250 = Vertex(name = 'V_250',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_81})

V_251 = Vertex(name = 'V_251',
               particles = [ P.Z, P.G0, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_72})

V_252 = Vertex(name = 'V_252',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_77})

V_253 = Vertex(name = 'V_253',
               particles = [ P.YF3Qd1__tilde__, P.YF3Qd1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_73})

V_254 = Vertex(name = 'V_254',
               particles = [ P.YF3Qd2__tilde__, P.YF3Qd2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_73})

V_255 = Vertex(name = 'V_255',
               particles = [ P.YF3Qd3__tilde__, P.YF3Qd3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_73})

V_256 = Vertex(name = 'V_256',
               particles = [ P.YF3Qu1__tilde__, P.YF3Qu1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_74})

V_257 = Vertex(name = 'V_257',
               particles = [ P.YF3Qu2__tilde__, P.YF3Qu2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_74})

V_258 = Vertex(name = 'V_258',
               particles = [ P.YF3Qu3__tilde__, P.YF3Qu3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_74})

V_259 = Vertex(name = 'V_259',
               particles = [ P.YF3d1__tilde__, P.YF3d1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_62})

V_260 = Vertex(name = 'V_260',
               particles = [ P.YF3d2__tilde__, P.YF3d2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_62})

V_261 = Vertex(name = 'V_261',
               particles = [ P.YF3d3__tilde__, P.YF3d3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_62})

V_262 = Vertex(name = 'V_262',
               particles = [ P.YF3u1__tilde__, P.YF3u1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_64})

V_263 = Vertex(name = 'V_263',
               particles = [ P.YF3u2__tilde__, P.YF3u2, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_64})

V_264 = Vertex(name = 'V_264',
               particles = [ P.YF3u3__tilde__, P.YF3u3, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_64})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_12})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_13})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_89})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_12})

V_269 = Vertex(name = 'V_269',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_11})

V_270 = Vertex(name = 'V_270',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_88})

V_271 = Vertex(name = 'V_271',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV9 ],
               couplings = {(0,0):C.GC_58})

V_272 = Vertex(name = 'V_272',
               particles = [ P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_61})

V_273 = Vertex(name = 'V_273',
               particles = [ P.a, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_66})

V_274 = Vertex(name = 'V_274',
               particles = [ P.g, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_275 = Vertex(name = 'V_275',
               particles = [ P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_61})

V_276 = Vertex(name = 'V_276',
               particles = [ P.a, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_66})

V_277 = Vertex(name = 'V_277',
               particles = [ P.g, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_278 = Vertex(name = 'V_278',
               particles = [ P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_61})

V_279 = Vertex(name = 'V_279',
               particles = [ P.a, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_66})

V_280 = Vertex(name = 'V_280',
               particles = [ P.g, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_68})

V_281 = Vertex(name = 'V_281',
               particles = [ P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_76})

V_282 = Vertex(name = 'V_282',
               particles = [ P.a, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_79})

V_283 = Vertex(name = 'V_283',
               particles = [ P.g, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_82})

V_284 = Vertex(name = 'V_284',
               particles = [ P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_76})

V_285 = Vertex(name = 'V_285',
               particles = [ P.a, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_79})

V_286 = Vertex(name = 'V_286',
               particles = [ P.g, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_82})

V_287 = Vertex(name = 'V_287',
               particles = [ P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_76})

V_288 = Vertex(name = 'V_288',
               particles = [ P.a, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_79})

V_289 = Vertex(name = 'V_289',
               particles = [ P.g, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_82})

V_290 = Vertex(name = 'V_290',
               particles = [ P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_75})

V_291 = Vertex(name = 'V_291',
               particles = [ P.W__plus__, P.Z, P.YS3Qd1, P.YS3Qu1__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_292 = Vertex(name = 'V_292',
               particles = [ P.W__minus__, P.Z, P.YS3Qd1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_293 = Vertex(name = 'V_293',
               particles = [ P.a, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_294 = Vertex(name = 'V_294',
               particles = [ P.g, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_83})

V_295 = Vertex(name = 'V_295',
               particles = [ P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_75})

V_296 = Vertex(name = 'V_296',
               particles = [ P.W__plus__, P.Z, P.YS3Qd2, P.YS3Qu2__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__minus__, P.Z, P.YS3Qd2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_298 = Vertex(name = 'V_298',
               particles = [ P.a, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_299 = Vertex(name = 'V_299',
               particles = [ P.g, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_83})

V_300 = Vertex(name = 'V_300',
               particles = [ P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_75})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__plus__, P.Z, P.YS3Qd3, P.YS3Qu3__tilde__ ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__minus__, P.Z, P.YS3Qd3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_14})

V_303 = Vertex(name = 'V_303',
               particles = [ P.a, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_80})

V_304 = Vertex(name = 'V_304',
               particles = [ P.g, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_83})

V_305 = Vertex(name = 'V_305',
               particles = [ P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_65})

V_306 = Vertex(name = 'V_306',
               particles = [ P.a, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_307 = Vertex(name = 'V_307',
               particles = [ P.g, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_69})

V_308 = Vertex(name = 'V_308',
               particles = [ P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_65})

V_309 = Vertex(name = 'V_309',
               particles = [ P.a, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_310 = Vertex(name = 'V_310',
               particles = [ P.g, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_69})

V_311 = Vertex(name = 'V_311',
               particles = [ P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(2,3)' ],
               lorentz = [ L.VSS2 ],
               couplings = {(0,0):C.GC_65})

V_312 = Vertex(name = 'V_312',
               particles = [ P.a, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_67})

V_313 = Vertex(name = 'V_313',
               particles = [ P.g, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'T(1,4,3)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_69})

V_314 = Vertex(name = 'V_314',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_87})

V_315 = Vertex(name = 'V_315',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_86})

V_316 = Vertex(name = 'V_316',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_87})

V_317 = Vertex(name = 'V_317',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_103})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_44})

V_319 = Vertex(name = 'V_319',
               particles = [ P.Z, P.Z, P.YS3d1__tilde__, P.YS3d1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_70})

V_320 = Vertex(name = 'V_320',
               particles = [ P.Z, P.Z, P.YS3d2__tilde__, P.YS3d2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_70})

V_321 = Vertex(name = 'V_321',
               particles = [ P.Z, P.Z, P.YS3d3__tilde__, P.YS3d3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_70})

V_322 = Vertex(name = 'V_322',
               particles = [ P.Z, P.Z, P.YS3Qd1__tilde__, P.YS3Qd1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_85})

V_323 = Vertex(name = 'V_323',
               particles = [ P.Z, P.Z, P.YS3Qd2__tilde__, P.YS3Qd2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_85})

V_324 = Vertex(name = 'V_324',
               particles = [ P.Z, P.Z, P.YS3Qd3__tilde__, P.YS3Qd3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_85})

V_325 = Vertex(name = 'V_325',
               particles = [ P.Z, P.Z, P.YS3Qu1__tilde__, P.YS3Qu1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_84})

V_326 = Vertex(name = 'V_326',
               particles = [ P.Z, P.Z, P.YS3Qu2__tilde__, P.YS3Qu2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_84})

V_327 = Vertex(name = 'V_327',
               particles = [ P.Z, P.Z, P.YS3Qu3__tilde__, P.YS3Qu3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_84})

V_328 = Vertex(name = 'V_328',
               particles = [ P.Z, P.Z, P.YS3u1__tilde__, P.YS3u1 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_71})

V_329 = Vertex(name = 'V_329',
               particles = [ P.Z, P.Z, P.YS3u2__tilde__, P.YS3u2 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_71})

V_330 = Vertex(name = 'V_330',
               particles = [ P.Z, P.Z, P.YS3u3__tilde__, P.YS3u3 ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_71})

V_331 = Vertex(name = 'V_331',
               particles = [ P.u__tilde__, P.YF3Qu1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_332 = Vertex(name = 'V_332',
               particles = [ P.d__tilde__, P.YF3Qd1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_333 = Vertex(name = 'V_333',
               particles = [ P.c__tilde__, P.YF3Qu2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_334 = Vertex(name = 'V_334',
               particles = [ P.s__tilde__, P.YF3Qd2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_335 = Vertex(name = 'V_335',
               particles = [ P.t__tilde__, P.YF3Qu3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_336 = Vertex(name = 'V_336',
               particles = [ P.b__tilde__, P.YF3Qd3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_337 = Vertex(name = 'V_337',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_338 = Vertex(name = 'V_338',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_339 = Vertex(name = 'V_339',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_340 = Vertex(name = 'V_340',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_341 = Vertex(name = 'V_341',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_342 = Vertex(name = 'V_342',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_343 = Vertex(name = 'V_343',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_344 = Vertex(name = 'V_344',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_345 = Vertex(name = 'V_345',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_346 = Vertex(name = 'V_346',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_347 = Vertex(name = 'V_347',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_348 = Vertex(name = 'V_348',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_349 = Vertex(name = 'V_349',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_350 = Vertex(name = 'V_350',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_351 = Vertex(name = 'V_351',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_17})

V_352 = Vertex(name = 'V_352',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_353 = Vertex(name = 'V_353',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_354 = Vertex(name = 'V_354',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_355 = Vertex(name = 'V_355',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_356 = Vertex(name = 'V_356',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_357 = Vertex(name = 'V_357',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_358 = Vertex(name = 'V_358',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_359 = Vertex(name = 'V_359',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_360 = Vertex(name = 'V_360',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_361 = Vertex(name = 'V_361',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_362 = Vertex(name = 'V_362',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_363 = Vertex(name = 'V_363',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_49})

V_364 = Vertex(name = 'V_364',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_51,(0,1):C.GC_60})

V_365 = Vertex(name = 'V_365',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_51,(0,1):C.GC_60})

V_366 = Vertex(name = 'V_366',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV7 ],
               couplings = {(0,0):C.GC_51,(0,1):C.GC_60})

V_367 = Vertex(name = 'V_367',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_60})

V_368 = Vertex(name = 'V_368',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_60})

V_369 = Vertex(name = 'V_369',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_60})

V_370 = Vertex(name = 'V_370',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_78})

V_371 = Vertex(name = 'V_371',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_78})

V_372 = Vertex(name = 'V_372',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_78})

V_373 = Vertex(name = 'V_373',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_63})

V_374 = Vertex(name = 'V_374',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_63})

V_375 = Vertex(name = 'V_375',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_50,(0,1):C.GC_63})

V_376 = Vertex(name = 'V_376',
               particles = [ P.YF3Qu1__tilde__, P.u, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_377 = Vertex(name = 'V_377',
               particles = [ P.YF3Qd1__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_378 = Vertex(name = 'V_378',
               particles = [ P.YF3Qu2__tilde__, P.c, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_379 = Vertex(name = 'V_379',
               particles = [ P.YF3Qd2__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_380 = Vertex(name = 'V_380',
               particles = [ P.YF3Qu3__tilde__, P.t, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_381 = Vertex(name = 'V_381',
               particles = [ P.YF3Qd3__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_382 = Vertex(name = 'V_382',
               particles = [ P.d__tilde__, P.YF3d1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_24})

V_383 = Vertex(name = 'V_383',
               particles = [ P.s__tilde__, P.YF3d2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_384 = Vertex(name = 'V_384',
               particles = [ P.b__tilde__, P.YF3d3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_385 = Vertex(name = 'V_385',
               particles = [ P.u__tilde__, P.YF3u1, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_30})

V_386 = Vertex(name = 'V_386',
               particles = [ P.c__tilde__, P.YF3u2, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_387 = Vertex(name = 'V_387',
               particles = [ P.t__tilde__, P.YF3u3, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

V_388 = Vertex(name = 'V_388',
               particles = [ P.YF3d1__tilde__, P.d, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_24})

V_389 = Vertex(name = 'V_389',
               particles = [ P.YF3d2__tilde__, P.s, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_25})

V_390 = Vertex(name = 'V_390',
               particles = [ P.YF3d3__tilde__, P.b, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_26})

V_391 = Vertex(name = 'V_391',
               particles = [ P.YF3u1__tilde__, P.u, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_30})

V_392 = Vertex(name = 'V_392',
               particles = [ P.YF3u2__tilde__, P.c, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_31})

V_393 = Vertex(name = 'V_393',
               particles = [ P.YF3u3__tilde__, P.t, P.Xv ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_32})

