import traceback
import matlab.engine
from generate_matrix import getRandomData
from py_nb import getNBAcc
from py_LR import getLRAcc
from py_Kmeans import getKmeansAcc
from py_svm import getSVMAcc
eng = matlab.engine.start_matlab()


no_itr = 10

avg_knn_accuracy = 0
avg_nb_accuracy = 0
avg_lr_accuracy = 0
avg_kmeans_accuracy = 0
avg_svm_accuracy = 0
for x in range(1,no_itr):
    try:
        getRandomData()
       
        knn_accuracy  = eng.knn(nargout=1)
        avg_knn_accuracy = avg_knn_accuracy + knn_accuracy
        
        nb_accuracy = getNBAcc()
        print("Iter " + str(x) + " nb_acc: " + str(nb_accuracy))
        print(nb_accuracy)
        avg_nb_accuracy = avg_nb_accuracy + nb_accuracy
        
        lr_accuracy = getLRAcc()
        avg_lr_accuracy = avg_lr_accuracy + lr_accuracy
        
        kmeans_accuracy = getKmeansAcc()
        avg_kmeans_accuracy = avg_kmeans_accuracy + kmeans_accuracy
        
        svm_accuracy = getSVMAcc()
        avg_svm_accuracy = avg_svm_accuracy + svm_accuracy
        
    except:
        traceback.print_exc()
        pass
    
#eng.edit('knn',nargout=0)

f = open("accuracy.txt","w")
f.write("FINAL KNN ACCURACY : "+str(avg_knn_accuracy/no_itr)+"\n")
f.write("FINAL NB ACCURACY : "+str(avg_nb_accuracy/no_itr)+"\n")
f.write("FINAL LR ACCURACY : "+str(avg_lr_accuracy/no_itr)+"\n")
f.write("FINAL KMEANS ACCURACY : "+str(avg_kmeans_accuracy/no_itr)+"\n")
f.write("FINAL SVM ACCURACY : "+str(avg_svm_accuracy/no_itr)+"\n")
f.close()


print("------------ACCURACY CALCULATION DONE------------")