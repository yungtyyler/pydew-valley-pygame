from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in sorted(img_files):
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def import_folder_dict(path):
    surface_dict = {}

    for _, __, soil_imgs in walk(path):
        for image in soil_imgs:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_dict[image.split('.')[0]] = image_surf

    return surface_dict