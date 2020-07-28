import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()

gpt2.download_gpt2()

gpt2.finetune(sess,
             dataset='BonIver.txt',
             model_name='124M',
             steps=100,
             restore_from='fresh',
             run_name='run1',
             print_every=5,
             sample_every=10,
             save_every=50)
