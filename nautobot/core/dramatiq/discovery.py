import importlib
from collections import defaultdict
from itertools import chain
from django.apps import apps
from nautobot.core.apps import NautobotConfig


def import_jobs_from_apps():
    jobs_module_map = {}
    for app_config in apps.get_app_configs():
        # Check if the app uses the specific subclass of AppConfig
        if isinstance(app_config, NautobotConfig):
            jobs_module_name = app_config.jobs
            try:
                # Dynamically import the "jobs" module from the app
                jobs_module = importlib.import_module(f"{app_config.name}.{jobs_module_name}")
                jobs_module_map[app_config.name] = jobs_module
            except ImportError:
                # No jobs module in this app
                pass

    return jobs_module_map


def get_jobs_classes(flat=False):
    from nautobot.extras.jobs import Job, JobButtonReceiver, JobHookReceiver  # circular import
    jobs_module_map = import_jobs_from_apps()
    jobs_map = defaultdict(list)

    for app_config_name, module in jobs_module_map.items():
        for entity in dir(module):
            entity = getattr(module, entity)
            if isinstance(entity, type) and issubclass(entity, Job) and entity not in [Job, JobButtonReceiver, JobHookReceiver]:
                # We have a subclass of Job
                jobs_map[app_config_name].append(entity)

            elif isinstance(entity, Job):
                # We have an instance of job
                jobs_map[app_config_name].append(entity.__class__)

    if flat:
        return list(chain(*jobs_map.values()))
    return jobs_map
