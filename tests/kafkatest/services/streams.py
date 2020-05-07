# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
import signal
import streams_property
import consumer_property
from ducktape.services.service import Service
from ducktape.utils.util import wait_until
from kafkatest.directory_layout.kafka_path import KafkaPathResolverMixin
from kafkatest.services.kafka import KafkaConfig
from kafkatest.services.monitor.jmx import JmxMixin
from kafkatest.version import LATEST_0_10_0, LATEST_0_10_1

STATE_DIR = "state.dir"

class StreamsTestBaseService(KafkaPathResolverMixin, JmxMixin, Service):
    """Base class for Streams Test services providing some common settings and functionality"""

    PERSISTENT_ROOT = "/mnt/streams"

    # The log file contains normal log4j logs written using a file appender. stdout and stderr are handled separately
    CONFIG_FILE = os.path.join(PERSISTENT_ROOT, "streams.properties")
    LOG_FILE = os.path.join(PERSISTENT_ROOT, "streams.log")
    STDOUT_FILE = os.path.join(PERSISTENT_ROOT, "streams.stdout")
    STDERR_FILE = os.path.join(PERSISTENT_ROOT, "streams.stderr")
    JMX_LOG_FILE = os.path.join(PERSISTENT_ROOT, "jmx_tool.log")
    JMX_ERR_FILE = os.path.join(PERSISTENT_ROOT, "jmx_tool.err.log")
    LOG4J_CONFIG_FILE = os.path.join(PERSISTENT_ROOT, "tools-log4j.properties")
    PID_FILE = os.path.join(PERSISTENT_ROOT, "streams.pid")

    CLEAN_NODE_ENABLED = True

    logs = {
        "streams_log": {
            "path": LOG_FILE,
            "collect_default": True},
        "streams_stdout": {
            "path": STDOUT_FILE,
            "collect_default": True},
        "streams_stderr": {
            "path": STDERR_FILE,
            "collect_default": True},
        "streams_log.1": {
            "path": LOG_FILE + ".1",
            "collect_default": True},
        "streams_stdout.1": {
            "path": STDOUT_FILE + ".1",
            "collect_default": True},
        "streams_stderr.1": {
            "path": STDERR_FILE + ".1",
            "collect_default": True},
        "streams_log.2": {
            "path": LOG_FILE + ".2",
            "collect_default": True},
        "streams_stdout.2": {
            "path": STDOUT_FILE + ".2",
            "collect_default": True},
        "streams_stderr.2": {
            "path": STDERR_FILE + ".2",
            "collect_default": True},
        "streams_log.3": {
            "path": LOG_FILE + ".3",
            "collect_default": True},
        "streams_stdout.3": {
            "path": STDOUT_FILE + ".3",
            "collect_default": True},
        "streams_stderr.3": {
            "path": STDERR_FILE + ".3",
            "collect_default": True},
        "streams_log.0-1": {
            "path": LOG_FILE + ".0-1",
            "collect_default": True},
        "streams_stdout.0-1": {
            "path": STDOUT_FILE + ".0-1",
            "collect_default": True},
        "streams_stderr.0-1": {
            "path": STDERR_FILE + ".0-1",
            "collect_default": True},
        "streams_log.0-2": {
            "path": LOG_FILE + ".0-2",
            "collect_default": True},
        "streams_stdout.0-2": {
            "path": STDOUT_FILE + ".0-2",
            "collect_default": True},
        "streams_stderr.0-2": {
            "path": STDERR_FILE + ".0-2",
            "collect_default": True},
        "streams_log.0-3": {
            "path": LOG_FILE + ".0-3",
            "collect_default": True},
        "streams_stdout.0-3": {
            "path": STDOUT_FILE + ".0-3",
            "collect_default": True},
        "streams_stderr.0-3": {
            "path": STDERR_FILE + ".0-3",
            "collect_default": True},
        "streams_log.0-4": {
            "path": LOG_FILE + ".0-4",
            "collect_default": True},
        "streams_stdout.0-4": {
            "path": STDOUT_FILE + ".0-4",
            "collect_default": True},
        "streams_stderr.0-4": {
            "path": STDERR_FILE + ".0-4",
            "collect_default": True},
        "streams_log.0-5": {
            "path": LOG_FILE + ".0-5",
            "collect_default": True},
        "streams_stdout.0-5": {
            "path": STDOUT_FILE + ".0-5",
            "collect_default": True},
        "streams_stderr.0-5": {
            "path": STDERR_FILE + ".0-5",
            "collect_default": True},
        "streams_log.0-6": {
            "path": LOG_FILE + ".0-6",
            "collect_default": True},
        "streams_stdout.0-6": {
            "path": STDOUT_FILE + ".0-6",
            "collect_default": True},
        "streams_stderr.0-6": {
            "path": STDERR_FILE + ".0-6",
            "collect_default": True},
        "streams_log.1-1": {
            "path": LOG_FILE + ".1-1",
            "collect_default": True},
        "streams_stdout.1-1": {
            "path": STDOUT_FILE + ".1-1",
            "collect_default": True},
        "streams_stderr.1-1": {
            "path": STDERR_FILE + ".1-1",
            "collect_default": True},
        "streams_log.1-2": {
            "path": LOG_FILE + ".1-2",
            "collect_default": True},
        "streams_stdout.1-2": {
            "path": STDOUT_FILE + ".1-2",
            "collect_default": True},
        "streams_stderr.1-2": {
            "path": STDERR_FILE + ".1-2",
            "collect_default": True},
        "streams_log.1-3": {
            "path": LOG_FILE + ".1-3",
            "collect_default": True},
        "streams_stdout.1-3": {
            "path": STDOUT_FILE + ".1-3",
            "collect_default": True},
        "streams_stderr.1-3": {
            "path": STDERR_FILE + ".1-3",
            "collect_default": True},
        "streams_log.1-4": {
            "path": LOG_FILE + ".1-4",
            "collect_default": True},
        "streams_stdout.1-4": {
            "path": STDOUT_FILE + ".1-4",
            "collect_default": True},
        "streams_stderr.1-4": {
            "path": STDERR_FILE + ".1-4",
            "collect_default": True},
        "streams_log.1-5": {
            "path": LOG_FILE + ".1-5",
            "collect_default": True},
        "streams_stdout.1-5": {
            "path": STDOUT_FILE + ".1-5",
            "collect_default": True},
        "streams_stderr.1-5": {
            "path": STDERR_FILE + ".1-5",
            "collect_default": True},
        "streams_log.1-6": {
            "path": LOG_FILE + ".1-6",
            "collect_default": True},
        "streams_stdout.1-6": {
            "path": STDOUT_FILE + ".1-6",
            "collect_default": True},
        "streams_stderr.1-6": {
            "path": STDERR_FILE + ".1-6",
            "collect_default": True},
        "jmx_log": {
            "path": JMX_LOG_FILE,
            "collect_default": True},
        "jmx_err": {
            "path": JMX_ERR_FILE,
            "collect_default": True},
    }

    def __init__(self, test_context, kafka, streams_class_name, user_test_args1, user_test_args2=None, user_test_args3=None, user_test_args4=None):
        Service.__init__(self, test_context, num_nodes=1)
        self.kafka = kafka
        self.args = {'streams_class_name': streams_class_name,
                     'user_test_args1': user_test_args1,
                     'user_test_args2': user_test_args2,
                     'user_test_args3': user_test_args3,
                     'user_test_args4': user_test_args4}
        self.log_level = "DEBUG"

    @property
    def node(self):
        return self.nodes[0]

    def pids(self, node):
        try:
            return [pid for pid in node.account.ssh_capture("cat " + self.PID_FILE, callback=int)]
        except:
            return []

    def stop_nodes(self, clean_shutdown=True):
        for node in self.nodes:
            self.stop_node(node, clean_shutdown)

    def stop_node(self, node, clean_shutdown=True):
        self.logger.info((clean_shutdown and "Cleanly" or "Forcibly") + " stopping Streams Test on " + str(node.account))
        pids = self.pids(node)
        sig = signal.SIGTERM if clean_shutdown else signal.SIGKILL

        for pid in pids:
            node.account.signal(pid, sig, allow_fail=True)
        if clean_shutdown:
            for pid in pids:
                wait_until(lambda: not node.account.alive(pid), timeout_sec=120, err_msg="Streams Test process on " + str(node.account) + " took too long to exit")

        node.account.ssh("rm -f " + self.PID_FILE, allow_fail=False)

    def restart(self):
        # We don't want to do any clean up here, just restart the process.
        for node in self.nodes:
            self.logger.info("Restarting Kafka Streams on " + str(node.account))
            self.stop_node(node)
            self.start_node(node)


    def abortThenRestart(self):
        # We don't want to do any clean up here, just abort then restart the process. The running service is killed immediately.
        for node in self.nodes:
            self.logger.info("Aborting Kafka Streams on " + str(node.account))
            self.stop_node(node, False)
            self.logger.info("Restarting Kafka Streams on " + str(node.account))
            self.start_node(node)

    def wait(self, timeout_sec=1440):
        for node in self.nodes:
            self.wait_node(node, timeout_sec)

    def wait_node(self, node, timeout_sec=None):
        for pid in self.pids(node):
            wait_until(lambda: not node.account.alive(pid), timeout_sec=timeout_sec, err_msg="Streams Test process on " + str(node.account) + " took too long to exit")

    def clean_node(self, node):
        node.account.kill_process("streams", clean_shutdown=False, allow_fail=True)
        if self.CLEAN_NODE_ENABLED:
            node.account.ssh("rm -rf " + self.PERSISTENT_ROOT, allow_fail=False)

    def start_cmd(self, node):
        args = self.args.copy()
        args['config_file'] = self.CONFIG_FILE
        args['stdout'] = self.STDOUT_FILE
        args['stderr'] = self.STDERR_FILE
        args['pidfile'] = self.PID_FILE
        args['log4j'] = self.LOG4J_CONFIG_FILE
        args['kafka_run_class'] = self.path.script("kafka-run-class.sh", node)

        cmd = "( export KAFKA_LOG4J_OPTS=\"-Dlog4j.configuration=file:%(log4j)s\"; " \
              "INCLUDE_TEST_JARS=true %(kafka_run_class)s %(streams_class_name)s " \
              " %(config_file)s %(user_test_args1)s %(user_test_args2)s %(user_test_args3)s" \
              " %(user_test_args4)s & echo $! >&3 ) 1>> %(stdout)s 2>> %(stderr)s 3> %(pidfile)s" % args

        self.logger.info("Executing streams cmd: " + cmd)

        return cmd

    def prop_file(self):
        cfg = KafkaConfig(**{streams_property.STATE_DIR: self.PERSISTENT_ROOT, streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers()})
        return cfg.render()

    def start_node(self, node):
        node.account.mkdirs(self.PERSISTENT_ROOT)
        prop_file = self.prop_file()
        node.account.create_file(self.CONFIG_FILE, prop_file)
        node.account.create_file(self.LOG4J_CONFIG_FILE, self.render('tools_log4j.properties', log_file=self.LOG_FILE))

        self.logger.info("Starting StreamsTest process on " + str(node.account))
        with node.account.monitor_log(self.STDOUT_FILE) as monitor:
            node.account.ssh(self.start_cmd(node))
            monitor.wait_until('StreamsTest instance started', timeout_sec=60, err_msg="Never saw message indicating StreamsTest finished startup on " + str(node.account))

        if len(self.pids(node)) == 0:
            raise RuntimeError("No process ids recorded")


