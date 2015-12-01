# Author: Jon Berliner 12.1.15

import numpy as np
# import pdb

def sql2csv(db_url, table_name, csv_name_head):
    """connects to database at db_url and converts psiturk datatable table_name to a pandas df."""
    from sqlalchemy import MetaData, Table, create_engine
    from json import loads
    from pandas import DataFrame, concat

    data_column_name = 'datastring'
    # boilerplace sqlalchemy setup
    engine = create_engine(db_url)
    metadata = MetaData()
    metadata.bind = engine
    table = Table(table_name, metadata, autoload=True)
    # make a query and loop through
    s = table.select()
    sql_expData = s.execute()  # all data from the experiment in sqlalchemy format

    # convert sql rows to lodicts, each containing a subject's full experiment
    # fields from orig datatable that you want attached to every trial
    idFields = ['uniqueid', 'assignmentid', 'workerid', 'hitid', 'status', 'condition', 'counterbalance']
    expData = []
    # sql_subData is a subject's full experiment data in sqlalchemy format
    for sql_subData in sql_expData:
        # try:
        if sql_subData:
            try:
                subData = loads(sql_subData[data_column_name])
            except:
                continue
            for field in idFields:
                if field=='condition':
                    subData['condition'] = sql_subData['cond']
                else:
                    subData[field] = sql_subData[field]
            expData.append(subData)
            # except:
            #     print 'BAD'
            #     continue

    # init lists of dataframes that we will combine and convert to csv
    datatypes = ['trialdata','questiondata','eventdata']
    minidicts = {}
    for dt in datatypes:
        minidicts[dt] = []

    for subData in expData:  # for every subject in experiment...
        # get id fields for this subject
        subid = {}
        for f in idFields:
            subid[f] = subData[f]

        # GET QUESTION DATA
        subq = subData['questiondata']
        # append id stuff
        for f in idFields:
            subq[f] = subid[f]
        minidicts['questiondata'].append(subq)

        # GET EVENT DATA
        sube = subData['eventdata']
        for event in sube:
            # append id stuff
            for f in idFields:
                event[f] = subid[f]
            # add to event csv
            minidicts['eventdata'].append(event)

        # GET TRIAL DATA
        for trial in subData['data']:
            try:
                trialdata = trial['trialdata']
                # add id stuff
                for field in idFields:
                    trialdata[field] = subid[field]
                minidicts['trialdata'].append(trialdata)
            except:
                print(subData['workerid']+' has no trialdata for trial ' + trial['current_trial'])
                continue

    # convert minidicts into dataframe!
    for dt in datatypes:
        df = DataFrame(minidicts[dt])
        # # get rid of residue from minidfs
        # df.reset_index(drop=True, inplace=True)
        fname = csv_name_head + '_' + dt + '.csv'
        df.to_csv(fname, index=None)

