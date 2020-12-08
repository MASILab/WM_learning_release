## White matter learning

### White matter learning-Introduction

We proposed spatial localized patch-wise framework to delineate white matter regions from structural image. To achieve this target, we select six state-of-the-art (TractSeg,Recobundle,Xtract,Tracula,AFQ and AFQ_clipped) tractography algorithms to reconstruct white matter pathways as ground-truth to supervise whole training process. The pipeline of proposed method is shown in the following figure

![method](method.png)

We envision the proposed framework as a tool to localize white matter regions of interest when diffusion image is not present. The output of propo sed framework is similar to a probability map rather than a binary image, which can provide user with more options to adjust threshold to adjust bundle overlap or bundle overreach for one specific white matter pathway. Different bundle segmentation algorithms do not have exactly same definition for same white matter tracts. Thus, we provide six definition schemes for user to reconstruct white matter in their preferred scheme.


### Source code
The github repo includes the train, valdiation and testing code. The different folder name corresponding to different tractography algorithm. As for specific output of each tractography algorithm, please check this [repo](https://github.com/MASILab/Pandora-WhiteMatterAtlas)

### Singularity

All sorce code binaries, and third-party dependencies have been packaged into a singulairty container. Each method corresponding to one singularity. User just need to build two folders **/path/to/inputs/directory/** and **/path/to/outputs/directory/**, putting T1 file into **/path/to/inputs/directory/** folder.

We use Singularity version 3.4 with root permissions. Because we have 125 models to run. So for now we only test GPU to make inference.The command of calling singularity is shown as below:

singularity run 
    -B /path/to/inputs/directory/:/INPUTS
    -B /path/to/outputs/directory/:/OUTPUTS
    -e
    --contain
    --nv
    /path/to/[method].simg

All the singularities can be found at this [link](https://vanderbilt365-my.sharepoint.com/:f:/g/personal/qi_yang_vanderbilt_edu/EpMsl1c0o69NiNBs4JzEPVABTezoFWPZTHOhwxGByVcVYw) 

### Reference:
 Need to be updated

### Contact:
If you find any issues or questions, please feel free to contact me (qi.yang@vanderbilt.edu)

