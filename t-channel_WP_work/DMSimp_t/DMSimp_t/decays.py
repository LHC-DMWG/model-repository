# This file was automatically created by FeynRules 2.4.68
# Mathematica version: 10.4.1 for Mac OS X x86 (64-bit) (April 11, 2016)
# Date: Thu 6 Jun 2019 21:52:44


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Xs,P.YF3Qu3):'((3*lamF3Q3x3**2*MT**2 - 3*lamF3Q3x3**2*MXs**2 + 3*lamF3Q3x3**2*MYF3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3Qu3**2 - 2*MXs**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Xs,P.YF3u3):'((3*lamF3u3x3**2*MT**2 - 3*lamF3u3x3**2*MXs**2 + 3*lamF3u3x3**2*MYF3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3u3**2 - 2*MXs**2*MYF3u3**2 + MYF3u3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Xv,P.YF3Qu3):'((3*lamF3Q3x3**2*MT**2 + (3*lamF3Q3x3**2*MT**4)/MXv**2 - 6*lamF3Q3x3**2*MXv**2 + 3*lamF3Q3x3**2*MYF3Qu3**2 - (6*lamF3Q3x3**2*MT**2*MYF3Qu3**2)/MXv**2 + (3*lamF3Q3x3**2*MYF3Qu3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3Qu3**2 - 2*MXv**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Xv,P.YF3u3):'((3*lamF3u3x3**2*MT**2 + (3*lamF3u3x3**2*MT**4)/MXv**2 - 6*lamF3u3x3**2*MXv**2 + 3*lamF3u3x3**2*MYF3u3**2 - (6*lamF3u3x3**2*MT**2*MYF3u3**2)/MXv**2 + (3*lamF3u3x3**2*MYF3u3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3u3**2 - 2*MXv**2*MYF3u3**2 + MYF3u3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.YS3Qu3,P.Xd):'((3*lamS3Q3x3**2*MT**2 + 3*lamS3Q3x3**2*MXd**2 - 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3Qu3**2 - 2*MXd**2*MYS3Qu3**2 + MYS3Qu3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.YS3Qu3,P.Xm):'((3*lamS3Q3x3**2*MT**2 + 3*lamS3Q3x3**2*MXm**2 - 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3Qu3**2 - 2*MXm**2*MYS3Qu3**2 + MYS3Qu3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.YS3u3,P.Xd):'((3*lamS3u3x3**2*MT**2 + 3*lamS3u3x3**2*MXd**2 - 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3u3**2 - 2*MXd**2*MYS3u3**2 + MYS3u3**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.YS3u3,P.Xm):'((3*lamS3u3x3**2*MT**2 + 3*lamS3u3x3**2*MXm**2 - 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3u3**2 - 2*MXm**2*MYS3u3**2 + MYS3u3**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YF3Qu1,P.YF3Qd1__tilde__):'(((6*ee**2*MW**2)/sw**2 - (3*ee**2*MYF3Qd1**2)/sw**2 - (3*ee**2*MYF3Qd1**4)/(MW**2*sw**2) + (18*ee**2*MYF3Qd1*MYF3Qu1)/sw**2 - (3*ee**2*MYF3Qu1**2)/sw**2 + (6*ee**2*MYF3Qd1**2*MYF3Qu1**2)/(MW**2*sw**2) - (3*ee**2*MYF3Qu1**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd1**2 + MYF3Qd1**4 - 2*MW**2*MYF3Qu1**2 - 2*MYF3Qd1**2*MYF3Qu1**2 + MYF3Qu1**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YF3Qu2,P.YF3Qd2__tilde__):'(((6*ee**2*MW**2)/sw**2 - (3*ee**2*MYF3Qd2**2)/sw**2 - (3*ee**2*MYF3Qd2**4)/(MW**2*sw**2) + (18*ee**2*MYF3Qd2*MYF3Qu2)/sw**2 - (3*ee**2*MYF3Qu2**2)/sw**2 + (6*ee**2*MYF3Qd2**2*MYF3Qu2**2)/(MW**2*sw**2) - (3*ee**2*MYF3Qu2**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd2**2 + MYF3Qd2**4 - 2*MW**2*MYF3Qu2**2 - 2*MYF3Qd2**2*MYF3Qu2**2 + MYF3Qu2**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YF3Qu3,P.YF3Qd3__tilde__):'(((6*ee**2*MW**2)/sw**2 - (3*ee**2*MYF3Qd3**2)/sw**2 - (3*ee**2*MYF3Qd3**4)/(MW**2*sw**2) + (18*ee**2*MYF3Qd3*MYF3Qu3)/sw**2 - (3*ee**2*MYF3Qu3**2)/sw**2 + (6*ee**2*MYF3Qd3**2*MYF3Qu3**2)/(MW**2*sw**2) - (3*ee**2*MYF3Qu3**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd3**2 + MYF3Qd3**4 - 2*MW**2*MYF3Qu3**2 - 2*MYF3Qd3**2*MYF3Qu3**2 + MYF3Qu3**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YS3Qd1__tilde__,P.YS3Qu1):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd1**2)/sw**2 + (3*ee**2*MYS3Qd1**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu1**2)/sw**2 - (3*ee**2*MYS3Qd1**2*MYS3Qu1**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu1**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd1**2 + MYS3Qd1**4 - 2*MW**2*MYS3Qu1**2 - 2*MYS3Qd1**2*MYS3Qu1**2 + MYS3Qu1**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YS3Qd2__tilde__,P.YS3Qu2):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd2**2)/sw**2 + (3*ee**2*MYS3Qd2**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu2**2)/sw**2 - (3*ee**2*MYS3Qd2**2*MYS3Qu2**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu2**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd2**2 + MYS3Qd2**4 - 2*MW**2*MYS3Qu2**2 - 2*MYS3Qd2**2*MYS3Qu2**2 + MYS3Qu2**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.YS3Qd3__tilde__,P.YS3Qu3):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd3**2)/sw**2 + (3*ee**2*MYS3Qd3**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu3**2)/sw**2 - (3*ee**2*MYS3Qd3**2*MYS3Qu3**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu3**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd3**2 + MYS3Qd3**4 - 2*MW**2*MYS3Qu3**2 - 2*MYS3Qd3**2*MYS3Qu3**2 + MYS3Qu3**4))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Xd = Decay(name = 'Decay_Xd',
                 particle = P.Xd,
                 partial_widths = {(P.YS3d1__tilde__,P.d):'((MXd**2 - MYS3d1**2)*(3*lamS3d1x1**2*MXd**2 - 3*lamS3d1x1**2*MYS3d1**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3d2__tilde__,P.s):'((MXd**2 - MYS3d2**2)*(3*lamS3d2x2**2*MXd**2 - 3*lamS3d2x2**2*MYS3d2**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3d3__tilde__,P.b):'((MXd**2 - MYS3d3**2)*(3*lamS3d3x3**2*MXd**2 - 3*lamS3d3x3**2*MYS3d3**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qd1__tilde__,P.d):'((MXd**2 - MYS3Qd1**2)*(3*lamS3Q1x1**2*MXd**2 - 3*lamS3Q1x1**2*MYS3Qd1**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qd2__tilde__,P.s):'((MXd**2 - MYS3Qd2**2)*(3*lamS3Q2x2**2*MXd**2 - 3*lamS3Q2x2**2*MYS3Qd2**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qd3__tilde__,P.b):'((MXd**2 - MYS3Qd3**2)*(3*lamS3Q3x3**2*MXd**2 - 3*lamS3Q3x3**2*MYS3Qd3**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qu1__tilde__,P.u):'((MXd**2 - MYS3Qu1**2)*(3*lamS3Q1x1**2*MXd**2 - 3*lamS3Q1x1**2*MYS3Qu1**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qu2__tilde__,P.c):'((MXd**2 - MYS3Qu2**2)*(3*lamS3Q2x2**2*MXd**2 - 3*lamS3Q2x2**2*MYS3Qu2**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3Qu3__tilde__,P.t):'((3*lamS3Q3x3**2*MT**2 + 3*lamS3Q3x3**2*MXd**2 - 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3Qu3**2 - 2*MXd**2*MYS3Qu3**2 + MYS3Qu3**4))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3u1__tilde__,P.u):'((MXd**2 - MYS3u1**2)*(3*lamS3u1x1**2*MXd**2 - 3*lamS3u1x1**2*MYS3u1**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3u2__tilde__,P.c):'((MXd**2 - MYS3u2**2)*(3*lamS3u2x2**2*MXd**2 - 3*lamS3u2x2**2*MYS3u2**2))/(32.*cmath.pi*abs(MXd)**3)',
                                   (P.YS3u3__tilde__,P.t):'((3*lamS3u3x3**2*MT**2 + 3*lamS3u3x3**2*MXd**2 - 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3u3**2 - 2*MXd**2*MYS3u3**2 + MYS3u3**4))/(32.*cmath.pi*abs(MXd)**3)'})

Decay_Xm = Decay(name = 'Decay_Xm',
                 particle = P.Xm,
                 partial_widths = {(P.YS3d1,P.d__tilde__):'((MXm**2 - MYS3d1**2)*(3*lamS3d1x1**2*MXm**2 - 3*lamS3d1x1**2*MYS3d1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3d1__tilde__,P.d):'((MXm**2 - MYS3d1**2)*(3*lamS3d1x1**2*MXm**2 - 3*lamS3d1x1**2*MYS3d1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3d2,P.s__tilde__):'((MXm**2 - MYS3d2**2)*(3*lamS3d2x2**2*MXm**2 - 3*lamS3d2x2**2*MYS3d2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3d2__tilde__,P.s):'((MXm**2 - MYS3d2**2)*(3*lamS3d2x2**2*MXm**2 - 3*lamS3d2x2**2*MYS3d2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3d3,P.b__tilde__):'((MXm**2 - MYS3d3**2)*(3*lamS3d3x3**2*MXm**2 - 3*lamS3d3x3**2*MYS3d3**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3d3__tilde__,P.b):'((MXm**2 - MYS3d3**2)*(3*lamS3d3x3**2*MXm**2 - 3*lamS3d3x3**2*MYS3d3**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd1,P.d__tilde__):'((MXm**2 - MYS3Qd1**2)*(3*lamS3Q1x1**2*MXm**2 - 3*lamS3Q1x1**2*MYS3Qd1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd1__tilde__,P.d):'((MXm**2 - MYS3Qd1**2)*(3*lamS3Q1x1**2*MXm**2 - 3*lamS3Q1x1**2*MYS3Qd1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd2,P.s__tilde__):'((MXm**2 - MYS3Qd2**2)*(3*lamS3Q2x2**2*MXm**2 - 3*lamS3Q2x2**2*MYS3Qd2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd2__tilde__,P.s):'((MXm**2 - MYS3Qd2**2)*(3*lamS3Q2x2**2*MXm**2 - 3*lamS3Q2x2**2*MYS3Qd2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd3,P.b__tilde__):'((MXm**2 - MYS3Qd3**2)*(3*lamS3Q3x3**2*MXm**2 - 3*lamS3Q3x3**2*MYS3Qd3**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qd3__tilde__,P.b):'((MXm**2 - MYS3Qd3**2)*(3*lamS3Q3x3**2*MXm**2 - 3*lamS3Q3x3**2*MYS3Qd3**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu1,P.u__tilde__):'((MXm**2 - MYS3Qu1**2)*(3*lamS3Q1x1**2*MXm**2 - 3*lamS3Q1x1**2*MYS3Qu1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu1__tilde__,P.u):'((MXm**2 - MYS3Qu1**2)*(3*lamS3Q1x1**2*MXm**2 - 3*lamS3Q1x1**2*MYS3Qu1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu2,P.c__tilde__):'((MXm**2 - MYS3Qu2**2)*(3*lamS3Q2x2**2*MXm**2 - 3*lamS3Q2x2**2*MYS3Qu2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu2__tilde__,P.c):'((MXm**2 - MYS3Qu2**2)*(3*lamS3Q2x2**2*MXm**2 - 3*lamS3Q2x2**2*MYS3Qu2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu3,P.t__tilde__):'((3*lamS3Q3x3**2*MT**2 + 3*lamS3Q3x3**2*MXm**2 - 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3Qu3**2 - 2*MXm**2*MYS3Qu3**2 + MYS3Qu3**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3Qu3__tilde__,P.t):'((3*lamS3Q3x3**2*MT**2 + 3*lamS3Q3x3**2*MXm**2 - 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3Qu3**2 - 2*MXm**2*MYS3Qu3**2 + MYS3Qu3**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u1,P.u__tilde__):'((MXm**2 - MYS3u1**2)*(3*lamS3u1x1**2*MXm**2 - 3*lamS3u1x1**2*MYS3u1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u1__tilde__,P.u):'((MXm**2 - MYS3u1**2)*(3*lamS3u1x1**2*MXm**2 - 3*lamS3u1x1**2*MYS3u1**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u2,P.c__tilde__):'((MXm**2 - MYS3u2**2)*(3*lamS3u2x2**2*MXm**2 - 3*lamS3u2x2**2*MYS3u2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u2__tilde__,P.c):'((MXm**2 - MYS3u2**2)*(3*lamS3u2x2**2*MXm**2 - 3*lamS3u2x2**2*MYS3u2**2))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u3,P.t__tilde__):'((3*lamS3u3x3**2*MT**2 + 3*lamS3u3x3**2*MXm**2 - 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3u3**2 - 2*MXm**2*MYS3u3**2 + MYS3u3**4))/(32.*cmath.pi*abs(MXm)**3)',
                                   (P.YS3u3__tilde__,P.t):'((3*lamS3u3x3**2*MT**2 + 3*lamS3u3x3**2*MXm**2 - 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3u3**2 - 2*MXm**2*MYS3u3**2 + MYS3u3**4))/(32.*cmath.pi*abs(MXm)**3)'})

Decay_Xs = Decay(name = 'Decay_Xs',
                 particle = P.Xs,
                 partial_widths = {(P.b,P.YF3d3__tilde__):'((MXs**2 - MYF3d3**2)*(3*lamF3d3x3**2*MXs**2 - 3*lamF3d3x3**2*MYF3d3**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.b,P.YF3Qd3__tilde__):'((MXs**2 - MYF3Qd3**2)*(3*lamF3Q3x3**2*MXs**2 - 3*lamF3Q3x3**2*MYF3Qd3**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.c,P.YF3Qu2__tilde__):'((MXs**2 - MYF3Qu2**2)*(3*lamF3Q2x2**2*MXs**2 - 3*lamF3Q2x2**2*MYF3Qu2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.c,P.YF3u2__tilde__):'((MXs**2 - MYF3u2**2)*(3*lamF3u2x2**2*MXs**2 - 3*lamF3u2x2**2*MYF3u2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.d,P.YF3d1__tilde__):'((MXs**2 - MYF3d1**2)*(3*lamF3d1x1**2*MXs**2 - 3*lamF3d1x1**2*MYF3d1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.d,P.YF3Qd1__tilde__):'((MXs**2 - MYF3Qd1**2)*(3*lamF3Q1x1**2*MXs**2 - 3*lamF3Q1x1**2*MYF3Qd1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.s,P.YF3d2__tilde__):'((MXs**2 - MYF3d2**2)*(3*lamF3d2x2**2*MXs**2 - 3*lamF3d2x2**2*MYF3d2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.s,P.YF3Qd2__tilde__):'((MXs**2 - MYF3Qd2**2)*(3*lamF3Q2x2**2*MXs**2 - 3*lamF3Q2x2**2*MYF3Qd2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.t,P.YF3Qu3__tilde__):'((-3*lamF3Q3x3**2*MT**2 + 3*lamF3Q3x3**2*MXs**2 - 3*lamF3Q3x3**2*MYF3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3Qu3**2 - 2*MXs**2*MYF3Qu3**2 + MYF3Qu3**4))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.t,P.YF3u3__tilde__):'((-3*lamF3u3x3**2*MT**2 + 3*lamF3u3x3**2*MXs**2 - 3*lamF3u3x3**2*MYF3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3u3**2 - 2*MXs**2*MYF3u3**2 + MYF3u3**4))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.u,P.YF3Qu1__tilde__):'((MXs**2 - MYF3Qu1**2)*(3*lamF3Q1x1**2*MXs**2 - 3*lamF3Q1x1**2*MYF3Qu1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.u,P.YF3u1__tilde__):'((MXs**2 - MYF3u1**2)*(3*lamF3u1x1**2*MXs**2 - 3*lamF3u1x1**2*MYF3u1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3d1,P.d__tilde__):'((MXs**2 - MYF3d1**2)*(3*lamF3d1x1**2*MXs**2 - 3*lamF3d1x1**2*MYF3d1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3d2,P.s__tilde__):'((MXs**2 - MYF3d2**2)*(3*lamF3d2x2**2*MXs**2 - 3*lamF3d2x2**2*MYF3d2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3d3,P.b__tilde__):'((MXs**2 - MYF3d3**2)*(3*lamF3d3x3**2*MXs**2 - 3*lamF3d3x3**2*MYF3d3**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qd1,P.d__tilde__):'((MXs**2 - MYF3Qd1**2)*(3*lamF3Q1x1**2*MXs**2 - 3*lamF3Q1x1**2*MYF3Qd1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qd2,P.s__tilde__):'((MXs**2 - MYF3Qd2**2)*(3*lamF3Q2x2**2*MXs**2 - 3*lamF3Q2x2**2*MYF3Qd2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qd3,P.b__tilde__):'((MXs**2 - MYF3Qd3**2)*(3*lamF3Q3x3**2*MXs**2 - 3*lamF3Q3x3**2*MYF3Qd3**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qu1,P.u__tilde__):'((MXs**2 - MYF3Qu1**2)*(3*lamF3Q1x1**2*MXs**2 - 3*lamF3Q1x1**2*MYF3Qu1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qu2,P.c__tilde__):'((MXs**2 - MYF3Qu2**2)*(3*lamF3Q2x2**2*MXs**2 - 3*lamF3Q2x2**2*MYF3Qu2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3Qu3,P.t__tilde__):'((-3*lamF3Q3x3**2*MT**2 + 3*lamF3Q3x3**2*MXs**2 - 3*lamF3Q3x3**2*MYF3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3Qu3**2 - 2*MXs**2*MYF3Qu3**2 + MYF3Qu3**4))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3u1,P.u__tilde__):'((MXs**2 - MYF3u1**2)*(3*lamF3u1x1**2*MXs**2 - 3*lamF3u1x1**2*MYF3u1**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3u2,P.c__tilde__):'((MXs**2 - MYF3u2**2)*(3*lamF3u2x2**2*MXs**2 - 3*lamF3u2x2**2*MYF3u2**2))/(16.*cmath.pi*abs(MXs)**3)',
                                   (P.YF3u3,P.t__tilde__):'((-3*lamF3u3x3**2*MT**2 + 3*lamF3u3x3**2*MXs**2 - 3*lamF3u3x3**2*MYF3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3u3**2 - 2*MXs**2*MYF3u3**2 + MYF3u3**4))/(16.*cmath.pi*abs(MXs)**3)'})

Decay_Xv = Decay(name = 'Decay_Xv',
                 particle = P.Xv,
                 partial_widths = {(P.b,P.YF3d3__tilde__):'((MXv**2 - MYF3d3**2)*(6*lamF3d3x3**2*MXv**2 - 3*lamF3d3x3**2*MYF3d3**2 - (3*lamF3d3x3**2*MYF3d3**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.b,P.YF3Qd3__tilde__):'((MXv**2 - MYF3Qd3**2)*(6*lamF3Q3x3**2*MXv**2 - 3*lamF3Q3x3**2*MYF3Qd3**2 - (3*lamF3Q3x3**2*MYF3Qd3**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.c,P.YF3Qu2__tilde__):'((MXv**2 - MYF3Qu2**2)*(6*lamF3Q2x2**2*MXv**2 - 3*lamF3Q2x2**2*MYF3Qu2**2 - (3*lamF3Q2x2**2*MYF3Qu2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.c,P.YF3u2__tilde__):'((MXv**2 - MYF3u2**2)*(6*lamF3u2x2**2*MXv**2 - 3*lamF3u2x2**2*MYF3u2**2 - (3*lamF3u2x2**2*MYF3u2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.d,P.YF3d1__tilde__):'((MXv**2 - MYF3d1**2)*(6*lamF3d1x1**2*MXv**2 - 3*lamF3d1x1**2*MYF3d1**2 - (3*lamF3d1x1**2*MYF3d1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.d,P.YF3Qd1__tilde__):'((MXv**2 - MYF3Qd1**2)*(6*lamF3Q1x1**2*MXv**2 - 3*lamF3Q1x1**2*MYF3Qd1**2 - (3*lamF3Q1x1**2*MYF3Qd1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.s,P.YF3d2__tilde__):'((MXv**2 - MYF3d2**2)*(6*lamF3d2x2**2*MXv**2 - 3*lamF3d2x2**2*MYF3d2**2 - (3*lamF3d2x2**2*MYF3d2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.s,P.YF3Qd2__tilde__):'((MXv**2 - MYF3Qd2**2)*(6*lamF3Q2x2**2*MXv**2 - 3*lamF3Q2x2**2*MYF3Qd2**2 - (3*lamF3Q2x2**2*MYF3Qd2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.t,P.YF3Qu3__tilde__):'((-3*lamF3Q3x3**2*MT**2 - (3*lamF3Q3x3**2*MT**4)/MXv**2 + 6*lamF3Q3x3**2*MXv**2 - 3*lamF3Q3x3**2*MYF3Qu3**2 + (6*lamF3Q3x3**2*MT**2*MYF3Qu3**2)/MXv**2 - (3*lamF3Q3x3**2*MYF3Qu3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3Qu3**2 - 2*MXv**2*MYF3Qu3**2 + MYF3Qu3**4))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.t,P.YF3u3__tilde__):'((-3*lamF3u3x3**2*MT**2 - (3*lamF3u3x3**2*MT**4)/MXv**2 + 6*lamF3u3x3**2*MXv**2 - 3*lamF3u3x3**2*MYF3u3**2 + (6*lamF3u3x3**2*MT**2*MYF3u3**2)/MXv**2 - (3*lamF3u3x3**2*MYF3u3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3u3**2 - 2*MXv**2*MYF3u3**2 + MYF3u3**4))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.u,P.YF3Qu1__tilde__):'((MXv**2 - MYF3Qu1**2)*(6*lamF3Q1x1**2*MXv**2 - 3*lamF3Q1x1**2*MYF3Qu1**2 - (3*lamF3Q1x1**2*MYF3Qu1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.u,P.YF3u1__tilde__):'((MXv**2 - MYF3u1**2)*(6*lamF3u1x1**2*MXv**2 - 3*lamF3u1x1**2*MYF3u1**2 - (3*lamF3u1x1**2*MYF3u1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3d1,P.d__tilde__):'((MXv**2 - MYF3d1**2)*(6*lamF3d1x1**2*MXv**2 - 3*lamF3d1x1**2*MYF3d1**2 - (3*lamF3d1x1**2*MYF3d1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3d2,P.s__tilde__):'((MXv**2 - MYF3d2**2)*(6*lamF3d2x2**2*MXv**2 - 3*lamF3d2x2**2*MYF3d2**2 - (3*lamF3d2x2**2*MYF3d2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3d3,P.b__tilde__):'((MXv**2 - MYF3d3**2)*(6*lamF3d3x3**2*MXv**2 - 3*lamF3d3x3**2*MYF3d3**2 - (3*lamF3d3x3**2*MYF3d3**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qd1,P.d__tilde__):'((MXv**2 - MYF3Qd1**2)*(6*lamF3Q1x1**2*MXv**2 - 3*lamF3Q1x1**2*MYF3Qd1**2 - (3*lamF3Q1x1**2*MYF3Qd1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qd2,P.s__tilde__):'((MXv**2 - MYF3Qd2**2)*(6*lamF3Q2x2**2*MXv**2 - 3*lamF3Q2x2**2*MYF3Qd2**2 - (3*lamF3Q2x2**2*MYF3Qd2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qd3,P.b__tilde__):'((MXv**2 - MYF3Qd3**2)*(6*lamF3Q3x3**2*MXv**2 - 3*lamF3Q3x3**2*MYF3Qd3**2 - (3*lamF3Q3x3**2*MYF3Qd3**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qu1,P.u__tilde__):'((MXv**2 - MYF3Qu1**2)*(6*lamF3Q1x1**2*MXv**2 - 3*lamF3Q1x1**2*MYF3Qu1**2 - (3*lamF3Q1x1**2*MYF3Qu1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qu2,P.c__tilde__):'((MXv**2 - MYF3Qu2**2)*(6*lamF3Q2x2**2*MXv**2 - 3*lamF3Q2x2**2*MYF3Qu2**2 - (3*lamF3Q2x2**2*MYF3Qu2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3Qu3,P.t__tilde__):'((-3*lamF3Q3x3**2*MT**2 - (3*lamF3Q3x3**2*MT**4)/MXv**2 + 6*lamF3Q3x3**2*MXv**2 - 3*lamF3Q3x3**2*MYF3Qu3**2 + (6*lamF3Q3x3**2*MT**2*MYF3Qu3**2)/MXv**2 - (3*lamF3Q3x3**2*MYF3Qu3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3Qu3**2 - 2*MXv**2*MYF3Qu3**2 + MYF3Qu3**4))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3u1,P.u__tilde__):'((MXv**2 - MYF3u1**2)*(6*lamF3u1x1**2*MXv**2 - 3*lamF3u1x1**2*MYF3u1**2 - (3*lamF3u1x1**2*MYF3u1**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3u2,P.c__tilde__):'((MXv**2 - MYF3u2**2)*(6*lamF3u2x2**2*MXv**2 - 3*lamF3u2x2**2*MYF3u2**2 - (3*lamF3u2x2**2*MYF3u2**4)/MXv**2))/(48.*cmath.pi*abs(MXv)**3)',
                                   (P.YF3u3,P.t__tilde__):'((-3*lamF3u3x3**2*MT**2 - (3*lamF3u3x3**2*MT**4)/MXv**2 + 6*lamF3u3x3**2*MXv**2 - 3*lamF3u3x3**2*MYF3u3**2 + (6*lamF3u3x3**2*MT**2*MYF3u3**2)/MXv**2 - (3*lamF3u3x3**2*MYF3u3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3u3**2 - 2*MXv**2*MYF3u3**2 + MYF3u3**4))/(48.*cmath.pi*abs(MXv)**3)'})

Decay_YF3d1 = Decay(name = 'Decay_YF3d1',
                    particle = P.YF3d1,
                    partial_widths = {(P.Xs,P.d):'((-MXs**2 + MYF3d1**2)*(-3*lamF3d1x1**2*MXs**2 + 3*lamF3d1x1**2*MYF3d1**2))/(96.*cmath.pi*abs(MYF3d1)**3)',
                                      (P.Xv,P.d):'((-MXv**2 + MYF3d1**2)*(-6*lamF3d1x1**2*MXv**2 + 3*lamF3d1x1**2*MYF3d1**2 + (3*lamF3d1x1**2*MYF3d1**4)/MXv**2))/(96.*cmath.pi*abs(MYF3d1)**3)'})

Decay_YF3d2 = Decay(name = 'Decay_YF3d2',
                    particle = P.YF3d2,
                    partial_widths = {(P.Xs,P.s):'((-MXs**2 + MYF3d2**2)*(-3*lamF3d2x2**2*MXs**2 + 3*lamF3d2x2**2*MYF3d2**2))/(96.*cmath.pi*abs(MYF3d2)**3)',
                                      (P.Xv,P.s):'((-MXv**2 + MYF3d2**2)*(-6*lamF3d2x2**2*MXv**2 + 3*lamF3d2x2**2*MYF3d2**2 + (3*lamF3d2x2**2*MYF3d2**4)/MXv**2))/(96.*cmath.pi*abs(MYF3d2)**3)'})

Decay_YF3d3 = Decay(name = 'Decay_YF3d3',
                    particle = P.YF3d3,
                    partial_widths = {(P.Xs,P.b):'((-MXs**2 + MYF3d3**2)*(-3*lamF3d3x3**2*MXs**2 + 3*lamF3d3x3**2*MYF3d3**2))/(96.*cmath.pi*abs(MYF3d3)**3)',
                                      (P.Xv,P.b):'((-MXv**2 + MYF3d3**2)*(-6*lamF3d3x3**2*MXv**2 + 3*lamF3d3x3**2*MYF3d3**2 + (3*lamF3d3x3**2*MYF3d3**4)/MXv**2))/(96.*cmath.pi*abs(MYF3d3)**3)'})

Decay_YF3Qd1 = Decay(name = 'Decay_YF3Qd1',
                     particle = P.YF3Qd1,
                     partial_widths = {(P.W__minus__,P.YF3Qu1):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd1**2)/sw**2 + (3*ee**2*MYF3Qd1**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd1*MYF3Qu1)/sw**2 + (3*ee**2*MYF3Qu1**2)/sw**2 - (6*ee**2*MYF3Qd1**2*MYF3Qu1**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu1**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd1**2 + MYF3Qd1**4 - 2*MW**2*MYF3Qu1**2 - 2*MYF3Qd1**2*MYF3Qu1**2 + MYF3Qu1**4))/(96.*cmath.pi*abs(MYF3Qd1)**3)',
                                       (P.Xs,P.d):'((-MXs**2 + MYF3Qd1**2)*(-3*lamF3Q1x1**2*MXs**2 + 3*lamF3Q1x1**2*MYF3Qd1**2))/(96.*cmath.pi*abs(MYF3Qd1)**3)',
                                       (P.Xv,P.d):'((-MXv**2 + MYF3Qd1**2)*(-6*lamF3Q1x1**2*MXv**2 + 3*lamF3Q1x1**2*MYF3Qd1**2 + (3*lamF3Q1x1**2*MYF3Qd1**4)/MXv**2))/(96.*cmath.pi*abs(MYF3Qd1)**3)'})

Decay_YF3Qd2 = Decay(name = 'Decay_YF3Qd2',
                     particle = P.YF3Qd2,
                     partial_widths = {(P.W__minus__,P.YF3Qu2):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd2**2)/sw**2 + (3*ee**2*MYF3Qd2**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd2*MYF3Qu2)/sw**2 + (3*ee**2*MYF3Qu2**2)/sw**2 - (6*ee**2*MYF3Qd2**2*MYF3Qu2**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu2**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd2**2 + MYF3Qd2**4 - 2*MW**2*MYF3Qu2**2 - 2*MYF3Qd2**2*MYF3Qu2**2 + MYF3Qu2**4))/(96.*cmath.pi*abs(MYF3Qd2)**3)',
                                       (P.Xs,P.s):'((-MXs**2 + MYF3Qd2**2)*(-3*lamF3Q2x2**2*MXs**2 + 3*lamF3Q2x2**2*MYF3Qd2**2))/(96.*cmath.pi*abs(MYF3Qd2)**3)',
                                       (P.Xv,P.s):'((-MXv**2 + MYF3Qd2**2)*(-6*lamF3Q2x2**2*MXv**2 + 3*lamF3Q2x2**2*MYF3Qd2**2 + (3*lamF3Q2x2**2*MYF3Qd2**4)/MXv**2))/(96.*cmath.pi*abs(MYF3Qd2)**3)'})

Decay_YF3Qd3 = Decay(name = 'Decay_YF3Qd3',
                     particle = P.YF3Qd3,
                     partial_widths = {(P.W__minus__,P.YF3Qu3):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd3**2)/sw**2 + (3*ee**2*MYF3Qd3**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd3*MYF3Qu3)/sw**2 + (3*ee**2*MYF3Qu3**2)/sw**2 - (6*ee**2*MYF3Qd3**2*MYF3Qu3**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu3**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd3**2 + MYF3Qd3**4 - 2*MW**2*MYF3Qu3**2 - 2*MYF3Qd3**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MYF3Qd3)**3)',
                                       (P.Xs,P.b):'((-MXs**2 + MYF3Qd3**2)*(-3*lamF3Q3x3**2*MXs**2 + 3*lamF3Q3x3**2*MYF3Qd3**2))/(96.*cmath.pi*abs(MYF3Qd3)**3)',
                                       (P.Xv,P.b):'((-MXv**2 + MYF3Qd3**2)*(-6*lamF3Q3x3**2*MXv**2 + 3*lamF3Q3x3**2*MYF3Qd3**2 + (3*lamF3Q3x3**2*MYF3Qd3**4)/MXv**2))/(96.*cmath.pi*abs(MYF3Qd3)**3)'})

Decay_YF3Qu1 = Decay(name = 'Decay_YF3Qu1',
                     particle = P.YF3Qu1,
                     partial_widths = {(P.W__plus__,P.YF3Qd1):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd1**2)/sw**2 + (3*ee**2*MYF3Qd1**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd1*MYF3Qu1)/sw**2 + (3*ee**2*MYF3Qu1**2)/sw**2 - (6*ee**2*MYF3Qd1**2*MYF3Qu1**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu1**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd1**2 + MYF3Qd1**4 - 2*MW**2*MYF3Qu1**2 - 2*MYF3Qd1**2*MYF3Qu1**2 + MYF3Qu1**4))/(96.*cmath.pi*abs(MYF3Qu1)**3)',
                                       (P.Xs,P.u):'((-MXs**2 + MYF3Qu1**2)*(-3*lamF3Q1x1**2*MXs**2 + 3*lamF3Q1x1**2*MYF3Qu1**2))/(96.*cmath.pi*abs(MYF3Qu1)**3)',
                                       (P.Xv,P.u):'((-MXv**2 + MYF3Qu1**2)*(-6*lamF3Q1x1**2*MXv**2 + 3*lamF3Q1x1**2*MYF3Qu1**2 + (3*lamF3Q1x1**2*MYF3Qu1**4)/MXv**2))/(96.*cmath.pi*abs(MYF3Qu1)**3)'})

Decay_YF3Qu2 = Decay(name = 'Decay_YF3Qu2',
                     particle = P.YF3Qu2,
                     partial_widths = {(P.W__plus__,P.YF3Qd2):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd2**2)/sw**2 + (3*ee**2*MYF3Qd2**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd2*MYF3Qu2)/sw**2 + (3*ee**2*MYF3Qu2**2)/sw**2 - (6*ee**2*MYF3Qd2**2*MYF3Qu2**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu2**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd2**2 + MYF3Qd2**4 - 2*MW**2*MYF3Qu2**2 - 2*MYF3Qd2**2*MYF3Qu2**2 + MYF3Qu2**4))/(96.*cmath.pi*abs(MYF3Qu2)**3)',
                                       (P.Xs,P.c):'((-MXs**2 + MYF3Qu2**2)*(-3*lamF3Q2x2**2*MXs**2 + 3*lamF3Q2x2**2*MYF3Qu2**2))/(96.*cmath.pi*abs(MYF3Qu2)**3)',
                                       (P.Xv,P.c):'((-MXv**2 + MYF3Qu2**2)*(-6*lamF3Q2x2**2*MXv**2 + 3*lamF3Q2x2**2*MYF3Qu2**2 + (3*lamF3Q2x2**2*MYF3Qu2**4)/MXv**2))/(96.*cmath.pi*abs(MYF3Qu2)**3)'})

Decay_YF3Qu3 = Decay(name = 'Decay_YF3Qu3',
                     particle = P.YF3Qu3,
                     partial_widths = {(P.W__plus__,P.YF3Qd3):'(((-6*ee**2*MW**2)/sw**2 + (3*ee**2*MYF3Qd3**2)/sw**2 + (3*ee**2*MYF3Qd3**4)/(MW**2*sw**2) - (18*ee**2*MYF3Qd3*MYF3Qu3)/sw**2 + (3*ee**2*MYF3Qu3**2)/sw**2 - (6*ee**2*MYF3Qd3**2*MYF3Qu3**2)/(MW**2*sw**2) + (3*ee**2*MYF3Qu3**4)/(MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYF3Qd3**2 + MYF3Qd3**4 - 2*MW**2*MYF3Qu3**2 - 2*MYF3Qd3**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MYF3Qu3)**3)',
                                       (P.Xs,P.t):'((3*lamF3Q3x3**2*MT**2 - 3*lamF3Q3x3**2*MXs**2 + 3*lamF3Q3x3**2*MYF3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3Qu3**2 - 2*MXs**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MYF3Qu3)**3)',
                                       (P.Xv,P.t):'((3*lamF3Q3x3**2*MT**2 + (3*lamF3Q3x3**2*MT**4)/MXv**2 - 6*lamF3Q3x3**2*MXv**2 + 3*lamF3Q3x3**2*MYF3Qu3**2 - (6*lamF3Q3x3**2*MT**2*MYF3Qu3**2)/MXv**2 + (3*lamF3Q3x3**2*MYF3Qu3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3Qu3**2 - 2*MXv**2*MYF3Qu3**2 + MYF3Qu3**4))/(96.*cmath.pi*abs(MYF3Qu3)**3)'})

Decay_YF3u1 = Decay(name = 'Decay_YF3u1',
                    particle = P.YF3u1,
                    partial_widths = {(P.Xs,P.u):'((-MXs**2 + MYF3u1**2)*(-3*lamF3u1x1**2*MXs**2 + 3*lamF3u1x1**2*MYF3u1**2))/(96.*cmath.pi*abs(MYF3u1)**3)',
                                      (P.Xv,P.u):'((-MXv**2 + MYF3u1**2)*(-6*lamF3u1x1**2*MXv**2 + 3*lamF3u1x1**2*MYF3u1**2 + (3*lamF3u1x1**2*MYF3u1**4)/MXv**2))/(96.*cmath.pi*abs(MYF3u1)**3)'})

Decay_YF3u2 = Decay(name = 'Decay_YF3u2',
                    particle = P.YF3u2,
                    partial_widths = {(P.Xs,P.c):'((-MXs**2 + MYF3u2**2)*(-3*lamF3u2x2**2*MXs**2 + 3*lamF3u2x2**2*MYF3u2**2))/(96.*cmath.pi*abs(MYF3u2)**3)',
                                      (P.Xv,P.c):'((-MXv**2 + MYF3u2**2)*(-6*lamF3u2x2**2*MXv**2 + 3*lamF3u2x2**2*MYF3u2**2 + (3*lamF3u2x2**2*MYF3u2**4)/MXv**2))/(96.*cmath.pi*abs(MYF3u2)**3)'})

Decay_YF3u3 = Decay(name = 'Decay_YF3u3',
                    particle = P.YF3u3,
                    partial_widths = {(P.Xs,P.t):'((3*lamF3u3x3**2*MT**2 - 3*lamF3u3x3**2*MXs**2 + 3*lamF3u3x3**2*MYF3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXs**2 + MXs**4 - 2*MT**2*MYF3u3**2 - 2*MXs**2*MYF3u3**2 + MYF3u3**4))/(96.*cmath.pi*abs(MYF3u3)**3)',
                                      (P.Xv,P.t):'((3*lamF3u3x3**2*MT**2 + (3*lamF3u3x3**2*MT**4)/MXv**2 - 6*lamF3u3x3**2*MXv**2 + 3*lamF3u3x3**2*MYF3u3**2 - (6*lamF3u3x3**2*MT**2*MYF3u3**2)/MXv**2 + (3*lamF3u3x3**2*MYF3u3**4)/MXv**2)*cmath.sqrt(MT**4 - 2*MT**2*MXv**2 + MXv**4 - 2*MT**2*MYF3u3**2 - 2*MXv**2*MYF3u3**2 + MYF3u3**4))/(96.*cmath.pi*abs(MYF3u3)**3)'})

Decay_YS3d1 = Decay(name = 'Decay_YS3d1',
                    particle = P.YS3d1,
                    partial_widths = {(P.d,P.Xd__tilde__):'((-MXd**2 + MYS3d1**2)*(-3*lamS3d1x1**2*MXd**2 + 3*lamS3d1x1**2*MYS3d1**2))/(48.*cmath.pi*abs(MYS3d1)**3)',
                                      (P.d,P.Xm):'((-MXm**2 + MYS3d1**2)*(-3*lamS3d1x1**2*MXm**2 + 3*lamS3d1x1**2*MYS3d1**2))/(48.*cmath.pi*abs(MYS3d1)**3)'})

Decay_YS3d2 = Decay(name = 'Decay_YS3d2',
                    particle = P.YS3d2,
                    partial_widths = {(P.s,P.Xd__tilde__):'((-MXd**2 + MYS3d2**2)*(-3*lamS3d2x2**2*MXd**2 + 3*lamS3d2x2**2*MYS3d2**2))/(48.*cmath.pi*abs(MYS3d2)**3)',
                                      (P.s,P.Xm):'((-MXm**2 + MYS3d2**2)*(-3*lamS3d2x2**2*MXm**2 + 3*lamS3d2x2**2*MYS3d2**2))/(48.*cmath.pi*abs(MYS3d2)**3)'})

Decay_YS3d3 = Decay(name = 'Decay_YS3d3',
                    particle = P.YS3d3,
                    partial_widths = {(P.b,P.Xd__tilde__):'((-MXd**2 + MYS3d3**2)*(-3*lamS3d3x3**2*MXd**2 + 3*lamS3d3x3**2*MYS3d3**2))/(48.*cmath.pi*abs(MYS3d3)**3)',
                                      (P.b,P.Xm):'((-MXm**2 + MYS3d3**2)*(-3*lamS3d3x3**2*MXm**2 + 3*lamS3d3x3**2*MYS3d3**2))/(48.*cmath.pi*abs(MYS3d3)**3)'})

Decay_YS3Qd1 = Decay(name = 'Decay_YS3Qd1',
                     particle = P.YS3Qd1,
                     partial_widths = {(P.d,P.Xd__tilde__):'((-MXd**2 + MYS3Qd1**2)*(-3*lamS3Q1x1**2*MXd**2 + 3*lamS3Q1x1**2*MYS3Qd1**2))/(48.*cmath.pi*abs(MYS3Qd1)**3)',
                                       (P.d,P.Xm):'((-MXm**2 + MYS3Qd1**2)*(-3*lamS3Q1x1**2*MXm**2 + 3*lamS3Q1x1**2*MYS3Qd1**2))/(48.*cmath.pi*abs(MYS3Qd1)**3)',
                                       (P.W__minus__,P.YS3Qu1):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd1**2)/sw**2 + (3*ee**2*MYS3Qd1**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu1**2)/sw**2 - (3*ee**2*MYS3Qd1**2*MYS3Qu1**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu1**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd1**2 + MYS3Qd1**4 - 2*MW**2*MYS3Qu1**2 - 2*MYS3Qd1**2*MYS3Qu1**2 + MYS3Qu1**4))/(48.*cmath.pi*abs(MYS3Qd1)**3)'})

Decay_YS3Qd2 = Decay(name = 'Decay_YS3Qd2',
                     particle = P.YS3Qd2,
                     partial_widths = {(P.s,P.Xd__tilde__):'((-MXd**2 + MYS3Qd2**2)*(-3*lamS3Q2x2**2*MXd**2 + 3*lamS3Q2x2**2*MYS3Qd2**2))/(48.*cmath.pi*abs(MYS3Qd2)**3)',
                                       (P.s,P.Xm):'((-MXm**2 + MYS3Qd2**2)*(-3*lamS3Q2x2**2*MXm**2 + 3*lamS3Q2x2**2*MYS3Qd2**2))/(48.*cmath.pi*abs(MYS3Qd2)**3)',
                                       (P.W__minus__,P.YS3Qu2):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd2**2)/sw**2 + (3*ee**2*MYS3Qd2**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu2**2)/sw**2 - (3*ee**2*MYS3Qd2**2*MYS3Qu2**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu2**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd2**2 + MYS3Qd2**4 - 2*MW**2*MYS3Qu2**2 - 2*MYS3Qd2**2*MYS3Qu2**2 + MYS3Qu2**4))/(48.*cmath.pi*abs(MYS3Qd2)**3)'})

Decay_YS3Qd3 = Decay(name = 'Decay_YS3Qd3',
                     particle = P.YS3Qd3,
                     partial_widths = {(P.b,P.Xd__tilde__):'((-MXd**2 + MYS3Qd3**2)*(-3*lamS3Q3x3**2*MXd**2 + 3*lamS3Q3x3**2*MYS3Qd3**2))/(48.*cmath.pi*abs(MYS3Qd3)**3)',
                                       (P.b,P.Xm):'((-MXm**2 + MYS3Qd3**2)*(-3*lamS3Q3x3**2*MXm**2 + 3*lamS3Q3x3**2*MYS3Qd3**2))/(48.*cmath.pi*abs(MYS3Qd3)**3)',
                                       (P.W__minus__,P.YS3Qu3):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd3**2)/sw**2 + (3*ee**2*MYS3Qd3**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu3**2)/sw**2 - (3*ee**2*MYS3Qd3**2*MYS3Qu3**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu3**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd3**2 + MYS3Qd3**4 - 2*MW**2*MYS3Qu3**2 - 2*MYS3Qd3**2*MYS3Qu3**2 + MYS3Qu3**4))/(48.*cmath.pi*abs(MYS3Qd3)**3)'})

Decay_YS3Qu1 = Decay(name = 'Decay_YS3Qu1',
                     particle = P.YS3Qu1,
                     partial_widths = {(P.u,P.Xd__tilde__):'((-MXd**2 + MYS3Qu1**2)*(-3*lamS3Q1x1**2*MXd**2 + 3*lamS3Q1x1**2*MYS3Qu1**2))/(48.*cmath.pi*abs(MYS3Qu1)**3)',
                                       (P.u,P.Xm):'((-MXm**2 + MYS3Qu1**2)*(-3*lamS3Q1x1**2*MXm**2 + 3*lamS3Q1x1**2*MYS3Qu1**2))/(48.*cmath.pi*abs(MYS3Qu1)**3)',
                                       (P.W__plus__,P.YS3Qd1):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd1**2)/sw**2 + (3*ee**2*MYS3Qd1**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu1**2)/sw**2 - (3*ee**2*MYS3Qd1**2*MYS3Qu1**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu1**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd1**2 + MYS3Qd1**4 - 2*MW**2*MYS3Qu1**2 - 2*MYS3Qd1**2*MYS3Qu1**2 + MYS3Qu1**4))/(48.*cmath.pi*abs(MYS3Qu1)**3)'})

Decay_YS3Qu2 = Decay(name = 'Decay_YS3Qu2',
                     particle = P.YS3Qu2,
                     partial_widths = {(P.c,P.Xd__tilde__):'((-MXd**2 + MYS3Qu2**2)*(-3*lamS3Q2x2**2*MXd**2 + 3*lamS3Q2x2**2*MYS3Qu2**2))/(48.*cmath.pi*abs(MYS3Qu2)**3)',
                                       (P.c,P.Xm):'((-MXm**2 + MYS3Qu2**2)*(-3*lamS3Q2x2**2*MXm**2 + 3*lamS3Q2x2**2*MYS3Qu2**2))/(48.*cmath.pi*abs(MYS3Qu2)**3)',
                                       (P.W__plus__,P.YS3Qd2):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd2**2)/sw**2 + (3*ee**2*MYS3Qd2**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu2**2)/sw**2 - (3*ee**2*MYS3Qd2**2*MYS3Qu2**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu2**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd2**2 + MYS3Qd2**4 - 2*MW**2*MYS3Qu2**2 - 2*MYS3Qd2**2*MYS3Qu2**2 + MYS3Qu2**4))/(48.*cmath.pi*abs(MYS3Qu2)**3)'})

Decay_YS3Qu3 = Decay(name = 'Decay_YS3Qu3',
                     particle = P.YS3Qu3,
                     partial_widths = {(P.t,P.Xd__tilde__):'((-3*lamS3Q3x3**2*MT**2 - 3*lamS3Q3x3**2*MXd**2 + 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3Qu3**2 - 2*MXd**2*MYS3Qu3**2 + MYS3Qu3**4))/(48.*cmath.pi*abs(MYS3Qu3)**3)',
                                       (P.t,P.Xm):'((-3*lamS3Q3x3**2*MT**2 - 3*lamS3Q3x3**2*MXm**2 + 3*lamS3Q3x3**2*MYS3Qu3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3Qu3**2 - 2*MXm**2*MYS3Qu3**2 + MYS3Qu3**4))/(48.*cmath.pi*abs(MYS3Qu3)**3)',
                                       (P.W__plus__,P.YS3Qd3):'(((3*ee**2*MW**2)/(2.*sw**2) - (3*ee**2*MYS3Qd3**2)/sw**2 + (3*ee**2*MYS3Qd3**4)/(2.*MW**2*sw**2) - (3*ee**2*MYS3Qu3**2)/sw**2 - (3*ee**2*MYS3Qd3**2*MYS3Qu3**2)/(MW**2*sw**2) + (3*ee**2*MYS3Qu3**4)/(2.*MW**2*sw**2))*cmath.sqrt(MW**4 - 2*MW**2*MYS3Qd3**2 + MYS3Qd3**4 - 2*MW**2*MYS3Qu3**2 - 2*MYS3Qd3**2*MYS3Qu3**2 + MYS3Qu3**4))/(48.*cmath.pi*abs(MYS3Qu3)**3)'})

Decay_YS3u1 = Decay(name = 'Decay_YS3u1',
                    particle = P.YS3u1,
                    partial_widths = {(P.u,P.Xd__tilde__):'((-MXd**2 + MYS3u1**2)*(-3*lamS3u1x1**2*MXd**2 + 3*lamS3u1x1**2*MYS3u1**2))/(48.*cmath.pi*abs(MYS3u1)**3)',
                                      (P.u,P.Xm):'((-MXm**2 + MYS3u1**2)*(-3*lamS3u1x1**2*MXm**2 + 3*lamS3u1x1**2*MYS3u1**2))/(48.*cmath.pi*abs(MYS3u1)**3)'})

Decay_YS3u2 = Decay(name = 'Decay_YS3u2',
                    particle = P.YS3u2,
                    partial_widths = {(P.c,P.Xd__tilde__):'((-MXd**2 + MYS3u2**2)*(-3*lamS3u2x2**2*MXd**2 + 3*lamS3u2x2**2*MYS3u2**2))/(48.*cmath.pi*abs(MYS3u2)**3)',
                                      (P.c,P.Xm):'((-MXm**2 + MYS3u2**2)*(-3*lamS3u2x2**2*MXm**2 + 3*lamS3u2x2**2*MYS3u2**2))/(48.*cmath.pi*abs(MYS3u2)**3)'})

Decay_YS3u3 = Decay(name = 'Decay_YS3u3',
                    particle = P.YS3u3,
                    partial_widths = {(P.t,P.Xd__tilde__):'((-3*lamS3u3x3**2*MT**2 - 3*lamS3u3x3**2*MXd**2 + 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXd**2 + MXd**4 - 2*MT**2*MYS3u3**2 - 2*MXd**2*MYS3u3**2 + MYS3u3**4))/(48.*cmath.pi*abs(MYS3u3)**3)',
                                      (P.t,P.Xm):'((-3*lamS3u3x3**2*MT**2 - 3*lamS3u3x3**2*MXm**2 + 3*lamS3u3x3**2*MYS3u3**2)*cmath.sqrt(MT**4 - 2*MT**2*MXm**2 + MXm**4 - 2*MT**2*MYS3u3**2 - 2*MXm**2*MYS3u3**2 + MYS3u3**4))/(48.*cmath.pi*abs(MYS3u3)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3d1,P.YF3d1__tilde__):'(((8*ee**2*MYF3d1**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3d1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3d2,P.YF3d2__tilde__):'(((8*ee**2*MYF3d2**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3d2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3d3,P.YF3d3__tilde__):'(((8*ee**2*MYF3d3**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3d3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qd1,P.YF3Qd1__tilde__):'((4*ee**2*MYF3Qd1**2 + 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qd1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qd1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qd1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qd2,P.YF3Qd2__tilde__):'((4*ee**2*MYF3Qd2**2 + 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qd2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qd2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qd2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qd3,P.YF3Qd3__tilde__):'((4*ee**2*MYF3Qd3**2 + 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qd3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qd3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qd3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qu1,P.YF3Qu1__tilde__):'((-4*ee**2*MYF3Qu1**2 - 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qu1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qu1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qu1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qu2,P.YF3Qu2__tilde__):'((-4*ee**2*MYF3Qu2**2 - 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qu2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qu2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qu2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3Qu3,P.YF3Qu3__tilde__):'((-4*ee**2*MYF3Qu3**2 - 2*ee**2*MZ**2 + (6*cw**2*ee**2*MYF3Qu3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/sw**2 + (2*ee**2*MYF3Qu3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3Qu3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3u1,P.YF3u1__tilde__):'(((32*ee**2*MYF3u1**2*sw**2)/(3.*cw**2) + (16*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3u1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3u2,P.YF3u2__tilde__):'(((32*ee**2*MYF3u2**2*sw**2)/(3.*cw**2) + (16*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3u2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YF3u3,P.YF3u3__tilde__):'(((32*ee**2*MYF3u3**2*sw**2)/(3.*cw**2) + (16*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYF3u3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3d1__tilde__,P.YS3d1):'(((-4*ee**2*MYS3d1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3d1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3d2__tilde__,P.YS3d2):'(((-4*ee**2*MYS3d2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3d2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3d3__tilde__,P.YS3d3):'(((-4*ee**2*MYS3d3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3d3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qd1__tilde__,P.YS3Qd1):'((-2*ee**2*MYS3Qd1**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qd1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qd1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qd1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qd2__tilde__,P.YS3Qd2):'((-2*ee**2*MYS3Qd2**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qd2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qd2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qd2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qd3__tilde__,P.YS3Qd3):'((-2*ee**2*MYS3Qd3**2 + (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qd3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qd3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qd3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qu1__tilde__,P.YS3Qu1):'((2*ee**2*MYS3Qu1**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qu1**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qu1**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qu1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qu2__tilde__,P.YS3Qu2):'((2*ee**2*MYS3Qu2**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qu2**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qu2**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qu2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3Qu3__tilde__,P.YS3Qu3):'((2*ee**2*MYS3Qu3**2 - (ee**2*MZ**2)/2. - (3*cw**2*ee**2*MYS3Qu3**2)/sw**2 + (3*cw**2*ee**2*MZ**2)/(4.*sw**2) - (ee**2*MYS3Qu3**2*sw**2)/(3.*cw**2) + (ee**2*MZ**2*sw**2)/(12.*cw**2))*cmath.sqrt(-4*MYS3Qu3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3u1__tilde__,P.YS3u1):'(((-16*ee**2*MYS3u1**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3u1**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3u2__tilde__,P.YS3u2):'(((-16*ee**2*MYS3u2**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3u2**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.YS3u3__tilde__,P.YS3u3):'(((-16*ee**2*MYS3u3**2*sw**2)/(3.*cw**2) + (4*ee**2*MZ**2*sw**2)/(3.*cw**2))*cmath.sqrt(-4*MYS3u3**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

