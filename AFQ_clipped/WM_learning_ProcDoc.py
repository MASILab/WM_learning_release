import os 
import sys

def open_doc(options):
    basic_para = ['222','111','113','131','311','331','313','133','333']
    if (options.scratch):
        print("We need to learn from scratch,open a new document")
        f = open(options.train_doc,'w')
        f.close()
        f = open(options.valid_doc,'w')
        f.close()
    elif (not options.scratch and not options.index in basic_para ):
        print('We do need to learn from scractch but used other models open a new document')
        f = open(options.train_doc,'w')
        f.close()
        f = open(options.valid_doc,'w')
        f.close()

    else:
        print("we need to do transfer learning, don't open new document")


def write_doc(options,train_loss,valid_loss):
    with open(options.train_doc, 'a') as f:
        f.write('{}\n'.format(train_loss))
    with open(options.valid_doc, 'a') as f:
        f.write('{}\n'.format(valid_loss))


