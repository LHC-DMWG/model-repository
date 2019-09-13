# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 6 Jun 2019 21:52:44



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
lamF3d1x1 = Parameter(name = 'lamF3d1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.26,
                      texname = '\\text{lamF3d1x1}',
                      lhablock = 'DMF3D',
                      lhacode = [ 1, 1 ])

lamF3d2x2 = Parameter(name = 'lamF3d2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.27,
                      texname = '\\text{lamF3d2x2}',
                      lhablock = 'DMF3D',
                      lhacode = [ 2, 2 ])

lamF3d3x3 = Parameter(name = 'lamF3d3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.28,
                      texname = '\\text{lamF3d3x3}',
                      lhablock = 'DMF3D',
                      lhacode = [ 3, 3 ])

lamF3Q1x1 = Parameter(name = 'lamF3Q1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.2,
                      texname = '\\text{lamF3Q1x1}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 1, 1 ])

lamF3Q2x2 = Parameter(name = 'lamF3Q2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.21,
                      texname = '\\text{lamF3Q2x2}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 2, 2 ])

lamF3Q3x3 = Parameter(name = 'lamF3Q3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.22,
                      texname = '\\text{lamF3Q3x3}',
                      lhablock = 'DMF3Q',
                      lhacode = [ 3, 3 ])

lamF3u1x1 = Parameter(name = 'lamF3u1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.23,
                      texname = '\\text{lamF3u1x1}',
                      lhablock = 'DMF3U',
                      lhacode = [ 1, 1 ])

lamF3u2x2 = Parameter(name = 'lamF3u2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.24,
                      texname = '\\text{lamF3u2x2}',
                      lhablock = 'DMF3U',
                      lhacode = [ 2, 2 ])

lamF3u3x3 = Parameter(name = 'lamF3u3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.25,
                      texname = '\\text{lamF3u3x3}',
                      lhablock = 'DMF3U',
                      lhacode = [ 3, 3 ])

lamS3d1x1 = Parameter(name = 'lamS3d1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.16,
                      texname = '\\text{lamS3d1x1}',
                      lhablock = 'DMS3D',
                      lhacode = [ 1, 1 ])

lamS3d2x2 = Parameter(name = 'lamS3d2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.17,
                      texname = '\\text{lamS3d2x2}',
                      lhablock = 'DMS3D',
                      lhacode = [ 2, 2 ])

lamS3d3x3 = Parameter(name = 'lamS3d3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.18,
                      texname = '\\text{lamS3d3x3}',
                      lhablock = 'DMS3D',
                      lhacode = [ 3, 3 ])

lamS3Q1x1 = Parameter(name = 'lamS3Q1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.1,
                      texname = '\\text{lamS3Q1x1}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 1, 1 ])

lamS3Q2x2 = Parameter(name = 'lamS3Q2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.11,
                      texname = '\\text{lamS3Q2x2}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 2, 2 ])

lamS3Q3x3 = Parameter(name = 'lamS3Q3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.12,
                      texname = '\\text{lamS3Q3x3}',
                      lhablock = 'DMS3Q',
                      lhacode = [ 3, 3 ])

lamS3u1x1 = Parameter(name = 'lamS3u1x1',
                      nature = 'external',
                      type = 'real',
                      value = 0.13,
                      texname = '\\text{lamS3u1x1}',
                      lhablock = 'DMS3U',
                      lhacode = [ 1, 1 ])

lamS3u2x2 = Parameter(name = 'lamS3u2x2',
                      nature = 'external',
                      type = 'real',
                      value = 0.14,
                      texname = '\\text{lamS3u2x2}',
                      lhablock = 'DMS3U',
                      lhacode = [ 2, 2 ])

lamS3u3x3 = Parameter(name = 'lamS3u3x3',
                      nature = 'external',
                      type = 'real',
                      value = 0.15,
                      texname = '\\text{lamS3u3x3}',
                      lhablock = 'DMS3U',
                      lhacode = [ 3, 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXm = Parameter(name = 'MXm',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXm}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 13.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 57 ])

MXs = Parameter(name = 'MXs',
                nature = 'external',
                type = 'real',
                value = 11.,
                texname = '\\text{MXs}',
                lhablock = 'MASS',
                lhacode = [ 51 ])

MXv = Parameter(name = 'MXv',
                nature = 'external',
                type = 'real',
                value = 12.,
                texname = '\\text{MXv}',
                lhablock = 'MASS',
                lhacode = [ 53 ])

MYS3Qu1 = Parameter(name = 'MYS3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 1000.,
                    texname = '\\text{MYS3Qu1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000002 ])

MYS3Qu2 = Parameter(name = 'MYS3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 1001.,
                    texname = '\\text{MYS3Qu2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000004 ])

MYS3Qu3 = Parameter(name = 'MYS3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 1002.,
                    texname = '\\text{MYS3Qu3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000006 ])

MYS3Qd1 = Parameter(name = 'MYS3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 1003.,
                    texname = '\\text{MYS3Qd1}',
                    lhablock = 'MASS',
                    lhacode = [ 1000001 ])

MYS3Qd2 = Parameter(name = 'MYS3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 1004.,
                    texname = '\\text{MYS3Qd2}',
                    lhablock = 'MASS',
                    lhacode = [ 1000003 ])

MYS3Qd3 = Parameter(name = 'MYS3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 1005.,
                    texname = '\\text{MYS3Qd3}',
                    lhablock = 'MASS',
                    lhacode = [ 1000005 ])

MYS3u1 = Parameter(name = 'MYS3u1',
                   nature = 'external',
                   type = 'real',
                   value = 2000.,
                   texname = '\\text{MYS3u1}',
                   lhablock = 'MASS',
                   lhacode = [ 2000002 ])

MYS3u2 = Parameter(name = 'MYS3u2',
                   nature = 'external',
                   type = 'real',
                   value = 2001.,
                   texname = '\\text{MYS3u2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000004 ])

MYS3u3 = Parameter(name = 'MYS3u3',
                   nature = 'external',
                   type = 'real',
                   value = 2002.,
                   texname = '\\text{MYS3u3}',
                   lhablock = 'MASS',
                   lhacode = [ 2000006 ])

MYS3d1 = Parameter(name = 'MYS3d1',
                   nature = 'external',
                   type = 'real',
                   value = 2003.,
                   texname = '\\text{MYS3d1}',
                   lhablock = 'MASS',
                   lhacode = [ 2000001 ])

MYS3d2 = Parameter(name = 'MYS3d2',
                   nature = 'external',
                   type = 'real',
                   value = 2004.,
                   texname = '\\text{MYS3d2}',
                   lhablock = 'MASS',
                   lhacode = [ 2000003 ])

MYS3d3 = Parameter(name = 'MYS3d3',
                   nature = 'external',
                   type = 'real',
                   value = 2005.,
                   texname = '\\text{MYS3d3}',
                   lhablock = 'MASS',
                   lhacode = [ 2000005 ])

MYF3Qu1 = Parameter(name = 'MYF3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 3000.,
                    texname = '\\text{MYF3Qu1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910002 ])

MYF3Qu2 = Parameter(name = 'MYF3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 3001.,
                    texname = '\\text{MYF3Qu2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910004 ])

MYF3Qu3 = Parameter(name = 'MYF3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 3002.,
                    texname = '\\text{MYF3Qu3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910006 ])

MYF3Qd1 = Parameter(name = 'MYF3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 3003.,
                    texname = '\\text{MYF3Qd1}',
                    lhablock = 'MASS',
                    lhacode = [ 5910001 ])

MYF3Qd2 = Parameter(name = 'MYF3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 3004.,
                    texname = '\\text{MYF3Qd2}',
                    lhablock = 'MASS',
                    lhacode = [ 5910003 ])

MYF3Qd3 = Parameter(name = 'MYF3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 3005.,
                    texname = '\\text{MYF3Qd3}',
                    lhablock = 'MASS',
                    lhacode = [ 5910005 ])

MYF3u1 = Parameter(name = 'MYF3u1',
                   nature = 'external',
                   type = 'real',
                   value = 4000.,
                   texname = '\\text{MYF3u1}',
                   lhablock = 'MASS',
                   lhacode = [ 5920002 ])

MYF3u2 = Parameter(name = 'MYF3u2',
                   nature = 'external',
                   type = 'real',
                   value = 4001.,
                   texname = '\\text{MYF3u2}',
                   lhablock = 'MASS',
                   lhacode = [ 5920004 ])

MYF3u3 = Parameter(name = 'MYF3u3',
                   nature = 'external',
                   type = 'real',
                   value = 4002.,
                   texname = '\\text{MYF3u3}',
                   lhablock = 'MASS',
                   lhacode = [ 5920006 ])

MYF3d1 = Parameter(name = 'MYF3d1',
                   nature = 'external',
                   type = 'real',
                   value = 4003.,
                   texname = '\\text{MYF3d1}',
                   lhablock = 'MASS',
                   lhacode = [ 5920001 ])

MYF3d2 = Parameter(name = 'MYF3d2',
                   nature = 'external',
                   type = 'real',
                   value = 4004.,
                   texname = '\\text{MYF3d2}',
                   lhablock = 'MASS',
                   lhacode = [ 5920003 ])

MYF3d3 = Parameter(name = 'MYF3d3',
                   nature = 'external',
                   type = 'real',
                   value = 4005.,
                   texname = '\\text{MYF3d3}',
                   lhablock = 'MASS',
                   lhacode = [ 5920005 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WYS3Qu1 = Parameter(name = 'WYS3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 10.,
                    texname = '\\text{WYS3Qu1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000002 ])

WYS3Qu2 = Parameter(name = 'WYS3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 11.,
                    texname = '\\text{WYS3Qu2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000004 ])

WYS3Qu3 = Parameter(name = 'WYS3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 12.,
                    texname = '\\text{WYS3Qu3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000006 ])

WYS3Qd1 = Parameter(name = 'WYS3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 13.,
                    texname = '\\text{WYS3Qd1}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000001 ])

WYS3Qd2 = Parameter(name = 'WYS3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 14.,
                    texname = '\\text{WYS3Qd2}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000003 ])

WYS3Qd3 = Parameter(name = 'WYS3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 15.,
                    texname = '\\text{WYS3Qd3}',
                    lhablock = 'DECAY',
                    lhacode = [ 1000005 ])

WYS3u1 = Parameter(name = 'WYS3u1',
                   nature = 'external',
                   type = 'real',
                   value = 20.,
                   texname = '\\text{WYS3u1}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000002 ])

WYS3u2 = Parameter(name = 'WYS3u2',
                   nature = 'external',
                   type = 'real',
                   value = 21.,
                   texname = '\\text{WYS3u2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000004 ])

WYS3u3 = Parameter(name = 'WYS3u3',
                   nature = 'external',
                   type = 'real',
                   value = 22.,
                   texname = '\\text{WYS3u3}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000006 ])

WYS3d1 = Parameter(name = 'WYS3d1',
                   nature = 'external',
                   type = 'real',
                   value = 23.,
                   texname = '\\text{WYS3d1}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000001 ])

WYS3d2 = Parameter(name = 'WYS3d2',
                   nature = 'external',
                   type = 'real',
                   value = 24.,
                   texname = '\\text{WYS3d2}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000003 ])

WYS3d3 = Parameter(name = 'WYS3d3',
                   nature = 'external',
                   type = 'real',
                   value = 25.,
                   texname = '\\text{WYS3d3}',
                   lhablock = 'DECAY',
                   lhacode = [ 2000005 ])

WYF3Qu1 = Parameter(name = 'WYF3Qu1',
                    nature = 'external',
                    type = 'real',
                    value = 30.,
                    texname = '\\text{WYF3Qu1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910002 ])

WYF3Qu2 = Parameter(name = 'WYF3Qu2',
                    nature = 'external',
                    type = 'real',
                    value = 31.,
                    texname = '\\text{WYF3Qu2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910004 ])

WYF3Qu3 = Parameter(name = 'WYF3Qu3',
                    nature = 'external',
                    type = 'real',
                    value = 32.,
                    texname = '\\text{WYF3Qu3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910006 ])

WYF3Qd1 = Parameter(name = 'WYF3Qd1',
                    nature = 'external',
                    type = 'real',
                    value = 33.,
                    texname = '\\text{WYF3Qd1}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910001 ])

WYF3Qd2 = Parameter(name = 'WYF3Qd2',
                    nature = 'external',
                    type = 'real',
                    value = 34.,
                    texname = '\\text{WYF3Qd2}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910003 ])

WYF3Qd3 = Parameter(name = 'WYF3Qd3',
                    nature = 'external',
                    type = 'real',
                    value = 35.,
                    texname = '\\text{WYF3Qd3}',
                    lhablock = 'DECAY',
                    lhacode = [ 5910005 ])

WYF3u1 = Parameter(name = 'WYF3u1',
                   nature = 'external',
                   type = 'real',
                   value = 40.,
                   texname = '\\text{WYF3u1}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920002 ])

WYF3u2 = Parameter(name = 'WYF3u2',
                   nature = 'external',
                   type = 'real',
                   value = 41.,
                   texname = '\\text{WYF3u2}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920004 ])

WYF3u3 = Parameter(name = 'WYF3u3',
                   nature = 'external',
                   type = 'real',
                   value = 42.,
                   texname = '\\text{WYF3u3}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920006 ])

WYF3d1 = Parameter(name = 'WYF3d1',
                   nature = 'external',
                   type = 'real',
                   value = 43.,
                   texname = '\\text{WYF3d1}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920001 ])

WYF3d2 = Parameter(name = 'WYF3d2',
                   nature = 'external',
                   type = 'real',
                   value = 44.,
                   texname = '\\text{WYF3d2}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920003 ])

WYF3d3 = Parameter(name = 'WYF3d3',
                   nature = 'external',
                   type = 'real',
                   value = 45.,
                   texname = '\\text{WYF3d3}',
                   lhablock = 'DECAY',
                   lhacode = [ 5920005 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

