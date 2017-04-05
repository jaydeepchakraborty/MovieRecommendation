import matlab.engine
from generate_matrix import getRandomData
eng = matlab.engine.start_matlab()
f = open("knn_accuracy.txt","w")

no_itr = 1000

avg_knn_accuracy = 0
for x in range(1,no_itr):
    try:
        getRandomData()
        knn_accuracy  = eng.knn(nargout=1)
        avg_knn_accuracy = avg_knn_accuracy + knn_accuracy
        f.write(str(knn_accuracy)+"\n")
    except:
        pass
#eng.edit('knn',nargout=0)
f.write("FINAL ACCURACY : "+str(avg_knn_accuracy/no_itr)+"\n")
f.close()
print("------------ACCURACY CALCULATION DONE------------")