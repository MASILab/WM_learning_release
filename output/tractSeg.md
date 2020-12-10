### The output of tractSeg singularity

In the $HOME/OUTPUTS folder, you will find four sub folders **anat**,**orig**,**affine**,**reg**.

- **anat** includes four files: 
  - T1_linear.nii.gz
  - T1_mask_mask.nii.gz
  - T1_mask.nii.gz
  - T1_max.nii.gz . 
  
The **T1_linear** represents the image after affine registration. **T1_mask_mask** represents binary mask of **T1_mask**. **T1_mask** represents the brain tissued extracted from **T1_linear**. **T1_max** represents input feeded into deep neural network after normalization

- **reg** includes three files:
  - ANTS0GenericAffine.mat 
  - ANTSInverseWarped.nii.gz
  - ANTSWarped.nii.gz  
  
The **ANTSGenericAffine.mat** includes affine transformation obtained from ANTS package. The **ANTSWarped.nii.gz** represents the output after affine transformation.**ANTSInverseWarped.nii.gz** represents affined out is inversed transformed to original space.

**affine** represents output pathways are on in affine MNI template (T1_linear) space.

**orig** represents output pathways are on original T1 space.

The specific output files please check following part:
./affine
├── AF_left.nii.gz
├── AF_right.nii.gz
├── ATR_left.nii.gz
├── ATR_right.nii.gz
├── CA.nii.gz
├── CC_1.nii.gz
├── CC_2.nii.gz
├── CC_3.nii.gz
├── CC_4.nii.gz
├── CC_5.nii.gz
├── CC_6.nii.gz
├── CC_7.nii.gz
├── CC.nii.gz
├── CG_left.nii.gz
├── CG_right.nii.gz
├── CST_left.nii.gz
├── CST_right.nii.gz
├── FPT_left.nii.gz
├── FPT_right.nii.gz
├── FX_left.nii.gz
├── FX_right.nii.gz
├── ICP_left.nii.gz
├── ICP_right.nii.gz
├── IFO_left.nii.gz
├── IFO_right.nii.gz
├── ILF_left.nii.gz
├── ILF_right.nii.gz
├── MCP.nii.gz
├── MLF_left.nii.gz
├── MLF_right.nii.gz
├── OR_left.nii.gz
├── OR_right.nii.gz
├── POPT_left.nii.gz
├── POPT_right.nii.gz
├── SCP_left.nii.gz
├── SCP_right.nii.gz
├── SLF_III_left.nii.gz
├── SLF_III_right.nii.gz
├── SLF_II_left.nii.gz
├── SLF_II_right.nii.gz
├── SLF_I_left.nii.gz
├── SLF_I_right.nii.gz
├── ST_FO_left.nii.gz
├── ST_FO_right.nii.gz
├── ST_OCC_left.nii.gz
├── ST_OCC_right.nii.gz
├── ST_PAR_left.nii.gz
├── ST_PAR_right.nii.gz
├── ST_POSTC_left.nii.gz
├── ST_POSTC_right.nii.gz
├── ST_PREC_left.nii.gz
├── ST_PREC_right.nii.gz
├── ST_PREF_left.nii.gz
├── ST_PREF_right.nii.gz
├── ST_PREM_left.nii.gz
├── ST_PREM_right.nii.gz
├── STR_left.nii.gz
├── STR_right.nii.gz
├── T_OCC_left.nii.gz
├── T_OCC_right.nii.gz
├── T_PAR_left.nii.gz
├── T_PAR_right.nii.gz
├── T_POSTC_left.nii.gz
├── T_POSTC_right.nii.gz
├── T_PREC_left.nii.gz
├── T_PREC_right.nii.gz
├── T_PREF_left.nii.gz
├── T_PREF_right.nii.gz
├── T_PREM_left.nii.gz
├── T_PREM_right.nii.gz
├── UF_left.nii.gz
└── UF_right.nii.gz
./anat
├── T1_linear.nii.gz
├── T1_mask_mask.nii.gz
├── T1_mask.nii.gz
└── T1_max.nii.gz
./orig
├── AF_left.nii.gz
├── AF_right.nii.gz
├── ATR_left.nii.gz
├── ATR_right.nii.gz
├── CA.nii.gz
├── CC_1.nii.gz
├── CC_2.nii.gz
├── CC_3.nii.gz
├── CC_4.nii.gz
├── CC_5.nii.gz
├── CC_6.nii.gz
├── CC_7.nii.gz
├── CC.nii.gz
├── CG_left.nii.gz
├── CG_right.nii.gz
├── CST_left.nii.gz
├── CST_right.nii.gz
├── FPT_left.nii.gz
├── FPT_right.nii.gz
├── FX_left.nii.gz
├── FX_right.nii.gz
├── ICP_left.nii.gz
├── ICP_right.nii.gz
├── IFO_left.nii.gz
├── IFO_right.nii.gz
├── ILF_left.nii.gz
├── ILF_right.nii.gz
├── MCP.nii.gz
├── MLF_left.nii.gz
├── MLF_right.nii.gz
├── OR_left.nii.gz
├── OR_right.nii.gz
├── POPT_left.nii.gz
├── POPT_right.nii.gz
├── SCP_left.nii.gz
├── SCP_right.nii.gz
├── SLF_III_left.nii.gz
├── SLF_III_right.nii.gz
├── SLF_II_left.nii.gz
├── SLF_II_right.nii.gz
├── SLF_I_left.nii.gz
├── SLF_I_right.nii.gz
├── ST_FO_left.nii.gz
├── ST_FO_right.nii.gz
├── ST_OCC_left.nii.gz
├── ST_OCC_right.nii.gz
├── ST_PAR_left.nii.gz
├── ST_PAR_right.nii.gz
├── ST_POSTC_left.nii.gz
├── ST_POSTC_right.nii.gz
├── ST_PREC_left.nii.gz
├── ST_PREC_right.nii.gz
├── ST_PREF_left.nii.gz
├── ST_PREF_right.nii.gz
├── ST_PREM_left.nii.gz
├── ST_PREM_right.nii.gz
├── STR_left.nii.gz
├── STR_right.nii.gz
├── T_OCC_left.nii.gz
├── T_OCC_right.nii.gz
├── T_PAR_left.nii.gz
├── T_PAR_right.nii.gz
├── T_POSTC_left.nii.gz
├── T_POSTC_right.nii.gz
├── T_PREC_left.nii.gz
├── T_PREC_right.nii.gz
├── T_PREF_left.nii.gz
├── T_PREF_right.nii.gz
├── T_PREM_left.nii.gz
├── T_PREM_right.nii.gz
├── UF_left.nii.gz
└── UF_right.nii.gz
./reg
├── ANTS0GenericAffine.mat
├── ANTSInverseWarped.nii.gz
└── ANTSWarped.nii.gz
  