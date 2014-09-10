from stats_pb2 import *
from timer_pb2 import *
from ipc_sem_pb2 import *
from core_pb2 import *
from core_x86_pb2 import *
from remap_file_path_pb2 import *
from fsnotify_pb2 import *
from inventory_pb2 import *
from tcp_stream_pb2 import *
from mnt_pb2 import *
from packet_sock_pb2 import *
from pipe_data_pb2 import *
from ipc_var_pb2 import *
from sa_pb2 import *
from tun_pb2 import *
from fown_pb2 import *
from tty_pb2 import *
from rlimit_pb2 import *
from ipc_shm_pb2 import *
from file_lock_pb2 import *
from sk_unix_pb2 import *
from sk_packet_pb2 import *
from pagemap_pb2 import *
from pipe_pb2 import *
from pstree_pb2 import *
from sk_opts_pb2 import *
from siginfo_pb2 import *
from cgroup_pb2 import *
from fh_pb2 import *
from ipc_msg_pb2 import *
from mm_pb2 import *
from netdev_pb2 import *
from timerfd_pb2 import *
from ns_pb2 import *
from fs_pb2 import *
from ext_file_pb2 import *
from signalfd_pb2 import *
from ipc_desc_pb2 import *
from fdinfo_pb2 import *
from fifo_pb2 import *
from eventpoll_pb2 import *
from regfile_pb2 import *
from core_arm_pb2 import *
from sk_netlink_pb2 import *
from sk_inet_pb2 import *
from utsns_pb2 import *
from core_aarch64_pb2 import *
from eventfd_pb2 import *
from creds_pb2 import *
from vma_pb2 import *
from rpc_pb2 import *
from ghost_file_pb2 import *

from magic import *

# This dict is needed to identify what type of pb messages
# we need to read from image.
pb = {
	IDS_MAGIC           : task_kobj_ids_entry,
	IRMAP_CACHE_MAGIC   : irmap_cache_entry,
	FS_MAGIC            : fs_entry,
	PAGEMAP_MAGIC       : pagemap_head,
	FIFO_MAGIC          : fifo_entry,
	EVENTFD_FILE_MAGIC  : eventfd_file_entry,
	PIPES_DATA_MAGIC    : pipe_data_entry,
	INETSK_MAGIC        : inet_sk_entry,
	TTY_FILES_MAGIC     : tty_file_entry,
	UTSNS_MAGIC         : utsns_entry,
	FDINFO_MAGIC        : fdinfo_entry,
	NS_FILES_MAGIC      : ns_file_entry,
	INOTIFY_WD_MAGIC    : inotify_wd_entry,
	EVENTPOLL_TFD_MAGIC : eventpoll_tfd_entry,
	MNTS_MAGIC          : mnt_entry,
	VMAS_MAGIC          : vma_entry,
	IPCNS_SHM_MAGIC     : ipc_shm_entry,
	CORE_MAGIC          : core_entry,
	FILE_LOCKS_MAGIC    : file_lock_entry,
	EVENTPOLL_FILE_MAGIC: eventpoll_file_entry,
	REMAP_FPATH_MAGIC   : remap_file_path_entry,
	SK_QUEUES_MAGIC     : sk_packet_entry,
	REG_FILES_MAGIC     : reg_file_entry,
	TUNFILE_MAGIC       : tunfile_entry,
	IPC_VAR_MAGIC       : ipc_var_entry,
	TTY_INFO_MAGIC      : tty_info_entry,
	PIPES_MAGIC         : pipe_entry,
	NETDEV_MAGIC        : net_device_entry,
	STATS_MAGIC         : stats_entry,
	RLIMIT_MAGIC        : rlimit_entry,
	POSIX_TIMERS_MAGIC  : posix_timer_entry,
	FANOTIFY_MARK_MAGIC : fanotify_mark_entry,
	TIMERFD_MAGIC       : timerfd_entry,
	ITIMERS_MAGIC       : itimer_entry,
	CREDS_MAGIC         : creds_entry,
	SIGACT_MAGIC        : sa_entry,
	FIFO_DATA_MAGIC     : pipe_data_entry,
	TCP_STREAM_MAGIC    : tcp_stream_entry,
	PSTREE_MAGIC        : pstree_entry,
	UNIXSK_MAGIC        : unix_sk_entry,
	EXT_FILES_MAGIC     : ext_file_entry,
	SIGNAL_MAGIC        : siginfo_entry,
	INOTIFY_FILE_MAGIC  : inotify_file_entry,
	IPCNS_SEM_MAGIC     : ipc_sem_entry,
	NETLINK_SK_MAGIC    : netlink_sk_entry,
	FANOTIFY_FILE_MAGIC : fanotify_file_entry,
	SIGNALFD_MAGIC      : signalfd_entry,
	MM_MAGIC            : mm_entry,
	CGROUP_MAGIC        : cgroup_entry,
	PACKETSK_MAGIC      : packet_sock_entry,
	GHOST_FILE_MAGIC    : ghost_file_entry,
	IPCNS_MSG_MAGIC     : ipc_msg_entry,
	INVENTORY_MAGIC     : inventory_entry,
}
