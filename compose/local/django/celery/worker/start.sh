#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A redpulse_rpx.taskapp worker -l INFO
