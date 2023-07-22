


def checkAndAdd(pid,array,t):
    for obj in array:
        if(obj['pid'].strip().upper()==pid.upper()):
            time=obj['date_time']
            time.append({"time":t})
            obj.update({'date_time':time})
            # array.append({"pid":pid,"date_time":time})
            return array
    t={"time":t}
    array.append({"pid":pid,"date_time":[t]})
    return array



