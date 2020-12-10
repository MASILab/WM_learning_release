### The output of AFQ singularity

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
├── Callosum_Forceps_Major.nii.gz
├── Callosum_Forceps_Minor.nii.gz
├── Left_Arcuate.nii.gz
├── Left_Cingulum_Cingulate.nii.gz
├── Left_Cingulum_Hippocampus.nii.gz
├── Left_Corticospinal.nii.gz
├── Left_IFOF.nii.gz
├── Left_ILF.nii.gz
├── Left_SLF.nii.gz
├── Left_Thalamic_Radiation.nii.gz
├── Left_Uncinate.nii.gz
├── Right_Arcuate.nii.gz
├── Right_Cingulum_Cingulate.nii.gz
├── Right_Cingulum_Hippocampus.nii.gz
├── Right_Corticospinal.nii.gz
├── Right_IFOF.nii.gz
├── Right_ILF.nii.gz
├── Right_SLF.nii.gz
├── Right_Thalamic_Radiation.nii.gz
└── Right_Uncinate.nii.gz
./anat
├── T1_linear.nii.gz
├── T1_mask_mask.nii.gz
├── T1_mask.nii.gz
└── T1_max.nii.gz
./orig
├── Callosum_Forceps_Major.nii.gz
├── Callosum_Forceps_Minor.nii.gz
├── Left_Arcuate.nii.gz
├── Left_Cingulum_Cingulate.nii.gz
├── Left_Cingulum_Hippocampus.nii.gz
├── Left_Corticospinal.nii.gz
├── Left_IFOF.nii.gz
├── Left_ILF.nii.gz
├── Left_SLF.nii.gz
├── Left_Thalamic_Radiation.nii.gz
├── Left_Uncinate.nii.gz
├── Right_Arcuate.nii.gz
├── Right_Cingulum_Cingulate.nii.gz
├── Right_Cingulum_Hippocampus.nii.gz
├── Right_Corticospinal.nii.gz
├── Right_IFOF.nii.gz
├── Right_ILF.nii.gz
├── Right_SLF.nii.gz
├── Right_Thalamic_Radiation.nii.gz
└── Right_Uncinate.nii.gz
./reg
├── ANTS0GenericAffine.mat
├── ANTSInverseWarped.nii.gz
└── ANTSWarped.nii.gz
