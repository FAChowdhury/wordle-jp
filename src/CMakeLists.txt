# CMakeList.txt : CMake project for wordle-jp, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_executable (wordle-jp main.cpp "dictionary/dictionary.hpp")

find_package(unofficial-sqlite3 CONFIG REQUIRED)
target_link_libraries(wordle-jp PRIVATE unofficial::sqlite3::sqlite3)

target_include_directories(wordle-jp PRIVATE ${CMAKE_SOURCE_DIR}/code-gen)

# Build database as part of the build
find_package(Python3 COMPONENTS Interpreter REQUIRED)

set(DB_OUT "${CMAKE_BINARY_DIR}/japanese.db")

add_custom_command(
  OUTPUT ${DB_OUT}
	COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/build_db.py ${DB_OUT}
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  COMMENT "Generating SQLite DB at ${DB_OUT}"
  VERBATIM
)

add_custom_target(build_database
  DEPENDS ${DB_OUT}
  COMMENT "Build database (db_manifest)"
)

# Ensure the database is built before the main executable
add_dependencies(wordle-jp build_database)

# Also generate dictionary headers after the DB is created
add_custom_command(
	OUTPUT ${CMAKE_SOURCE_DIR}/code-gen/dictionary_entries.hpp
  COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/generate_dictionary.py ${DB_OUT}
	COMMAND_EXPAND_LISTS
  COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/generate_dictionary.py ${DB_OUT} ${CMAKE_SOURCE_DIR}/code-gen
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  COMMENT "Generating dictionary headers from DB"
  VERBATIM
)

add_custom_target(generate_dictionary
	DEPENDS ${CMAKE_SOURCE_DIR}/code-gen/dictionary_entries.hpp
)

# Ensure dictionary generation runs after the DB is built and before compilation
add_dependencies(generate_dictionary build_database)
add_dependencies(wordle-jp generate_dictionary)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET wordle-jp PROPERTY CXX_STANDARD 23)
endif()

# TODO: Add tests and install targets if needed.
