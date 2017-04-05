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

