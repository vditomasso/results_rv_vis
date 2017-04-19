import pandas as pd
import numpy as np
import astrometry
	
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
	
	# print "Avg RV = " + str(calc_rv_unc[0]) + " +/- " + str(calc_rv_unc[1])

	return calc_rv_unc