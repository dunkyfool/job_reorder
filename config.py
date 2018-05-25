from datetime import date, datetime

# info:
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
# renew [2]:
#    Revise Jenkinsfile(codeline) [1] -> Create New SSC [1]
# new   [3]:
#    wait vm -> apply codeline -> new user + install Fortify [1]
#                              -> revise Jenkinsfile + download codeline + set up Jenkins [1]
#                              -> set up SSC [1]
# self  [1]:
#    install Fortify[1]
#
#

DAY_POINT   = 3
SELF_POINT  = 1
NEW_POINT   = 3
REUSE_POINT = 2
URGENCY_HIGH = 30
URGENCY_MED  = 60
URGENCY_LOW  = 90

def create_job(info):
    # Calculagte point, Initialize remain point, days & Tag Urgency

    point, tag = 0, 0
    if info['type'] == 'self':
        point += SELF_POINT
    elif info['type'] == 'reuse':
        point += REUSE_POINT
    elif info['type'] == 'new':
        point += NEW_POINT
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

def calculate_queue():
    # sum up the point and calculate each job's finish date
    pass

def show_task_queue():
    # recommend today task
    pass
