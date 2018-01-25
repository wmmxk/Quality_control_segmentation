from match_dic_2_contour import match_dic_2_contour
import glob
import os
import numpy as np
def get_list(dic_folder, contour_folder, patients):
    '''
     summary: get a list of all the pair of dic folder and contour file
     inputs:
           dic_folder: a parental path to the dic folder of a patient
           contour_folder: a parental path to the contour folder of a patient
           patients: a list of tuples. Each tuple consists of a patient ID for DICOM file and contour ID for the same patient
    outputs: a list of tuples

    '''
    dic_contour_pairs = []
    for patient in patients:
        dic_path = os.path.join(dic_folder,patient[0])
        contour_path = os.path.join(contour_folder, patient[1],"i-contours","*.txt")
        contour_files = glob.glob(contour_path)
        for contour_file in contour_files:
            dic_contour_pairs.append((dic_path,contour_file))
    return dic_contour_pairs
      

def traing_generator(dic_folder, contour_folder, patients,batch_size = 8):

    '''
    summary: this fun is to create a data generator
    inputs: same as the arguments in get_list
    outputs: a cyclic generator with random shuffle after each cycle

    '''


    dic_contour_pairs = get_list(dic_folder, contour_folder, patients)

    while True:
        np.random.shuffle(dic_contour_pairs)
        count = 0
        imgs = []
        masks = []
        for dic_contour in dic_contour_pairs:
            try:
               img, mask = match_dic_2_contour(*dic_contour)
               imgs.append(img)
               masks.append(mask)
               count +=1
            except:
               pass
            if count == batch_size:
               imgs_arr = np.array(imgs)
               masks_arr = np.array(masks)
               count = 0
               imgs = []
               masks = []
               yield(imgs_arr, masks_arr)



if __name__=="__main__": 
    patients = [("SCD0000101","SC-HF-I-1"),("SCD0000201","SC-HF-I-2")]
    dic_folder =  "../../final_data/dicoms"
    contour_folder = "../../final_data/contourfiles"
    get_list(dic_folder, contour_folder, patients)
    tr_gen =  traing_generator(dic_folder, contour_folder, patients,batch_size = 2)
    imgs,masks = next(tr_gen)
    print(imgs.shape)
