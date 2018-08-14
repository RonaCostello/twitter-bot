# -*- coding: utf-8 -*-

from panoptes_client import Project

project_info = []

for project in Project.where(launch_approved=True):
    if project.completeness < 1:
        print(project.title + "\n" +"www.zooniverse.org/projects/" + project.slug)

        # project_info.append([project.description, project.slug]) #For twitter message? Largest is 265
