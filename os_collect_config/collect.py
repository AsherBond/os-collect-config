# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from openstack.common import log
from os_collect_config import ec2
from oslo.config import cfg

opts = [
    cfg.StrOpt('command',
               short='c',
               help='Command to run on metadata changes.'),
    cfg.StrOpt('cachedir',
               default='/var/run/os-collect-config',
               help='Directory in which to store local cache of metadata'),
]

CONF = cfg.CONF


def setup_conf():
    ec2_group = cfg.OptGroup(name='ec2',
                             title='EC2 Metadata options')

    CONF.register_group(ec2_group)
    CONF.register_opts(ec2.opts, group='ec2')

    CONF.register_cli_opts(opts)


def __main__():
    setup_conf()
    CONF(prog="os-collect-config")
    log.setup("os-collect-config")
    print json.dumps(ec2.collect(), indent=1)


if __name__ == '__main__':
    __main__()
