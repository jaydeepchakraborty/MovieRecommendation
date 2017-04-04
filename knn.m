clear all; clc;
% load data
data = load('text.csv');
data = data(2:size(data, 1),2:size(data, 2));
[n_rows, n_cols] = size(data);


test_rows = int32(n_rows*.3);
[TrainIndices, TestIndices] = crossvalind('LeaveMOut', n_rows,test_rows);
train_set = data(TrainIndices, :);
test_set = data(TestIndices, :);

mdl = fitcknn(train_set(:,1:n_cols-1), train_set(:,n_cols-1));
pred_output = mdl.predict(test_set(:,1:n_cols-1));

error = sum(test_set(:,n_cols-1) ~= pred_output);
accuracy = (double(n_rows - error) / n_rows) * 100;

% a = confusionmat(test_set(:,n_cols-1), pred_output);
% disp(a);
disp(accuracy);