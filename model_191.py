# exported from PySB model 'model_191'

import numpy as np
from pysb.integrate import Solver
import pylab as pl
import matplotlib.pyplot as plt
from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, ANY, WILD

Model()

Monomer('BAR', ['C8A'])
Monomer('Apop', ['XIAP', 'C3pro'])
Monomer('BaxM', ['BidM', 'BaxA'])
Monomer('C8A', ['BAR', 'BidU', 'C3pro'])
Monomer('XIAP', ['Apop', 'SmacA', 'C3A'])
Monomer('DISC', ['C8pro', 'flip'])
Monomer('SmacM', ['BakA', 'BaxA'])
Monomer('C6pro', ['C3A'])
Monomer('BclxLM', ['BakA', 'BaxA', 'BidM', 'BadM'])
Monomer('SmacA', ['XIAP'])
Monomer('SmacC')
Monomer('PARPU', ['C3A'])
Monomer('C9')
Monomer('C3ub')
Monomer('C8pro', ['DISC', 'C6A'])
Monomer('C6A', ['C8pro'])
Monomer('NoxaM', ['Mcl1M'])
Monomer('L', ['R'])
Monomer('C3pro', ['C8A', 'Apop'])
Monomer('R', ['L'])
Monomer('CytoCM', ['BakA', 'BaxA'])
Monomer('CytoCA', ['ApafI'])
Monomer('CytoCC')
Monomer('BakA', ['BakA_1', 'BakA_2', 'SmacM', 'CytoCM', 'BclxLM', 'Mcl1M', 'BakM'])
Monomer('BaxC')
Monomer('BaxA', ['BaxA_1', 'BaxA_2', 'SmacM', 'CytoCM', 'BclxLM', 'Bcl2', 'BaxM'])
Monomer('Mcl1M', ['BakA', 'BidM', 'NoxaM'])
Monomer('ApafI', ['CytoCA'])
Monomer('Bcl2', ['BaxA', 'BidM', 'BadM'])
Monomer('BidU', ['C8A'])
Monomer('BidT')
Monomer('C3A', ['XIAP', 'PARPU', 'C6pro'])
Monomer('flip', ['DISC'])
Monomer('ApafA')
Monomer('BidM', ['BakM', 'BaxM', 'Mcl1M', 'Bcl2', 'BclxLM'])
Monomer('BakM', ['BidM', 'BakA'])
Monomer('BadM', ['BclxLM', 'Bcl2'])
Monomer('PARPC')
Monomer('BclxLC')

