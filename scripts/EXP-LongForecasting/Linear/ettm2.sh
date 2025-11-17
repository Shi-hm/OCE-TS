
if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
seq_len=336
model_name=DLinear
my_loss=cov_hsic

for seq_len in 48 96 120 192 336 504 720
do
    python -u run_longExp.py \
      --is_training 1 \
      --root_path ./dataset/ETT/ \
      --data_path ETTm2.csv \
      --model_id ETTm2_$seq_len'_'96 \
      --model $model_name \
      --data ETTm2 \
      --features M \
      --seq_len $seq_len \
      --pred_len 96 \
      --enc_in 7 \
      --des 'Exp' \
      --my_loss $my_loss \
      --itr 1 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log
    #
    python -u run_longExp.py \
      --is_training 1 \
      --root_path ./dataset/ETT/ \
      --data_path ETTm2.csv \
      --model_id ETTm2_$seq_len'_'192 \
      --model $model_name \
      --data ETTm2 \
      --features M \
      --seq_len $seq_len \
      --pred_len 192 \
      --enc_in 7 \
      --des 'Exp' \
      --my_loss $my_loss \
      --itr 1 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

    python -u run_longExp.py \
      --is_training 1 \
      --root_path ./dataset/ETT/ \
      --data_path ETTm2.csv \
      --model_id ETTm2_$seq_len'_'336 \
      --model $model_name \
      --data ETTm2 \
      --features M \
      --seq_len $seq_len \
      --pred_len 336 \
      --enc_in 7 \
      --des 'Exp' \
      --my_loss $my_loss \
      --itr 1 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

    python -u run_longExp.py \
      --is_training 1 \
      --root_path ./dataset/ETT/ \
      --data_path ETTm2.csv \
      --model_id ETTm2_$seq_len'_'720 \
      --model $model_name \
      --data ETTm2 \
      --features M \
      --seq_len $seq_len \
      --pred_len 720 \
      --enc_in 7 \
      --des 'Exp' \
      --my_loss $my_loss \
      --itr 3 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log
#done