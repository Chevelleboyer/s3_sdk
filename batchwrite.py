response = client.batch_write_item(
    RequestItems={
        'music': [
            # {
            #     "PutRequest": {
            #         "Item": {
            #             "pk": {"S": "song"},
            #             "sk": {"S": "girls"},
            #             "type": {"S": "song"},
            #             "name": {"S": "girls"},
            #             "s3_key": {"S": "path/to/song_1"},
            #         },
            #     },
            # },
            # {
            #     "PutRequest": {
            #         "Item": {
            #             "pk": {"S": "album#g_strait"},
            #             "sk": {"S": "song#song_2"},
            #             "type": {"S": "song"},
            #             "name": {"S": "Song 2"},
            #             "s3_key": {"S": "path/to/song_2"},
            #         },
            #     },
            # },
            # {
            #     'PutRequest': {
            #         'Item': {
            #             "pk": {"S": "artist#fgl"},
            #             "sk": {"S": "album#sucks"},
            #             "type": {"S": "album"},
            #             "name": {"S": "sucks"},
            #         },
            #     },
            # },


            # {
            #     'PutRequest': {
            #         'Item': {
            #             "pk": {"S": "genre#country"},
            #             "sk": {"S": "artist#g_strait"},
            #             "type": {"S": "artist"},
            #             "name": {"S": "Goerge Strait"},
            #         }
            #     },
            # },
            # {
            #     'PutRequest': {
            #         'Item': {
            #             "pk": {"S": "genre"},
            #             "sk": {"S": "rap"},
            #             "type": {"S": "genre"},
            #             "name": {"S": "rap"},
            #         }
            #     },
            # },
        ]
    },
    ReturnConsumedCapacity='INDEXES'|'TOTAL'|'NONE',
    ReturnItemCollectionMetrics='SIZE'|'NONE'
)