Parameter('BakA_formation_0_2kf', 1.0)
Parameter('BakA_formation_0_1kr', 1.0)
Parameter('BakA_formation_1_2kf', 1.0)
Parameter('BakA_formation_1_1kr', 1.0)
Parameter('BakA_formation_2_2kf', 1.0)
Parameter('BakA_formation_2_1kr', 1.0)
Parameter('BaxA_formation_0_2kf', 1.0)
Parameter('BaxA_formation_0_1kr', 1.0)
Parameter('BaxA_formation_1_2kf', 1.0)
Parameter('BaxA_formation_1_1kr', 1.0)
Parameter('BaxA_formation_2_2kf', 1.0)
Parameter('BaxA_formation_2_1kr', 1.0)
Parameter('ApafA_C9_conversion_Apop_0_2kf', 1.0)
Parameter('ApafA_C9_conversion_Apop_0_1kr', 1.0)
Parameter('XIAP_inhibition_Apop_0_2kf', 1.0)
Parameter('XIAP_inhibition_Apop_0_1kr', 1.0)
Parameter('BAR_inhibition_C8A_0_2kf', 1.0)
Parameter('BAR_inhibition_C8A_0_1kr', 1.0)
Parameter('DISC_C8pro_catalysis_C8A_0_1kc', 1.0)
Parameter('C6A_C8pro_catalysis_C8A_0_1kc', 1.0)
Parameter('DISC_substrate_binding_C8pro_0_2kf', 1.0)
Parameter('DISC_substrate_binding_C8pro_0_1kr', 1.0)
Parameter('C6A_substrate_binding_C8pro_0_2kf', 1.0)
Parameter('C6A_substrate_binding_C8pro_0_1kr', 1.0)
Parameter('L_R_dimerization_DISC_0_1kc', 1.0)
Parameter('flip_inhibition_DISC_0_2kf', 1.0)
Parameter('flip_inhibition_DISC_0_1kr', 1.0)
Parameter('L_dimer_binding_R_0_2kf', 1.0)
Parameter('L_dimer_binding_R_0_1kr', 1.0)
Parameter('CytoCA_ApafI_catalysis_ApafA_0_1kc', 1.0)
Parameter('CytoCA_substrate_binding_ApafI_0_2kf', 1.0)
Parameter('CytoCA_substrate_binding_ApafI_0_1kr', 1.0)
Parameter('BclxLC_equilibration_BclxLM_0_1kf', 1.0)
Parameter('BclxLC_equilibration_BclxLM_0_1kr', 1.0)
Parameter('SmacC_equilibration_SmacA_0_1kf', 1.0)
Parameter('SmacC_equilibration_SmacA_0_1kr', 1.0)
Parameter('XIAP_inhibition_SmacA_0_2kf', 1.0)
Parameter('XIAP_inhibition_SmacA_0_1kr', 1.0)
Parameter('BakA_SmacM_transport_SmacC_0_1kc', 1.0)
Parameter('BaxA_SmacM_transport_SmacC_0_1kc', 1.0)
Parameter('BakA_transport_binding_SmacM_0_2kf', 1.0)
Parameter('BakA_transport_binding_SmacM_0_1kr', 1.0)
Parameter('BaxA_transport_binding_SmacM_0_2kf', 1.0)
Parameter('BaxA_transport_binding_SmacM_0_1kr', 1.0)
Parameter('C3A_XIAP_catalysis_C3ub_0_1kc', 1.0)
Parameter('XIAP_substrate_binding_C3A_0_2kf', 1.0)
Parameter('XIAP_substrate_binding_C3A_0_1kr', 1.0)
Parameter('C3A_PARPU_catalysis_PARPC_0_1kc', 1.0)
Parameter('C3A_substrate_binding_PARPU_0_2kf', 1.0)
Parameter('C3A_substrate_binding_PARPU_0_1kr', 1.0)
Parameter('C3A_C6pro_catalysis_C6A_0_1kc', 1.0)
Parameter('C3A_substrate_binding_C6pro_0_2kf', 1.0)
Parameter('C3A_substrate_binding_C6pro_0_1kr', 1.0)
Parameter('CytoCC_equilibration_CytoCA_0_1kf', 1.0)
Parameter('CytoCC_equilibration_CytoCA_0_1kr', 1.0)
Parameter('BakA_CytoCM_transport_CytoCC_0_1kc', 1.0)
Parameter('BaxA_CytoCM_transport_CytoCC_0_1kc', 1.0)
Parameter('BakA_transport_binding_CytoCM_0_2kf', 1.0)
Parameter('BakA_transport_binding_CytoCM_0_1kr', 1.0)
Parameter('BaxA_transport_binding_CytoCM_0_2kf', 1.0)
Parameter('BaxA_transport_binding_CytoCM_0_1kr', 1.0)
Parameter('BidM_BakM_catalysis_BakA_0_1kc', 1.0)
Parameter('BclxLM_inhibition_BakA_0_2kf', 1.0)
Parameter('BclxLM_inhibition_BakA_0_1kr', 1.0)
Parameter('Mcl1M_inhibition_BakA_0_2kf', 1.0)
Parameter('Mcl1M_inhibition_BakA_0_1kr', 1.0)
Parameter('BidM_substrate_binding_BakM_0_2kf', 1.0)
Parameter('BidM_substrate_binding_BakM_0_1kr', 1.0)
Parameter('BaxM_BidM_catalysis_BaxA_0_1kc', 1.0)
Parameter('BclxLM_inhibition_BaxA_0_2kf', 1.0)
Parameter('BclxLM_inhibition_BaxA_0_1kr', 1.0)
Parameter('Bcl2_inhibition_BaxA_0_2kf', 1.0)
Parameter('Bcl2_inhibition_BaxA_0_1kr', 1.0)
Parameter('BidM_substrate_binding_BaxM_0_2kf', 1.0)
Parameter('BidM_substrate_binding_BaxM_0_1kr', 1.0)
Parameter('C8A_BidU_catalysis_BidT_0_1kc', 1.0)
Parameter('C8A_substrate_binding_BidU_0_2kf', 1.0)
Parameter('C8A_substrate_binding_BidU_0_1kr', 1.0)
Parameter('C8A_C3pro_catalysis_C3A_0_1kc', 1.0)
Parameter('Apop_substrate_binding_C3pro_0_2kf', 1.0)
Parameter('Apop_substrate_binding_C3pro_0_1kr', 1.0)
Parameter('C8A_substrate_binding_C3pro_0_2kf', 1.0)
Parameter('C8A_substrate_binding_C3pro_0_1kr', 1.0)
Parameter('Apop_C3pro_catalysis_C8A_0_1kc', 1.0)
Parameter('BaxA_self_catalyze_BaxM_0_2kf', 1.0)
Parameter('BaxA_self_catalyze_BaxM_0_1kr', 1.0)
Parameter('BaxA_self_catalyze_BaxM_1_1kc', 1.0)
Parameter('BaxC_equilibration_BaxM_0_1kf', 1.0)
Parameter('BaxC_equilibration_BaxM_0_1kr', 1.0)
Parameter('Mcl1M_inhibition_BidM_0_2kf', 1.0)
Parameter('Mcl1M_inhibition_BidM_0_1kr', 1.0)
Parameter('Bcl2_inhibition_BidM_0_2kf', 1.0)
Parameter('Bcl2_inhibition_BidM_0_1kr', 1.0)
Parameter('BclxLM_inhibition_BidM_0_2kf', 1.0)
Parameter('BclxLM_inhibition_BidM_0_1kr', 1.0)
Parameter('BidT_equilibration_BidM_0_1kf', 1.0)
Parameter('BidT_equilibration_BidM_0_1kr', 1.0)
Parameter('BakA_self_catalyze_BakM_0_2kf', 1.0)
Parameter('BakA_self_catalyze_BakM_0_1kr', 1.0)
Parameter('BakA_self_catalyze_BakM_1_1kc', 1.0)
Parameter('BclxLM_inhibition_BadM_0_2kf', 1.0)
Parameter('BclxLM_inhibition_BadM_0_1kr', 1.0)
Parameter('Bcl2_inhibition_BadM_0_2kf', 1.0)
Parameter('Bcl2_inhibition_BadM_0_1kr', 1.0)
Parameter('NoxaM_inhibition_Mcl1M_0_2kf', 1.0)
Parameter('NoxaM_inhibition_Mcl1M_0_1kr', 1.0)
Parameter('BAR_0', 1000.0)
Parameter('Apop_0', 0.0)
Parameter('BaxM_0', 0.0)
Parameter('C8A_0', 0.0)
Parameter('XIAP_0', 100000.0)
Parameter('DISC_0', 0.0)
Parameter('SmacM_0', 100000.0)
Parameter('C6pro_0', 10000.0)
Parameter('BclxLM_0', 0.0)
Parameter('SmacA_0', 0.0)
Parameter('SmacC_0', 0.0)
Parameter('PARPU_0', 1000000.0)
Parameter('C9_0', 100000.0)
Parameter('C3ub_0', 0.0)
Parameter('C8pro_0', 20000.0)
Parameter('C6A_0', 0.0)
Parameter('NoxaM_0', 0.0)
Parameter('L_0', 3000.0)
Parameter('C3pro_0', 10000.0)
Parameter('R_0', 200.0)
Parameter('CytoCM_0', 500000.0)
Parameter('CytoCA_0', 0.0)
Parameter('CytoCC_0', 0.0)
Parameter('BakA_0', 0.0)
Parameter('BaxC_0', 80000.0)
Parameter('BaxA_0', 0.0)
Parameter('Mcl1M_0', 20000.0)
Parameter('ApafI_0', 100000.0)
Parameter('Bcl2_0', 20000.0)
Parameter('BidU_0', 40000.0)
Parameter('BidT_0', 0.0)
Parameter('C3A_0', 0.0)
Parameter('flip_0', 100.0)
Parameter('ApafA_0', 0.0)
Parameter('BidM_0', 0.0)
Parameter('BakM_0', 20000.0)
Parameter('BadM_0', 0.0)
Parameter('PARPC_0', 0.0)
Parameter('BclxLC_0', 20000.0)

