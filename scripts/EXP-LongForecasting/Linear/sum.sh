
if [ ! -d "./logs" ]; then
    mkdir ./logs
fi

if [ ! -d "./logs/LongForecasting" ]; then
    mkdir ./logs/LongForecasting
fi
seq_len=336
model_name=DLinear
my_loss=mse

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'336 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'336_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'720 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'720_$my_loss.log

  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'96 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'192 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'336 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'720 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'720_$my_loss.log


  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'96 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'192 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'336 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'720 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'720_$my_loss.log


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
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log

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
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

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
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

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
  --sigma 0.01\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'336 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'336_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'720 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'720_$my_loss.log

  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'96 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'192 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'336 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'720 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'720_$my_loss.log


  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'96 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'192 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'336 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'720 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'720_$my_loss.log


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
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log

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
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

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
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

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
  --sigma 0.1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log





python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'336 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'336_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'720 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'720_$my_loss.log

  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'96 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'192 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'336 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'720 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'720_$my_loss.log


  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'96 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'192 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'336 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'720 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'720_$my_loss.log


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
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log

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
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

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
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

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
  --sigma 1\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log


python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'336 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'336_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'720 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'720_$my_loss.log

  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'96 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'192 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'336 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'720 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'720_$my_loss.log


  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'96 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'192 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'336 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'720 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'720_$my_loss.log


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
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log

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
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

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
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

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
  --sigma 10\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log






python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'96 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'96_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'192 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'192_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'336 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'336_$my_loss.log

python -u D:/MyLinear/run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh1.csv \
  --model_id ETTh1_$seq_len'_'720 \
  --model $model_name \
  --data ETTh1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth1_$seq_len'_'720_$my_loss.log

  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'96 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'192 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'336 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --train_epochs 15\
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTh2.csv \
  --model_id ETTh2_$seq_len'_'720 \
  --model $model_name \
  --data ETTh2 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.005 >logs/LongForecasting/$model_name'_'Etth2_$seq_len'_'720_$my_loss.log


  python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'96 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 96 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'96_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'192 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 192 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'192_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'336 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 336 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'336_$my_loss.log

python -u run_longExp.py \
  --is_training 1 \
  --root_path ./dataset/ETT/ \
  --data_path ETTm1.csv \
  --model_id ETTm1_$seq_len'_'720 \
  --model $model_name \
  --data ETTm1 \
  --features M \
  --seq_len $seq_len \
  --pred_len 720 \
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm1_$seq_len'_'720_$my_loss.log


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
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'96_$my_loss.log

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
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'192_$my_loss.log

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
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.01 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'336_$my_loss.log

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
  --sigma 100\
  --num_bins 100\
  --enc_in 7 \
  --des 'Exp' \
  --my_loss $my_loss \
  --itr 5 --batch_size 32 --learning_rate 0.0001 >logs/LongForecasting/$model_name'_'ETTm2_$seq_len'_'720_$my_loss.log