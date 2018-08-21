# -*- coding: utf-8 -*-

from panoptes_client import Project
import random

def select_project():
    project_list = {}
    for project in Project.where(launch_approved=True):
        if project.completeness < 0.9:  # Project completeness ranges between 0 and 1
            project_list[project.title] = [("www.zooniverse.org/projects/" + project.slug), project.description] #For twitter message? Largest is 265
    random_project = select_random(project_list)
    write_out(random_project)
    return random_project


def select_random(projects):
    return random.choice(list(projects.items()  ))

def write_out(string):
    with open("last-promoted-project.txt", "a") as file:
        file.write(str(string) + "\n")