Observable('BAR_obs', BAR())
Observable('Apop_obs', Apop())
Observable('BaxM_obs', BaxM())
Observable('C8A_obs', C8A())
Observable('XIAP_obs', XIAP())
Observable('DISC_obs', DISC())
Observable('SmacM_obs', SmacM())
Observable('C6pro_obs', C6pro())
Observable('BclxLM_obs', BclxLM())
Observable('SmacA_obs', SmacA())
Observable('SmacC_obs', SmacC())
Observable('PARPU_obs', PARPU())
Observable('C9_obs', C9())
Observable('C3ub_obs', C3ub())
Observable('C8pro_obs', C8pro())
Observable('C6A_obs', C6A())
Observable('NoxaM_obs', NoxaM())
Observable('L_obs', L())
Observable('C3pro_obs', C3pro())
Observable('R_obs', R())
Observable('CytoCM_obs', CytoCM())
Observable('CytoCA_obs', CytoCA())
Observable('CytoCC_obs', CytoCC())
Observable('BakA_obs', BakA())
Observable('BaxC_obs', BaxC())
Observable('BaxA_obs', BaxA())
Observable('Mcl1M_obs', Mcl1M())
Observable('ApafI_obs', ApafI())
Observable('Bcl2_obs', Bcl2())
Observable('BidU_obs', BidU())
Observable('BidT_obs', BidT())
Observable('C3A_obs', C3A())
Observable('flip_obs', flip())
Observable('ApafA_obs', ApafA())
Observable('BidM_obs', BidM())
Observable('BakM_obs', BakM())
Observable('BadM_obs', BadM())
Observable('PARPC_obs', PARPC())
Observable('BclxLC_obs', BclxLC())