class StreamsSmokeTestBaseService(StreamsTestBaseService):
    """Base class for Streams Smoke Test services providing some common settings and functionality"""

    def __init__(self, test_context, kafka, command, processing_guarantee = 'at_least_once', num_threads = 3):
        super(StreamsSmokeTestBaseService, self).__init__(test_context,
                                                          kafka,
                                                          "org.apache.kafka.streams.tests.StreamsSmokeTest",
                                                          command)
        self.NUM_THREADS = num_threads
        self.PROCESSING_GUARANTEE = processing_guarantee

    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers(),
                      streams_property.PROCESSING_GUARANTEE: self.PROCESSING_GUARANTEE,
                      streams_property.NUM_THREADS: self.NUM_THREADS}

        cfg = KafkaConfig(**properties)
        return cfg.render()

class StreamsEosTestBaseService(StreamsTestBaseService):
    """Base class for Streams EOS Test services providing some common settings and functionality"""

    clean_node_enabled = True

    def __init__(self, test_context, kafka, processing_guarantee, command):
        super(StreamsEosTestBaseService, self).__init__(test_context,
                                                        kafka,
                                                        "org.apache.kafka.streams.tests.StreamsEosTest",
                                                        command)
        self.PROCESSING_GUARANTEE = processing_guarantee

    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers(),
                      streams_property.PROCESSING_GUARANTEE: self.PROCESSING_GUARANTEE}

        cfg = KafkaConfig(**properties)
        return cfg.render()

    def clean_node(self, node):
        if self.clean_node_enabled:
            super(StreamsEosTestBaseService, self).clean_node(node)


