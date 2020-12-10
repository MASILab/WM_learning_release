### The output of xtract singularity

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
├── ac.nii.gz
├── af_l.nii.gz
├── af_r.nii.gz
├── ar_l.nii.gz
├── ar_r.nii.gz
├── atr_l.nii.gz
├── atr_r.nii.gz
├── cbd_l.nii.gz
├── cbd_r.nii.gz
├── cbp_l.nii.gz
├── cbp_r.nii.gz
├── cbt_l.nii.gz
├── cbt_r.nii.gz
├── cst_l.nii.gz
├── cst_r.nii.gz
├── fa_l.nii.gz
├── fa_r.nii.gz
├── fma.nii.gz
├── fm.nii.gz
├── fo_l.nii.gz
├── fo_r.nii.gz
├── fx_l.nii.gz
├── fx_r.nii.gz
├── lf_l.nii.gz
├── lf_r.nii.gz
├── mcp.nii.gz
├── mdlf_l.nii.gz
├── mdlf_r.nii.gz
├── or_l.nii.gz
├── or_r.nii.gz
├── slf1_l.nii.gz
├── slf1_r.nii.gz
├── slf2_l.nii.gz
├── slf2_r.nii.gz
├── slf3_l.nii.gz
├── slf3_r.nii.gz
├── str_l.nii.gz
├── str_r.nii.gz
├── uf_l.nii.gz
├── uf_r.nii.gz
├── vof_l.nii.gz
└── vof_r.nii.gz
./anat
├── T1_linear.nii.gz
├── T1_mask_mask.nii.gz
├── T1_mask.nii.gz
└── T1_max.nii.gz
./orig
├── ac.nii.gz
├── af_l.nii.gz
├── af_r.nii.gz
├── ar_l.nii.gz
├── ar_r.nii.gz
├── atr_l.nii.gz
├── atr_r.nii.gz
├── cbd_l.nii.gz
├── cbd_r.nii.gz
├── cbp_l.nii.gz
├── cbp_r.nii.gz
├── cbt_l.nii.gz
├── cbt_r.nii.gz
├── cst_l.nii.gz
├── cst_r.nii.gz
├── fa_l.nii.gz
├── fa_r.nii.gz
├── fma.nii.gz
├── fm.nii.gz
├── fo_l.nii.gz
├── fo_r.nii.gz
├── fx_l.nii.gz
├── fx_r.nii.gz
├── lf_l.nii.gz
├── lf_r.nii.gz
├── mcp.nii.gz
├── mdlf_l.nii.gz
├── mdlf_r.nii.gz
├── or_l.nii.gz
├── or_r.nii.gz
├── slf1_l.nii.gz
├── slf1_r.nii.gz
├── slf2_l.nii.gz
├── slf2_r.nii.gz
├── slf3_l.nii.gz
├── slf3_r.nii.gz
├── str_l.nii.gz
├── str_r.nii.gz
├── uf_l.nii.gz
├── uf_r.nii.gz
├── vof_l.nii.gz
└── vof_r.nii.gz
./reg
├── ANTS0GenericAffine.mat
├── ANTSInverseWarped.nii.gz
└── ANTSWarped.nii.gz