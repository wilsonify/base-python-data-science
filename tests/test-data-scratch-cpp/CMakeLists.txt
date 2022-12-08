


# Tests
enable_testing ()
add_test(run-testfizzbuzzer testfizzbuzzer)
add_test(run-testfortranlibray testfortranlibray)
add_test(run-testcheckout testcheckout)
add_test(run-testdataholder testdataholder)

# build an installer
include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/LICENSE")
set (CPACK_PACKAGE_NAME "googletest-examples")
set (CPACK_PACKAGE_VERSION_MAJOR "${VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${VERSION_MINOR}")
set (CPACK_SOURCE_GENERATOR "TGZ")
include (CPack)