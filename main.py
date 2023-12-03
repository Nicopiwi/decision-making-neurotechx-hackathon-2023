# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 04:08:39 2023

@author: 54113
"""

import numpy as np
from nilearn import datasets, image, plotting
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def prepare_data():
        
    atlas = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
    
    fmri_img = image.load_img('sub-02-run-01.nii.gz')
    
    prefrontal_roi = image.math_img('(img == 1)', img=atlas['maps'])

    fmri_prefrontal = image.math_img('fmri_img * prefrontal_roi', fmri_img=fmri_img, prefrontal_roi=prefrontal_roi)

    X = fmri_prefrontal.get_fdata()

    labels = np.ones(length(X))

    return X, labels

    
    
def pipeline(data, labels):
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)

    X_train_flat = [ts.flatten() for ts in X_train]
    X_test_flat = [ts.flatten() for ts in X_test]

    # Train Random Forest Classifier
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_pca, y_train)

    # Step 6: Model Evaluation
    predictions = rf.predict(X_test_pca)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    data, labels = get_data()
    pipeline(data, labels)
