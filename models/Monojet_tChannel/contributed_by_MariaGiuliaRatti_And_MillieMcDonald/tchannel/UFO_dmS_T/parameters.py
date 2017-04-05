# This file was automatically created by FeynRules 2.0.31
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Wed 3 Jun 2015 14:26:28



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

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

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

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

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MEtaD = Parameter(name = 'MEtaD',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaD}',
                  lhablock = 'MASS',
                  lhacode = [ 9000006 ])

MEtaU = Parameter(name = 'MEtaU',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaU}',
                  lhablock = 'MASS',
                  lhacode = [ 9000007 ])

MEtaS = Parameter(name = 'MEtaS',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaS}',
                  lhablock = 'MASS',
                  lhacode = [ 9000008 ])

MEtaC = Parameter(name = 'MEtaC',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaC}',
                  lhablock = 'MASS',
                  lhacode = [ 9000009 ])

MEtaB = Parameter(name = 'MEtaB',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaB}',
                  lhablock = 'MASS',
                  lhacode = [ 9000014 ])

MEtaT = Parameter(name = 'MEtaT',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaT}',
                  lhablock = 'MASS',
                  lhacode = [ 9000011 ])

MEta0 = Parameter(name = 'MEta0',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEta0}',
                  lhablock = 'MASS',
                  lhacode = [ 9000012 ])

MEtaP = Parameter(name = 'MEtaP',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MEtaP}',
                  lhablock = 'MASS',
                  lhacode = [ 9000013 ])

MChi = Parameter(name = 'MChi',
                 nature = 'external',
                 type = 'real',
                 value = 10,
                 texname = '\\text{MChi}',
                 lhablock = 'MASS',
                 lhacode = [ 1000022 ])

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

WEtaD = Parameter(name = 'WEtaD',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaD}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000006 ])

WEtaU = Parameter(name = 'WEtaU',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaU}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000007 ])

WEtaS = Parameter(name = 'WEtaS',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaS}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000008 ])

WEtaC = Parameter(name = 'WEtaC',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaC}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000009 ])

WEtaB = Parameter(name = 'WEtaB',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaB}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000014 ])

WEtaT = Parameter(name = 'WEtaT',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaT}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000011 ])

WEta0 = Parameter(name = 'WEta0',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEta0}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000012 ])

WEtaP = Parameter(name = 'WEtaP',
                  nature = 'external',
                  type = 'real',
                  value = 1,
                  texname = '\\text{WEtaP}',
                  lhablock = 'DECAY',
                  lhacode = [ 9000013 ])

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

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

fUD = Parameter(name = 'fUD',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{fUD}',
                lhablock = 'HIDDEN',
                lhacode = [ 1 ])

fCS = Parameter(name = 'fCS',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{fCS}',
                lhablock = 'HIDDEN',
                lhacode = [ 2 ])

fTB = Parameter(name = 'fTB',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{fTB}',
                lhablock = 'HIDDEN',
                lhacode = [ 3 ])

fe = Parameter(name = 'fe',
               nature = 'internal',
               type = 'real',
               value = '0',
               texname = '\\text{fe}')

fmu = Parameter(name = 'fmu',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{fmu}')

ftau = Parameter(name = 'ftau',
                 nature = 'internal',
                 type = 'real',
                 value = '0',
                 texname = '\\text{ftau}')

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

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

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

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