class StreamsSmokeTestDriverService(StreamsSmokeTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsSmokeTestDriverService, self).__init__(test_context, kafka, "run")
        self.DISABLE_AUTO_TERMINATE = ""

    def disable_auto_terminate(self):
        self.DISABLE_AUTO_TERMINATE = "disableAutoTerminate"

    def start_cmd(self, node):
        args = self.args.copy()
        args['config_file'] = self.CONFIG_FILE
        args['stdout'] = self.STDOUT_FILE
        args['stderr'] = self.STDERR_FILE
        args['pidfile'] = self.PID_FILE
        args['log4j'] = self.LOG4J_CONFIG_FILE
        args['disable_auto_terminate'] = self.DISABLE_AUTO_TERMINATE
        args['kafka_run_class'] = self.path.script("kafka-run-class.sh", node)

        cmd = "( export KAFKA_LOG4J_OPTS=\"-Dlog4j.configuration=file:%(log4j)s\"; " \
              "INCLUDE_TEST_JARS=true %(kafka_run_class)s %(streams_class_name)s " \
              " %(config_file)s %(user_test_args1)s %(disable_auto_terminate)s" \
              " & echo $! >&3 ) 1>> %(stdout)s 2>> %(stderr)s 3> %(pidfile)s" % args

        return cmd

