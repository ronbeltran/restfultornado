import logging
from datetime import datetime, timedelta

from mapreduce import base_handler
from mapreduce import context 
from mapreduce import mapreduce_pipeline
from mapreduce import operation as op

import models

def events_hourly_map(event):
    """Event hourly count map function.
    """
    ctx = context.get()
    params = ctx.mapreduce_spec.mapper.params

    user_id = int(params['user_id'])

    if int(event.user.id) == user_id:
        # Yield events per hour grouping
        # eg. ('e1',1), ('e1',1), ('e2',2), ('e2',3)
        # ('e1',['1','1']), ('e2',['2','3'])
        logging.debug('events_hourly_map(): yield (%s, %s)', event.name, str(event.created.hour))
        yield (event.name, str(event.created.hour) )


def events_count_reduce(key, values):
    """Event count reduce function"""
    # For ('e1',['1','1']) => ('e1',2) means two e1 event for the first hour.
    # For ('e2',['2','3']) => ('e2', 1), ('e2', 1) means one e2 event for second and third hours respectively.
    for i in set(values):
        logging.debug('events_count_reduce(): yield (%s, %s)', key, str( values.count(i) ))
        yield ( key, str(values.count(i)) )


class EventCountPipeline(base_handler.PipelineBase):

    def run(self, user_id):
        output = yield mapreduce_pipeline.MapreducePipeline(
            "event_count",
            "precompute.events_hourly_map",
            "precompute.events_count_reduce",
            "mapreduce.input_readers.DatastoreInputReader",
            "mapreduce.output_writers.BlobstoreOutputWriter",
            mapper_params={
                "entity_kind": "models.Event",
                "user_id": str(user_id),
            },
            reducer_params={
                "mime_type": "text/plain",
            },
            shards=20)
        yield StoreOutput("EventCount", user_id, output)


class StoreOutput(base_handler.PipelineBase):

    def run(self, mr_type, user_id, output):
        logging.debug("output is %s", str(output))
        user = models.User.all().filter("id =", int(user_id))
        if mr_type=="EventCount":
            logging.debug("mr_type is %s", str(mr_type))
#            e = models.EventCount(user=user,
#                                  name="",
#                                  count=0)
#            e.put()
