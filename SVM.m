% SVM
svm()
function svm_accuracy = svm()

clear all; clc;
% load data
data = load('text_big.csv');
data = data(2:size(data, 1),2:size(data, 2));
[n_rows, n_cols] = size(data);


test_rows = int32(n_rows*.3);
[TrainIndices, TestIndices] = crossvalind('LeaveMOut', n_rows,test_rows);
train_set = data(TrainIndices, :);
test_set = data(TestIndices, :);

XTrain = train_set(:,1:n_cols-1);
YTrain = train_set(:,n_cols-1);

XTest = test_set(:,1:n_cols-1);
YTest = test_set(:,n_cols-1);

% SVM Model training - check for CECOC
% Mdl = fitcecoc(XTrain,YTrain);
pred_output = predict(Mdl,XTest);

disp(size(pred_output));

error = sum(YTest ~= pred_output);
svm_accuracy = (double(n_rows - error) / n_rows) * 100;
end

