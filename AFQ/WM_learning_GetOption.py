import sys
import argparse


def get_test_option(args=sys.argv[2:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-t", "--type",    default='High', type=str, help="Choose resolution of the image [High]/[low]")
    parser.add_argument("-i", "--index",   default=None,  type=str, help="The index of the data you want to train on")
    parser.add_argument("-n", "--norm",    default='max',  type=str, help="The normal type [N3]/[max]/[zscore]")
    parser.add_argument("-r", "--range",   default='00',  type=str, help="The range of normalization [00] means doesn't need to normalize to [0~1],[01] means normalize to [0~1]")
    parser.add_argument("-e", "--epoch",   default=10,    type=int, help="which epoch model you want to load ")
    parser.add_argument("-f", "--folder",  default='../pred_valid',  type=str, help="which folder you want to save the result")
    parser.add_argument("--test_doc",      default=None,  type=str, help="where need to save the test loss txt file")
    parser.add_argument("--model_prefix",  default=None,  type=str, help="where need to save the model")
    parser.add_argument("--model_dir",     default='../model', type=str, help="where need to save the model")
    parser.add_argument("--test_list",     default='/scratch/yangq6/learning/AFQ/doc/valid_AFQ.txt', type=str,help="which database we want to use")

    options = parser.parse_args(args)

    return proc_test_option(options)


def proc_test_option(options):

    if (options.folder == None):
        raise ValueError("You must assign the folder to save prediction")

    if options.test_doc == None and options.model_prefix == None:
        if (options.type == 'High'):
            prefix = '{}_{}_{}_{}'.format('high',options.index,options.norm,options.range)

        if (options.type == 'low'):
            prefix = '{}_{}_{}'.format(options.type,options.norm,options.range)

        options.test_doc     = '../results/{}-test_loss.txt'.format(prefix)
        options.model_prefix = '{}-'.format(options.index)


    return options

def get_train_option(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-t", "--type",        default='High' ,type=str, help="Choose resolution of the image [high]/[low]")
    parser.add_argument("-i", "--index",       default=None  ,type=str, help="The index of the data you want to train on")
    parser.add_argument("-n", "--norm",        default='max' ,type=str, help="The normal type [N3]/[max]/[zscore]")
    parser.add_argument("-r", "--range",       default='00'  ,type=str, help="The range of normalization [00] means doesn't need to normalize to [0~1],[01] means normalize to [0~1]")
    parser.add_argument("--transfer",          default='None',type=str, help="This argument will be used to choose which model we need to load initial weight")
    parser.add_argument("--scratch",           default=False ,type=bool,help="Whether we want to learn from scratch")
    parser.add_argument("-e", "--epochs",      default=3   ,type=int, help="how many epochs that we need to train")
    parser.add_argument("--start_epoch",       default=1     ,type=int, help="Start epoch")
    parser.add_argument("--train_doc",         default=None  ,type=str, help="where need to save the train loss txt file")
    parser.add_argument("--valid_doc",         default=None  ,type=str, help="where need to save the valid loss txt file")
    parser.add_argument("--model_prefix",      default=None  ,type=str, help="where need to save the model")
    parser.add_argument("--train_list",        default='../doc/train_AFQ.txt',type=str,help="which database we want to use")
    parser.add_argument("--valid_list",        default='../doc/valid_AFQ.txt', type=str,help="which database we want to use")

    options = parser.parse_args(args)


    return proc_train_option(options)

def proc_train_option(options):

    if options.train_doc == None and options.valid_doc == None and options.model_prefix == None:
        if (options.type == 'High'):
            prefix = '{}_{}'.format('High',options.index)

        if (options.type == 'low'):
            prefix = '{}_{}_{}'.format(options.type,options.norm,options.range)

        options.train_doc    = '../results/{}-train_loss.txt'.format(prefix)
        options.valid_doc    = '../results/{}-valid_loss.txt'.format(prefix)
        options.model_prefix = '../model/{}-'.format(prefix)


    return options