# -*- coding: utf-8 -*-

from panoptes_client import Project
import random

def random_project():
    project_list = []
    for project in Project.where(launch_approved=True):
        if not project.redirect:
            if incompleteness(project) > 500:
                project_list.append(project)
    return(random.choice(project_list))


def incompleteness(project):
    incomplete_subjects = project.subjects_count - project.retired_subjects_count
    return incomplete_subjects
