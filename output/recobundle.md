### The output of recobundle singularity

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
├── AF_L.nii.gz
├── AF_R.nii.gz
├── AST_L.nii.gz
├── AST_R.nii.gz
├── CB_L.nii.gz
├── CB_R.nii.gz
├── CC_ForcepsMajor.nii.gz
├── CC_ForcepsMinor.nii.gz
├── CCMid.nii.gz
├── CC.nii.gz
├── CST_L.nii.gz
├── CST_R.nii.gz
├── CTT_L.nii.gz
├── CTT_R.nii.gz
├── EMC_L.nii.gz
├── EMC_R.nii.gz
├── FPT_L.nii.gz
├── FPT_R.nii.gz
├── IFOF_L.nii.gz
├── IFOF_R.nii.gz
├── ILF_L.nii.gz
├── ILF_R.nii.gz
├── MCP.nii.gz
├── MdLF_L.nii.gz
├── MdLF_R.nii.gz
├── MLF_L.nii.gz
├── MLF_R.nii.gz
├── ML_L.nii.gz
├── ML_R.nii.gz
├── OPT_L.nii.gz
├── OPT_R.nii.gz
├── OR_L.nii.gz
├── OR_R.nii.gz
├── PPT_L.nii.gz
├── PPT_R.nii.gz
├── SLF_L.nii.gz
├── SLF_R.nii.gz
├── STT_L.nii.gz
├── STT_R.nii.gz
├── TPT_L.nii.gz
├── TPT_R.nii.gz
├── UF_L.nii.gz
├── UF_R.nii.gz
└── V.nii.gz
./anat
├── T1_linear.nii.gz
├── T1_mask_mask.nii.gz
├── T1_mask.nii.gz
└── T1_max.nii.gz
./orig
├── AF_L.nii.gz
├── AF_R.nii.gz
├── AST_L.nii.gz
├── AST_R.nii.gz
├── CB_L.nii.gz
├── CB_R.nii.gz
├── CC_ForcepsMajor.nii.gz
├── CC_ForcepsMinor.nii.gz
├── CCMid.nii.gz
├── CC.nii.gz
├── CST_L.nii.gz
├── CST_R.nii.gz
├── CTT_L.nii.gz
├── CTT_R.nii.gz
├── EMC_L.nii.gz
├── EMC_R.nii.gz
├── FPT_L.nii.gz
├── FPT_R.nii.gz
├── IFOF_L.nii.gz
├── IFOF_R.nii.gz
├── ILF_L.nii.gz
├── ILF_R.nii.gz
├── MCP.nii.gz
├── MdLF_L.nii.gz
├── MdLF_R.nii.gz
├── MLF_L.nii.gz
├── MLF_R.nii.gz
├── ML_L.nii.gz
├── ML_R.nii.gz
├── OPT_L.nii.gz
├── OPT_R.nii.gz
├── OR_L.nii.gz
├── OR_R.nii.gz
├── PPT_L.nii.gz
├── PPT_R.nii.gz
├── SLF_L.nii.gz
├── SLF_R.nii.gz
├── STT_L.nii.gz
├── STT_R.nii.gz
├── TPT_L.nii.gz
├── TPT_R.nii.gz
├── UF_L.nii.gz
├── UF_R.nii.gz
└── V.nii.gz
./reg
├── ANTS0GenericAffine.mat
├── ANTSInverseWarped.nii.gz
└── ANTSWarped.nii.gz