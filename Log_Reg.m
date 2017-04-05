clear all; clc;
% load data
data = load('text.csv');
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

sp = double(nominal(YTrain));

[B,dev,stats] = mnrfit(XTrain, sp);
[pihat, dlow, dhi] = mnrval( B, XTest, stats)
% Fit = mnrval(B, XTest, stats);


% mdl.predict(test_set(:,1:n_cols-1))
% mdl = LRClassifier(train_set(:,1:n_cols-1), train_set(:,n_cols-1), unique(train_set(:,n_cols-1)), 0.1);