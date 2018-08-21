# -*- coding: utf-8 -*-

from panoptes_client import Project
import random

def select_project():
    project_list = {}
    for project in Project.where(launch_approved=True):
        if not project.redirect:
            if completedness(project) > 500:
                if project.completeness == 1.0:
                    print project.title


        #     if project.completeness < 0.9:  # Project completeness ranges between 0 and 1
        #         project_list[project.title] = [("www.zooniverse.org/projects/" + project.slug), project.description] #For twitter message? Largest is 265
        # random_project = select_random(project_list)
        # write_out(random_project)
        # return random_project

def completedness(project):
    incomplete_subjects = project.subjects_count - project.retired_subjects_count
    return incomplete_subjects


def select_random(project_dict):
    return random.choice(list(projects_dict.items()  ))

def write_out(string):
    with open("last-promoted-project.txt", "a") as file:
        file.write(str(string) + "\n")

select_project()
