# ./taichi/rhi/common/CMakeLists.txt

set(COMMON_RHI common_rhi)
add_library(${COMMON_RHI})
target_sources(${COMMON_RHI}
  PRIVATE
    memory_pool.cpp
    unified_allocator.cpp
  )

target_include_directories(${COMMON_RHI}
  PRIVATE
    ${PROJECT_SOURCE_DIR}
  )

target_link_libraries(${COMMON_RHI} PRIVATE taichi_util)
