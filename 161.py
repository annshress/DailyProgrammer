"""[5/7/2014] Challenge #161 [Medium] Appointing Workers"""
# seems like a backtracking problem

s = """6
GUI
Documentation
Finances
Frontend
Backend
Support
Alice GUI,Backend,Support
Bill Finances,Backend
Cath Documentation,Finances
Jack Documentation,Frontend,Support
Michael Frontend
Steve Documentation,Backend"""

s = s.split("\n")
count = int(s[0])
jobs = s[1 : count + 1]
workers_jobs = s[count + 1 :]

workers_jobs = {
    wj.split(" ")[0]: {"ava": wj.split(" ")[1].split(","), "picked": None, "recent": 0}
    for wj in workers_jobs
}

# theory:
"""
start with the person with least capabilities
if (no capabalities):
    - revert the last action in the queue
    - remove the job from his list == BAD
    - remove his picked attirbute
      - increase his recent counter, so that he picks a different job on the next loop
    - whoever called the revert action, gets his recent counter set to 0
pick him a job (based on his recent visit)
    - push this action into a queue
    - make the job unvailable

if all has picked one job: break
and repeat
"""

unavailable_jobs = []


def revert(caller):
    # reverts the last action
    last_job = unavailable_jobs.pop()
    worker, jobs = list(
        filter(lambda x: x[1]["picked"] == last_job, workers_jobs.items())
    )[0]
    workers_jobs[worker]["picked"] = None
    workers_jobs[worker]["recent"] += 1
    # whoever calls needs to have its recent (visited) index set to zero
    workers_jobs[caller]["recent"] = 0


def check_all_picked():
    return all([each["picked"] for each in workers_jobs.values()])


def pick_a_job():
    while not check_all_picked():
        worker_job = min(
            filter(lambda x: not x[1]["picked"], workers_jobs.items()),
            key=lambda x: len(set(x[1]["ava"]).difference(set(unavailable_jobs))),
        )
        # TO SEE revert in action,,, disable ABOVE `.difference`

        worker, jobs = worker_job

        try:
            picked = list(filter(lambda x: x not in unavailable_jobs, jobs["ava"]))[
                workers_jobs[worker]["recent"]
            ]
            unavailable_jobs.append(picked)
            workers_jobs[worker]["picked"] = picked
        except:
            print(f"{worker} wants to revert previous action", end="\t^^^^^^^^^^^^\n")
            try:
                revert(caller=worker)
            except IndexError:
                print("There is no solution!")
                break


pick_a_job()
print(
    [
        (each[0], each[1]["picked"])
        for each in filter(lambda x: x[1]["picked"], workers_jobs.items())
    ]
)
