import sys
import numpy as np
import JSTMB_O185

def STMB(data_file, target_file):
    my_STMB = JSTMB_O185.initialize()
    feat = my_STMB.JSTMB_primitive_O185(data_file, target_file)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    selected_feature = np.array(STMB(data, target), dtype=np.int16)
    np.savetxt('Features_O185_JSTMB.csv', selected_feature, delimiter=',')
    print selected_feature