class StreamsSmokeTestJobRunnerService(StreamsSmokeTestBaseService):
    def __init__(self, test_context, kafka, processing_guarantee, num_threads = 3):
        super(StreamsSmokeTestJobRunnerService, self).__init__(test_context, kafka, "process", processing_guarantee, num_threads)

class StreamsEosTestDriverService(StreamsEosTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsEosTestDriverService, self).__init__(test_context, kafka, "not-required", "run")


class StreamsEosTestJobRunnerService(StreamsEosTestBaseService):
    def __init__(self, test_context, kafka, processing_guarantee):
        super(StreamsEosTestJobRunnerService, self).__init__(test_context, kafka, processing_guarantee, "process")

class StreamsComplexEosTestJobRunnerService(StreamsEosTestBaseService):
    def __init__(self, test_context, kafka, processing_guarantee):
        super(StreamsComplexEosTestJobRunnerService, self).__init__(test_context, kafka, processing_guarantee, "process-complex")

class StreamsEosTestVerifyRunnerService(StreamsEosTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsEosTestVerifyRunnerService, self).__init__(test_context, kafka, "not-required", "verify")


class StreamsComplexEosTestVerifyRunnerService(StreamsEosTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsComplexEosTestVerifyRunnerService, self).__init__(test_context, kafka, "not-required", "verify-complex")


class StreamsSmokeTestShutdownDeadlockService(StreamsSmokeTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsSmokeTestShutdownDeadlockService, self).__init__(test_context, kafka, "close-deadlock-test")


class StreamsBrokerCompatibilityService(StreamsTestBaseService):
    def __init__(self, test_context, kafka, processingMode):
        super(StreamsBrokerCompatibilityService, self).__init__(test_context,
                                                                kafka,
                                                                "org.apache.kafka.streams.tests.BrokerCompatibilityTest",
                                                                processingMode)


class StreamsBrokerDownResilienceService(StreamsTestBaseService):
    def __init__(self, test_context, kafka, configs):
        super(StreamsBrokerDownResilienceService, self).__init__(test_context,
                                                                 kafka,
                                                                 "org.apache.kafka.streams.tests.StreamsBrokerDownResilienceTest",
                                                                 configs)

    def start_cmd(self, node):
        args = self.args.copy()
        args['config_file'] = self.CONFIG_FILE
        args['stdout'] = self.STDOUT_FILE
        args['stderr'] = self.STDERR_FILE
        args['pidfile'] = self.PID_FILE
        args['log4j'] = self.LOG4J_CONFIG_FILE
        args['kafka_run_class'] = self.path.script("kafka-run-class.sh", node)

        cmd = "( export KAFKA_LOG4J_OPTS=\"-Dlog4j.configuration=file:%(log4j)s\"; " \
              "INCLUDE_TEST_JARS=true %(kafka_run_class)s %(streams_class_name)s " \
              " %(config_file)s %(user_test_args1)s %(user_test_args2)s %(user_test_args3)s" \
              " %(user_test_args4)s & echo $! >&3 ) 1>> %(stdout)s 2>> %(stderr)s 3> %(pidfile)s" % args

        self.logger.info("Executing: " + cmd)

        return cmd


class StreamsStandbyTaskService(StreamsTestBaseService):
    def __init__(self, test_context, kafka, configs):
        super(StreamsStandbyTaskService, self).__init__(test_context,
                                                        kafka,
                                                        "org.apache.kafka.streams.tests.StreamsStandByReplicaTest",
                                                        configs)