Rule('BakA_formation_0', BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) <> BakA(BakA_1=None, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BakA_formation_0_2kf, BakA_formation_0_1kr)
Rule('BakA_formation_1', BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + BakA(BakA_1=None, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) <> BakA(BakA_1=3, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BakA_formation_1_2kf, BakA_formation_1_1kr)
Rule('BakA_formation_2', BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + BakA(BakA_1=3, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) <> BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BakA_formation_2_2kf, BakA_formation_2_1kr)
Rule('BaxA_formation_0', BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) <> BaxA(BaxA_1=None, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxA_formation_0_2kf, BaxA_formation_0_1kr)
Rule('BaxA_formation_1', BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + BaxA(BaxA_1=None, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) <> BaxA(BaxA_1=3, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxA_formation_1_2kf, BaxA_formation_1_1kr)
Rule('BaxA_formation_2', BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + BaxA(BaxA_1=3, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) <> BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxA_formation_2_2kf, BaxA_formation_2_1kr)
Rule('ApafA_C9_conversion_Apop_0', ApafA() + C9() <> Apop(XIAP=None, C3pro=None), ApafA_C9_conversion_Apop_0_2kf, ApafA_C9_conversion_Apop_0_1kr)
Rule('XIAP_inhibition_Apop_0', XIAP(Apop=None, SmacA=None, C3A=None) + Apop(XIAP=None, C3pro=None) <> XIAP(Apop=1, SmacA=None, C3A=None) % Apop(XIAP=1, C3pro=None), XIAP_inhibition_Apop_0_2kf, XIAP_inhibition_Apop_0_1kr)
Rule('BAR_inhibition_C8A_0', BAR(C8A=None) + C8A(BAR=None, BidU=None, C3pro=None) <> BAR(C8A=1) % C8A(BAR=1, BidU=None, C3pro=None), BAR_inhibition_C8A_0_2kf, BAR_inhibition_C8A_0_1kr)
Rule('DISC_C8pro_catalysis_C8A_0', DISC(C8pro=1, flip=None) % C8pro(DISC=1, C6A=None) >> DISC(C8pro=None, flip=None) + C8A(BAR=None, BidU=None, C3pro=None), DISC_C8pro_catalysis_C8A_0_1kc)
Rule('C6A_C8pro_catalysis_C8A_0', C6A(C8pro=1) % C8pro(DISC=None, C6A=1) >> C6A(C8pro=None) + C8A(BAR=None, BidU=None, C3pro=None), C6A_C8pro_catalysis_C8A_0_1kc)
Rule('DISC_substrate_binding_C8pro_0', DISC(C8pro=None, flip=None) + C8pro(DISC=None, C6A=None) <> DISC(C8pro=1, flip=None) % C8pro(DISC=1, C6A=None), DISC_substrate_binding_C8pro_0_2kf, DISC_substrate_binding_C8pro_0_1kr)
Rule('C6A_substrate_binding_C8pro_0', C6A(C8pro=None) + C8pro(DISC=None, C6A=None) <> C6A(C8pro=1) % C8pro(DISC=None, C6A=1), C6A_substrate_binding_C8pro_0_2kf, C6A_substrate_binding_C8pro_0_1kr)
Rule('L_R_dimerization_DISC_0', L(R=1) % R(L=1) >> DISC(C8pro=None, flip=None), L_R_dimerization_DISC_0_1kc)
Rule('flip_inhibition_DISC_0', flip(DISC=None) + DISC(C8pro=None, flip=None) <> flip(DISC=1) % DISC(C8pro=None, flip=1), flip_inhibition_DISC_0_2kf, flip_inhibition_DISC_0_1kr)
Rule('L_dimer_binding_R_0', L(R=None) + R(L=None) <> L(R=1) % R(L=1), L_dimer_binding_R_0_2kf, L_dimer_binding_R_0_1kr)
Rule('CytoCA_ApafI_catalysis_ApafA_0', CytoCA(ApafI=1) % ApafI(CytoCA=1) >> CytoCA(ApafI=None) + ApafA(), CytoCA_ApafI_catalysis_ApafA_0_1kc)
Rule('CytoCA_substrate_binding_ApafI_0', CytoCA(ApafI=None) + ApafI(CytoCA=None) <> CytoCA(ApafI=1) % ApafI(CytoCA=1), CytoCA_substrate_binding_ApafI_0_2kf, CytoCA_substrate_binding_ApafI_0_1kr)
Rule('BclxLC_equilibration_BclxLM_0', BclxLC() <> BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None), BclxLC_equilibration_BclxLM_0_1kf, BclxLC_equilibration_BclxLM_0_1kr)
Rule('SmacC_equilibration_SmacA_0', SmacC() <> SmacA(XIAP=None), SmacC_equilibration_SmacA_0_1kf, SmacC_equilibration_SmacA_0_1kr)
Rule('XIAP_inhibition_SmacA_0', XIAP(Apop=None, SmacA=None, C3A=None) + SmacA(XIAP=None) <> XIAP(Apop=None, SmacA=1, C3A=None) % SmacA(XIAP=1), XIAP_inhibition_SmacA_0_2kf, XIAP_inhibition_SmacA_0_1kr)
Rule('BakA_SmacM_transport_SmacC_0', BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=5, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % SmacM(BakA=5, BaxA=None) >> BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + SmacC(), BakA_SmacM_transport_SmacC_0_1kc)
Rule('BaxA_SmacM_transport_SmacC_0', BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=5, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % SmacM(BakA=None, BaxA=5) >> BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + SmacC(), BaxA_SmacM_transport_SmacC_0_1kc)
Rule('BakA_transport_binding_SmacM_0', BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + SmacM(BakA=None, BaxA=None) <> BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=5, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % SmacM(BakA=5, BaxA=None), BakA_transport_binding_SmacM_0_2kf, BakA_transport_binding_SmacM_0_1kr)
Rule('BaxA_transport_binding_SmacM_0', BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + SmacM(BakA=None, BaxA=None) <> BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=5, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % SmacM(BakA=None, BaxA=5), BaxA_transport_binding_SmacM_0_2kf, BaxA_transport_binding_SmacM_0_1kr)
Rule('C3A_XIAP_catalysis_C3ub_0', XIAP(Apop=None, SmacA=None, C3A=1) % C3A(XIAP=1, PARPU=None, C6pro=None) >> XIAP(Apop=None, SmacA=None, C3A=None) + C3ub(), C3A_XIAP_catalysis_C3ub_0_1kc)
Rule('XIAP_substrate_binding_C3A_0', XIAP(Apop=None, SmacA=None, C3A=None) + C3A(XIAP=None, PARPU=None, C6pro=None) <> XIAP(Apop=None, SmacA=None, C3A=1) % C3A(XIAP=1, PARPU=None, C6pro=None), XIAP_substrate_binding_C3A_0_2kf, XIAP_substrate_binding_C3A_0_1kr)
Rule('C3A_PARPU_catalysis_PARPC_0', C3A(XIAP=None, PARPU=1, C6pro=None) % PARPU(C3A=1) >> C3A(XIAP=None, PARPU=None, C6pro=None) + PARPC(), C3A_PARPU_catalysis_PARPC_0_1kc)
Rule('C3A_substrate_binding_PARPU_0', C3A(XIAP=None, PARPU=None, C6pro=None) + PARPU(C3A=None) <> C3A(XIAP=None, PARPU=1, C6pro=None) % PARPU(C3A=1), C3A_substrate_binding_PARPU_0_2kf, C3A_substrate_binding_PARPU_0_1kr)
Rule('C3A_C6pro_catalysis_C6A_0', C3A(XIAP=None, PARPU=None, C6pro=1) % C6pro(C3A=1) >> C3A(XIAP=None, PARPU=None, C6pro=None) + C6A(C8pro=None), C3A_C6pro_catalysis_C6A_0_1kc)
Rule('C3A_substrate_binding_C6pro_0', C3A(XIAP=None, PARPU=None, C6pro=None) + C6pro(C3A=None) <> C3A(XIAP=None, PARPU=None, C6pro=1) % C6pro(C3A=1), C3A_substrate_binding_C6pro_0_2kf, C3A_substrate_binding_C6pro_0_1kr)
Rule('CytoCC_equilibration_CytoCA_0', CytoCC() <> CytoCA(ApafI=None), CytoCC_equilibration_CytoCA_0_1kf, CytoCC_equilibration_CytoCA_0_1kr)
Rule('BakA_CytoCM_transport_CytoCC_0', BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=5, BclxLM=None, Mcl1M=None, BakM=None) % CytoCM(BakA=5, BaxA=None) >> BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + CytoCC(), BakA_CytoCM_transport_CytoCC_0_1kc)
Rule('BaxA_CytoCM_transport_CytoCC_0', BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=5, BclxLM=None, Bcl2=None, BaxM=None) % CytoCM(BakA=None, BaxA=5) >> BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + CytoCC(), BaxA_CytoCM_transport_CytoCC_0_1kc)
Rule('BakA_transport_binding_CytoCM_0', BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + CytoCM(BakA=None, BaxA=None) <> BakA(BakA_1=4, BakA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=1, BakA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=2, BakA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) % BakA(BakA_1=3, BakA_2=4, SmacM=None, CytoCM=5, BclxLM=None, Mcl1M=None, BakM=None) % CytoCM(BakA=5, BaxA=None), BakA_transport_binding_CytoCM_0_2kf, BakA_transport_binding_CytoCM_0_1kr)
Rule('BaxA_transport_binding_CytoCM_0', BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + CytoCM(BakA=None, BaxA=None) <> BaxA(BaxA_1=4, BaxA_2=1, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=1, BaxA_2=2, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=2, BaxA_2=3, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) % BaxA(BaxA_1=3, BaxA_2=4, SmacM=None, CytoCM=5, BclxLM=None, Bcl2=None, BaxM=None) % CytoCM(BakA=None, BaxA=5), BaxA_transport_binding_CytoCM_0_2kf, BaxA_transport_binding_CytoCM_0_1kr)
Rule('BidM_BakM_catalysis_BakA_0', BidM(BakM=1, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) % BakM(BidM=1, BakA=None) >> BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) + BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BidM_BakM_catalysis_BakA_0_1kc)
Rule('BclxLM_inhibition_BakA_0', BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None) + BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) <> BclxLM(BakA=1, BaxA=None, BidM=None, BadM=None) % BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=1, Mcl1M=None, BakM=None), BclxLM_inhibition_BakA_0_2kf, BclxLM_inhibition_BakA_0_1kr)
Rule('Mcl1M_inhibition_BakA_0', Mcl1M(BakA=None, BidM=None, NoxaM=None) + BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) <> Mcl1M(BakA=1, BidM=None, NoxaM=None) % BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=1, BakM=None), Mcl1M_inhibition_BakA_0_2kf, Mcl1M_inhibition_BakA_0_1kr)
Rule('BidM_substrate_binding_BakM_0', BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) + BakM(BidM=None, BakA=None) <> BidM(BakM=1, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) % BakM(BidM=1, BakA=None), BidM_substrate_binding_BakM_0_2kf, BidM_substrate_binding_BakM_0_1kr)
Rule('BaxM_BidM_catalysis_BaxA_0', BidM(BakM=None, BaxM=1, Mcl1M=None, Bcl2=None, BclxLM=None) % BaxM(BidM=1, BaxA=None) >> BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) + BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxM_BidM_catalysis_BaxA_0_1kc)
Rule('BclxLM_inhibition_BaxA_0', BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None) + BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) <> BclxLM(BakA=None, BaxA=1, BidM=None, BadM=None) % BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=1, Bcl2=None, BaxM=None), BclxLM_inhibition_BaxA_0_2kf, BclxLM_inhibition_BaxA_0_1kr)
Rule('Bcl2_inhibition_BaxA_0', Bcl2(BaxA=None, BidM=None, BadM=None) + BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) <> Bcl2(BaxA=1, BidM=None, BadM=None) % BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=1, BaxM=None), Bcl2_inhibition_BaxA_0_2kf, Bcl2_inhibition_BaxA_0_1kr)
Rule('BidM_substrate_binding_BaxM_0', BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) + BaxM(BidM=None, BaxA=None) <> BidM(BakM=None, BaxM=1, Mcl1M=None, Bcl2=None, BclxLM=None) % BaxM(BidM=1, BaxA=None), BidM_substrate_binding_BaxM_0_2kf, BidM_substrate_binding_BaxM_0_1kr)
Rule('C8A_BidU_catalysis_BidT_0', C8A(BAR=None, BidU=1, C3pro=None) % BidU(C8A=1) >> C8A(BAR=None, BidU=None, C3pro=None) + BidT(), C8A_BidU_catalysis_BidT_0_1kc)
Rule('C8A_substrate_binding_BidU_0', C8A(BAR=None, BidU=None, C3pro=None) + BidU(C8A=None) <> C8A(BAR=None, BidU=1, C3pro=None) % BidU(C8A=1), C8A_substrate_binding_BidU_0_2kf, C8A_substrate_binding_BidU_0_1kr)
Rule('C8A_C3pro_catalysis_C3A_0', C8A(BAR=None, BidU=None, C3pro=1) % C3pro(C8A=1, Apop=None) >> C8A(BAR=None, BidU=None, C3pro=None) + C3A(XIAP=None, PARPU=None, C6pro=None), C8A_C3pro_catalysis_C3A_0_1kc)
Rule('Apop_substrate_binding_C3pro_0', Apop(XIAP=None, C3pro=None) + C3pro(C8A=None, Apop=None) <> Apop(XIAP=None, C3pro=1) % C3pro(C8A=None, Apop=1), Apop_substrate_binding_C3pro_0_2kf, Apop_substrate_binding_C3pro_0_1kr)
Rule('C8A_substrate_binding_C3pro_0', C8A(BAR=None, BidU=None, C3pro=None) + C3pro(C8A=None, Apop=None) <> C8A(BAR=None, BidU=None, C3pro=1) % C3pro(C8A=1, Apop=None), C8A_substrate_binding_C3pro_0_2kf, C8A_substrate_binding_C3pro_0_1kr)
Rule('Apop_C3pro_catalysis_C8A_0', Apop(XIAP=None, C3pro=1) % C3pro(C8A=None, Apop=1) >> Apop(XIAP=None, C3pro=None) + C8A(BAR=None, BidU=None, C3pro=None), Apop_C3pro_catalysis_C8A_0_1kc)
Rule('BaxA_self_catalyze_BaxM_0', BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + BaxM(BidM=None, BaxA=None) <> BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=1) % BaxM(BidM=None, BaxA=1), BaxA_self_catalyze_BaxM_0_2kf, BaxA_self_catalyze_BaxM_0_1kr)
Rule('BaxA_self_catalyze_BaxM_1', BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=1) % BaxM(BidM=None, BaxA=1) >> BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None) + BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxA_self_catalyze_BaxM_1_1kc)
Rule('BaxC_equilibration_BaxM_0', BaxC() <> BaxM(BidM=None, BaxA=None), BaxC_equilibration_BaxM_0_1kf, BaxC_equilibration_BaxM_0_1kr)
Rule('Mcl1M_inhibition_BidM_0', Mcl1M(BakA=None, BidM=None, NoxaM=None) + BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) <> Mcl1M(BakA=None, BidM=1, NoxaM=None) % BidM(BakM=None, BaxM=None, Mcl1M=1, Bcl2=None, BclxLM=None), Mcl1M_inhibition_BidM_0_2kf, Mcl1M_inhibition_BidM_0_1kr)
Rule('Bcl2_inhibition_BidM_0', Bcl2(BaxA=None, BidM=None, BadM=None) + BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) <> Bcl2(BaxA=None, BidM=1, BadM=None) % BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=1, BclxLM=None), Bcl2_inhibition_BidM_0_2kf, Bcl2_inhibition_BidM_0_1kr)
Rule('BclxLM_inhibition_BidM_0', BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None) + BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None) <> BclxLM(BakA=None, BaxA=None, BidM=1, BadM=None) % BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=1), BclxLM_inhibition_BidM_0_2kf, BclxLM_inhibition_BidM_0_1kr)
Rule('BidT_equilibration_BidM_0', BidT() <> BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None), BidT_equilibration_BidM_0_1kf, BidT_equilibration_BidM_0_1kr)
Rule('BakA_self_catalyze_BakM_0', BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + BakM(BidM=None, BakA=None) <> BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=1) % BakM(BidM=None, BakA=1), BakA_self_catalyze_BakM_0_2kf, BakA_self_catalyze_BakM_0_1kr)
Rule('BakA_self_catalyze_BakM_1', BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=1) % BakM(BidM=None, BakA=1) >> BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None) + BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BakA_self_catalyze_BakM_1_1kc)
Rule('BclxLM_inhibition_BadM_0', BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None) + BadM(BclxLM=None, Bcl2=None) <> BclxLM(BakA=None, BaxA=None, BidM=None, BadM=1) % BadM(BclxLM=1, Bcl2=None), BclxLM_inhibition_BadM_0_2kf, BclxLM_inhibition_BadM_0_1kr)
Rule('Bcl2_inhibition_BadM_0', Bcl2(BaxA=None, BidM=None, BadM=None) + BadM(BclxLM=None, Bcl2=None) <> Bcl2(BaxA=None, BidM=None, BadM=1) % BadM(BclxLM=None, Bcl2=1), Bcl2_inhibition_BadM_0_2kf, Bcl2_inhibition_BadM_0_1kr)
Rule('NoxaM_inhibition_Mcl1M_0', NoxaM(Mcl1M=None) + Mcl1M(BakA=None, BidM=None, NoxaM=None) <> NoxaM(Mcl1M=1) % Mcl1M(BakA=None, BidM=None, NoxaM=1), NoxaM_inhibition_Mcl1M_0_2kf, NoxaM_inhibition_Mcl1M_0_1kr)

