import traceback
import numpy
import time
# import matlab.engine
from generate_matrix import getRandomData
from py_Knn import getKnnAcc
from py_nb import getNBAcc
from py_LR import getLRAcc
from py_Kmeans import getKmeansAcc
from py_svm import getSVMAcc
# eng = matlab.engine.start_matlab()


no_itr = 1000
actual_itr = 0

avg_knn_accuracy = 0
avg_nb_accuracy = 0
avg_lr_accuracy = 0
avg_kmeans_accuracy = 0
avg_svm_accuracy = 0

train_ratio = .9
start_time = time.time()

for x in range(1,no_itr):
    try:
        print("Iteration Number:-"+str(x))
        getRandomData()
        
        my_data = numpy.genfromtxt('text_big.csv', delimiter=',')
        my_data = numpy.delete(my_data, (0), axis=0)
        my_data_transpose = my_data.transpose()
       
        knn_accuracy  = getKnnAcc(my_data_transpose,train_ratio)
        nb_accuracy = getNBAcc(my_data_transpose,train_ratio)
        lr_accuracy = getLRAcc(my_data_transpose,train_ratio)
        kmeans_accuracy = getKmeansAcc(my_data_transpose,train_ratio)
        svm_accuracy = getSVMAcc(my_data_transpose,train_ratio)
        
        
        avg_nb_accuracy = avg_nb_accuracy + nb_accuracy
        avg_knn_accuracy = avg_knn_accuracy + knn_accuracy
        avg_lr_accuracy = avg_lr_accuracy + lr_accuracy
        avg_kmeans_accuracy = avg_kmeans_accuracy + kmeans_accuracy
        avg_svm_accuracy = avg_svm_accuracy + svm_accuracy
        actual_itr = actual_itr + 1
    except:
        traceback.print_exc()
        pass
    
#eng.edit('knn',nargout=0)

f = open("accuracy.txt","w")
f.write("FINAL KNN ACCURACY : "+str(avg_knn_accuracy/actual_itr)+"\n")
f.write("FINAL NB ACCURACY : "+str(avg_nb_accuracy/actual_itr)+"\n")
f.write("FINAL LR ACCURACY : "+str(avg_lr_accuracy/actual_itr)+"\n")
f.write("FINAL KMEANS ACCURACY : "+str(avg_kmeans_accuracy/actual_itr)+"\n")
f.write("FINAL SVM ACCURACY : "+str(avg_svm_accuracy/actual_itr)+"\n")
f.close()


print("------------ACCURACY CALCULATION DONE------------")
print("--- %s seconds ---" % (time.time() - start_time))