class StreamsOptimizedUpgradeTestService(StreamsTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsOptimizedUpgradeTestService, self).__init__(test_context,
                                                                 kafka,
                                                                 "org.apache.kafka.streams.tests.StreamsOptimizedTest",
                                                                 "")
        self.OPTIMIZED_CONFIG = 'none'
        self.INPUT_TOPIC = None
        self.AGGREGATION_TOPIC = None
        self.REDUCE_TOPIC = None
        self.JOIN_TOPIC = None

    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers()}

        properties['topology.optimization'] = self.OPTIMIZED_CONFIG
        properties['input.topic'] = self.INPUT_TOPIC
        properties['aggregation.topic'] = self.AGGREGATION_TOPIC
        properties['reduce.topic'] = self.REDUCE_TOPIC
        properties['join.topic'] = self.JOIN_TOPIC

        cfg = KafkaConfig(**properties)
        return cfg.render()


class StreamsUpgradeTestJobRunnerService(StreamsTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsUpgradeTestJobRunnerService, self).__init__(test_context,
                                                                 kafka,
                                                                 "org.apache.kafka.streams.tests.StreamsUpgradeTest",
                                                                 "")
        self.UPGRADE_FROM = None
        self.UPGRADE_TO = None
        self.extra_properties = {}

    def set_config(self, key, value):
        self.extra_properties[key] = value

    def set_version(self, kafka_streams_version):
        self.KAFKA_STREAMS_VERSION = kafka_streams_version

    def set_upgrade_from(self, upgrade_from):
        self.UPGRADE_FROM = upgrade_from

    def set_upgrade_to(self, upgrade_to):
        self.UPGRADE_TO = upgrade_to

    def prop_file(self):
        properties = self.extra_properties.copy()
        properties[streams_property.STATE_DIR] = self.PERSISTENT_ROOT
        properties[streams_property.KAFKA_SERVERS] = self.kafka.bootstrap_servers()

        if self.UPGRADE_FROM is not None:
            properties['upgrade.from'] = self.UPGRADE_FROM
        if self.UPGRADE_TO == "future_version":
            properties['test.future.metadata'] = "any_value"

        cfg = KafkaConfig(**properties)
        return cfg.render()

    def start_cmd(self, node):
        args = self.args.copy()

        if self.KAFKA_STREAMS_VERSION == str(LATEST_0_10_0) or self.KAFKA_STREAMS_VERSION == str(LATEST_0_10_1):
            args['zk'] = self.kafka.zk.connect_setting()
        else:
            args['zk'] = ""
        args['config_file'] = self.CONFIG_FILE
        args['stdout'] = self.STDOUT_FILE
        args['stderr'] = self.STDERR_FILE
        args['pidfile'] = self.PID_FILE
        args['log4j'] = self.LOG4J_CONFIG_FILE
        args['version'] = self.KAFKA_STREAMS_VERSION
        args['kafka_run_class'] = self.path.script("kafka-run-class.sh", node)

        cmd = "( export KAFKA_LOG4J_OPTS=\"-Dlog4j.configuration=file:%(log4j)s\"; " \
              "INCLUDE_TEST_JARS=true UPGRADE_KAFKA_STREAMS_TEST_VERSION=%(version)s " \
              " %(kafka_run_class)s %(streams_class_name)s %(zk)s %(config_file)s " \
              " & echo $! >&3 ) 1>> %(stdout)s 2>> %(stderr)s 3> %(pidfile)s" % args

        self.logger.info("Executing: " + cmd)

        return cmd


class StreamsNamedRepartitionTopicService(StreamsTestBaseService):
    def __init__(self, test_context, kafka):
        super(StreamsNamedRepartitionTopicService, self).__init__(test_context,
                                                                  kafka,
                                                                  "org.apache.kafka.streams.tests.StreamsNamedRepartitionTest",
                                                                  "")
        self.ADD_ADDITIONAL_OPS = 'false'
        self.INPUT_TOPIC = None
        self.AGGREGATION_TOPIC = None

    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers()}

        properties['input.topic'] = self.INPUT_TOPIC
        properties['aggregation.topic'] = self.AGGREGATION_TOPIC
        properties['add.operations'] = self.ADD_ADDITIONAL_OPS

        cfg = KafkaConfig(**properties)
        return cfg.render()


