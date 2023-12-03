# decision-making-neurotechx-hackathon-2023
Database used: https://openneuro.org/datasets/ds001882/versions/1.0.7

We first downloaded subject 2 fmri data in order to test the pipeline generated with GPT4 (already in the repository).
Using FSL we  discovered that the fmri data was not normalized, so with the FSL MCFLIRT tool we adapted the images to the Harvard-Oxford cortical and subcortical atlases.

Then, when trying to apply the ROIs, an error related to files not having the same affinity arised. 
We couldn't solve this problem, so we attempted a "plan B" and went for a PCA using all voxels, but our computing power wasn't enough to resize all features.

All attempted code is available in this repository. 
