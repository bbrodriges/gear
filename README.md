# gear
A pure-Python asynchronous library to interface with Gearman.

# Brief history
Initially developed by [OpenStack](https://github.com/openstack-infra/gear) this package was adopted and patched to support Python 3 by [Edadeal](https://github.com/edadeal) in 2015.
Now, battle-proven, it can be safely published.

# Installation
```
pip install git+https://github.com/bbrodriges/gear.git#egg=gear
```

# Usage example
Producer:
```python
import json
import gear

# connect to gearmand
client = gear.Client()
client.addServer(host='localhost', port=4730)
client.waitForServer(timeout=0.5)  # will raise gear.TimeoutError after 500 milliseconds

# prepare job data
data = {
    'var1': 6,
    'var2': 3
}
# gearman communicates using bytes
job_data = bytes(json.dumps(data), encoding='utf-8')

# submit job to queue pipe (e.g. divider)
job = gear.Job('divider', job_data)
client.submitJob(job)
```

Consumer:
```python
import gear

# create worker and listen for specific queue pipe
worker = gear.Worker()
worker.addServer(host='localhost', port=4730)
worker.registerFunction('divider')

# get job and its data from queue
job = gearman.getJob()
data = json.loads(job.arguments.decode('utf-8'))

# do your magic
result = data['var1'] / data['var2']
print(result)
```

# Docs
This version of gear is moslty compatible with original OpenStack version, so you can use their [documentation](https://gear.readthedocs.io/en/latest/).

# Differences
* Python3 support
* timeout option for `Client.waitForServer()` method