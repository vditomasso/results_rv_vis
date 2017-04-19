import NIRSPEC
import pandas as pd
import numpy as np
import astrometry

def mass_rv(obj_filename,obj_name):

	df=pd.read_csv('/Users/victoriaditomasso/Desktop/RV_comp_spectra/All_RV_comps_DF.txt',sep='\t')
	
	RV = []
	error = []
	
	for i, row in df.iterrows() :
	
		rv_and_error = NIRSPEC.main(['',row['filename'],row['std_rv'],row['std_unc'],obj_filename,1])
		RV.append(rv_and_error[0])
		error.append(rv_and_error[1])
		
	df['obj_rv'] = RV
	df['obj_unc'] = error
	
	df.to_csv(str(obj_name)+'_against_all_comps.txt',sep='\t')
	
def avg_rv(path_to_df):

	df=pd.read_csv(path_to_df,sep='\t')
	
	RV=[]
	eRV=[]
	
	for i, row in df.iterrows():
		RV.append(row['obj_rv'])
		eRV.append(row['obj_unc'])
	
	RV = np.asarray(RV)
	eRV = np.asarray(eRV)

	calc_rv_unc = astrometry.wstddev(RV,eRV)
	
	print "Avg RV = " + str(calc_rv_unc[0]) + " +/- " + str(calc_rv_unc[1])