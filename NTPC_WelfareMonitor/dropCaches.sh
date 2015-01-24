#!/bin/bash
# Linux 2.6.16 之後增加 drop caches 機制
#
# /proc/sys/vm/drop_caches 表示目前設定
# 0 表示開啟 cache
# 1 釋放 沒在使用的 cache (一般建議)
# 2 釋放 dentry, inode cache
# 3 = 1 + 2 (不建議)
 
sync;sync;echo 1 > /proc/sys/vm/drop_caches
sync;sync;echo 0 > /proc/sys/vm/drop_caches
sync;sync;
