cmake_minimum_required(VERSION 3.12)
project(example)

# Установить стандарт C++
set(CMAKE_CXX_STANDARD 11)

# Добавить pybind11 из локальной папки
add_subdirectory(pybind11)

# Создать Python-совместимый модуль
pybind11_add_module(example example.cpp)
