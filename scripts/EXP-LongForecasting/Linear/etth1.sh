if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi

model_name=DLinear
my_loss=Ordinal_CrossEntropy_Loss

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1'_'192'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len 192 \
  --pred_len 96 \
  --sigma 0.015 \
  --num_bins 44 \
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 1 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name_ETTm1_192_96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1'_'336'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len 336 \
  --pred_len 192 \
  --sigma 0.015 \
  --num_bins 44 \
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 1 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name_ETTm1_336_192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1'_'192'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len 192 \
  --pred_len 96 \
  --sigma 0.015 \
  --num_bins 44 \
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 1 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name_ETTm1_192_96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1'_'192'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len 192 \
  --pred_len 96 \
  --sigma 0.015 \
  --num_bins 44 \
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 1 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name_ETTm1_192_96_$my_loss.log