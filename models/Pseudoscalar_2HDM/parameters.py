# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Mon 11 Sep 2017 14:35:03



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
gPXd = Parameter(name = 'gPXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{PXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

lam3 = Parameter(name = 'lam3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{lam3}',
                 lhablock = 'Higgs',
                 lhacode = [ 1 ])

laP1 = Parameter(name = 'laP1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{laP1}',
                 lhablock = 'Higgs',
                 lhacode = [ 2 ])

laP2 = Parameter(name = 'laP2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{laP2}',
                 lhablock = 'Higgs',
                 lhacode = [ 3 ])

sinp = Parameter(name = 'sinp',
                 nature = 'external',
                 type = 'real',
                 value = 0.707107,
                 texname = '\\text{sinp}',
                 lhablock = 'Higgs',
                 lhacode = [ 5 ])

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
               value = 0.000011663900000000002,
               texname = '\\text{Gf}',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
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

tanbeta = Parameter(name = 'tanbeta',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = '\\text{tanbeta}',
                    lhablock = 'FRBlock',
                    lhacode = [ 2 ])

sinbma = Parameter(name = 'sinbma',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{sinbma}',
                   lhablock = 'FRBlock',
                   lhacode = [ 3 ])

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

mhc = Parameter(name = 'mhc',
                nature = 'external',
                type = 'real',
                value = 750,
                texname = '\\text{mhc}',
                lhablock = 'MASS',
                lhacode = [ 37 ])

mh1 = Parameter(name = 'mh1',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

mh2 = Parameter(name = 'mh2',
                nature = 'external',
                type = 'real',
                value = 750,
                texname = '\\text{mh2}',
                lhablock = 'MASS',
                lhacode = [ 35 ])

mh3 = Parameter(name = 'mh3',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{mh3}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

mh4 = Parameter(name = 'mh4',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{mh4}',
                lhablock = 'MASS',
                lhacode = [ 55 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 52 ])

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

whc = Parameter(name = 'whc',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{whc}',
                lhablock = 'DECAY',
                lhacode = [ 37 ])

Wh1 = Parameter(name = 'Wh1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

Wh2 = Parameter(name = 'Wh2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh2}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

Wh3 = Parameter(name = 'Wh3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh3}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

Wh4 = Parameter(name = 'Wh4',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh4}',
                lhablock = 'DECAY',
                lhacode = [ 55 ])

dm2 = Parameter(name = 'dm2',
                nature = 'internal',
                type = 'real',
                value = '-mh1**2 + mh2**2',
                texname = '\\text{dm2}')

mA = Parameter(name = 'mA',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(mh3**2 + mh4**2 + (mh3**2 - mh4**2)*cmath.cos(2*cmath.asin(sinp)))/cmath.sqrt(2)',
               texname = '\\text{mA}')

mP = Parameter(name = 'mP',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(mh3**2 + mh4**2 + (-mh3**2 + mh4**2)*cmath.cos(2*cmath.asin(sinp)))/cmath.sqrt(2)',
               texname = '\\text{mP}')

mu1 = Parameter(name = 'mu1',
                nature = 'internal',
                type = 'real',
                value = '(-mh1**2 - mh2**2 + (-mh1**2 + mh2**2)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))))/4.',
                texname = '\\text{mu1}')

mu3 = Parameter(name = 'mu3',
                nature = 'internal',
                type = 'real',
                value = '-((-mh1**2 + mh2**2)*cmath.sin(2*(cmath.pi/2. - cmath.asin(sinbma))))/4.',
                texname = '\\text{mu3}')

TH1x1 = Parameter(name = 'TH1x1',
                  nature = 'internal',
                  type = 'real',
                  value = 'sinbma',
                  texname = '\\text{TH1x1}')

TH1x2 = Parameter(name = 'TH1x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(1 - sinbma**2)',
                  texname = '\\text{TH1x2}')

TH2x1 = Parameter(name = 'TH2x1',
                  nature = 'internal',
                  type = 'real',
                  value = '-cmath.sqrt(1 - sinbma**2)',
                  texname = '\\text{TH2x1}')

TH2x2 = Parameter(name = 'TH2x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'sinbma',
                  texname = '\\text{TH2x2}')

TH3x3 = Parameter(name = 'TH3x3',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(1 - sinp**2)',
                  texname = '\\text{TH3x3}')

TH3x4 = Parameter(name = 'TH3x4',
                  nature = 'internal',
                  type = 'real',
                  value = 'sinp',
                  texname = '\\text{TH3x4}')

TH4x3 = Parameter(name = 'TH4x3',
                  nature = 'internal',
                  type = 'real',
                  value = '-sinp',
                  texname = '\\text{TH4x3}')

TH4x4 = Parameter(name = 'TH4x4',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sqrt(1 - sinp**2)',
                  texname = '\\text{TH4x4}')

tmc = Parameter(name = 'tmc',
                nature = 'internal',
                type = 'real',
                value = '-(1/tanbeta) + tanbeta',
                texname = '\\text{tmc}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

lP = Parameter(name = 'lP',
               nature = 'internal',
               type = 'real',
               value = '((-laP1 + laP2)*tanbeta)/(1 + tanbeta**2)',
               texname = '\\text{lP}')

lP1 = Parameter(name = 'lP1',
                nature = 'internal',
                type = 'real',
                value = '(laP1 + laP2*tanbeta**2)/(1 + tanbeta**2)',
                texname = '\\text{lP1}')

lP2 = Parameter(name = 'lP2',
                nature = 'internal',
                type = 'real',
                value = '(laP2 + laP1*tanbeta**2)/(1 + tanbeta**2)',
                texname = '\\text{lP2}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = '\\text{MW}')

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

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'real',
                value = '(-mh1**2 - mh2**2 + 8*mhc**2 - 4*lam3*vev**2 - (-mh1**2 + mh2**2)*(3*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))) + (-(1/tanbeta) + tanbeta)*cmath.sin(2*(cmath.pi/2. - cmath.asin(sinbma)))))/4.',
                texname = '\\text{mu2}')

l1 = Parameter(name = 'l1',
               nature = 'internal',
               type = 'real',
               value = '(mh1**2 + mh2**2 - (-mh1**2 + mh2**2)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))))/(4.*vev**2)',
               texname = '\\text{l1}')

l2 = Parameter(name = 'l2',
               nature = 'internal',
               type = 'real',
               value = '(-4*mhc**2*(-(1/tanbeta) + tanbeta)**2 + (mh1**2 + mh2**2)*(1 + (-(1/tanbeta) + tanbeta)**2) + 2*lam3*(-(1/tanbeta) + tanbeta)**2*vev**2 + (-mh1**2 + mh2**2)*((-7 + 3/tanbeta**2 + 3*tanbeta**2)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))) - (tanbeta**(-3) - 5/tanbeta + 5*tanbeta - tanbeta**3)*cmath.sin(2*(cmath.pi/2. - cmath.asin(sinbma)))))/(4.*vev**2)',
               texname = '\\text{l2}')

l3 = Parameter(name = 'l3',
               nature = 'internal',
               type = 'real',
               value = '(mh1**2 + mh2**2 - 4*mhc**2 + 4*lam3*vev**2 + (-mh1**2 + mh2**2)*(3*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))) + (-(1/tanbeta) + tanbeta)*cmath.sin(2*(cmath.pi/2. - cmath.asin(sinbma)))))/(2.*vev**2)',
               texname = '\\text{l3}')

l4 = Parameter(name = 'l4',
               nature = 'internal',
               type = 'real',
               value = '(2*mA**2 + mh1**2 + mh2**2 - 4*mhc**2 + (-mh1**2 + mh2**2)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))))/(2.*vev**2)',
               texname = '\\text{l4}')

l5 = Parameter(name = 'l5',
               nature = 'internal',
               type = 'real',
               value = '(-2*mA**2 + mh1**2 + mh2**2 + (-mh1**2 + mh2**2)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))))/(4.*vev**2)',
               texname = '\\text{l5}')

l6 = Parameter(name = 'l6',
               nature = 'internal',
               type = 'real',
               value = '((-mh1**2 + mh2**2)*sinbma*cmath.sqrt(1 - sinbma**2))/vev**2',
               texname = '\\text{l6}')

l7 = Parameter(name = 'l7',
               nature = 'internal',
               type = 'real',
               value = '((-mh1**2 - mh2**2 + 4*mhc**2)*(-(1/tanbeta) + tanbeta) - 2*lam3*(-(1/tanbeta) + tanbeta)*vev**2 - (-mh1**2 + mh2**2)*(3*(-(1/tanbeta) + tanbeta)*cmath.cos(2*(cmath.pi/2. - cmath.asin(sinbma))) + (-1 + (-(1/tanbeta) + tanbeta)**2)*cmath.sin(2*(cmath.pi/2. - cmath.asin(sinbma)))))/(2.*vev**2)',
               texname = '\\text{l7}')

muP = Parameter(name = 'muP',
                nature = 'internal',
                type = 'real',
                value = '((mh3**2 - mh4**2)*cmath.sin(2*cmath.asin(sinp)))/(2.*vev)',
                texname = '\\mu _P')

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

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*ymdo*cmath.sqrt(2))/vev',
                  texname = '\\text{I1a11}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*yms*cmath.sqrt(2))/vev',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*ymb*cmath.sqrt(2))/vev',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymup*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I2a11}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymc*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymt*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymup*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I3a11}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymc*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I3a22}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((ymt*cmath.sqrt(2))/(tanbeta*vev))',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*ymdo*cmath.sqrt(2))/vev',
                  texname = '\\text{I4a11}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*yms*cmath.sqrt(2))/vev',
                  texname = '\\text{I4a22}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = '(tanbeta*ymb*cmath.sqrt(2))/vev',
                  texname = '\\text{I4a33}')

I5a11 = Parameter(name = 'I5a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo',
                  texname = '\\text{I5a11}')

I5a22 = Parameter(name = 'I5a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys',
                  texname = '\\text{I5a22}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I5a33}')

I6a11 = Parameter(name = 'I6a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup',
                  texname = '\\text{I6a11}')

I6a22 = Parameter(name = 'I6a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc',
                  texname = '\\text{I6a22}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I6a33}')

I7a11 = Parameter(name = 'I7a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup',
                  texname = '\\text{I7a11}')

I7a22 = Parameter(name = 'I7a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc',
                  texname = '\\text{I7a22}')

I7a33 = Parameter(name = 'I7a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I7a33}')

I8a11 = Parameter(name = 'I8a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo',
                  texname = '\\text{I8a11}')

I8a22 = Parameter(name = 'I8a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys',
                  texname = '\\text{I8a22}')

I8a33 = Parameter(name = 'I8a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I8a33}')

