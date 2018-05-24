from datetime import date, datetime

# info
#   proj
#   jid
#   ko_date
#   gm_date
#   apply_date
#   type: ['self', 'reuse', 'new']
#   repo_num
#   vm_num
#   extra: [(job, point), ...]
#

DAY_POINT = 3
URGENCY_HIGH = 30
URGENCY_MED  = 60
URGENCY_LOW  = 90

def create_job(info):
    # Calculagte point, Initialize remain point, days & Tag Urgency

    point, tag = 0, 0
    if info['type'] == 'self':
        point += 0.5
    elif info['type'] == 'reuse':
        point += 1
    elif info['type'] == 'new':
        point +=2
    point += info['repo_num'] * 0.1 + info['vm_num']
    point += sum([x[1] for x in info['extra']])

    gm  = info['gm_date'].split('-')
    now = str(datetime.now())[:10].split('-')
    gm  = date(gm[0], gm[1], gm[2])
    now = date(now[0], now[1], now[2])
    days= (gm - now).days

    if days > URGENCY_LOW:
        tag = 3
    elif days < URGENCY_LOW and days > URGENCY_MED:
        tag = 2
    elif days < URGENCY_MED and days > URGENCY_HIGH:
        tag = 1

    info['point'] = point
    info['remain_point'] = point
    info['days']  = days
    info['level'] = tag

    return info

def update_job(jid, point):
    # Update remain point
    pass

def transform_as_job():
    # Parse sth and transform into info
    pass

def refresh_queue():
    # Refresh all jobs' remain day in queue 
    # Send reminder if Urgency change
    pass

def reorder_queue():
    # keep order as possible
    pass
