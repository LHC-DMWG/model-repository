# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Mon 11 Sep 2017 14:35:03


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-2*complex(0,1)*l1*TH1x1*TH1x2 - complex(0,1)*l6*TH1x2*TH2x1 - complex(0,1)*l6*TH1x1*TH2x2 - complex(0,1)*l3*TH2x1*TH2x2 - complex(0,1)*l4*TH2x1*TH2x2 + 2*complex(0,1)*l5*TH2x1*TH2x2',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(complex(0,1)*l6*TH1x1*TH1x2) - (complex(0,1)*l4*TH1x2*TH2x1)/2. - complex(0,1)*l5*TH1x2*TH2x1 - (complex(0,1)*l4*TH1x1*TH2x2)/2. - complex(0,1)*l5*TH1x1*TH2x2 - complex(0,1)*l7*TH2x1*TH2x2',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ee**2*complex(0,1)*TH1x1*TH1x2)/(2.*sw**2) + (ee**2*complex(0,1)*TH2x1*TH2x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = 'ee**2*complex(0,1)*TH1x1*TH1x2 + (cw**2*ee**2*complex(0,1)*TH1x1*TH1x2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH1x1*TH1x2)/(2.*cw**2) + ee**2*complex(0,1)*TH2x1*TH2x2 + (cw**2*ee**2*complex(0,1)*TH2x1*TH2x2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH2x1*TH2x2)/(2.*cw**2)',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-6*complex(0,1)*l1*TH1x1**3*TH1x2 - 9*complex(0,1)*l6*TH1x1**2*TH1x2*TH2x1 - 3*complex(0,1)*l3*TH1x1*TH1x2*TH2x1**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH2x1**2 - 6*complex(0,1)*l5*TH1x1*TH1x2*TH2x1**2 - 3*complex(0,1)*l7*TH1x2*TH2x1**3 - 3*complex(0,1)*l6*TH1x1**3*TH2x2 - 3*complex(0,1)*l3*TH1x1**2*TH2x1*TH2x2 - 3*complex(0,1)*l4*TH1x1**2*TH2x1*TH2x2 - 6*complex(0,1)*l5*TH1x1**2*TH2x1*TH2x2 - 9*complex(0,1)*l7*TH1x1*TH2x1**2*TH2x2 - 6*complex(0,1)*l2*TH2x1**3*TH2x2',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(complex(0,1)*l3*TH1x2**2) - 2*complex(0,1)*l7*TH1x2*TH2x2 - 2*complex(0,1)*l2*TH2x2**2',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-2*complex(0,1)*l1*TH1x2**2 - 2*complex(0,1)*l6*TH1x2*TH2x2 - complex(0,1)*l3*TH2x2**2',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '-2*complex(0,1)*l1*TH1x2**2 - 2*complex(0,1)*l6*TH1x2*TH2x2 - complex(0,1)*l3*TH2x2**2 - complex(0,1)*l4*TH2x2**2 + 2*complex(0,1)*l5*TH2x2**2',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(complex(0,1)*l6*TH1x2**2) - complex(0,1)*l4*TH1x2*TH2x2 - 2*complex(0,1)*l5*TH1x2*TH2x2 - complex(0,1)*l7*TH2x2**2',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ee**2*complex(0,1)*TH1x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*TH2x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_110 = Coupling(name = 'GC_110',
                  value = 'ee**2*complex(0,1)*TH1x2**2 + (cw**2*ee**2*complex(0,1)*TH1x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH1x2**2)/(2.*cw**2) + ee**2*complex(0,1)*TH2x2**2 + (cw**2*ee**2*complex(0,1)*TH2x2**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH2x2**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x2**2 - 6*complex(0,1)*l6*TH1x1*TH1x2**2*TH2x1 - complex(0,1)*l3*TH1x2**2*TH2x1**2 - complex(0,1)*l4*TH1x2**2*TH2x1**2 - 2*complex(0,1)*l5*TH1x2**2*TH2x1**2 - 6*complex(0,1)*l6*TH1x1**2*TH1x2*TH2x2 - 4*complex(0,1)*l3*TH1x1*TH1x2*TH2x1*TH2x2 - 4*complex(0,1)*l4*TH1x1*TH1x2*TH2x1*TH2x2 - 8*complex(0,1)*l5*TH1x1*TH1x2*TH2x1*TH2x2 - 6*complex(0,1)*l7*TH1x2*TH2x1**2*TH2x2 - complex(0,1)*l3*TH1x1**2*TH2x2**2 - complex(0,1)*l4*TH1x1**2*TH2x2**2 - 2*complex(0,1)*l5*TH1x1**2*TH2x2**2 - 6*complex(0,1)*l7*TH1x1*TH2x1*TH2x2**2 - 6*complex(0,1)*l2*TH2x1**2*TH2x2**2',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2**3 - 3*complex(0,1)*l6*TH1x2**3*TH2x1 - 9*complex(0,1)*l6*TH1x1*TH1x2**2*TH2x2 - 3*complex(0,1)*l3*TH1x2**2*TH2x1*TH2x2 - 3*complex(0,1)*l4*TH1x2**2*TH2x1*TH2x2 - 6*complex(0,1)*l5*TH1x2**2*TH2x1*TH2x2 - 3*complex(0,1)*l3*TH1x1*TH1x2*TH2x2**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH2x2**2 - 6*complex(0,1)*l5*TH1x1*TH1x2*TH2x2**2 - 9*complex(0,1)*l7*TH1x2*TH2x1*TH2x2**2 - 3*complex(0,1)*l7*TH1x1*TH2x2**3 - 6*complex(0,1)*l2*TH2x1*TH2x2**3',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-6*complex(0,1)*l1*TH1x2**4 - 12*complex(0,1)*l6*TH1x2**3*TH2x2 - 6*complex(0,1)*l3*TH1x2**2*TH2x2**2 - 6*complex(0,1)*l4*TH1x2**2*TH2x2**2 - 12*complex(0,1)*l5*TH1x2**2*TH2x2**2 - 12*complex(0,1)*l7*TH1x2*TH2x2**3 - 6*complex(0,1)*l2*TH2x2**4',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(ee**2*TH3x3)/(2.*cw)',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee**2*TH3x3)/(2.*cw)',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(complex(0,1)*l6*TH3x3)',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '-3*complex(0,1)*l6*TH3x3',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(complex(0,1)*l7*TH3x3)',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(ee*TH3x3)/(2.*sw)',
                  order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(complex(0,1)*I1a11)',
                 order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(ee**2*TH3x3)/(2.*sw)',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee**2*TH3x3)/(2.*sw)',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ee**2*complex(0,1)*TH3x3**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-(complex(0,1)*l4*TH3x3)/2. - complex(0,1)*l5*TH3x3',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(l4*TH1x1*TH3x3)/2. - l5*TH1x1*TH3x3',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(l4*TH1x1*TH3x3)/2. + l5*TH1x1*TH3x3',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(l4*TH1x2*TH3x3)/2. - l5*TH1x2*TH3x3',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(l4*TH1x2*TH3x3)/2. + l5*TH1x2*TH3x3',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cw*ee*TH2x1*TH3x3)/(2.*sw) + (ee*sw*TH2x1*TH3x3)/(2.*cw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(complex(0,1)*l6*TH1x1**2*TH3x3) - 4*complex(0,1)*l5*TH1x1*TH2x1*TH3x3 - complex(0,1)*l7*TH2x1**2*TH3x3',
                  order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*I1a22)',
                 order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cw*ee*TH2x2*TH3x3)/(2.*sw) + (ee*sw*TH2x2*TH3x3)/(2.*cw)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(complex(0,1)*l6*TH1x1*TH1x2*TH3x3) - 2*complex(0,1)*l5*TH1x2*TH2x1*TH3x3 - 2*complex(0,1)*l5*TH1x1*TH2x2*TH3x3 - complex(0,1)*l7*TH2x1*TH2x2*TH3x3',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(complex(0,1)*l6*TH1x2**2*TH3x3) - 4*complex(0,1)*l5*TH1x2*TH2x2*TH3x3 - complex(0,1)*l7*TH2x2**2*TH3x3',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = 'ee**2*complex(0,1)*TH3x3**2 + (cw**2*ee**2*complex(0,1)*TH3x3**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH3x3**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(ee**2*TH3x4)/(2.*cw)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*TH3x4)/(2.*cw)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-(complex(0,1)*l6*TH3x4)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '-3*complex(0,1)*l6*TH3x4',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(complex(0,1)*l7*TH3x4)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee*TH3x4)/(2.*sw)',
                  order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*I1a33)',
                 order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(ee**2*TH3x4)/(2.*sw)',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*TH3x4)/(2.*sw)',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee**2*complex(0,1)*TH3x3*TH3x4)/(2.*sw**2)',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee**2*complex(0,1)*TH3x4**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(complex(0,1)*l4*TH3x4)/2. - complex(0,1)*l5*TH3x4',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(l4*TH1x1*TH3x4)/2. - l5*TH1x1*TH3x4',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(l4*TH1x1*TH3x4)/2. + l5*TH1x1*TH3x4',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '(l4*TH1x2*TH3x4)/2. - l5*TH1x2*TH3x4',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-(l4*TH1x2*TH3x4)/2. + l5*TH1x2*TH3x4',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '(cw*ee*TH2x1*TH3x4)/(2.*sw) + (ee*sw*TH2x1*TH3x4)/(2.*cw)',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*I2a11',
                 order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(complex(0,1)*l6*TH1x1**2*TH3x4) - 4*complex(0,1)*l5*TH1x1*TH2x1*TH3x4 - complex(0,1)*l7*TH2x1**2*TH3x4',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(cw*ee*TH2x2*TH3x4)/(2.*sw) + (ee*sw*TH2x2*TH3x4)/(2.*cw)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(complex(0,1)*l6*TH1x1*TH1x2*TH3x4) - 2*complex(0,1)*l5*TH1x2*TH2x1*TH3x4 - 2*complex(0,1)*l5*TH1x1*TH2x2*TH3x4 - complex(0,1)*l7*TH2x1*TH2x2*TH3x4',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(complex(0,1)*l6*TH1x2**2*TH3x4) - 4*complex(0,1)*l5*TH1x2*TH2x2*TH3x4 - complex(0,1)*l7*TH2x2**2*TH3x4',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = 'ee**2*complex(0,1)*TH3x3*TH3x4 + (cw**2*ee**2*complex(0,1)*TH3x3*TH3x4)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH3x3*TH3x4)/(2.*cw**2)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = 'ee**2*complex(0,1)*TH3x4**2 + (cw**2*ee**2*complex(0,1)*TH3x4**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH3x4**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(gPXd*TH4x3)',
                  order = {'DS':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-(muP*TH4x3)',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = 'muP*TH4x3',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(complex(0,1)*muP*TH2x1*TH4x3)',
                  order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*I2a22',
                 order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(complex(0,1)*muP*TH2x2*TH4x3)',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '2*complex(0,1)*muP*TH1x1*TH3x3*TH4x3',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '2*complex(0,1)*muP*TH1x2*TH3x3*TH4x3',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(complex(0,1)*l7*TH3x3**2) - 2*complex(0,1)*lP*TH4x3**2',
                  order = {'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '-(complex(0,1)*l3*TH3x3**2) - 2*complex(0,1)*lP1*TH4x3**2',
                  order = {'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(complex(0,1)*l3*TH3x3**2) - complex(0,1)*l4*TH3x3**2 - 2*complex(0,1)*l5*TH3x3**2 - 2*complex(0,1)*lP1*TH4x3**2',
                  order = {'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '-2*complex(0,1)*l2*TH3x3**2 - 2*complex(0,1)*lP2*TH4x3**2',
                  order = {'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-(complex(0,1)*l3*TH1x1**2*TH3x3**2) - complex(0,1)*l4*TH1x1**2*TH3x3**2 + 2*complex(0,1)*l5*TH1x1**2*TH3x3**2 - 2*complex(0,1)*l7*TH1x1*TH2x1*TH3x3**2 - 2*complex(0,1)*l2*TH2x1**2*TH3x3**2 - 2*complex(0,1)*lP1*TH1x1**2*TH4x3**2 - 4*complex(0,1)*lP*TH1x1*TH2x1*TH4x3**2 - 2*complex(0,1)*lP2*TH2x1**2*TH4x3**2',
                  order = {'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '-(complex(0,1)*l3*TH1x1*TH1x2*TH3x3**2) - complex(0,1)*l4*TH1x1*TH1x2*TH3x3**2 + 2*complex(0,1)*l5*TH1x1*TH1x2*TH3x3**2 - complex(0,1)*l7*TH1x2*TH2x1*TH3x3**2 - complex(0,1)*l7*TH1x1*TH2x2*TH3x3**2 - 2*complex(0,1)*l2*TH2x1*TH2x2*TH3x3**2 - 2*complex(0,1)*lP1*TH1x1*TH1x2*TH4x3**2 - 2*complex(0,1)*lP*TH1x2*TH2x1*TH4x3**2 - 2*complex(0,1)*lP*TH1x1*TH2x2*TH4x3**2 - 2*complex(0,1)*lP2*TH2x1*TH2x2*TH4x3**2',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '-(complex(0,1)*l3*TH1x2**2*TH3x3**2) - complex(0,1)*l4*TH1x2**2*TH3x3**2 + 2*complex(0,1)*l5*TH1x2**2*TH3x3**2 - 2*complex(0,1)*l7*TH1x2*TH2x2*TH3x3**2 - 2*complex(0,1)*l2*TH2x2**2*TH3x3**2 - 2*complex(0,1)*lP1*TH1x2**2*TH4x3**2 - 4*complex(0,1)*lP*TH1x2*TH2x2*TH4x3**2 - 2*complex(0,1)*lP2*TH2x2**2*TH4x3**2',
                  order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*I2a33',
                 order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-3*complex(0,1)*l7*TH3x3**3 - 6*complex(0,1)*lP*TH3x3*TH4x3**2',
                  order = {'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '-6*complex(0,1)*l2*TH3x3**4 - 12*complex(0,1)*lP2*TH3x3**2*TH4x3**2',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '-(gPXd*TH4x4)',
                  order = {'DS':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(muP*TH4x4)',
                  order = {'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = 'muP*TH4x4',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '-(complex(0,1)*muP*TH2x1*TH4x4)',
                  order = {'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-(complex(0,1)*muP*TH2x2*TH4x4)',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '2*complex(0,1)*muP*TH1x1*TH3x4*TH4x4',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '2*complex(0,1)*muP*TH1x2*TH3x4*TH4x4',
                  order = {'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = 'complex(0,1)*muP*TH1x1*TH3x4*TH4x3 + complex(0,1)*muP*TH1x1*TH3x3*TH4x4',
                  order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*I3a11',
                 order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = 'complex(0,1)*muP*TH1x2*TH3x4*TH4x3 + complex(0,1)*muP*TH1x2*TH3x3*TH4x4',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '-(complex(0,1)*l7*TH3x3*TH3x4) - 2*complex(0,1)*lP*TH4x3*TH4x4',
                  order = {'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '-(complex(0,1)*l3*TH3x3*TH3x4) - 2*complex(0,1)*lP1*TH4x3*TH4x4',
                  order = {'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(complex(0,1)*l3*TH3x3*TH3x4) - complex(0,1)*l4*TH3x3*TH3x4 - 2*complex(0,1)*l5*TH3x3*TH3x4 - 2*complex(0,1)*lP1*TH4x3*TH4x4',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '-2*complex(0,1)*l2*TH3x3*TH3x4 - 2*complex(0,1)*lP2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-(complex(0,1)*l3*TH1x1**2*TH3x3*TH3x4) - complex(0,1)*l4*TH1x1**2*TH3x3*TH3x4 + 2*complex(0,1)*l5*TH1x1**2*TH3x3*TH3x4 - 2*complex(0,1)*l7*TH1x1*TH2x1*TH3x3*TH3x4 - 2*complex(0,1)*l2*TH2x1**2*TH3x3*TH3x4 - 2*complex(0,1)*lP1*TH1x1**2*TH4x3*TH4x4 - 4*complex(0,1)*lP*TH1x1*TH2x1*TH4x3*TH4x4 - 2*complex(0,1)*lP2*TH2x1**2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '-(complex(0,1)*l3*TH1x1*TH1x2*TH3x3*TH3x4) - complex(0,1)*l4*TH1x1*TH1x2*TH3x3*TH3x4 + 2*complex(0,1)*l5*TH1x1*TH1x2*TH3x3*TH3x4 - complex(0,1)*l7*TH1x2*TH2x1*TH3x3*TH3x4 - complex(0,1)*l7*TH1x1*TH2x2*TH3x3*TH3x4 - 2*complex(0,1)*l2*TH2x1*TH2x2*TH3x3*TH3x4 - 2*complex(0,1)*lP1*TH1x1*TH1x2*TH4x3*TH4x4 - 2*complex(0,1)*lP*TH1x2*TH2x1*TH4x3*TH4x4 - 2*complex(0,1)*lP*TH1x1*TH2x2*TH4x3*TH4x4 - 2*complex(0,1)*lP2*TH2x1*TH2x2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '-(complex(0,1)*l3*TH1x2**2*TH3x3*TH3x4) - complex(0,1)*l4*TH1x2**2*TH3x3*TH3x4 + 2*complex(0,1)*l5*TH1x2**2*TH3x3*TH3x4 - 2*complex(0,1)*l7*TH1x2*TH2x2*TH3x3*TH3x4 - 2*complex(0,1)*l2*TH2x2**2*TH3x3*TH3x4 - 2*complex(0,1)*lP1*TH1x2**2*TH4x3*TH4x4 - 4*complex(0,1)*lP*TH1x2*TH2x2*TH4x3*TH4x4 - 2*complex(0,1)*lP2*TH2x2**2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-3*complex(0,1)*l7*TH3x3**2*TH3x4 - 2*complex(0,1)*lP*TH3x4*TH4x3**2 - 4*complex(0,1)*lP*TH3x3*TH4x3*TH4x4',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '-6*complex(0,1)*l2*TH3x3**3*TH3x4 - 6*complex(0,1)*lP2*TH3x3*TH3x4*TH4x3**2 - 6*complex(0,1)*lP2*TH3x3**2*TH4x3*TH4x4',
                  order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*I3a22',
                 order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(complex(0,1)*l7*TH3x4**2) - 2*complex(0,1)*lP*TH4x4**2',
                  order = {'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '-(complex(0,1)*l3*TH3x4**2) - 2*complex(0,1)*lP1*TH4x4**2',
                  order = {'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '-(complex(0,1)*l3*TH3x4**2) - complex(0,1)*l4*TH3x4**2 - 2*complex(0,1)*l5*TH3x4**2 - 2*complex(0,1)*lP1*TH4x4**2',
                  order = {'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '-2*complex(0,1)*l2*TH3x4**2 - 2*complex(0,1)*lP2*TH4x4**2',
                  order = {'QED':2})

GC_194 = Coupling(name = 'GC_194',
                  value = '-(complex(0,1)*l3*TH1x1**2*TH3x4**2) - complex(0,1)*l4*TH1x1**2*TH3x4**2 + 2*complex(0,1)*l5*TH1x1**2*TH3x4**2 - 2*complex(0,1)*l7*TH1x1*TH2x1*TH3x4**2 - 2*complex(0,1)*l2*TH2x1**2*TH3x4**2 - 2*complex(0,1)*lP1*TH1x1**2*TH4x4**2 - 4*complex(0,1)*lP*TH1x1*TH2x1*TH4x4**2 - 2*complex(0,1)*lP2*TH2x1**2*TH4x4**2',
                  order = {'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(complex(0,1)*l3*TH1x1*TH1x2*TH3x4**2) - complex(0,1)*l4*TH1x1*TH1x2*TH3x4**2 + 2*complex(0,1)*l5*TH1x1*TH1x2*TH3x4**2 - complex(0,1)*l7*TH1x2*TH2x1*TH3x4**2 - complex(0,1)*l7*TH1x1*TH2x2*TH3x4**2 - 2*complex(0,1)*l2*TH2x1*TH2x2*TH3x4**2 - 2*complex(0,1)*lP1*TH1x1*TH1x2*TH4x4**2 - 2*complex(0,1)*lP*TH1x2*TH2x1*TH4x4**2 - 2*complex(0,1)*lP*TH1x1*TH2x2*TH4x4**2 - 2*complex(0,1)*lP2*TH2x1*TH2x2*TH4x4**2',
                  order = {'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '-(complex(0,1)*l3*TH1x2**2*TH3x4**2) - complex(0,1)*l4*TH1x2**2*TH3x4**2 + 2*complex(0,1)*l5*TH1x2**2*TH3x4**2 - 2*complex(0,1)*l7*TH1x2*TH2x2*TH3x4**2 - 2*complex(0,1)*l2*TH2x2**2*TH3x4**2 - 2*complex(0,1)*lP1*TH1x2**2*TH4x4**2 - 4*complex(0,1)*lP*TH1x2*TH2x2*TH4x4**2 - 2*complex(0,1)*lP2*TH2x2**2*TH4x4**2',
                  order = {'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '-3*complex(0,1)*l7*TH3x3*TH3x4**2 - 4*complex(0,1)*lP*TH3x4*TH4x3*TH4x4 - 2*complex(0,1)*lP*TH3x3*TH4x4**2',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '-6*complex(0,1)*l2*TH3x3**2*TH3x4**2 - 2*complex(0,1)*lP2*TH3x4**2*TH4x3**2 - 8*complex(0,1)*lP2*TH3x3*TH3x4*TH4x3*TH4x4 - 2*complex(0,1)*lP2*TH3x3**2*TH4x4**2',
                  order = {'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '-3*complex(0,1)*l7*TH3x4**3 - 6*complex(0,1)*lP*TH3x4*TH4x4**2',
                  order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*I3a33',
                 order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-6*complex(0,1)*l2*TH3x3*TH3x4**3 - 6*complex(0,1)*lP2*TH3x4**2*TH4x3*TH4x4 - 6*complex(0,1)*lP2*TH3x3*TH3x4*TH4x4**2',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '-6*complex(0,1)*l2*TH3x4**4 - 12*complex(0,1)*lP2*TH3x4**2*TH4x4**2',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(ee**2*complex(0,1)*vev)/(2.*cw)',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw)',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-(ee**2*complex(0,1)*TH1x1*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ee**2*complex(0,1)*TH1x1*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(complex(0,1)*I4a11)',
                 order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-(ee**2*complex(0,1)*TH1x2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee**2*complex(0,1)*TH1x2*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-(ee**2*complex(0,1)*TH1x1*vev)/2. - (cw**2*ee**2*complex(0,1)*TH1x1*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*TH1x1*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = 'ee**2*complex(0,1)*TH1x1*vev + (cw**2*ee**2*complex(0,1)*TH1x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH1x1*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-(ee**2*complex(0,1)*TH1x2*vev)/2. - (cw**2*ee**2*complex(0,1)*TH1x2*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*TH1x2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = 'ee**2*complex(0,1)*TH1x2*vev + (cw**2*ee**2*complex(0,1)*TH1x2*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH1x2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(complex(0,1)*I4a22)',
                 order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '-(complex(0,1)*l6*TH1x1*vev) - (complex(0,1)*l4*TH2x1*vev)/2. - complex(0,1)*l5*TH2x1*vev',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-2*complex(0,1)*l1*TH1x1*vev - complex(0,1)*l6*TH2x1*vev',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-(complex(0,1)*l3*TH1x1*vev) - complex(0,1)*l7*TH2x1*vev',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-6*complex(0,1)*l1*TH1x1**3*vev - 9*complex(0,1)*l6*TH1x1**2*TH2x1*vev - 3*complex(0,1)*l3*TH1x1*TH2x1**2*vev - 3*complex(0,1)*l4*TH1x1*TH2x1**2*vev - 6*complex(0,1)*l5*TH1x1*TH2x1**2*vev - 3*complex(0,1)*l7*TH2x1**3*vev',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '-(complex(0,1)*l6*TH1x2*vev) - (complex(0,1)*l4*TH2x2*vev)/2. - complex(0,1)*l5*TH2x2*vev',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-2*complex(0,1)*l1*TH1x2*vev - complex(0,1)*l6*TH2x2*vev',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-(complex(0,1)*l3*TH1x2*vev) - complex(0,1)*l7*TH2x2*vev',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x2*vev - 6*complex(0,1)*l6*TH1x1*TH1x2*TH2x1*vev - complex(0,1)*l3*TH1x2*TH2x1**2*vev - complex(0,1)*l4*TH1x2*TH2x1**2*vev - 2*complex(0,1)*l5*TH1x2*TH2x1**2*vev - 3*complex(0,1)*l6*TH1x1**2*TH2x2*vev - 2*complex(0,1)*l3*TH1x1*TH2x1*TH2x2*vev - 2*complex(0,1)*l4*TH1x1*TH2x1*TH2x2*vev - 4*complex(0,1)*l5*TH1x1*TH2x1*TH2x2*vev - 3*complex(0,1)*l7*TH2x1**2*TH2x2*vev',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2**2*vev - 3*complex(0,1)*l6*TH1x2**2*TH2x1*vev - 6*complex(0,1)*l6*TH1x1*TH1x2*TH2x2*vev - 2*complex(0,1)*l3*TH1x2*TH2x1*TH2x2*vev - 2*complex(0,1)*l4*TH1x2*TH2x1*TH2x2*vev - 4*complex(0,1)*l5*TH1x2*TH2x1*TH2x2*vev - complex(0,1)*l3*TH1x1*TH2x2**2*vev - complex(0,1)*l4*TH1x1*TH2x2**2*vev - 2*complex(0,1)*l5*TH1x1*TH2x2**2*vev - 3*complex(0,1)*l7*TH2x1*TH2x2**2*vev',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-6*complex(0,1)*l1*TH1x2**3*vev - 9*complex(0,1)*l6*TH1x2**2*TH2x2*vev - 3*complex(0,1)*l3*TH1x2*TH2x2**2*vev - 3*complex(0,1)*l4*TH1x2*TH2x2**2*vev - 6*complex(0,1)*l5*TH1x2*TH2x2**2*vev - 3*complex(0,1)*l7*TH2x2**3*vev',
                  order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(complex(0,1)*I4a33)',
                 order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(l4*TH3x3*vev)/2. - l5*TH3x3*vev',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-(l4*TH3x3*vev)/2. + l5*TH3x3*vev',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '-(complex(0,1)*l6*TH1x1*TH3x3*vev) - 2*complex(0,1)*l5*TH2x1*TH3x3*vev',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-(complex(0,1)*l6*TH1x2*TH3x3*vev) - 2*complex(0,1)*l5*TH2x2*TH3x3*vev',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(l4*TH3x4*vev)/2. - l5*TH3x4*vev',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '-(l4*TH3x4*vev)/2. + l5*TH3x4*vev',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-(complex(0,1)*l6*TH1x1*TH3x4*vev) - 2*complex(0,1)*l5*TH2x1*TH3x4*vev',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-(complex(0,1)*l6*TH1x2*TH3x4*vev) - 2*complex(0,1)*l5*TH2x2*TH3x4*vev',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-(complex(0,1)*l3*TH1x1*TH3x3**2*vev) - complex(0,1)*l4*TH1x1*TH3x3**2*vev + 2*complex(0,1)*l5*TH1x1*TH3x3**2*vev - complex(0,1)*l7*TH2x1*TH3x3**2*vev - 2*complex(0,1)*lP1*TH1x1*TH4x3**2*vev - 2*complex(0,1)*lP*TH2x1*TH4x3**2*vev',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-(complex(0,1)*l3*TH1x2*TH3x3**2*vev) - complex(0,1)*l4*TH1x2*TH3x3**2*vev + 2*complex(0,1)*l5*TH1x2*TH3x3**2*vev - complex(0,1)*l7*TH2x2*TH3x3**2*vev - 2*complex(0,1)*lP1*TH1x2*TH4x3**2*vev - 2*complex(0,1)*lP*TH2x2*TH4x3**2*vev',
                  order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(complex(0,1)*I5a11)',
                 order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-(complex(0,1)*l3*TH1x1*TH3x3*TH3x4*vev) - complex(0,1)*l4*TH1x1*TH3x3*TH3x4*vev + 2*complex(0,1)*l5*TH1x1*TH3x3*TH3x4*vev - complex(0,1)*l7*TH2x1*TH3x3*TH3x4*vev - 2*complex(0,1)*lP1*TH1x1*TH4x3*TH4x4*vev - 2*complex(0,1)*lP*TH2x1*TH4x3*TH4x4*vev',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-(complex(0,1)*l3*TH1x2*TH3x3*TH3x4*vev) - complex(0,1)*l4*TH1x2*TH3x3*TH3x4*vev + 2*complex(0,1)*l5*TH1x2*TH3x3*TH3x4*vev - complex(0,1)*l7*TH2x2*TH3x3*TH3x4*vev - 2*complex(0,1)*lP1*TH1x2*TH4x3*TH4x4*vev - 2*complex(0,1)*lP*TH2x2*TH4x3*TH4x4*vev',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-(complex(0,1)*l3*TH1x1*TH3x4**2*vev) - complex(0,1)*l4*TH1x1*TH3x4**2*vev + 2*complex(0,1)*l5*TH1x1*TH3x4**2*vev - complex(0,1)*l7*TH2x1*TH3x4**2*vev - 2*complex(0,1)*lP1*TH1x1*TH4x4**2*vev - 2*complex(0,1)*lP*TH2x1*TH4x4**2*vev',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '-(complex(0,1)*l3*TH1x2*TH3x4**2*vev) - complex(0,1)*l4*TH1x2*TH3x4**2*vev + 2*complex(0,1)*l5*TH1x2*TH3x4**2*vev - complex(0,1)*l7*TH2x2*TH3x4**2*vev - 2*complex(0,1)*lP1*TH1x2*TH4x4**2*vev - 2*complex(0,1)*lP*TH2x2*TH4x4**2*vev',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = 'yb/cmath.sqrt(2)',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '-(yc/cmath.sqrt(2))',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = 'yc/cmath.sqrt(2)',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-(ydo/cmath.sqrt(2))',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = 'ydo/cmath.sqrt(2)',
                  order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(complex(0,1)*I5a22)',
                 order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(complex(0,1)*ye)',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '-(ye/cmath.sqrt(2))',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = 'ye/cmath.sqrt(2)',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-(complex(0,1)*ym)',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = 'ym/cmath.sqrt(2)',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-((tanbeta*TH3x3*ymb)/vev)',
                  order = {'QED':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '-((tanbeta*TH3x4*ymb)/vev)',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '-((complex(0,1)*tanbeta*TH2x1*ymb)/vev) - (complex(0,1)*TH1x1*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-((complex(0,1)*tanbeta*TH2x2*ymb)/vev) - (complex(0,1)*TH1x2*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(complex(0,1)*I5a33)',
                 order = {'QED':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-((TH3x3*ymc)/(tanbeta*vev))',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(TH3x3*ymc)/(tanbeta*vev)',
                  order = {'QED':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-((TH3x4*ymc)/(tanbeta*vev))',
                  order = {'QED':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(TH3x4*ymc)/(tanbeta*vev)',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(complex(0,1)*TH2x1*ymc)/(tanbeta*vev) - (complex(0,1)*TH1x1*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '(complex(0,1)*TH2x2*ymc)/(tanbeta*vev) - (complex(0,1)*TH1x2*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-((tanbeta*TH3x3*ymdo)/vev)',
                  order = {'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '-((tanbeta*TH3x4*ymdo)/vev)',
                  order = {'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-((complex(0,1)*tanbeta*TH2x1*ymdo)/vev) - (complex(0,1)*TH1x1*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '-((complex(0,1)*tanbeta*TH2x2*ymdo)/vev) - (complex(0,1)*TH1x2*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = 'complex(0,1)*I6a11',
                 order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((complex(0,1)*tanbeta*yme*cmath.sqrt(2))/vev)',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((tanbeta*TH3x3*yme)/vev)',
                  order = {'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((tanbeta*TH3x4*yme)/vev)',
                  order = {'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '-((complex(0,1)*tanbeta*TH2x1*yme)/vev) - (complex(0,1)*TH1x1*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '-((complex(0,1)*tanbeta*TH2x2*yme)/vev) - (complex(0,1)*TH1x2*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-((complex(0,1)*tanbeta*ymm*cmath.sqrt(2))/vev)',
                  order = {'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((tanbeta*TH3x3*ymm)/vev)',
                  order = {'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((tanbeta*TH3x4*ymm)/vev)',
                  order = {'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-((complex(0,1)*tanbeta*TH2x1*ymm)/vev) - (complex(0,1)*TH1x1*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-((complex(0,1)*tanbeta*TH2x2*ymm)/vev) - (complex(0,1)*TH1x2*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'complex(0,1)*I6a22',
                 order = {'QED':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-((tanbeta*TH3x3*yms)/vev)',
                  order = {'QED':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '-((tanbeta*TH3x4*yms)/vev)',
                  order = {'QED':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '-((TH3x3*ymt)/(tanbeta*vev))',
                  order = {'QED':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '(TH3x3*ymt)/(tanbeta*vev)',
                  order = {'QED':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-((TH3x4*ymt)/(tanbeta*vev))',
                  order = {'QED':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '(TH3x4*ymt)/(tanbeta*vev)',
                  order = {'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((complex(0,1)*tanbeta*ymtau*cmath.sqrt(2))/vev)',
                  order = {'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((tanbeta*TH3x3*ymtau)/vev)',
                  order = {'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((tanbeta*TH3x4*ymtau)/vev)',
                  order = {'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((TH3x3*ymup)/(tanbeta*vev))',
                  order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'complex(0,1)*I6a33',
                 order = {'QED':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '(TH3x3*ymup)/(tanbeta*vev)',
                  order = {'QED':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '-((TH3x4*ymup)/(tanbeta*vev))',
                  order = {'QED':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '(TH3x4*ymup)/(tanbeta*vev)',
                  order = {'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = 'ys/cmath.sqrt(2)',
                  order = {'QED':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '-((complex(0,1)*tanbeta*TH2x1*yms)/vev) - (complex(0,1)*TH1x1*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((complex(0,1)*tanbeta*TH2x2*yms)/vev) - (complex(0,1)*TH1x2*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '(complex(0,1)*TH2x1*ymt)/(tanbeta*vev) - (complex(0,1)*TH1x1*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = 'complex(0,1)*I7a11',
                 order = {'QED':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '(complex(0,1)*TH2x2*ymt)/(tanbeta*vev) - (complex(0,1)*TH1x2*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '-(complex(0,1)*ytau)',
                  order = {'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_303 = Coupling(name = 'GC_303',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '-((complex(0,1)*tanbeta*TH2x1*ymtau)/vev) - (complex(0,1)*TH1x1*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '-((complex(0,1)*tanbeta*TH2x2*ymtau)/vev) - (complex(0,1)*TH1x2*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_307 = Coupling(name = 'GC_307',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '(complex(0,1)*TH2x1*ymup)/(tanbeta*vev) - (complex(0,1)*TH1x1*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '(complex(0,1)*TH2x2*ymup)/(tanbeta*vev) - (complex(0,1)*TH1x2*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'complex(0,1)*I7a22',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'complex(0,1)*I7a33',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(complex(0,1)*I8a11)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(complex(0,1)*I8a22)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(complex(0,1)*I8a33)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-2*complex(0,1)*l1',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-4*complex(0,1)*l1',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-6*complex(0,1)*l1',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-4*complex(0,1)*l2',
                 order = {'QED':2})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(complex(0,1)*l3)',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(complex(0,1)*l3) - complex(0,1)*l4',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-4*complex(0,1)*l5',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(complex(0,1)*l6)',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-2*complex(0,1)*l6',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-2*complex(0,1)*l7',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(-2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ee/(2.*sw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(ee**2*complex(0,1)*TH1x1)/(2.*cw)',
                 order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(ee*complex(0,1)*TH1x1)/(2.*sw)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*TH1x1)/(2.*sw)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(ee**2*complex(0,1)*TH1x1)/(2.*sw)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(cw*ee*TH1x1)/(2.*sw) - (ee*sw*TH1x1)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ee**2*complex(0,1)*TH1x2)/(2.*cw)',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-(ee*complex(0,1)*TH1x2)/(2.*sw)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(ee*complex(0,1)*TH1x2)/(2.*sw)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ee**2*complex(0,1)*TH1x2)/(2.*sw)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(cw*ee*TH1x2)/(2.*sw) - (ee*sw*TH1x2)/(2.*cw)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(ee**2*complex(0,1)*TH2x1)/(2.*cw)',
                 order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ee*complex(0,1)*TH2x1)/(2.*sw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee*complex(0,1)*TH2x1)/(2.*sw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*complex(0,1)*TH2x1)/(2.*sw)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(l4*TH2x1)/2. - l5*TH2x1',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(l4*TH2x1)/2. + l5*TH2x1',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(complex(0,1)*l3*TH1x1**2) - 2*complex(0,1)*l7*TH1x1*TH2x1 - 2*complex(0,1)*l2*TH2x1**2',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-2*complex(0,1)*l1*TH1x1**2 - 2*complex(0,1)*l6*TH1x1*TH2x1 - complex(0,1)*l3*TH2x1**2',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-2*complex(0,1)*l1*TH1x1**2 - 2*complex(0,1)*l6*TH1x1*TH2x1 - complex(0,1)*l3*TH2x1**2 - complex(0,1)*l4*TH2x1**2 + 2*complex(0,1)*l5*TH2x1**2',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(complex(0,1)*l6*TH1x1**2) - complex(0,1)*l4*TH1x1*TH2x1 - 2*complex(0,1)*l5*TH1x1*TH2x1 - complex(0,1)*l7*TH2x1**2',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ee**2*complex(0,1)*TH1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*TH2x1**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-G',
                order = {'QCD':1})

GC_90 = Coupling(name = 'GC_90',
                 value = 'ee**2*complex(0,1)*TH1x1**2 + (cw**2*ee**2*complex(0,1)*TH1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH1x1**2)/(2.*cw**2) + ee**2*complex(0,1)*TH2x1**2 + (cw**2*ee**2*complex(0,1)*TH2x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*TH2x1**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '-6*complex(0,1)*l1*TH1x1**4 - 12*complex(0,1)*l6*TH1x1**3*TH2x1 - 6*complex(0,1)*l3*TH1x1**2*TH2x1**2 - 6*complex(0,1)*l4*TH1x1**2*TH2x1**2 - 12*complex(0,1)*l5*TH1x1**2*TH2x1**2 - 12*complex(0,1)*l7*TH1x1*TH2x1**3 - 6*complex(0,1)*l2*TH2x1**4',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(ee**2*complex(0,1)*TH2x2)/(2.*cw)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(ee*complex(0,1)*TH2x2)/(2.*sw)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*TH2x2)/(2.*sw)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee**2*complex(0,1)*TH2x2)/(2.*sw)',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(l4*TH2x2)/2. - l5*TH2x2',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(l4*TH2x2)/2. + l5*TH2x2',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(complex(0,1)*l3*TH1x1*TH1x2) - complex(0,1)*l7*TH1x2*TH2x1 - complex(0,1)*l7*TH1x1*TH2x2 - 2*complex(0,1)*l2*TH2x1*TH2x2',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-2*complex(0,1)*l1*TH1x1*TH1x2 - complex(0,1)*l6*TH1x2*TH2x1 - complex(0,1)*l6*TH1x1*TH2x2 - complex(0,1)*l3*TH2x1*TH2x2',
                 order = {'QED':2})

