# CMakeList.txt : CMake project for wordle-jp, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_executable (wordle-jp main.cpp "dictionary.h")

find_package(unofficial-sqlite3 CONFIG REQUIRED)
target_link_libraries(wordle-jp PRIVATE unofficial::sqlite3::sqlite3)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET wordle-jp PROPERTY CXX_STANDARD 23)
endif()

# TODO: Add tests and install targets if needed.
