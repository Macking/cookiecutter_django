#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A redpulse_rpx.taskapp beat -l INFO