class StaticMemberTestService(StreamsTestBaseService):
    def __init__(self, test_context, kafka, group_instance_id, num_threads):
        super(StaticMemberTestService, self).__init__(test_context,
                                                      kafka,
                                                      "org.apache.kafka.streams.tests.StaticMemberTestClient",
                                                      "")
        self.INPUT_TOPIC = None
        self.GROUP_INSTANCE_ID = group_instance_id
        self.NUM_THREADS = num_threads
    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers(),
                      streams_property.NUM_THREADS: self.NUM_THREADS,
                      consumer_property.GROUP_INSTANCE_ID: self.GROUP_INSTANCE_ID,
                      consumer_property.SESSION_TIMEOUT_MS: 60000}

        properties['input.topic'] = self.INPUT_TOPIC
        # TODO KIP-441: consider rewriting the test for HighAvailabilityTaskAssignor
        properties['internal.task.assignor.class'] = "org.apache.kafka.streams.processor.internals.assignment.StickyTaskAssignor"

        cfg = KafkaConfig(**properties)
        return cfg.render()


class CooperativeRebalanceUpgradeService(StreamsTestBaseService):
    def __init__(self, test_context, kafka):
        super(CooperativeRebalanceUpgradeService, self).__init__(test_context,
                                                                 kafka,
                                                                 "org.apache.kafka.streams.tests.StreamsUpgradeToCooperativeRebalanceTest",
                                                                 "")
        self.UPGRADE_FROM = None
        # these properties will be overridden in test
        self.SOURCE_TOPIC = None
        self.SINK_TOPIC = None
        self.TASK_DELIMITER = "#"
        self.REPORT_INTERVAL = None

        self.standby_tasks = None
        self.active_tasks = None
        self.upgrade_phase = None

    def set_tasks(self, task_string):
        label = "TASK-ASSIGNMENTS:"
        task_string_substr = task_string[len(label):]
        all_tasks = task_string_substr.split(self.TASK_DELIMITER)
        self.active_tasks = set(all_tasks[0].split(","))
        if len(all_tasks) > 1:
            self.standby_tasks = set(all_tasks[1].split(","))

    def set_version(self, kafka_streams_version):
        self.KAFKA_STREAMS_VERSION = kafka_streams_version

    def set_upgrade_phase(self, upgrade_phase):
        self.upgrade_phase = upgrade_phase

    def start_cmd(self, node):
        args = self.args.copy()

        if self.KAFKA_STREAMS_VERSION == str(LATEST_0_10_0) or self.KAFKA_STREAMS_VERSION == str(LATEST_0_10_1):
            args['zk'] = self.kafka.zk.connect_setting()
        else:
            args['zk'] = ""
        args['config_file'] = self.CONFIG_FILE
        args['stdout'] = self.STDOUT_FILE
        args['stderr'] = self.STDERR_FILE
        args['pidfile'] = self.PID_FILE
        args['log4j'] = self.LOG4J_CONFIG_FILE
        args['version'] = self.KAFKA_STREAMS_VERSION
        args['kafka_run_class'] = self.path.script("kafka-run-class.sh", node)

        cmd = "( export KAFKA_LOG4J_OPTS=\"-Dlog4j.configuration=file:%(log4j)s\"; " \
              "INCLUDE_TEST_JARS=true UPGRADE_KAFKA_STREAMS_TEST_VERSION=%(version)s " \
              " %(kafka_run_class)s %(streams_class_name)s %(zk)s %(config_file)s " \
              " & echo $! >&3 ) 1>> %(stdout)s 2>> %(stderr)s 3> %(pidfile)s" % args

        self.logger.info("Executing: " + cmd)

        return cmd

    def prop_file(self):
        properties = {streams_property.STATE_DIR: self.PERSISTENT_ROOT,
                      streams_property.KAFKA_SERVERS: self.kafka.bootstrap_servers()}

        if self.UPGRADE_FROM is not None:
            properties['upgrade.from'] = self.UPGRADE_FROM
        else:
            try:
                del properties['upgrade.from']
            except KeyError:
                self.logger.info("Key 'upgrade.from' not there, better safe than sorry")

        if self.upgrade_phase is not None:
            properties['upgrade.phase'] = self.upgrade_phase

        properties['source.topic'] = self.SOURCE_TOPIC
        properties['sink.topic'] = self.SINK_TOPIC
        properties['task.delimiter'] = self.TASK_DELIMITER
        properties['report.interval'] = self.REPORT_INTERVAL

        cfg = KafkaConfig(**properties)
        return cfg.render()
