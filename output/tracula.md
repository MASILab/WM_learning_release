### The output of tracula singularity

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

./affine
├── fmajor_PP_avg33_mni_bbr.nii.gz
├── fminor_PP_avg33_mni_bbr.nii.gz
├── lh_atr_PP_avg33_mni_bbr.nii.gz
├── lh_cab_PP_avg33_mni_bbr.nii.gz
├── lh_ccg_PP_avg33_mni_bbr.nii.gz
├── lh_cst_AS_avg33_mni_bbr.nii.gz
├── lh_ilf_AS_avg33_mni_bbr.nii.gz
├── lh_slfp_PP_avg33_mni_bbr.nii.gz
├── lh_slft_PP_avg33_mni_bbr.nii.gz
├── lh_unc_AS_avg33_mni_bbr.nii.gz
├── rh_atr_PP_avg33_mni_bbr.nii.gz
├── rh_cab_PP_avg33_mni_bbr.nii.gz
├── rh_ccg_PP_avg33_mni_bbr.nii.gz
├── rh_cst_AS_avg33_mni_bbr.nii.gz
├── rh_ilf_AS_avg33_mni_bbr.nii.gz
├── rh_slfp_PP_avg33_mni_bbr.nii.gz
├── rh_slft_PP_avg33_mni_bbr.nii.gz
└── rh_unc_AS_avg33_mni_bbr.nii.gz
./anat
├── T1_linear.nii.gz
├── T1_mask_mask.nii.gz
├── T1_mask.nii.gz
└── T1_max.nii.gz
./orig
├── fmajor_PP_avg33_mni_bbr.nii.gz
├── fminor_PP_avg33_mni_bbr.nii.gz
├── lh_atr_PP_avg33_mni_bbr.nii.gz
├── lh_cab_PP_avg33_mni_bbr.nii.gz
├── lh_ccg_PP_avg33_mni_bbr.nii.gz
├── lh_cst_AS_avg33_mni_bbr.nii.gz
├── lh_ilf_AS_avg33_mni_bbr.nii.gz
├── lh_slfp_PP_avg33_mni_bbr.nii.gz
├── lh_slft_PP_avg33_mni_bbr.nii.gz
├── lh_unc_AS_avg33_mni_bbr.nii.gz
├── rh_atr_PP_avg33_mni_bbr.nii.gz
├── rh_cab_PP_avg33_mni_bbr.nii.gz
├── rh_ccg_PP_avg33_mni_bbr.nii.gz
├── rh_cst_AS_avg33_mni_bbr.nii.gz
├── rh_ilf_AS_avg33_mni_bbr.nii.gz
├── rh_slfp_PP_avg33_mni_bbr.nii.gz
├── rh_slft_PP_avg33_mni_bbr.nii.gz
└── rh_unc_AS_avg33_mni_bbr.nii.gz
./reg
├── ANTS0GenericAffine.mat
├── ANTSInverseWarped.nii.gz
└── ANTSWarped.nii.gz