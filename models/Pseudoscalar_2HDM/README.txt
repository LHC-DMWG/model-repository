+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++  README v1 +++++++++++++++++++++++++++++++ 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This UFO file contains an implementation of the Two Higgs Doublet Model (THDM) plus pseudoscalar extension described in arXiv:1701.07427.
The implemented Yukawa sector is of type II. The UFO implementation can be used with MadGraph5_aMC@NLO available at https://launchpad.net/mg5amcnlo.

The additional parameters in the param_card.dat are:

gPXd = The coupling of the additional pseudoscalar mediator to dark matter (DM). This coupling is called $y_\chi$ in (2.5) of arXiv:1701.07427.

tanbeta	= The ratio of the vacuum expectation values $\tan \beta = v_2/v_1$ of the Higgs doublets $H_2$ and $H_1$, as defined in Section 2.1 of
	  arXiv:1701.07427.

sinbma = The sine of the difference of the mixing angles $\sin (\beta - \alpha)$ in the scalar potential containing only the Higgs doublets.
         This quantity is defined in Section 3.1 of arXiv:1701.07427. 

lam3 = The quartic coupling of the scalar doublets $H_1$ and $H_2$. This parameter corresponds to the coefficient $\lambda_3$ in (2.1) of
       arXiv:1701.07427.

lamP1 =	The quartic coupling between the scalar doublets $H_1$ and the pseudoscalar $P$. This parameter corresponds to the coefficient
        $\lambda_{P1}$ in (2.2) of arXiv:1701.07427.

lamP2 =	The quartic coupling between the scalar doublets $H_2$ and the pseudoscalar $P$. This parameter corresponds to the coefficient
        $\lambda_{P2}$ in (2.2) of arXiv:1701.07427.

sinp = The sine of the mixing angle $\theta$, as defined in Section 2.1 of arXiv:1701.07427.

Mxd = The mass of the fermionic DM candidate denoted by $m_\chi$ in arXiv:1701.07427.

mh1 = The mass of the lightest scalar mass eigenstate $h$, which is identified in arXiv:1701.07427 with the Higgs-like resonance found
      at the LHC.

mh2 = The mass of the heavy scalar mass eigenstate $H$. See Section 2.1 of arXiv:1701.07427 for further details.

mh3 = The mass of the heavy pseudoscalar mass eigenstate $A$. See Section 2.1 of arXiv:1701.07427 for further details.

mhc = The mass of the charged scalar eigenstate $H^\pm$. See Section 2.1 of arXiv:1701.07427 for further details.

mh4 = The mass of the pseudoscalar mass eigenstate $a$ that decouples for $\sin \theta = 0$. See Section 2.1 of arXiv:1701.07427 for
      further details.

Wh1 = The total width of the mass eigenstate $h$. If set to Auto the total and partial decay widths are calculated by MadGraph. 

Wh2 = The total width of the mass eigenstate $H$. If set to Auto the total and partial decay widths are calculated by MadGraph. 

Wh3 = The total width of the mass eigenstate $A$. If set to Auto the total and partial decay widths are calculated by MadGraph. 

Whc = The total width of the mass eigenstate $H^\pm$. If set to Auto the total and partial decay widths are calculated by MadGraph. 

Wh4 = The total width of the mass eigenstate $a$. If set to Auto the total and partial decay widths are calculated by MadGraph.

In case of questions etc. please write to one of the authors of arXiv:1701.07427:

bauer@thphys.uni-heidelberg.de
ulrich.haisch@physics.ox.ac.uk
felix.kahlhoefer@desy.de

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++  README v2 +++++++++++++++++++++++++++++++  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Below we give the MadGraph syntax used to generate various mono-X signals using version 2
of the Pseudoscalar_2HDM UFO. 

To generate mono-jet events one uses the following commands:

import model Pseudoscalar_2HDM

generate p p > j xd xd~ [QCD]

The result is leading order (LO) accurate and involves contribution from both top and bottom 
loops. Both the top and bottom quarks are massive and the corresponding Yukawa couplings 
are non-zero. The calculation is thus performed in a four flavour scheme (4FS).

Using 

generate p p > t t~ xd xd~ [QCD]

generates a ttbar plus missing energy (MET) signal. Next-to-leading order (NLO) corrections are 
included via [QCD] and the 4FS is employed. 

Likewise

generate p p > b b~ xd xd~ [QCD]

produces bbbar plus MET events with NLO accuracy. Again the 4FS is used meaning that 
contributions from initial-state bottom quarks are not present. 

The UFO is however also able to simulate processes in the five flavour scheme (5FS). 
For instance the relevant commands to produce a bbbar plus MET signal at NLO are 

import model Pseudoscalar_2HDM-bbMET_5FS 

generate p p > j j xd xd~ [QCD]

In this case only the top quark is massive while the bottom quark is massless and thus 
can appear as a parton in the colliding protons. Both the top and bottom Yukawa coupling 
are however non-zero. 

To generate a mono-W signal arising from the exchange of a charged Higgs one also has 
to include non-zero light Yukawa couplings. The appropriate commands are 

import model Pseudoscalar_2HDM-WMET

generate p p > w+ xd xd~ [QCD]

In such a case only the top quark is massive while all the other quarks are treated as massless.
All Yukawa couplings are however non-zero. The calculation can again be performed at NLO. 

To calculate the relic density one should use 

import model Pseudoscalar_2HDM-relic

In this case all fermion masses and Yukawa couplings are non-zero.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++  KNOWN ISSUES ++++++++++++++++++++++++++++++ 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

There is one known issue with the UFO. As explained in 

https://answers.launchpad.net/mg5amcnlo/+question/657910

in the case of bbbar plus MET production in the 5FS, MadGraph can stop because some
collinear tests fail.

To circumvent this problem the parameter

max_fail

as declared and defined in line 21 and 22 of the file

test_soft_col_limits.f

(or symmetry_fks_test_ME.f in older MadGraph versions) in the directory

SubProcesses

should be increased from 0.3 to a value of around 0.5.

Further details on the above issue can be found in

https://answers.launchpad.net/mg5amcnlo/+question/657910

In case of questions conerning version 2 of the UFO please write to

ulrich.haisch@physics.ox.ac.uk










