# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 6 Jun 2019 21:52:47


from object_library import all_CTparameters, CTParameter

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



invFREps = CTParameter(name = 'invFREps',
                       type = 'complex',
                       value = {-1:'1'},
                       texname = 'invFREps')

FRCTdeltaZxuuLxuG = CTParameter(name = 'FRCTdeltaZxuuLxuG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxuuLxuG')

FRCTdeltaZxuuRxuG = CTParameter(name = 'FRCTdeltaZxuuRxuG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxuuRxuG')

FRCTdeltaZxccLxcG = CTParameter(name = 'FRCTdeltaZxccLxcG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxccLxcG')

FRCTdeltaZxccRxcG = CTParameter(name = 'FRCTdeltaZxccRxcG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxccRxcG')

FRCTdeltaxMTxtG = CTParameter(name = 'FRCTdeltaxMTxtG',
                              type = 'complex',
                              value = {0:'-(G**2*MT)/(3.*cmath.pi**2) + (G**2*MT*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                              texname = 'FRCTdeltaxMTxtG')

FRCTdeltaZxttLxtG = CTParameter(name = 'FRCTdeltaZxttLxtG',
                                type = 'complex',
                                value = {-1:'-G**2/(6.*cmath.pi**2)',0:'-G**2/(3.*cmath.pi**2) + (G**2*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxttLxtG')

FRCTdeltaZxttRxtG = CTParameter(name = 'FRCTdeltaZxttRxtG',
                                type = 'complex',
                                value = {-1:'-G**2/(6.*cmath.pi**2)',0:'-G**2/(3.*cmath.pi**2) + (G**2*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxttRxtG')

FRCTdeltaZxddLxdG = CTParameter(name = 'FRCTdeltaZxddLxdG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxddLxdG')

FRCTdeltaZxddRxdG = CTParameter(name = 'FRCTdeltaZxddRxdG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxddRxdG')

FRCTdeltaZxssLxsG = CTParameter(name = 'FRCTdeltaZxssLxsG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxssLxsG')

FRCTdeltaZxssRxsG = CTParameter(name = 'FRCTdeltaZxssRxsG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxssRxsG')

FRCTdeltaZxbbLxbG = CTParameter(name = 'FRCTdeltaZxbbLxbG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxbbLxbG')

FRCTdeltaZxbbRxbG = CTParameter(name = 'FRCTdeltaZxbbRxbG',
                                type = 'complex',
                                value = {-1:'G**2/(12.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxbbRxbG')

FRCTdeltaxMYF3Qu1xYF3Qu1G = CTParameter(name = 'FRCTdeltaxMYF3Qu1xYF3Qu1G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qu1)/(3.*cmath.pi**2) + (G**2*MYF3Qu1*reglog(MYF3Qu1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu1 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qu1xYF3Qu1G')

FRCTdeltaZxYF3Qu1YF3Qu1LxYF3Qu1G = CTParameter(name = 'FRCTdeltaZxYF3Qu1YF3Qu1LxYF3Qu1G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu1YF3Qu1LxYF3Qu1G')

FRCTdeltaZxYF3Qu1YF3Qu1RxYF3Qu1G = CTParameter(name = 'FRCTdeltaZxYF3Qu1YF3Qu1RxYF3Qu1G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu1YF3Qu1RxYF3Qu1G')

FRCTdeltaxMYF3Qu2xYF3Qu2G = CTParameter(name = 'FRCTdeltaxMYF3Qu2xYF3Qu2G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qu2)/(3.*cmath.pi**2) + (G**2*MYF3Qu2*reglog(MYF3Qu2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu2 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qu2xYF3Qu2G')

FRCTdeltaZxYF3Qu2YF3Qu2LxYF3Qu2G = CTParameter(name = 'FRCTdeltaZxYF3Qu2YF3Qu2LxYF3Qu2G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu2YF3Qu2LxYF3Qu2G')

FRCTdeltaZxYF3Qu2YF3Qu2RxYF3Qu2G = CTParameter(name = 'FRCTdeltaZxYF3Qu2YF3Qu2RxYF3Qu2G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu2YF3Qu2RxYF3Qu2G')

FRCTdeltaxMYF3Qu3xYF3Qu3G = CTParameter(name = 'FRCTdeltaxMYF3Qu3xYF3Qu3G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qu3)/(3.*cmath.pi**2) + (G**2*MYF3Qu3*reglog(MYF3Qu3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu3 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qu3xYF3Qu3G')

FRCTdeltaZxYF3Qu3YF3Qu3LxYF3Qu3G = CTParameter(name = 'FRCTdeltaZxYF3Qu3YF3Qu3LxYF3Qu3G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu3YF3Qu3LxYF3Qu3G')

FRCTdeltaZxYF3Qu3YF3Qu3RxYF3Qu3G = CTParameter(name = 'FRCTdeltaZxYF3Qu3YF3Qu3RxYF3Qu3G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qu3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qu3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qu3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qu3YF3Qu3RxYF3Qu3G')

FRCTdeltaxMYF3Qd1xYF3Qd1G = CTParameter(name = 'FRCTdeltaxMYF3Qd1xYF3Qd1G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qd1)/(3.*cmath.pi**2) + (G**2*MYF3Qd1*reglog(MYF3Qd1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd1 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qd1xYF3Qd1G')

FRCTdeltaZxYF3Qd1YF3Qd1LxYF3Qd1G = CTParameter(name = 'FRCTdeltaZxYF3Qd1YF3Qd1LxYF3Qd1G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd1YF3Qd1LxYF3Qd1G')

FRCTdeltaZxYF3Qd1YF3Qd1RxYF3Qd1G = CTParameter(name = 'FRCTdeltaZxYF3Qd1YF3Qd1RxYF3Qd1G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd1YF3Qd1RxYF3Qd1G')

FRCTdeltaxMYF3Qd2xYF3Qd2G = CTParameter(name = 'FRCTdeltaxMYF3Qd2xYF3Qd2G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qd2)/(3.*cmath.pi**2) + (G**2*MYF3Qd2*reglog(MYF3Qd2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd2 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qd2xYF3Qd2G')

FRCTdeltaZxYF3Qd2YF3Qd2LxYF3Qd2G = CTParameter(name = 'FRCTdeltaZxYF3Qd2YF3Qd2LxYF3Qd2G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd2YF3Qd2LxYF3Qd2G')

FRCTdeltaZxYF3Qd2YF3Qd2RxYF3Qd2G = CTParameter(name = 'FRCTdeltaZxYF3Qd2YF3Qd2RxYF3Qd2G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd2YF3Qd2RxYF3Qd2G')

FRCTdeltaxMYF3Qd3xYF3Qd3G = CTParameter(name = 'FRCTdeltaxMYF3Qd3xYF3Qd3G',
                                        type = 'complex',
                                        value = {0:'( -(G**2*MYF3Qd3)/(3.*cmath.pi**2) + (G**2*MYF3Qd3*reglog(MYF3Qd3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd3 else 0 )'},
                                        texname = 'FRCTdeltaxMYF3Qd3xYF3Qd3G')

FRCTdeltaZxYF3Qd3YF3Qd3LxYF3Qd3G = CTParameter(name = 'FRCTdeltaZxYF3Qd3YF3Qd3LxYF3Qd3G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd3YF3Qd3LxYF3Qd3G')

FRCTdeltaZxYF3Qd3YF3Qd3RxYF3Qd3G = CTParameter(name = 'FRCTdeltaZxYF3Qd3YF3Qd3RxYF3Qd3G',
                                               type = 'complex',
                                               value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3Qd3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3Qd3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3Qd3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                               texname = 'FRCTdeltaZxYF3Qd3YF3Qd3RxYF3Qd3G')

FRCTdeltaxMYF3u1xYF3u1G = CTParameter(name = 'FRCTdeltaxMYF3u1xYF3u1G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3u1)/(3.*cmath.pi**2) + (G**2*MYF3u1*reglog(MYF3u1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u1 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3u1xYF3u1G')

FRCTdeltaZxYF3u1YF3u1LxYF3u1G = CTParameter(name = 'FRCTdeltaZxYF3u1YF3u1LxYF3u1G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u1YF3u1LxYF3u1G')

FRCTdeltaZxYF3u1YF3u1RxYF3u1G = CTParameter(name = 'FRCTdeltaZxYF3u1YF3u1RxYF3u1G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u1YF3u1RxYF3u1G')

FRCTdeltaxMYF3u2xYF3u2G = CTParameter(name = 'FRCTdeltaxMYF3u2xYF3u2G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3u2)/(3.*cmath.pi**2) + (G**2*MYF3u2*reglog(MYF3u2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u2 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3u2xYF3u2G')

FRCTdeltaZxYF3u2YF3u2LxYF3u2G = CTParameter(name = 'FRCTdeltaZxYF3u2YF3u2LxYF3u2G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u2YF3u2LxYF3u2G')

FRCTdeltaZxYF3u2YF3u2RxYF3u2G = CTParameter(name = 'FRCTdeltaZxYF3u2YF3u2RxYF3u2G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u2YF3u2RxYF3u2G')

FRCTdeltaxMYF3u3xYF3u3G = CTParameter(name = 'FRCTdeltaxMYF3u3xYF3u3G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3u3)/(3.*cmath.pi**2) + (G**2*MYF3u3*reglog(MYF3u3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u3 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3u3xYF3u3G')

FRCTdeltaZxYF3u3YF3u3LxYF3u3G = CTParameter(name = 'FRCTdeltaZxYF3u3YF3u3LxYF3u3G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u3YF3u3LxYF3u3G')

FRCTdeltaZxYF3u3YF3u3RxYF3u3G = CTParameter(name = 'FRCTdeltaZxYF3u3YF3u3RxYF3u3G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3u3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3u3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3u3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3u3YF3u3RxYF3u3G')

FRCTdeltaxMYF3d1xYF3d1G = CTParameter(name = 'FRCTdeltaxMYF3d1xYF3d1G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3d1)/(3.*cmath.pi**2) + (G**2*MYF3d1*reglog(MYF3d1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d1 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3d1xYF3d1G')

FRCTdeltaZxYF3d1YF3d1LxYF3d1G = CTParameter(name = 'FRCTdeltaZxYF3d1YF3d1LxYF3d1G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d1YF3d1LxYF3d1G')

FRCTdeltaZxYF3d1YF3d1RxYF3d1G = CTParameter(name = 'FRCTdeltaZxYF3d1YF3d1RxYF3d1G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d1 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d1**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d1 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d1YF3d1RxYF3d1G')

FRCTdeltaxMYF3d2xYF3d2G = CTParameter(name = 'FRCTdeltaxMYF3d2xYF3d2G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3d2)/(3.*cmath.pi**2) + (G**2*MYF3d2*reglog(MYF3d2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d2 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3d2xYF3d2G')

FRCTdeltaZxYF3d2YF3d2LxYF3d2G = CTParameter(name = 'FRCTdeltaZxYF3d2YF3d2LxYF3d2G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d2YF3d2LxYF3d2G')

FRCTdeltaZxYF3d2YF3d2RxYF3d2G = CTParameter(name = 'FRCTdeltaZxYF3d2YF3d2RxYF3d2G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d2 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d2**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d2 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d2YF3d2RxYF3d2G')

FRCTdeltaxMYF3d3xYF3d3G = CTParameter(name = 'FRCTdeltaxMYF3d3xYF3d3G',
                                      type = 'complex',
                                      value = {0:'( -(G**2*MYF3d3)/(3.*cmath.pi**2) + (G**2*MYF3d3*reglog(MYF3d3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d3 else 0 )'},
                                      texname = 'FRCTdeltaxMYF3d3xYF3d3G')

FRCTdeltaZxYF3d3YF3d3LxYF3d3G = CTParameter(name = 'FRCTdeltaZxYF3d3YF3d3LxYF3d3G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d3YF3d3LxYF3d3G')

FRCTdeltaZxYF3d3YF3d3RxYF3d3G = CTParameter(name = 'FRCTdeltaZxYF3d3YF3d3RxYF3d3G',
                                            type = 'complex',
                                            value = {-1:'( -G**2/(6.*cmath.pi**2) if MYF3d3 else G**2/(12.*cmath.pi**2) )',0:'( (-5*G**2)/(12.*cmath.pi**2) + (G**2*reglog(MYF3d3**2/MU_R**2))/(4.*cmath.pi**2) if MYF3d3 else -G**2/(12.*cmath.pi**2) ) + G**2/(12.*cmath.pi**2)'},
                                            texname = 'FRCTdeltaZxYF3d3YF3d3RxYF3d3G')

FRCTdeltaZxGGxb = CTParameter(name = 'FRCTdeltaZxGGxb',
                              type = 'complex',
                              value = {-1:'G**2/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxb')

FRCTdeltaZxGGxc = CTParameter(name = 'FRCTdeltaZxGGxc',
                              type = 'complex',
                              value = {-1:'G**2/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxc')

FRCTdeltaZxGGxd = CTParameter(name = 'FRCTdeltaZxGGxd',
                              type = 'complex',
                              value = {-1:'G**2/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxd')

FRCTdeltaZxGGxG = CTParameter(name = 'FRCTdeltaZxGGxG',
                              type = 'complex',
                              value = {-1:'(-19*G**2)/(64.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxG')

FRCTdeltaZxGGxghG = CTParameter(name = 'FRCTdeltaZxGGxghG',
                                type = 'complex',
                                value = {-1:'-G**2/(64.*cmath.pi**2)'},
                                texname = 'FRCTdeltaZxGGxghG')

FRCTdeltaZxGGxs = CTParameter(name = 'FRCTdeltaZxGGxs',
                              type = 'complex',
                              value = {-1:'G**2/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxs')

FRCTdeltaZxGGxu = CTParameter(name = 'FRCTdeltaZxGGxu',
                              type = 'complex',
                              value = {-1:'G**2/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxu')

FRCTdeltaZxGGxYF3d1 = CTParameter(name = 'FRCTdeltaZxGGxYF3d1',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3d1 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3d1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d1 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3d1')

FRCTdeltaZxGGxYF3d2 = CTParameter(name = 'FRCTdeltaZxGGxYF3d2',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3d2 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3d2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d2 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3d2')

FRCTdeltaZxGGxYF3d3 = CTParameter(name = 'FRCTdeltaZxGGxYF3d3',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3d3 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3d3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d3 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3d3')

FRCTdeltaZxGGxYF3Qd1 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qd1',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qd1 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qd1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd1 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qd1')

FRCTdeltaZxGGxYF3Qd2 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qd2',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qd2 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qd2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd2 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qd2')

FRCTdeltaZxGGxYF3Qd3 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qd3',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qd3 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qd3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd3 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qd3')

FRCTdeltaZxGGxYF3Qu1 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qu1',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qu1 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qu1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu1 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qu1')

FRCTdeltaZxGGxYF3Qu2 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qu2',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qu2 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qu2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu2 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qu2')

FRCTdeltaZxGGxYF3Qu3 = CTParameter(name = 'FRCTdeltaZxGGxYF3Qu3',
                                   type = 'complex',
                                   value = {-1:'( 0 if MYF3Qu3 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3Qu3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu3 else 0 )'},
                                   texname = 'FRCTdeltaZxGGxYF3Qu3')

FRCTdeltaZxGGxYF3u1 = CTParameter(name = 'FRCTdeltaZxGGxYF3u1',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3u1 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3u1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u1 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3u1')

FRCTdeltaZxGGxYF3u2 = CTParameter(name = 'FRCTdeltaZxGGxYF3u2',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3u2 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3u2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u2 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3u2')

FRCTdeltaZxGGxYF3u3 = CTParameter(name = 'FRCTdeltaZxGGxYF3u3',
                                  type = 'complex',
                                  value = {-1:'( 0 if MYF3u3 else G**2/(24.*cmath.pi**2) )',0:'( (G**2*reglog(MYF3u3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u3 else 0 )'},
                                  texname = 'FRCTdeltaZxGGxYF3u3')

FRCTdeltaZxGGxt = CTParameter(name = 'FRCTdeltaZxGGxt',
                              type = 'complex',
                              value = {0:'(G**2*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                              texname = 'FRCTdeltaZxGGxt')

FRCTdeltaZxGGxYS3d1 = CTParameter(name = 'FRCTdeltaZxGGxYS3d1',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3d1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3d1')

FRCTdeltaZxGGxYS3d2 = CTParameter(name = 'FRCTdeltaZxGGxYS3d2',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3d2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3d2')

FRCTdeltaZxGGxYS3d3 = CTParameter(name = 'FRCTdeltaZxGGxYS3d3',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3d3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3d3')

FRCTdeltaZxGGxYS3Qd1 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qd1',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qd1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qd1')

FRCTdeltaZxGGxYS3Qd2 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qd2',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qd2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qd2')

FRCTdeltaZxGGxYS3Qd3 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qd3',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qd3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qd3')

FRCTdeltaZxGGxYS3Qu1 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qu1',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qu1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qu1')

FRCTdeltaZxGGxYS3Qu2 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qu2',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qu2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qu2')

FRCTdeltaZxGGxYS3Qu3 = CTParameter(name = 'FRCTdeltaZxGGxYS3Qu3',
                                   type = 'complex',
                                   value = {0:'(G**2*reglog(MYS3Qu3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                   texname = 'FRCTdeltaZxGGxYS3Qu3')

FRCTdeltaZxGGxYS3u1 = CTParameter(name = 'FRCTdeltaZxGGxYS3u1',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3u1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3u1')

FRCTdeltaZxGGxYS3u2 = CTParameter(name = 'FRCTdeltaZxGGxYS3u2',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3u2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3u2')

FRCTdeltaZxGGxYS3u3 = CTParameter(name = 'FRCTdeltaZxGGxYS3u3',
                                  type = 'complex',
                                  value = {0:'(G**2*reglog(MYS3u3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaZxGGxYS3u3')

FRCTdeltaxMYS3Qu1xGYS3Qu1 = CTParameter(name = 'FRCTdeltaxMYS3Qu1xGYS3Qu1',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qu1)/(24.*cmath.pi**2) + (G**2*MYS3Qu1*reglog(MYS3Qu1**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qu1xGYS3Qu1')

FRCTdeltaZxYS3Qu1YS3Qu1xGYS3Qu1 = CTParameter(name = 'FRCTdeltaZxYS3Qu1YS3Qu1xGYS3Qu1',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qu1YS3Qu1xGYS3Qu1')

FRCTdeltaxMYS3Qu2xGYS3Qu2 = CTParameter(name = 'FRCTdeltaxMYS3Qu2xGYS3Qu2',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qu2)/(24.*cmath.pi**2) + (G**2*MYS3Qu2*reglog(MYS3Qu2**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qu2xGYS3Qu2')

FRCTdeltaZxYS3Qu2YS3Qu2xGYS3Qu2 = CTParameter(name = 'FRCTdeltaZxYS3Qu2YS3Qu2xGYS3Qu2',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qu2YS3Qu2xGYS3Qu2')

FRCTdeltaxMYS3Qu3xGYS3Qu3 = CTParameter(name = 'FRCTdeltaxMYS3Qu3xGYS3Qu3',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qu3)/(24.*cmath.pi**2) + (G**2*MYS3Qu3*reglog(MYS3Qu3**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qu3xGYS3Qu3')

FRCTdeltaZxYS3Qu3YS3Qu3xGYS3Qu3 = CTParameter(name = 'FRCTdeltaZxYS3Qu3YS3Qu3xGYS3Qu3',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qu3YS3Qu3xGYS3Qu3')

FRCTdeltaxMYS3Qd1xGYS3Qd1 = CTParameter(name = 'FRCTdeltaxMYS3Qd1xGYS3Qd1',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qd1)/(24.*cmath.pi**2) + (G**2*MYS3Qd1*reglog(MYS3Qd1**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qd1xGYS3Qd1')

FRCTdeltaZxYS3Qd1YS3Qd1xGYS3Qd1 = CTParameter(name = 'FRCTdeltaZxYS3Qd1YS3Qd1xGYS3Qd1',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qd1YS3Qd1xGYS3Qd1')

FRCTdeltaxMYS3Qd2xGYS3Qd2 = CTParameter(name = 'FRCTdeltaxMYS3Qd2xGYS3Qd2',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qd2)/(24.*cmath.pi**2) + (G**2*MYS3Qd2*reglog(MYS3Qd2**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qd2xGYS3Qd2')

FRCTdeltaZxYS3Qd2YS3Qd2xGYS3Qd2 = CTParameter(name = 'FRCTdeltaZxYS3Qd2YS3Qd2xGYS3Qd2',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qd2YS3Qd2xGYS3Qd2')

FRCTdeltaxMYS3Qd3xGYS3Qd3 = CTParameter(name = 'FRCTdeltaxMYS3Qd3xGYS3Qd3',
                                        type = 'complex',
                                        value = {0:'(-7*G**2*MYS3Qd3)/(24.*cmath.pi**2) + (G**2*MYS3Qd3*reglog(MYS3Qd3**2/MU_R**2))/(8.*cmath.pi**2)'},
                                        texname = 'FRCTdeltaxMYS3Qd3xGYS3Qd3')

FRCTdeltaZxYS3Qd3YS3Qd3xGYS3Qd3 = CTParameter(name = 'FRCTdeltaZxYS3Qd3YS3Qd3xGYS3Qd3',
                                              type = 'complex',
                                              value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                              texname = 'FRCTdeltaZxYS3Qd3YS3Qd3xGYS3Qd3')

FRCTdeltaxMYS3u1xGYS3u1 = CTParameter(name = 'FRCTdeltaxMYS3u1xGYS3u1',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3u1)/(24.*cmath.pi**2) + (G**2*MYS3u1*reglog(MYS3u1**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3u1xGYS3u1')

FRCTdeltaZxYS3u1YS3u1xGYS3u1 = CTParameter(name = 'FRCTdeltaZxYS3u1YS3u1xGYS3u1',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3u1YS3u1xGYS3u1')

FRCTdeltaxMYS3u2xGYS3u2 = CTParameter(name = 'FRCTdeltaxMYS3u2xGYS3u2',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3u2)/(24.*cmath.pi**2) + (G**2*MYS3u2*reglog(MYS3u2**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3u2xGYS3u2')

FRCTdeltaZxYS3u2YS3u2xGYS3u2 = CTParameter(name = 'FRCTdeltaZxYS3u2YS3u2xGYS3u2',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3u2YS3u2xGYS3u2')

FRCTdeltaxMYS3u3xGYS3u3 = CTParameter(name = 'FRCTdeltaxMYS3u3xGYS3u3',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3u3)/(24.*cmath.pi**2) + (G**2*MYS3u3*reglog(MYS3u3**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3u3xGYS3u3')

FRCTdeltaZxYS3u3YS3u3xGYS3u3 = CTParameter(name = 'FRCTdeltaZxYS3u3YS3u3xGYS3u3',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3u3YS3u3xGYS3u3')

FRCTdeltaxMYS3d1xGYS3d1 = CTParameter(name = 'FRCTdeltaxMYS3d1xGYS3d1',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3d1)/(24.*cmath.pi**2) + (G**2*MYS3d1*reglog(MYS3d1**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3d1xGYS3d1')

FRCTdeltaZxYS3d1YS3d1xGYS3d1 = CTParameter(name = 'FRCTdeltaZxYS3d1YS3d1xGYS3d1',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3d1YS3d1xGYS3d1')

FRCTdeltaxMYS3d2xGYS3d2 = CTParameter(name = 'FRCTdeltaxMYS3d2xGYS3d2',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3d2)/(24.*cmath.pi**2) + (G**2*MYS3d2*reglog(MYS3d2**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3d2xGYS3d2')

FRCTdeltaZxYS3d2YS3d2xGYS3d2 = CTParameter(name = 'FRCTdeltaZxYS3d2YS3d2xGYS3d2',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3d2YS3d2xGYS3d2')

FRCTdeltaxMYS3d3xGYS3d3 = CTParameter(name = 'FRCTdeltaxMYS3d3xGYS3d3',
                                      type = 'complex',
                                      value = {0:'(-7*G**2*MYS3d3)/(24.*cmath.pi**2) + (G**2*MYS3d3*reglog(MYS3d3**2/MU_R**2))/(8.*cmath.pi**2)'},
                                      texname = 'FRCTdeltaxMYS3d3xGYS3d3')

FRCTdeltaZxYS3d3YS3d3xGYS3d3 = CTParameter(name = 'FRCTdeltaZxYS3d3YS3d3xGYS3d3',
                                           type = 'complex',
                                           value = {-1:'-G**2/(6.*cmath.pi**2)'},
                                           texname = 'FRCTdeltaZxYS3d3YS3d3xGYS3d3')

FRCTdeltaxaSxt = CTParameter(name = 'FRCTdeltaxaSxt',
                             type = 'complex',
                             value = {0:'-(aS*G**2*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                             texname = 'FRCTdeltaxaSxt')

FRCTdeltaxaSxYF3d1 = CTParameter(name = 'FRCTdeltaxaSxYF3d1',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3d1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d1 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3d1')

FRCTdeltaxaSxYF3d2 = CTParameter(name = 'FRCTdeltaxaSxYF3d2',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3d2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d2 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3d2')

FRCTdeltaxaSxYF3d3 = CTParameter(name = 'FRCTdeltaxaSxYF3d3',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3d3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3d3 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3d3')

FRCTdeltaxaSxYF3Qd1 = CTParameter(name = 'FRCTdeltaxaSxYF3Qd1',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qd1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd1 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qd1')

FRCTdeltaxaSxYF3Qd2 = CTParameter(name = 'FRCTdeltaxaSxYF3Qd2',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qd2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd2 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qd2')

FRCTdeltaxaSxYF3Qd3 = CTParameter(name = 'FRCTdeltaxaSxYF3Qd3',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qd3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qd3 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qd3')

FRCTdeltaxaSxYF3Qu1 = CTParameter(name = 'FRCTdeltaxaSxYF3Qu1',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qu1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu1 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qu1')

FRCTdeltaxaSxYF3Qu2 = CTParameter(name = 'FRCTdeltaxaSxYF3Qu2',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qu2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu2 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qu2')

FRCTdeltaxaSxYF3Qu3 = CTParameter(name = 'FRCTdeltaxaSxYF3Qu3',
                                  type = 'complex',
                                  value = {0:'( -(aS*G**2*reglog(MYF3Qu3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3Qu3 else 0 )'},
                                  texname = 'FRCTdeltaxaSxYF3Qu3')

FRCTdeltaxaSxYF3u1 = CTParameter(name = 'FRCTdeltaxaSxYF3u1',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3u1**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u1 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3u1')

FRCTdeltaxaSxYF3u2 = CTParameter(name = 'FRCTdeltaxaSxYF3u2',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3u2**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u2 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3u2')

FRCTdeltaxaSxYF3u3 = CTParameter(name = 'FRCTdeltaxaSxYF3u3',
                                 type = 'complex',
                                 value = {0:'( -(aS*G**2*reglog(MYF3u3**2/MU_R**2))/(24.*cmath.pi**2) if MYF3u3 else 0 )'},
                                 texname = 'FRCTdeltaxaSxYF3u3')

FRCTdeltaxaSxYS3d1 = CTParameter(name = 'FRCTdeltaxaSxYS3d1',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3d1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3d1')

FRCTdeltaxaSxYS3d2 = CTParameter(name = 'FRCTdeltaxaSxYS3d2',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3d2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3d2')

FRCTdeltaxaSxYS3d3 = CTParameter(name = 'FRCTdeltaxaSxYS3d3',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3d3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3d3')

FRCTdeltaxaSxYS3Qd1 = CTParameter(name = 'FRCTdeltaxaSxYS3Qd1',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qd1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qd1')

FRCTdeltaxaSxYS3Qd2 = CTParameter(name = 'FRCTdeltaxaSxYS3Qd2',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qd2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qd2')

FRCTdeltaxaSxYS3Qd3 = CTParameter(name = 'FRCTdeltaxaSxYS3Qd3',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qd3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qd3')

FRCTdeltaxaSxYS3Qu1 = CTParameter(name = 'FRCTdeltaxaSxYS3Qu1',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qu1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qu1')

FRCTdeltaxaSxYS3Qu2 = CTParameter(name = 'FRCTdeltaxaSxYS3Qu2',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qu2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qu2')

FRCTdeltaxaSxYS3Qu3 = CTParameter(name = 'FRCTdeltaxaSxYS3Qu3',
                                  type = 'complex',
                                  value = {0:'-(aS*G**2*reglog(MYS3Qu3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                  texname = 'FRCTdeltaxaSxYS3Qu3')

FRCTdeltaxaSxYS3u1 = CTParameter(name = 'FRCTdeltaxaSxYS3u1',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3u1**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3u1')

FRCTdeltaxaSxYS3u2 = CTParameter(name = 'FRCTdeltaxaSxYS3u2',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3u2**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3u2')

FRCTdeltaxaSxYS3u3 = CTParameter(name = 'FRCTdeltaxaSxYS3u3',
                                 type = 'complex',
                                 value = {0:'-(aS*G**2*reglog(MYS3u3**2/MU_R**2))/(96.*cmath.pi**2)'},
                                 texname = 'FRCTdeltaxaSxYS3u3')

