import pandas
import dataset
from .utils import load, flattenit

def create_db(jsonpath='/media/data_cifs/irodri15/data/processed/datasets.json',output='sqlite:///leavesdb.db' ):
    '''
    File to create a db from a json file. check the structure of the Json. The function would look for the key 'paths' as a stop key. 
    Arguments:
        - Json file with the following structure: 
            file: { 'dataset1' : {'family1': 
                                        'genus1':{ 
                                            'specie1':{
                                                'paths': [path1.jpg,...],
                                                .....
                                            },
                                            ...    
                                        },
                                  
                                  'family2':{},.. , ...}}
    Returns
    '''
    file =load(jsonpath)
    db = dataset.connect(output)
    db.begin()

    table = db['dataset']
    counter= 0 

    for data_set in file:
        res = {k:v for k, v in flattenit(file[data_set])}
        print(data_set)
        for key in res: 
            if 'paths' in key:
                names = key.split('_')[:-1]
                if len(names)==1:
                    continue 
                    print(names[0])
                    for p  in res[key]:
                        table.insert(dict(path=p,
                                      dataset=data_set,
                                      family=names[0],
                                      specie='nn',
                                      genus='nn'
                                      ))
                        counter+=1

                else:   
                    print(names)
                    for p  in res[key]:
                        family = names[0]
                        if 'uncertain' in family:
                            family='uncertain'
                        table.insert(dict(path=p,
                                      dataset=data_set,
                                      family=names[0],
                                      specie=names[2],
                                      genus=names[1]
                                      ))
                        counter+=1
                        if counter%1000==0:
                            print(counter)
    db.commit()