Initial(BAR(C8A=None), BAR_0)
Initial(Apop(XIAP=None, C3pro=None), Apop_0)
Initial(BaxM(BidM=None, BaxA=None), BaxM_0)
Initial(C8A(BAR=None, BidU=None, C3pro=None), C8A_0)
Initial(XIAP(Apop=None, SmacA=None, C3A=None), XIAP_0)
Initial(DISC(C8pro=None, flip=None), DISC_0)
Initial(SmacM(BakA=None, BaxA=None), SmacM_0)
Initial(C6pro(C3A=None), C6pro_0)
Initial(BclxLM(BakA=None, BaxA=None, BidM=None, BadM=None), BclxLM_0)
Initial(SmacA(XIAP=None), SmacA_0)
Initial(SmacC(), SmacC_0)
Initial(PARPU(C3A=None), PARPU_0)
Initial(C9(), C9_0)
Initial(C3ub(), C3ub_0)
Initial(C8pro(DISC=None, C6A=None), C8pro_0)
Initial(C6A(C8pro=None), C6A_0)
Initial(NoxaM(Mcl1M=None), NoxaM_0)
Initial(L(R=None), L_0)
Initial(C3pro(C8A=None, Apop=None), C3pro_0)
Initial(R(L=None), R_0)
Initial(CytoCM(BakA=None, BaxA=None), CytoCM_0)
Initial(CytoCA(ApafI=None), CytoCA_0)
Initial(CytoCC(), CytoCC_0)
Initial(BakA(BakA_1=None, BakA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Mcl1M=None, BakM=None), BakA_0)
Initial(BaxC(), BaxC_0)
Initial(BaxA(BaxA_1=None, BaxA_2=None, SmacM=None, CytoCM=None, BclxLM=None, Bcl2=None, BaxM=None), BaxA_0)
Initial(Mcl1M(BakA=None, BidM=None, NoxaM=None), Mcl1M_0)
Initial(ApafI(CytoCA=None), ApafI_0)
Initial(Bcl2(BaxA=None, BidM=None, BadM=None), Bcl2_0)
Initial(BidU(C8A=None), BidU_0)
Initial(BidT(), BidT_0)
Initial(C3A(XIAP=None, PARPU=None, C6pro=None), C3A_0)
Initial(flip(DISC=None), flip_0)
Initial(ApafA(), ApafA_0)
Initial(BidM(BakM=None, BaxM=None, Mcl1M=None, Bcl2=None, BclxLM=None), BidM_0)
Initial(BakM(BidM=None, BakA=None), BakM_0)
Initial(BadM(BclxLM=None, Bcl2=None), BadM_0)
Initial(PARPC(), PARPC_0)
Initial(BclxLC(), BclxLC_0)

