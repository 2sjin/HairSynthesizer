cd D:\Naver MYBOX\��ǻ�Ͱ��а�\2021-�ΰ�����Ư��\stargan-v2-master
python main.py --mode align --inp_dir assets/representative/my_image/src/male --out_dir assets/representative/my_image/src/male
python main.py --mode align --inp_dir assets/representative/my_image/ref/male --out_dir assets/representative/my_image/ref/male
python main.py --mode sample --num_domains 2 --resume_iter 100000 --w_hpf 1 --checkpoint_dir expr/checkpoints/celeba_hq --src_dir assets/representative/my_image/src --ref_dir assets/representative/my_image/ref
