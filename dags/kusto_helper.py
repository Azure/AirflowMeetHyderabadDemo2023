def get_kusto_query():
    return '''
                let 4xx = apiLogs
                | where message startswith "4XX Error Random number"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "4XX"
                | project correlationId, type;
                let 5xx = apiLogs
                | where message startswith "InternalServer Error Random number"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "5XX"
                | project correlationId, type;
                apiLogs
                | where message endswith "returned successfully"
                | where startofday(['datetime']) == startofday(now())
                | where datetime_part("hour", ['datetime']) == datetime_part("hour", now())
                | extend type = "2XX"
                | project correlationId, type
                | union ( ['4xx'] )
                | union ( ['5xx'] )
            '''
