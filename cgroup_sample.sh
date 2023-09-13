mount -t tmpfs none /sys/fs/cgroup
mkdir /sys/fs/cgroup/memory
mount -t cgroup none /sys/fs/cgroup/memory -o memory
# instead of 0 you can replace your own group name
mkdir /sys/fs/cgroup/memory/0
echo 4M > /sys/fs/cgroup/memory/0/memory.limit_in_bytes 
echo '' >/sys/fs/cgroup/memory/0/cgroup.procs
#replace 4M with your own value
echo [pid] >/sys/fs/cgroup/memory/0/tasks
cat /sys/fs/cgroup/memory/0/memory.limit_in_bytes
