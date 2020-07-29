import gpt_2_simple as gpt2
import yaml


def create_data(data_path = 'data/BonIver.txt', 
                model_name = '124M', 
                steps = 70, 
                restore_from = 'fresh', 
                run_name = 'run1', 
                print_every = 5, 
                sample_every = 10, 
                save_every = 50):
    
    sess = gpt2.start_tf_sess()
    gpt2.download_gpt2()
    gpt2.finetune(sess,
                dataset=data_path,
                model_name=model_name,
                steps=steps,
                restore_from=restore_from,
                run_name=run_name,
                print_every=print_every,
                sample_every=sample_every,
                save_every=save_every)

if __name__ == "__main__":
    config = yaml.safe_load(open("config.yml"))
    kwargs = config['create_model']
    create_data(**kwargs)